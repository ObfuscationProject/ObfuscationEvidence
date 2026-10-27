#!/bin/bash
# build.sh <tree> <arch> <mode> <tag> : configure+build okernel_image with an isolated config dir
set -e
S=<scratch>
tree=$1; arch=$2; mode=$3; tag=$4
declare -A T=([i386]=i386-elf [x86_64]=x86_64-elf [aarch64]=aarch64-elf [arm32]=arm-none-eabi [rv64]=riscv64-elf [rv32]=riscv32-elf [loongarch64]=loongarch64-elf [mips]=mips-elf [mips64]=mips64-elf [ppc]=powerpc-eabi)
export XMAKE_CONFIGDIR=$S/cfg/$tag-$arch-$mode
mkdir -p $XMAKE_CONFIGDIR
cd $tree
out=$S/out/$tag/$arch-$mode; mkdir -p $out
xmake f -P $tree -c -y -m $mode -a $arch -o $S/bld/$tag/$arch-$mode --systoolchain_dir=$S/st/${T[$arch]} > $out/config.log 2>&1
xmake -P $tree -y -b -j8 okernel_image > $out/build.log 2>&1
find $S/bld/$tag/$arch-$mode -name 'kernel.elf' -o -name 'kernel.bin' | head
