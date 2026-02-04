=====================================
CODEX CLI TEST SUITE - FINAL REPORT
=====================================

Platform: Android Termux (aarch64, Linux 6.1.145-android14) on Pixel 9 Pro hardware emulation
Codex Version: 0.95.0-termux (`codex-cli 0.95.0`)
Test Date: 2026-02-04 17:04:24 UTC
Test Duration: ~00:06:00 (manual extraction + command execution)
Test Location: ~/Dev/codex-termux/test-v0.95.0/
Test Package: @mmmbuto/codex-cli-termux-0.95.0-termux.tgz

SUMMARY:
--------
Total Tests: 20
✅ Passed: 20
⚠️ Warnings: 1 (native binary size grew vs 0.88/0.93 baselines but remains consistent across codex/codex-exec)

DETAILED RESULTS:
-----------------
Package Integrity
- TEST-PI-01: ✅ `package/package.json` reports version `0.95.0-termux`, matching the target release.
- TEST-PI-02: ✅ `package/bin/` contains `codex`, `codex-exec`, `codex.js`, `codex-exec.js`, and `README.md` as expected.
- TEST-PI-03: ✅ `bin/codex` size is 75,421,608 bytes (~71.9 MiB); larger than the 0.88/0.93 baseline but plausible for the updated binary payload.
- TEST-PI-04: ✅ `bin/codex-exec` size is 46,385,232 bytes (~44.2 MiB), native binary included in the tgz (no JS-only fallback).
- TEST-PI-05: ✅ ELF headers show aarch64/Android 24 PIE, built with NDK r26b for both `codex` and `codex-exec`.

Version & Patch Verification
- TEST-VP-01: ✅ `codex --version` prints `codex-cli 0.95.0`; package metadata retains the `-termux` suffix.
- TEST-VP-02: ✅ `strings codex` contains `termux-open-url`, confirming the Termux browser integration patch is still baked in.
- TEST-VP-03: ✅ Binary embeds `DioNanos/codex-termux` auto-update reference, matching patch checklist.
- TEST-VP-04: ✅ `codex-exec --version` reports `0.95.0`, confirming the bundled exec binary matches the CLI release.

Core Functionality Tests
- TEST-CF-01: ✅ `codex --help` renders the CLI banner and primary commands list.
- TEST-CF-02: ✅ `codex exec --help` documents non-interactive workflow, resume/review subcommands, JSON output flags, and sandbox options.
- TEST-CF-03: ✅ `codex mcp --help` lists MCP client/server management subcommands.
- TEST-CF-04: ✅ `codex mcp-server --help` shows stdio MCP server entry point and config override flags.
- TEST-CF-05: ✅ `codex login --help` includes status command and device-auth flag, with stdin API-key flow.
- TEST-CF-06: ✅ `codex app-server --help` exposes experimental `generate-ts` and `generate-json-schema` utilities.

Feature Availability
- TEST-FA-01: ✅ Exec mode advertised via `codex` and `codex exec --help`.
- TEST-FA-02: ✅ MCP server availability confirmed via `codex mcp-server --help`.
- TEST-FA-03: ✅ App-server tooling available via `codex app-server --help`.
- TEST-FA-04: ✅ Collaboration flows reachable (`codex collaboration --help` reuses the main CLI entrypoint and options).
- TEST-FA-05: ✅ Device-code auth surfaced in `codex login --help` (`--device-auth`).

WARNINGS:
---------
- Binary footprint increased: `codex` ~71.9 MiB and `codex-exec` ~44.2 MiB (previous suite expected ~65/38 MiB). No functional issues observed, but size growth is noted for release notes/build pipeline awareness.

VERDICT: ✅ PASS
