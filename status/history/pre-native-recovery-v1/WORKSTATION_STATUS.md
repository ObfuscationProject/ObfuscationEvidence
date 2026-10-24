# Current checkpoint: signal waits promoted; journal mode native matrix in progress

Accepted private integration is now Kernel865 / OS439, SDK29, in
`prototypes/native-signal-actions-sdk29-v1/working`. Promotion receipt:
`prototypes/native-signal-wait-merge-v1/promotion-v1.json`, SHA256
`a19d5a4d351f9b5f17a9e4f91af51e1aaa6a2a3240b5029a2d52fae6e3f0dc65`.
This is the required predecessor for subsequent integration. All 26 changed/new
paths were backed up and promoted from the exact qualified candidates.

Wait qualification: all 20 SDK rows; ten actual guest campaigns, 20 commands and
4,840 cases; eleven inherited x86 campaigns, 22 commands and 2,824 cases; 180
captured-log parser controls. Kernel hosted/runtime and guest Linux controls are
separately attributed. Production signals remain disabled. No complete M0-M12
milestone or distribution-support expansion is claimed.

M4 candidate Kernel867 / SDK30 is qualified by all 20 SDK rows and ten Debug
boots, plus inherited x86 native campaigns. Journal-mode exact guest successor
`native-journalled-mode-guest-v1/clock-fixture-candidate-v1` has inventory
`8f6dc06dff81251796b11c3f8090f3078a8fd52fb8465d7beba39428f0027132`.
The ordinary root and private negative-clock x86 runs passed. Matrix v2 is
executing three scenarios per architecture. Independent disk/collector review
and ABI30 wait-guest migration run separately. Recovery/interoperability gates
remain open; no default-root or complete M4 claim.

User deferred M11 physical and M12 manual desktop acceptance. Continue code and
automated qualification without requesting these again. Always use
`PYTHONDONTWRITEBYTECODE=1 python3 -B`, including subprocesses. Preserve failed
attempts and frozen evidence. Older checkpoints below are historical.

# Resume update: SDK30 qualification and native guest work

Accepted integration remains Kernel856/OS426, SDK29, with promotion3078ff0b
as the required predecessor. No candidate has been promoted in this update.
User deferred M11 physical and M12 manual acceptance; continue automation.

- Repaired865 all20 SDK rows, ten Debug boots and eleven inherited x86 native
  campaigns (22 commands/2824 cases) are sealed and replayed; no routine rerun.
- Wait guest preliminary-v3 OS433 exploratory x86 run is retained at
  native-signal-wait-build-v1/exploratory-v3-x86. It failed T22 while sending
  another realtime signal into a full pending queue (code0184); author is
  investigating. No new wait guest acceptance. Independent ledger reviewer
  vector_runtime_review owns only ledger tests and proposes module changes to
  pipe_signal_guest, avoiding overlapping writes.
- M4 frozen867 inventory0cacc4d45421411b1a62f0d0580c56ab7d84686960bc4117462d4f2dda9b3e0a
  at native-journalled-mode-v1/candidate-v1; author host7664/allten objects/
  inherited suites/five controls completed. Root SDK30 driver now running
  author replay then firstx86 plus remaining19 SDK rows. No SDK30 native claim.
- OS SDK30 migration candidate-v2 inventory1992283153cd01eb409a0761c042d8a8001bfdccd0d2ce6e369c9d33ebba3fe1
  passed502 unique tool tests and rejected all20 retained actualSDK29 manifests.
  Receiptc02e625a24c1ec50d36f83eb6cb30cdd13996457ea052bc55a98cd8442356810
  was replayed. It still needs reconciliation with wait guest additions.
- M4 musl C fixture built allten staticELFs at native-journalled-mode-guest-v1/static-v1;
  no execution yet. Offline seeded journal volume fixture-v1 passed e2fsck,
  inodeCRC, timestamp and payload checks. Root owns image/oracle/collector;
  mechanism author was assigned SDK-only C++ actual-runtime fixture+runner.

All Python: PYTHONDONTWRITEBYTECODE=1 python3 -B. Preserve frozen/failed evidence.

# Workstation implementation status

This is an integration index for the M0–M12 plan, not a completed-workstation
claim. The plan remains `ObfuscationOS/docs/plans/README.md`. Some progress
documents inside older frozen source snapshots describe earlier SDK generations;
the accepted promotion and its exact source inventories take precedence for
identifying the current integration source.

## Accepted source and evidence

The current accepted integration workspace is
`build/prototypes/native-signal-actions-sdk29-v1/working`: Kernel856 and OS426,
SDK29. It is separate from the preserved, dirty top-level repositories.

The latest promotion is
`build/prototypes/native-process-signals-merge-v1/promotion-v1.json`,
SHA256 `3078ff0b00fb6e9f7d647d473c709801749b00466bbad8c57969c4e15197d58e`.
Its `after` inventories are the required predecessor for the next promotion.

Recent accepted changes include complete blocking pipe write/writev
continuations, signal interruption and automatic SIGPIPE behavior within the
private signal profile. Large writes preserve their committed prefix across
waits, faults and interrupts. Actual native campaigns, independent runtime tests
and transcript controls are bound under `native-pipe-blocking-merge-v1`.

