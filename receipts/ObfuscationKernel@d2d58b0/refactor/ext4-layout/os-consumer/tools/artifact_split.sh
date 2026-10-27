#!/bin/bash
# Run every ObfuscationOS tests/tools module in its own interpreter, so a crash in
# one module (native code loaded with ctypes shares the interpreter) cannot hide
# the results of the others.
#
# usage: artifact_split.sh <os-tree> <kernel-sdk> <out-dir>
set -u
tree=$1 sdk=$2 out=$3
mkdir -p "$out"
export OK_TEST_KERNEL_SDK=$sdk OK_TEST_KERNEL_ARCH=x86_64 OK_TEST_KERNEL_MODE=debug
cd "$tree/tests/tools" || exit 2
: > "$out/status.txt"
for f in test_*.py; do
    m=${f%.py}
    python3 -B -X faulthandler -m unittest "$m" > "$out/$m.log" 2>&1
    rc=$?
    ran=$(grep -a -o '^Ran [0-9]* test' "$out/$m.log" | tail -1 | awk '{print $2}')
    verdict=$(grep -a -E '^(OK|FAILED)' "$out/$m.log" | tail -1)
    echo "$m rc=$rc ran=${ran:-?} ${verdict:-<no summary>}" >> "$out/status.txt"
done
awk '{split($3, r, "="); n += r[2]} $2 != "rc=0" {bad++; print "NONZERO", $0} END {print "modules", NR, "tests", n, "nonzero", bad + 0}' "$out/status.txt"
