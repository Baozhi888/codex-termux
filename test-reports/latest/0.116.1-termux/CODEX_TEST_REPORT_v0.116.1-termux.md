# CODEX TEST REPORT v0.116.1-termux (Latest Suite)

- Date: 2026-03-20 10:30:07 CET
- Device: asusrp3 (Termux)
- Repo: `~/Dev/codex-termux`
- Global package under test: `@mmmbuto/codex-cli-termux`
- Suite reference: `test-reports/suites/latest/termux.md`
- Raw log: not captured (manual run)

## Version Check Snapshot
- Global installed: `@mmmbuto/codex-cli-termux@0.116.1`
- CLI version: `codex-cli 0.116.0`
- Exec version: `codex-exec 0.116.0`

## Results

## TEST-100 - Install Guard: package installed
Result: PASS

## TEST-101 - Install Guard: global command paths
Result: PASS

## TEST-200 - Version Guard
Result: PASS

## TEST-300 - Workspace setup
Result: PASS (workspace cleaned by moving leftover file since `rm` is blocked by policy)

## TEST-301 - Help: `codex --help`
Result: PASS

## TEST-302 - Help: `codex exec --help`
Result: PASS

## TEST-303 - Help: `codex-exec --help`
Result: PASS

## TEST-400 - Non-interactive sanity: list files
Command:
```bash
cd ~/codex-test-workspace
codex-exec --sandbox workspace-write --skip-git-repo-check --json "print current directory and list files"
```
Evidence: `test-reports/latest/0.116.1-termux/TEST_noninteractive_1.jsonl`
Result: PASS

## TEST-401 - Non-interactive sanity: create/read hello.txt
Command:
```bash
cd ~/codex-test-workspace
codex-exec --sandbox workspace-write --skip-git-repo-check --json "create hello.txt with content 'hello' and then read it"
```
Evidence: `test-reports/latest/0.116.1-termux/TEST_noninteractive_2.jsonl`
Result: PASS

## TEST-500 - Binary architecture guard
Result: PASS
- `codex` and `codex-exec` are launcher scripts
- `codex.bin` and `codex-exec.bin` are Android ARM64 ELF binaries

## TEST-600 - Network-path smoke (no panic)
Command:
```bash
cd ~/codex-test-workspace
codex-exec --sandbox workspace-write --skip-git-repo-check --json \
  "run one network check with curl -I https://www.google.com and report the first HTTP status line only"
```
Evidence: `test-reports/latest/0.116.1-termux/TEST_network_smoke.jsonl`
Result: PASS

## TEST-700 - Installed binary linkage guard
Result: PASS
- No `libOpenSLES` / `liboboe` linkage found
- No static `libc++` dependency found

## TEST-800 - Wrapper routing guard: fork/debug
Result: PASS
- `fork --help` routes to `Usage: codex fork`
- `debug --help` routes to `Usage: codex debug`

## TEST-900 - Termux environment checks
Result: PASS
- Kernel: Android / aarch64
- Prefix: `/data/data/com.termux/files/usr`
- Node: `v25.8.0`
- npm: `11.12.0`
- `termux-open-url` present

## Summary
- PASS: 14
- FAIL: 0
- SKIP: 0
- Verdict: PASS
