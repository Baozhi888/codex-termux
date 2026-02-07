# @mmmbuto/codex-cli-lts

Repackaged builds of the upstream Codex CLI with minimal compatibility patches
for Android Termux.

## Version

- **Package**: `@mmmbuto/codex-cli-lts`
- **Version**: `0.80.4-lts` (based on rust-v0.80.0)
- **Supported**: Linux x64 + Android Termux (ARM64) + macOS arm64 (via CI artifacts/releases)

## Install

```bash
npm install -g @mmmbuto/codex-cli-lts
```

## Verify

```bash
codex --version
codex exec --help
```

## Documentation

- Configuration: [`../../docs/configuration.md`](../../docs/configuration.md)
- Building: [`../../BUILDING.md`](../../BUILDING.md)
- Patches: [`../../patches/`](../../patches/)
- Test Reports: [`../../test-reports/`](../../test-reports/)
