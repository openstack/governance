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
import operator

import prettytable
import requests

LOG = logging.getLogger(__name__)


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
    url = 'https://review.openstack.org/changes/'
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


def has_approved(name, review):
    for vote in review['labels'].get('Code-Review', {}).get('all', []):
        voter = vote.get('name', '')
        value = vote.get('value', 0)
        if voter == name and value == 1:
            return True
    return False


def all_changes():
    offset = 0
    while True:
        changes = query_gerrit(offset)

        yield from changes

        if changes and changes[-1].get('_more_changes', False):
            offset += 100
        else:
            break


def get_one_status(change, delegates):
    topic = change.get('topic', 'unknown topic')
    subject = change.get('subject')
    owner = change.get('owner', {}).get('name')
    url = 'https://review.openstack.org/{}\n'.format(change['_number'])

    latest = find_latest_revision(change)
    latest_created = to_datetime(latest['created'])
    now = datetime.datetime.now()
    age = now.date() - latest_created.date()
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

    elif topic == 'on-hold':
        can_approve = 'on hold'

    elif topic == 'formal-vote':
        # https://governance.openstack.org/tc/reference/charter.html#motions
        parts = []

        # At least 5 positive votes and more positive than negative
        # votes.
        votes_to_approve = (votes[1] >= 5 and votes[1] > votes[-1])

        # Wait at least 3 days after reaching majority.
        reached_majority = when_majority(change, 5)
        if reached_majority:
            earliest = str(reached_majority.date() + datetime.timedelta(4))
            since_majority = now.date() - reached_majority.date()
            time_to_approve = since_majority > datetime.timedelta(3)
        else:
            time_to_approve = False
            earliest = '4 days after 5 positive votes'

        if votes_to_approve and time_to_approve:
            parts.append('YES')

        if reached_majority and not time_to_approve:
            parts.append('too soon')

        # Even if we can approve it, if there are dissenting votes we
        # may want to continue discussion or refine the proposal.
        if votes[-1]:
            if votes[-1] >= votes[1]:
                parts.append('too many dissenting votes')
            else:
                parts.append('dissenting votes')

        if votes[1] < 5:
            parts.append('not enough votes')
        elif votes[1] == 5:
            parts.append('minimum favorable votes')
        elif reached_majority:
            parts.append('majority')
        else:
            parts.append('enough votes')

        if not reached_majority:
            # Even if we can approve it, if the majority have not
            # voted yes we may want to continue discussion or call for
            # a final vote.
            parts.append('not majority')

        can_approve = ',\n'.join(parts)

    elif topic == 'charter-change':
        # https://governance.openstack.org/tc/reference/charter.html#amendment
        parts = []

        # At least 2/3 (9) positive votes.
        votes_to_approve = votes[1] > 9

        # Wait least 3 days after reaching majority.
        reached_majority = when_majority(change, 9)
        if reached_majority:
            earliest = str(reached_majority.date() + datetime.timedelta(4))
            since_majority = now.date() - reached_majority.date()
            time_to_approve = since_majority > datetime.timedelta(3)
        else:
            time_to_approve = False
            earliest = '4 days after 9 positive votes'

        if votes_to_approve and time_to_approve:
            parts.append('YES')

        if reached_majority and not time_to_approve:
            parts.append('too soon')

        # Even if we can approve it, if there are dissenting votes we
        # may want to continue discussion or refine the proposal.
        if votes[-1]:
            parts.append('dissenting votes')

        if votes[1] < 9:
            parts.append('not enough votes')
        elif votes[1] == 9:
            parts.append('minimum favorable votes')
        else:
            parts.append('enough votes')

        can_approve = ',\n'.join(parts)

    elif topic == 'typo-fix':
        # https://governance.openstack.org/tc/reference/house-rules.html#typo-fixes
        if votes[-1] or code_reviews[-1]:
            can_approve = 'dissenting votes'
        elif owner == 'Doug Hellmann' or owner == 'Mohammed Naser':  # TC-chairs
            if votes[1] < 2:
                can_approve = 'not enough reviews'
            else:
                can_approve = 'YES, chair rules'
        else:
            can_approve = 'YES'

    elif topic in ('code-change', 'documentation-change'):
        # https://governance.openstack.org/tc/reference/house-rules.html#code-changes
        if votes[-1] or code_reviews[-1]:
            can_approve = 'dissenting votes'
        elif votes[1] < 2:
            can_approve = 'not enough reviews'
        else:
            can_approve = 'YES'

    elif topic in ('stable:follows-policy', 'vulnerability:managed'):
        # https://governance.openstack.org/tc/reference/house-rules.html#delegated-tags
        approver_name = delegates[topic]
        can_approve = 'delegated to {}'.format(approver_name)
        if has_approved(approver_name, change):
            can_approve += ', YES'

    elif topic in ('project-update', 'new-project'):
        # https://governance.openstack.org/tc/reference/house-rules.html#other-project-team-updates

        # At least 7 days old.
        earliest = str(latest_created.date() + datetime.timedelta(8))

        if votes[-1]:
            can_approve = 'dissenting votes'
        elif age < datetime.timedelta(7):
            can_approve = 'too soon'
        else:
            can_approve = 'YES'

    elif topic == 'goal-update':
        # https://governance.openstack.org/tc/reference/house-rules.html#goal-updates-from-ptls

        # At least 7 days old.
        earliest = str(latest_created.date() + datetime.timedelta(8))

        if votes[-1]:
            can_approve = 'dissenting votes'
        elif age < datetime.timedelta(7):
            can_approve = 'too soon'
        else:
            can_approve = 'YES'

    else:
        topic = 'unknown topic'
        can_approve = 'unknown topic'

    votes = '\n'.join([
        'CR:' + format_votes(code_reviews),
        ' V:' + format_votes(votes),
    ])

    return {
        'Topic': topic,
        'Subject': subject,
        'Summary': '\n'.join([subject.strip(), '', url]),
        'Owner': owner,
        'URL': url,
        'Age': age.days,
        'Date': latest_created.date(),
        'Can Approve': can_approve,
        'Status': '\n'.join([topic, can_approve,
                             '{} days old'.format(age.days),
                             earliest]),
        'Earliest': earliest,
        'Votes': votes,
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

    delegates = {
        'stable:follows-policy': 'Tony Breeds',
        'vulnerability:managed': 'VMT',
    }

    status = sorted(
        (get_one_status(change, delegates)
         for change in all_changes()),
        key=operator.itemgetter('URL'),
    )

    columns = (
        'Summary',
        'Status',
        'Votes',
    )

    x = prettytable.PrettyTable(
        field_names=columns,
        hrules=prettytable.ALL,
    )
    x.align['Summary'] = 'l'
    x.align['Status'] = 'l'
    x.align['Votes'] = 'l'
    for row in status:
        x.add_row([row[c] for c in columns])
    print(x.get_string())

if __name__ == '__main__':
    main()
