# @mmmbuto/codex-cli-lts

> **Long-term support line based on upstream rust-v0.80.0, minimal features + security patches to maintain /chat compatibility**

[![npm](https://img.shields.io/npm/v/@mmmbuto/codex-cli-lts?style=flat-square&logo=npm)](https://www.npmjs.org/package/@mmmbuto/codex-cli-lts)
[![downloads](https://img.shields.io/npm/dt/@mmmbuto/codex-cli-lts?style=flat-square)](https://www.npmjs.org/package/@mmmbuto/codex-cli-lts)
[![ko-fi](https://img.shields.io/badge/☕_Support-Ko--fi-FF5E5B?style=flat-square&logo=ko-fi)](https://ko-fi.com/dionanos)

---

## What This Is

LTS (Long-term support) release line based on upstream OpenAI Codex rust-v0.80.0. This version focuses on stability and /chat compatibility with minimal features and security patches.

### Supported Platforms

- Linux x64
- Android Termux (ARM64)
- macOS arm64 (via CI artifacts/releases)

### What We Do:
✅ **Use official OpenAI Codex source** (https://github.com/openai/codex)
✅ **Compile for Linux x64 + ARM64** (Android Termux native)
✅ **Apply minimal patches** only for Termux-specific issues not addressed upstream
✅ **Package as npm** for easy installation
✅ **Maintain full Apache 2.0 compliance** with OpenAI attribution

### What We DON'T Do:
❌ **NO new features**
❌ **NO behavior modifications** (works exactly like upstream)
❌ **NO replacement** of official Codex

### 🔧 Compatibility Patches

We only apply patches for issues that:
- **Prevent Codex from working on Termux**
- **Are not addressed by upstream** (Termux is not officially supported)
- **Are minimal and well-documented**

**Current patches**: See [../patches/](../patches/) directory for full documentation.

Need help debugging upgrade alerts? See
[../docs/termux-upgrade-checks.md](../docs/termux-upgrade-checks.md) for known causes
and fix strategies.

**Found an issue?** Well-documented bug reports with reproduction steps are welcome! Open an [issue](https://github.com/DioNanos/codex-termux/issues).

---

## 📦 Installation

### Termux (Android ARM64)

```bash
# Update Termux packages and install Node.js
pkg update && pkg upgrade -y
pkg install nodejs-lts -y

# Install LTS
npm install -g @mmmbuto/codex-cli-lts

# Verify
codex --version
codex login
```

**Requirements:** Android 7+, ARM64, Node.js >=18 (recommended v22+), ~50MB storage

---

### Linux (x64)

```bash
# Install Node.js (example for Debian/Ubuntu)
sudo apt-get update
sudo apt-get install -y nodejs npm

# Install LTS
npm install -g @mmmbuto/codex-cli-lts

# Verify
codex --version
codex login
```

**Requirements:** Linux x64, Node.js >=18 (recommended v22+), ~80MB storage

---

### macOS (arm64)

Download from GitHub [releases](https://github.com/DioNanos/codex-termux/releases) or use CI artifacts.

---

## 🚀 Quickstart

Get started with Codex LTS in 2 minutes. Choose your setup:

- **Path 1**: OpenAI (default) - `codex login && codex`
- **Path 2**: /chat providers (native support for wire_api)
- **Path 3**: OpenRouter & gateways

See [../docs/quickstart.md](../docs/quickstart.md) for complete instructions.

---

## 📚 Documentation

- [Installation Details](../docs/installation.md)
- [Quickstart](../docs/quickstart.md)
- [Testing](../docs/testing.md)
- [Building from Source](../BUILDING.md)
- [Test Reports](../test-reports/)
- [Full Documentation](../docs/)

---

## 🔧 Project Maintenance

Community-maintained port enabling AI-powered coding on Android Termux. Activities include ARM64 compilation, upstream synchronization, Termux compatibility patches, and documentation.

**Thank you** to all users who have reported issues, provided feedback, and helped improve this project.

---

## 📝 License

This project maintains full compliance with the Apache 2.0 license from OpenAI Codex.

**Original work**: Copyright OpenAI (https://github.com/openai/codex)
**Termux port**: Minimal patches for Android compatibility

See [../LICENSE](../LICENSE) file for details.

---

## 🙏 Credits

- **OpenAI** for the amazing Codex CLI
- **Termux** community for Android terminal environment
- All contributors to upstream Codex project

---

**Maintained**: Community-driven, not affiliated with OpenAI
