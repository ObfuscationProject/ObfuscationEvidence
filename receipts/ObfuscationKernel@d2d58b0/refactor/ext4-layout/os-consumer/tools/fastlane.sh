#!/bin/bash
# fastlane.sh <tree> <tag> <arch...>: xmake test + kernel-sdk export per arch (debug)
S=<scratch>
tree=$1; tag=$2; shift 2
cd $tree
for arch in "$@"; do
  export XMAKE_CONFIGDIR=$S/cfg/$tag-$arch-debug
  out=$S/out/$tag/$arch-debug
  xmake -P $tree -y -b -j8 okernel okernel_image > $out/fast-build.log 2>&1 || { echo "$arch build FAIL"; continue; }
  if xmake test -P $tree -y > $out/test.log 2>&1; then echo "$arch test ok"; else echo "$arch test FAIL"; fi
  grep -E 'tests? (passed|failed)|[0-9]+% tests passed' $out/test.log | tail -2
  if xmake -P $tree -y -b kernel-sdk > $out/sdk.log 2>&1; then echo "$arch sdk ok"; else echo "$arch sdk FAIL"; fi
done
