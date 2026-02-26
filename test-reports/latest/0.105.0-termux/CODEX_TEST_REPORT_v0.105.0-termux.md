=====================================
CODEX CLI TEST SUITE - FINAL REPORT
=====================================

Platform: Android Termux ARM64
Codex Version: codex-cli 0.105.0 / codex-exec 0.105.0
Test Date: 2026-02-26 (CET)
Suite Source: test-reports/suites/latest/termux.md
Primary Raw Log: TERMUX_SUITE_RAW_20260226-074529.log
Primary JSON Log: TERMUX_SUITE_JSON_20260226-074529.log
Create JSON Log: TERMUX_SUITE_JSON_CREATE_20260226-074529.log
Network Rerun Log: TERMUX_SUITE_JSON_NETWORK_20260226-074529.log

SUMMARY:
--------
Total Checks: 10
Passed: 10
Failed: 0
Skipped: 0

SECTION BREAKDOWN:
------------------
1. Install Guard: 2/2 passed
2. Version Guard: 1/1 passed
3. Core Tests: 4/4 passed
4. v0.104.0 Regression Guard: 2/2 passed
5. Termux Checks: 1/1 passed

CRITICAL FAILURES:
------------------
None.

WARNINGS:
---------
None.

NOTES:
------
- Global package verified: @mmmbuto/codex-cli-termux@0.105.0-termux.
- Global commands verified:
  - codex -> /data/data/com.termux/files/usr/bin/codex
  - codex-exec -> /data/data/com.termux/files/usr/bin/codex-exec

DETAILED RESULTS:
-----------------
- Install Guard / npm package: PASS
  - @mmmbuto/codex-cli-termux@0.105.0-termux found globally.

- Install Guard / global commands: PASS
  - codex => /data/data/com.termux/files/usr/bin/codex
  - codex-exec => /data/data/com.termux/files/usr/bin/codex-exec

- Version Guard: PASS
  - codex --version => codex-cli 0.105.0
  - codex-exec --version => codex-exec 0.105.0

- Core / workspace reset: PASS
  - Workspace created at /data/data/com.termux/files/home/codex-test-workspace.

- Core / help commands: PASS
  - help output returned for codex, codex exec, codex-exec.

- Core / codex-exec json sanity #1: PASS
  - JSON event stream returned.

- Core / codex-exec json sanity #2: PASS
  - hello.txt created and read back successfully.

- Regression / binary architecture guard: PASS
  - Both package binaries are ARM64 Android ELF.

- Regression / network-path smoke: PASS
  - No crash/panic. First status detected: HTTP/2 200.

- Termux checks: PASS
  - uname => Android detected
  - PREFIX => /data/data/com.termux/files/usr
  - node => v25.3.0
  - npm => 11.11.0
  - termux-open-url => /data/data/com.termux/files/usr/bin/termux-open-url

VERDICT: PASS
