# CODEX CLI TEST SUITE - FINAL REPORT

Platform: Android Termux ARM64
Codex Version: codex-cli 0.105.0
Test Date (UTC): 2026-02-26
Test Duration: 77s

## Summary
- Total tests: 50
- Passed: 48
- Failed: 0
- Skipped: 2

## Critical Failures
- None

## Warnings
- TEST-601: Web search tool not available in this local shell test harness
- TEST-702: Git Information (Not in a git repo in test workspace)

## Notes
- Suite file: /data/data/com.termux/files/home/Dev/codex-termux/test-reports/CODEX_TEST_SUITE.md
- Runner log: /data/data/com.termux/files/home/Dev/codex-termux/test-reports/latest/0.105.0-termux/TERMUX_EXTENDED_RAW_20260226-074959.log

## Environment Summary
- User: u0_a594
- Shell: /data/data/com.termux/files/usr/bin/zsh
- PREFIX: /data/data/com.termux/files/usr
- HOME: /data/data/com.termux/files/home
- Node: v25.3.0
- npm: 11.11.0
- termux-info: Termux Variables:

## Per-Test Results
- TEST-000: PASS - Environment Preparation (Workspace created at /data/data/com.termux/files/home/codex-test-workspace)
- TEST-101: PASS - Display Codex Version (codex --version => codex-cli 0.105.0)
- TEST-102: PASS - Environment Context (PWD=/data/data/com.termux/files/home USER=u0_a594 SHELL=/data/data/com.termux/files/usr/bin/zsh)
- TEST-103: PASS - Platform Detection (arch=aarch64 node=v25.3.0 termux-info=present)
- TEST-201: PASS - Create Text File (test-file-1.txt created with expected content)
- TEST-202: PASS - Read File (Read matches TEST-201)
- TEST-203: PASS - Modify File (Append) (File now has 5 lines)
- TEST-204: PASS - Modify File (Edit/Replace) (Replacement applied)
- TEST-205: PASS - Create Directory Structure (Nested dirs created)
- TEST-206: PASS - List Directory Contents (Workspace listing includes project/)
- TEST-207: PASS - Create Multiple Files (3 files created with expected content)
- TEST-208: PASS - Delete File (test-file-1.txt removed)
- TEST-301: PASS - Find Files by Pattern (Found expected .js files)
- TEST-302: PASS - Search File Contents (Grep) (Content search returned expected hits)
- TEST-303: PASS - Recursive Directory Search (Found markdown/files; total files=3)
- TEST-401: PASS - Simple Shell Command (echo/whoami/uname ok)
- TEST-402: PASS - Command with Output Capture (Captured ls -la)
- TEST-403: PASS - Command Chain (Pipes) (Pipes behaved as expected)
- TEST-404: PASS - Package Manager Test (pkg command available / termux-tools appears installed)
- TEST-501: PASS - JSON File Operations (Extracted platform=Android)
- TEST-502: PASS - Multi-line File Creation (Script executed and printed expected lines)
- TEST-601: SKIPPED - Web search tool not available in this local shell test harness
- TEST-602: PASS - Network Connectivity (curl -I returned HTTP/2 200 )
- TEST-701: PASS - Git Repository Detection (git status reports not a git repo (expected in test workspace))
- TEST-702: SKIPPED - Git Information (Not in a git repo in test workspace)
- TEST-801: PASS - Code Analysis (Codex returned analysis/improvement for hello.js)
- TEST-802: PASS - Problem Solving (numbers.py prints 1..10 using a for loop)
- TEST-803: PASS - Documentation Generation (README updated with description, structure, usage)
- TEST-901: PASS - Handle Non-existent File (cat nonexistent.txt errors as expected)
- TEST-902: PASS - Handle Invalid Command (Invalid command fails gracefully)
- TEST-903: PASS - Handle Permission Issues (Access to /root blocked or unavailable as expected)
- TEST-1001: PASS - Termux Paths (PREFIX/HOME expected)
- TEST-1002: PASS - Termux Shell Detection (SHELL=/data/data/com.termux/files/usr/bin/zsh)
- TEST-1003: PASS - Termux-API Availability (Termux commands present)
- TEST-1004: PASS - Termux Package Manager (pkg command executes/is available)
- TEST-1005: PASS - Termux Storage Paths (~/storage or /sdcard accessible)
- TEST-1006: PASS - Termux Environment Variables (LD_LIBRARY_PATH/ANDROID_ROOT present)
- TEST-1007: PASS - Android-Specific Commands (arch=aarch64 sdk=31)
- TEST-1008: PASS - Library Path Preservation (LD_LIBRARY_PATH preserved; ldd shows no missing libs)
- TEST-1009: PASS - Termux Browser Open (termux-open-url present: /data/data/com.termux/files/usr/bin/termux-open-url)
- TEST-1010: PASS - Android Permissions (Own app data accessible; cross-app access restricted by sandbox model)
- TEST-1201: PASS - Verify codex Binary (package binary ok; size >30MB)
- TEST-1202: PASS - Verify codex-exec Binary (codex-exec ok)
- TEST-1203: PASS - Verify codex-exec JSON Flag (--json and --output-schema present)
- TEST-1204: PASS - NPM Package Structure (All expected files present in /data/data/com.termux/files/usr/lib/node_modules/@mmmbuto/codex-cli-termux/bin)
- TEST-1205: PASS - Binary Version Consistency (Versions match: 0.105.0)
- TEST-1206: PASS - Package.json Bin Entries (package.json exposes codex and codex-exec)
- TEST-1207: PASS - Global Command Availability (codex=/data/data/com.termux/files/usr/bin/codex codex-exec=/data/data/com.termux/files/usr/bin/codex-exec)
- TEST-1208: PASS - Upstream Crate Inventory (Cargo workspace release binaries present for Android target)
- TEST-1101: PASS - Remove Test Files (Workspace removed)
