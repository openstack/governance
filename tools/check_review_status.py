#!/usr/bin/env python3

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import argparse
import collections
import datetime
import json
import logging
import math
import operator

import prettytable
import requests

from openstack_governance import governance
from openstack_governance import members


LOG = logging.getLogger(__name__)

TC_SIZE = 9

# For formal-vote votes, age in days that a change has to have existed
# before it can be approved
creation_age_threshold = datetime.timedelta(days=7)


def decode_json(raw):
    """Trap JSON decoding failures and provide more detailed errors

    Remove ')]}' XSS prefix from data if it is present, then decode it
    as JSON and return the results.

    :param raw: Response text from API
    :type raw: str

    """

    # Gerrit's REST API prepends a JSON-breaker to avoid XSS vulnerabilities
    if raw.text.startswith(")]}'"):
        trimmed = raw.text[4:]
    else:
        trimmed = raw.text

    # Try to decode and bail with much detail if it fails
    try:
        decoded = json.loads(trimmed)
    except Exception:
        LOG.error(
            '\nrequest returned %s error to query:\n\n    %s\n'
            '\nwith detail:\n\n    %s\n',
            raw, raw.url, trimmed)
        raise
    return decoded


def query_gerrit(offset=0):
    """Query the Gerrit REST API"""
    url = 'https://review.opendev.org/changes/'
    LOG.debug('fetching %s', url)
    raw = requests.get(
        url,
        params={
            'n': '100',
            'start': offset,
            'q': 'project:openstack/governance is:open',
            'o': [
                'ALL_REVISIONS',
                'REVIEWER_UPDATES',
                'DETAILED_ACCOUNTS',
                'CURRENT_COMMIT',
                'LABELS',
                'DETAILED_LABELS',
                'MESSAGES',
            ],
        },
        headers={'Accept': 'application/json'},
    )
    return decode_json(raw)


def to_datetime(s, default=None):
    "Convert a string to a datetime.datetime instance"
    # Ignore the trailing decimal seconds.
    if s is None:
        return default
    s = s.rpartition('.')[0]
    return datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')


def find_latest_revision(review):
    result = None
    result_date = None
    for rev in review.get('revisions', {}).values():
        rev_date = to_datetime(rev.get('created'))
        if not result or rev_date > result_date:
            result = rev
            result_date = rev_date
    return result


def count_votes(review, group='Rollcall-Vote'):
    votes = collections.Counter()
    votes.update(
        vote.get('value')
        for vote in review['labels'].get(group, {}).get('all', [])
    )
    if None in votes:
        del votes[None]
    return votes


def when_majority(review, required_count):
    "Return the date when the vote reached the required count."
    n = 0
    votes = review['labels'].get('Rollcall-Vote', {}).get('all', [])
    now = datetime.datetime.now()
    for vote in sorted(votes, key=lambda x: to_datetime(x.get('date'), now)):
        if vote.get('value'):
            n += 1
        if n >= required_count:
            d = vote.get('date')
            if d:
                return to_datetime(d)


def format_votes(votes):
    return 'nay:{:2d} / abs:{:2d} / yes:{:2d}'.format(
        votes.get(-1, 0), votes.get(0, 0), votes.get(1, 0)
    )


def get_votes_by_person(member, review):
    for label in ['Code-Review', 'Rollcall-Vote']:
        for vote in review['labels'].get(label, {}).get('all', []):
            if member['gerritid'] == vote['_account_id']:
                yield vote


def has_approved(member, review):
    return any(
        vote.get('value', 0) == 1
        for vote in get_votes_by_person(member, review)
    )


def has_rejected(member, review):
    return any(
        vote.get('value', 0) == -1
        for vote in get_votes_by_person(member, review)
    )


def has_commented(member, review):
    desired_revision = max(
        r.get('_number', -1)
        for r in review.get('revisions', {}).values()
    )
    for msg in review.get('messages', []):
        if msg.get('_revision_number', -1) != desired_revision:
            continue
        if msg.get('author', {}).get('_account_id', '') == member['gerritid']:
            return True


def all_changes():
    offset = 0
    while True:
        changes = query_gerrit(offset)

        yield from changes

        if changes and changes[-1].get('_more_changes', False):
            offset += 100
        else:
            break


