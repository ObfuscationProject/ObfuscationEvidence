#!/bin/bash
# matrix.sh <tree> <tag> <archs...>: debug+release builds, 3 concurrent
S=<scratch>
tree=$1; tag=$2; shift 2
for a in "$@"; do for m in debug release; do echo "$a $m"; done; done | xargs -P 3 -L 1 bash -c 'if '$S'/build.sh '$tree' $0 $1 '$tag' >/dev/null 2>&1; then echo "$0 $1 ok"; else echo "$0 $1 FAIL"; fi'
