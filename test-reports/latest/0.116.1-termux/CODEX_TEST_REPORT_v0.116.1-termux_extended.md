# CODEX TEST REPORT v0.116.1-termux (Extended)

- Date: 2026-03-20 10:30:07 CET
- Device: asusrp3 (Termux)
- Repo: `~/Dev/codex-termux`
- Scope: extended validation on top of `test-reports/suites/latest/termux.md`
- Raw log: not captured (manual run)

## Extended Checks

## EXT-100 - Patch set verification
Command: `bash verify-patches.sh`
Result: PASS
Notes:
- Critical patches #1, #2, #4, #5, #6, #9, #10, #11, #12 present
- Informational warning on extra undeclared patch files remains unchanged from baseline

## EXT-110 - Android feature guard (`codex-cli`)
Command:
```bash
cd codex-rs
cargo tree -p codex-cli -e features --target aarch64-linux-android | rg -e 'voice-input|cpal|oboe|oboe-sys' || true
```
Result: PASS (empty output)

## EXT-111 - Android feature guard (`codex-cloud-tasks`)
Command:
```bash
cd codex-rs
cargo tree -p codex-cloud-tasks -e features --target aarch64-linux-android | rg -e 'voice-input|cpal|oboe|oboe-sys' || true
```
Result: PASS (empty output)
Notes:
- Cargo emitted a cache warning: `database is locked`

## EXT-120 - Android compile guard (`codex-network-proxy`)
Command: `cargo check -p codex-network-proxy --target aarch64-linux-android`
Result: SKIP (per user request: no build tests)

## EXT-121 - Android compile guard (`codex-core`)
Command: `cargo check -p codex-core --target aarch64-linux-android`
Result: SKIP (per user request: no build tests)

## EXT-122 - Android compile guard (`codex-cli`)
Command: `cargo check -p codex-cli --target aarch64-linux-android`
Result: SKIP (per user request: no build tests)

## EXT-130 - Trusted-directory guard behavior
Command:
```bash
cd ~/codex-test-workspace
codex-exec --sandbox workspace-write --json "print current directory"
```
Result: PASS
Expected refusal observed:
```text
Not inside a trusted directory and --skip-git-repo-check was not specified.
```

## Summary
- PASS: 4
- FAIL: 0
- SKIP: 3
- Verdict: PASS (build guards skipped by request)
