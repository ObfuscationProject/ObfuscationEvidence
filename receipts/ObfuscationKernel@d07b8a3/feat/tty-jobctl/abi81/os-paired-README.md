# Paired ObfuscationOS changes for kernel ABI 81 (feat/getty-login obligations)

Base: ObfuscationOS main c3e1c55 (`Merge feat/smp-bringup onto main`, ABI 80), taken with
`git archive` into notes/os-s81-main and notes/os-s81 (the OS checkout was only fetched, never edited).
Diff: `os-paired.diff` = `diff -ruN os-s81-main os-s81` (27 files; apply with `patch -p1` in an OS
tree at c3e1c55; checked to apply cleanly). Kernel SDK: claude/tty-jobctl-feat-bcfe42 at d07b8a3
(module ABI 81, UAPI 0.17.0), exported from a `git archive` copy (notes/wt/s81/build/sdk/x86_64/debug).

## How it was made

1. notes/out-s9/os-paired.diff (made against OS f2b3bf3, ABI 79) was three-way merged onto c3e1c55
   per file (`git merge-file`, base os-s9-main, other os-s9). Conflicts were only in the ABI lines that
   OS main moved to 80 (test_kernel_sdk.py, test_native_console_control_sdk.py,
   test_native_group_signal_sdk.py, test_native_sessions_sdk.py, test_uapi_fields.py, kernel_sdk.py);
   each took the paired side with its ABI numbers shifted to 80, and the paired-only lines (TTY and
   job-control validators and fixtures, test_native_tty_sdk.py) moved to 80 too.
2. Then the consumer moved 80 -> 81 exactly like OS 3ed4160 (ABI 80): tools/kernel_sdk.py (marker lines,
   `SDK81`/`ABI81` diagnostics, manifest abi_version), tools/object_pressure_evidence.py, and the tests
   test_kernel_sdk.py, test_native_console_control_sdk.py, test_native_group_signal_sdk.py,
   test_native_metadata_sdk.py, test_native_persistent_sync_sdk.py, test_native_sessions_sdk.py,
   test_object_pressure.py, test_uapi_fields.py and test_native_tty_sdk.py; stale/future lists refuse
   80 and 82 (and every older value they listed).
3. The kernel exporter and the consumer validators stay byte-identical (the NATIVE_SESSIONS..NATIVE_METADATA
   region diff between kernel tools/export_sdk.py and OS tools/kernel_sdk.py is empty).

Content otherwise as notes/out-s9/os-paired-README.md items 1-7: storage attach_terminals, okcrt
sigaction()/signal() with SIG_DFL/SIG_IGN, oksh/login ignoring SIGTTOU/SIGTTIN/SIGTSTP, the UAPI 0.17
consumer validators and pins, test_native_tty_sdk.py.

## Lanes (x86_64, debug, QEMU 10.2.0 TCG) against the ABI 81 SDK

| Lane | Result |
|---|---|
| `kernel-sdk-check` | pass |
| `qemu-distro --fs=simplefs --require-native` | `OK_DEV source=kernel devices=null,zero,full,tty,console,ptmx,pts`, `OK_USERLAND scope=hardware acceptance=pass shell_pipeline=pass` |
| same with `--smp=2` | `acceptance=pass shell_pipeline=pass`, `OK_SMP_CPUS online=2` with user entries on both CPUs, every lock/assert counter 0 |
| interactive driver `--posix-check` (os-interactive.sh) | rc=0, every command PASS |
| devpts probe (out-s6fix/probe, lane-only fixture target, removed afterwards) | `TTY_DEVPTS_PROBE stage=PASS value=0 arch=x86_64 scope=guest-native-qemu` |
| static musl Linux PTY probe (out-s7, ELF sha 33e67a19...) | `TTY_LINUX_PROBE stage=PASS arch=x86_64 checks=43 interrupts=2` |
| OS SDK suites (`discover -p 'test_*sdk*.py'`, OK_TEST_KERNEL_SDK + OK_KERNEL_CHECKOUT) | Ran 134 tests, OK |
| test_uapi_fields, test_object_pressure, test_native_console_gate, test_native_pty_wrappers, test_native_console_sdk, test_mount_info_sdk, test_native_power_sdk | OK |
| kernel `test_tty_sdk_contract.py --os-root notes/os-s81` | `TTY_SDK_CONTRACT_PASS suites=3 guest=0` |

Not run here: the full OS `tests/tools` discover (1336 tests, ~13 min) and the other nine profiles'
OS distro boots; both are due before the paired PR (see memory kernel-validation-lanes: run qemu-distro on
all ten profiles plus a ppc musl run for runtime changes merged with SMP).

## Obligations for the paired worktree feat/getty-login

Adopt this diff (or equivalent), rewrite the stale tests/native/native_console_control.c probe and any
qualifier expecting EIO/POLLERR/ENOTTY (out-s9 README item 2), run the login lane, and merge right after
the kernel PR. Kernel and OS both declare ABI 81 / UAPI 0.17.0.
