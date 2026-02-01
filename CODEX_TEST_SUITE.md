# Codex-Termux Test Suite

**Version Target**: 0.88.0-termux
**Test Date**: 2026-01-22
**Test Location**: ~/Dev/codex-termux/test-v0.88.0/

---

## Objective

Test the npm package @mmmbuto/codex-cli-termux version 0.88.0-termux
without installing it locally (preserve codex 0.80.0 installed).

---

## Test Environment

- Device: SamsungWork (Asus ROG Phone 3)
- OS: Android Termux
- Current codex version: 0.80.0-termux (preserved)
- Test package: @mmmbuto/codex-cli-termux-0.88.0-termux.tgz

---

## Test Categories

### 1. Package Integrity
- Verify package.json version matches 0.88.0-termux
- Verify binary size (~45MB codex, ~38MB codex-exec)
- Verify package structure (bin/, package.json, README.md)
- Verify architecture arm64

### 2. Version Verification
- Run codex --version returns codex-cli 0.88.0-termux
- Check package.json version matches

### 3. Patch Verification
- Check termux-open-url integration (strings in binary)
- Check DioNanos/codex-termux auto-update (strings in binary)
- Check -termux suffix in version

### 4. Core Functionality Tests
- codex --help displays usage
- codex exec --help displays usage
- codex mcp --help displays usage
- codex mcp-server --help displays usage
- codex login --help displays usage

### 5. Feature Availability
- Verify exec mode available
- Verify MCP server available
- Verify app-server command available
- Verify collaboration modes available
- Verify device-code auth available

---

## Test Execution

### Binary Path
cd ~/Dev/codex-termux/test-v0.88.0/package/bin/

---

## Expected Results

- Version: 0.88.0-termux
- Binary sizes: codex ~65MB, codex-exec ~38MB
- termux-open-url integration present
- Auto-update redirects to DioNanos/codex-termux
- All core commands available

---

## Known Limitations

- No network tests (requires API key)
- No login tests (requires browser/auth)
- No actual task execution tests (requires authenticated session)
- Binary executed directly without npm install

---

*Created: 2026-01-22*
*Status: Pending execution*