Signal runtime implementation headers now reside under Kernel `src/user/signals`
instead of `tests/native`. That extraction preserved 172 public headers and
matched all 40 cross-compiled runtime/scheduler objects against its predecessor.
Its qualification includes 20 standalone SDK rows and 16 x86 native commands;
it does not assert a new all-ten user-workload run for the extraction itself.

All ten Kernel profiles remain: x86_64, i386, aarch64, arm32, rv64, rv32,
loongarch64, mips, mips64 and ppc. The OS distribution userland matrix remains
x86_64, aarch64, rv64 and loongarch64. Additional all-ten musl qualification
fixtures do not by themselves expand the supported distribution matrix.

## Milestone gates

No complete M0–M12 milestone is closed by the recent signal work. This table
identifies the main remaining gates; it does not replace the requirement ledger
or reduce any milestone's scope.

| Milestone | Status | Main remaining gate |
| --- | --- | --- |
| M0 contracts | Open | Complete normative interface, clause, utility and option inventories; close explicit qualification gaps |
| M1 resources | Open | General resource policy, mapping/lifetime breadth and pressure qualification beyond bounded bootstrap facilities |
| M2 common objects | Open | Complete path and credential semantics, descriptor IPC, TTY/PTY behavior and concurrent lifetimes |
| M3 libc substrate | Active | Complete signals and their wait/restart/lifecycle semantics, remaining thread/ABI behavior, production integration and all-ten musl acceptance |
| M4 durable root | Open | Integrated journal recovery and writer, real crash/flush qualification and default-root adoption |
| M5 POSIX environment | Open | Shared musl/loader, file mappings/cache coherence, shell job control, cancellation, utilities and remaining mandatory semantics |
| M6 networking | Open | Actual NIC-to-user socket path and IPv4/IPv6 interoperability, transport robustness, DNS and TLS clients |
| M7 services | Open | Persistent userspace supervision, sessions/accounts, service recovery and consistent shutdown |
| M8 graphics | Open | Isolated compositor/clients, shared display buffers, input/seat ownership, fonts/toolkit and PTY terminal |
| M9 desktop | Open | Working persistent applications, installer/recovery, accessibility and automated end-to-end workflows |
| M10 ext4 breadth | Open | Every selected advanced feature and combination, including Linux/e2fsprogs round trips |
| M11 execution breadth | Open; hardware acceptance deferred | Real SMP, loaded module execution/unload lifetimes, IRQ/DMA/hotplug and physical reference-machine evidence |
| M12 release | Open; manual acceptance deferred | Close mandatory gaps, reproduce release artifacts, automate applicable workflows and perform the retained human checks |

The user has no physical reference machine available and cannot currently run
manual desktop acceptance. Those two gates remain recorded for later. Continue
implementation and automated qualification without waiting for those resources.

## Current integration work

Process-shared pending queues and positive PID/TID `kill` are now accepted.
Their qualification binds twenty SDK rows, twenty all-ten-profile process-signal
commands with 2,904 cases, twenty inherited x86 commands with 2,560 cases,
independent hosted review, captured-log controls and two actual native assertion
mutants. The unchanged OS415 regression sources remain byte-identical in OS426.

The next private signal-wait implementation is undergoing integration. Its
original frozen Kernel865 candidate corrected the independently observed Linux
ignored-signal semantics, but root review then found a dropped ignored signal
between scheduler wakeup and recipient rearm. The retained failing hosted
runtime and an isolated two-file repair are bound in
`native-signal-wait-root-review-v1/ready-runtime-receipt-v1.json`.
The repair passes 1,751 actual hosted runtime assertions with ASan/UBSan;
the ten-profile codec models separately pass 3,370 assertions.

The repaired candidate is frozen under `native-signal-wait-ready-mask-fix-v1`,
inventory `074ed5e5163a203f35a06ea0e193b061e60edbe7011e7ec47174275908858dc5`.
Its twenty standalone SDK rows and ten Debug boots passed and are sealed under
`native-signal-wait-build-v1`; eleven inherited x86 native campaigns also passed
with 22 commands and 2,824 cases. The repaired author qualification was replayed
from `native-signal-wait-author-v2`. OS signal-wait guests are
being implemented under `native-signal-wait-guest-v1`. These candidates are not
accepted yet. SDK29 retains existing record layouts and old wait-reason values;
one public header appends two explicit u8 reasons, and 171 headers are unchanged.

The next M4 source branch, `native-journalled-mode-v1`, is implementing checked
mode changes and qualified stat metadata on a bounded scratch journal mount.
An immutable maintained/noatime policy requires a separate SDK30 boundary.
Its mechanism and hosted tests are active; the OS ABI30 validator migration is
being tested independently under `native-sdk30-os-v1`. These branches are not
accepted and do not change default root format policy or close M4.

The current private signal implementation still excludes nonpositive process
groups/broadcasts, job control, signal wait/suspend interfaces and other
unimplemented sources. Console waits guarantee the separate SIGKILL path;
other nonignored signals can remain unsupported there. Production signal
enablement is still disabled. Hosted assertions, Linux references, standalone
boots, native guest execution, SMP and physical tests remain separate evidence
classes.

The live operational checkpoint is `build/CONTINUATION.md`; earlier frozen and
failed evidence is retained. A future promotion must bind the exact candidate,
SDKs and executed consumer sources before updating the accepted workspace.
