=====================================
CODEX CLI TEST SUITE - FINAL REPORT
=====================================

Platform: Android Termux ARM64
Codex Version: codex-cli 0.100.0 / codex-exec 0.100.0
Test Date: 2026-02-12
Suite Source: test-reports/suites/latest/termux.md
Primary Raw Log: TERMUX_SUITE_RAW_20260212-235154.log
Rerun Raw Log: TERMUX_SUITE_RERUN_JSON_20260212-235234.log

SUMMARY:
--------
Total Checks: 8
Passed: 8
Failed: 0
Skipped: 0

SECTION BREAKDOWN:
------------------
1. Install Guard: 2/2 passed
2. Version Guard: 1/1 passed
3. Core Tests: 4/4 passed (2 required a rerun)
4. Termux Checks: 1/1 passed

CRITICAL FAILURES:
------------------
None.

NOTES:
------
- Initial execution of the two `codex-exec --json` sanity checks failed in
  `~/codex-test-workspace` due to trusted-directory policy.
- Same two checks were re-run with `--skip-git-repo-check` and passed.
- In rerun JSON logs, a non-fatal warning was observed:
  `ERROR codex_core::rollout::list: state db missing rollout path for thread ...`.

DETAILED RESULTS:
-----------------
- Install Guard / npm package: PASS
  - `@mmmbuto/codex-cli-termux@0.100.0-termux` found globally.

- Install Guard / global commands: PASS
  - `codex` -> `/data/data/com.termux/files/usr/bin/codex`
  - `codex-exec` -> `/data/data/com.termux/files/usr/bin/codex-exec`

- Version Guard: PASS
  - `codex --version` => `codex-cli 0.100.0`
  - `codex-exec --version` => `codex-exec 0.100.0`

- Core / workspace reset: PASS
  - Workspace created at `/data/data/com.termux/files/home/codex-test-workspace`.

- Core / help commands: PASS
  - `codex --help`, `codex exec --help`, `codex-exec --help` all returned usage output.

- Core / codex-exec json sanity #1: PASS (rerun)
  - Command: `codex-exec --skip-git-repo-check --json "print current directory and list files"`
  - Result: current directory and listing returned in JSON event stream.

- Core / codex-exec json sanity #2: PASS (rerun)
  - Command: `codex-exec --skip-git-repo-check --json "create hello.txt with content 'hello' and then read it"`
  - Result: `hello.txt` created and read back successfully.

- Termux checks: PASS
  - `uname -a` => Android aarch64 kernel detected
  - `$PREFIX` => `/data/data/com.termux/files/usr`
  - `node --version` => `v25.3.0`
  - `npm --version` => `11.8.0`
  - `termux-open-url` found

VERDICT: PASS