def get_one_status(change, delegates, tc_members):
    topic = change.get('topic', 'unknown topic')
    subject = change.get('subject')
    owner = change.get('owner', {}).get('name')
    url = 'https://review.opendev.org/{}\n'.format(change['_number'])

    latest = find_latest_revision(change)
    latest_created = to_datetime(latest['created'])
    now = datetime.datetime.utcnow()
    age = now - latest_created
    earliest = ''

    code_reviews = count_votes(change, 'Code-Review')
    votes = count_votes(change)
    workflow = count_votes(change, 'Workflow')
    verified = count_votes(change, 'Verified')

    can_approve = 'no'

    if workflow[-1]:
        can_approve = 'WIP'

    elif workflow[1]:
        can_approve = 'APPROVED'

    elif verified[-1]:
        can_approve = 'NO, verification failure'
        earliest = 'when passing'

    elif topic == 'on-hold':
        can_approve = 'on hold'

    elif topic == 'formal-vote':
        # https://governance.openstack.org/tc/reference/charter.html#motions
        parts = []

        # At least at third rounded up positive votes and more positive than
        # negative votes.
        necessary_votes = math.ceil(TC_SIZE / 3)
        votes_to_approve = votes[1] >= necessary_votes and votes[1] > votes[-1]
        reached_necessary_votes = when_majority(change, necessary_votes)

        parts.append('last change on {}'.format(
            latest_created.isoformat(timespec='minutes')
        ))

        # At least creation_age_threshold days old.
        if age < creation_age_threshold:
            time_to_approve = False
            parts.append("has not been open %d days" %
                         creation_age_threshold.days)
            earliest = str(latest_created + creation_age_threshold)
        elif reached_necessary_votes:
            time_to_approve = True
        else:
            time_to_approve = False
            earliest = "after {} positive votes".format(necessary_votes)

        if votes_to_approve and time_to_approve:
            parts.append('YES')

        if reached_necessary_votes and not time_to_approve:
            parts.append('enough required votes but too soon')

        # Even if we can approve it, if there are dissenting votes we
        # may want to continue discussion or refine the proposal.
        if votes[-1]:
            if votes[-1] >= votes[1]:
                parts.append('too many dissenting votes')
            else:
                parts.append('dissenting votes')

        if votes[1] < necessary_votes:
            parts.append('not enough votes')
        elif votes[1] == necessary_votes:
            parts.append('minimum favorable votes')
        else:
            parts.append('sufficient votes')

        if not (votes[1] > math.floor(TC_SIZE / 2)):
            # Even if we can approve it, if the majority have not
            # voted yes we may want to continue discussion or call for
            # a final vote.
            parts.append('plz whip votes - no majority and things can change')

        can_approve = ',\n'.join(parts)

    elif topic == 'charter-change':
        # https://governance.openstack.org/tc/reference/charter.html#amendment
        parts = []

        # At least 2/3 positive votes.
        necessary_votes = math.ceil(TC_SIZE / 3 * 2)
        votes_to_approve = votes[1] > necessary_votes

        # Wait least 3 days after reaching majority.
        reached_supermajority = when_majority(change, necessary_votes)
        if reached_supermajority:
            earliest = str(
                reached_supermajority.date() + datetime.timedelta(4)
            )
            since_supermajority = now.date() - reached_supermajority.date()
            time_to_approve = since_supermajority > datetime.timedelta(3)
        else:
            time_to_approve = False
            earliest = '4 days after {} positive votes'.format(necessary_votes)

        if votes_to_approve and time_to_approve:
            parts.append('CAN APPROVE')

        if reached_supermajority and not time_to_approve:
            parts.append('enough required votes but too soon')

        # Even if we can approve it, if there are dissenting votes we
        # may want to continue discussion or refine the proposal.
        if votes[-1]:
            parts.append('dissenting votes')

        if votes[1] < necessary_votes:
            parts.append('not enough votes')
        elif votes[1] == necessary_votes:
            parts.append('minimum favorable votes')
        else:
            parts.append('enough votes')

        can_approve = ',\n'.join(parts)

    elif topic in (
        'code-change',
        'documentation-change',
        'election-results',
        'typo-fix',
    ):
        # https://governance.openstack.org/tc/reference/house-rules.html#code-changes
        # https://governance.openstack.org/tc/reference/house-rules.html#documentation-changes
        # https://governance.openstack.org/tc/reference/house-rules.html#election-results
        # https://governance.openstack.org/tc/reference/house-rules.html#typo-fixes

        earliest = 'Can be voted anytime'

        if votes[-1] or code_reviews[-1]:
            can_approve = 'dissenting votes'
        elif votes[1] < 2:
            can_approve = 'not enough reviews'
        else:
            can_approve = 'CAN APPROVE'

    elif topic in delegates.keys():
        # https://governance.openstack.org/tc/reference/house-rules.html#delegated-tags
        # https://governance.openstack.org/tc/reference/house-rules.html#delegated-metadata
        approver_name = delegates[topic]
        can_approve = 'delegated to {}'.format(approver_name)
        if has_approved(approver_name, change):
            can_approve += '\nYES'
        elif has_rejected(approver_name, change):
            can_approve += '\nNO - delegate voted against'
        elif has_commented(approver_name, change):
            can_approve += '\ndelegate has commented'

    elif topic in ('project-update', 'new-project'):
        # https://governance.openstack.org/tc/reference/house-rules.html#other-project-team-updates

        if votes[-1] or code_reviews[-1]:
            can_approve = 'dissenting votes'
        elif votes[1] < 2:
            can_approve = 'not enough reviews'
        else:
            can_approve = 'CAN APPROVE'

    elif topic == 'goal-update':
        # https://governance.openstack.org/tc/reference/house-rules.html#goal-updates-from-ptls

        # At least 7 days old.
        earliest = str(latest_created + creation_age_threshold)

        if votes[-1]:
            can_approve = 'dissenting votes'
        elif age <= datetime.timedelta(7):
            can_approve = 'too soon'
        else:
            can_approve = 'CAN APPROVE'

    else:
        topic = 'unknown topic'
        can_approve = 'unknown topic'

    votes = '\n'.join([
        'CR:' + format_votes(code_reviews),
        ' V:' + format_votes(votes),
    ])

    tc_member_votes = {}
    for member in tc_members:
        name = member['name']
        if has_approved(member, change):
            tc_member_votes[name] = '+'
        elif has_rejected(member, change):
            tc_member_votes[name] = '-'
        elif has_commented(member, change):
            tc_member_votes[name] = 'C'
        else:
            tc_member_votes[name] = ' '
    member_votes = '\n'.join(
        '{} : {}'.format(value, name)
        for name, value in sorted(tc_member_votes.items())
    )

    return {
        'Topic': topic,
        'Subject': subject,
        'Summary': '\n'.join([
            subject.strip(),
            '',
            url,
            'Submitted by: {}'.format(owner.strip())
        ]),
        'Owner': owner,
        'URL': url,
        'Age': age.days,
        'Date': latest_created.date(),
        'Can Approve': can_approve,
        'Status': '\n'.join([topic, can_approve,
                             '{} days old'.format(age.days),
                             'earliest: {}'.format(earliest)]),
        'Earliest': earliest,
        'Votes': votes,
        'Members': member_votes,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--verbose', '-v',
        action='store_const',
        dest='log_level',
        default=logging.INFO,
        const=logging.DEBUG,
    )

    args = parser.parse_args()
    logging.basicConfig(
        level=args.log_level,
    )

    tc_members = members.parse_members_file('./reference/members.yaml')
    # NOTE(mnaser): In order to consistently and properly track the votes,
    #               we need to lookup every users Gerrit account ID based
    #               on their email.
    for member in tc_members:
        raw = requests.get(
            'https://review.opendev.org/accounts/%s' % member['email'],
            headers={'Accept': 'application/json'},
        )
        member['gerritid'] = decode_json(raw).get('_account_id')

    gov = governance.Governance.from_local_repo()
    release_team = gov.get_team('Release Management')

    delegates = {
        'stable:follows-policy': 'Tony Breeds',
        'vulnerability:managed': 'VMT',
        'release-management': release_team.ptl['name'],
    }
    for tag, name in sorted(delegates.items()):
        print('Delegating {} tags to {}'.format(tag, name))

    status = sorted(
        (get_one_status(change, delegates, tc_members)
         for change in all_changes()),
        key=operator.itemgetter('URL'),
    )

    columns = (
        'Summary',
        'Status',
        'Votes',
        'Members',
    )

    x = prettytable.PrettyTable(
        field_names=columns,
        hrules=prettytable.ALL,
    )
    x.align['Summary'] = 'l'
    x.align['Status'] = 'l'
    x.align['Votes'] = 'l'
    x.align['Members'] = 'l'
    for row in status:
        x.add_row([row[c] for c in columns])
    print(x.get_string())


if __name__ == '__main__':
    main()
