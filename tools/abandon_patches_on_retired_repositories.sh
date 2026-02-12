#!/usr/bin/env bash
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# This script helps to abandon open patches when a project has been retired
# and all patches need to be abandoned.

set -e

DRY_RUN=0

function usage {
    echo "Usage: $(basename $0) [-n|--dry-run] <repo> [<repo>...]"
    echo "repo should be e.g. glance or openstack/glance"
    echo
    echo "Options:"
    echo "  -n, --dry-run    List changes that would be abandoned \\"
    echo "                   without actually abandoning them"
    echo
    echo "Example: $(basename $0) openstack/monasca-api \\"
    echo "                            openstack/monasca-ui"
    echo "         $(basename $0) --dry-run openstack/monasca-api"
    echo
    echo " !!! WARNING: please do not run this script without \\"
    echo "              discussing it"
    echo "              first with the Technical Commitee!"
    exit 1
}

if [[ $# -lt 1 ]]; then
    usage
fi

# Parse arguments
repos=()
while [[ $# -gt 0 ]]; do
    case $1 in
        -n|--dry-run)
            DRY_RUN=1
            shift
            ;;
        -h|--help)
            usage
            ;;
        *)
            repos+=("$1")
            shift
            ;;
    esac
done

if [[ ${#repos[@]} -eq 0 ]]; then
    echo "Error: No repositories specified"
    echo
    usage
fi

function abandon_change {
    gitid=$1
    msg=$2
    dry_run=$3
    commit_message=$(ssh review.opendev.org \
        "gerrit query $gitid --current-patch-set --format json" | \
        head -n1 | jq .subject)

    if [[ $dry_run -eq 1 ]]; then
        echo "[DRY RUN] Would abandon: $change -- $commit_message"
    else
        echo "Abandoning: $change -- $commit_message"
        ssh review.opendev.org gerrit review $gitid \
            --abandon --message \"$msg\"
    fi
}


if [[ $DRY_RUN -eq 1 ]]; then
    echo "=== DRY RUN MODE - No changes will be abandoned ==="
    echo
fi

for repo in "${repos[@]}"; do
    # Ensure repo has the openstack/ prefix
    if [[ ! "$repo" =~ / ]]; then
        repo="openstack/$repo"
    fi

    echo "Processing retired repository: $repo..."
    open_changes=$(
        ssh review.opendev.org \
        "gerrit query --current-patch-set --format json \
        status:open project:${repo}" | \
        jq .currentPatchSet.revision | grep -v null | sed 's/"//g'
    )

    if [[ -z "$open_changes" ]]; then
        echo "  No open changes found."
    else
        change_count=$(echo "$open_changes" | wc -l | tr -d ' ')
        echo "  Found $change_count open change(s)."
    fi

    abandon_message="This project has been retired and no longer \
accepts code changes via https://review.opendev.org."

    for change in $open_changes; do
        abandon_change $change "$abandon_message" $DRY_RUN
    done
    echo
done

if [[ $DRY_RUN -eq 1 ]]; then
    echo "=== DRY RUN COMPLETE - Run without --dry-run to \\"
    echo "    actually abandon changes ==="
fi
