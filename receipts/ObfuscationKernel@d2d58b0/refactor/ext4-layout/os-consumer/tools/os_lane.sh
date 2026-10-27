#!/bin/bash
# os_lane.sh <os-tree> <tag> <arch> <kernel-sdk>: the OS CI fast-lane steps against one SDK
S=<scratch>
tree=$1; tag=$2; arch=$3; sdk=$4
declare -A T=([i386]=i386-elf [x86_64]=x86_64-elf [aarch64]=aarch64-elf [arm32]=arm-none-eabi [rv64]=riscv64-elf [rv32]=riscv32-elf [loongarch64]=loongarch64-elf [mips]=mips-elf [mips64]=mips64-elf [ppc]=powerpc-eabi)
export XMAKE_CONFIGDIR=$S/cfg/os-$tag-$arch
out=$S/out/os-$tag/$arch; mkdir -p $out $XMAKE_CONFIGDIR
cd $tree
step() { local label=$1; shift; if "$@" > $out/$label.log 2>&1; then echo "$arch $label ok"; else echo "$arch $label FAIL"; fi; }
step configure xmake f -P $tree -c -y -m debug -a $arch --kernel_sdk=$sdk --systoolchain_dir=$S/st/${T[$arch]}
for t in ${SKIP_ARTIFACT:+} $([ -z "$SKIP_ARTIFACT" ] && echo artifact-test) kernel-sdk-check uapi-test libc-test; do step $t xmake -P $tree -y -b $t; done
[ $arch = x86_64 ] && step compat-test xmake -P $tree -y -b compat-test
for t in distro_image linux-driver-compat rootfs-simplefs rootfs-ext4; do step $t xmake -P $tree -y -b $t; done
step qemu-distro xmake qemu-distro -P $tree --fs=simplefs --require-native --timeout=30
if [ $arch = x86_64 ]; then
  rm -rf $out/persistence
  step persistence python3 scripts/test_persistent_ext4.py --arch x86_64 --qemu $S/st/x86_64-elf/bin/qemu-system-x86_64 \
    --kernel build/x86_64/debug/distro/kernel.bin --rootfs build/x86_64/debug/rootfs.ext4.img --out $out/persistence
fi
