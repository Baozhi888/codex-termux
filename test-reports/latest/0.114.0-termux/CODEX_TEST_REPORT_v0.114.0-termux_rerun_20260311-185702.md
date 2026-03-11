# CODEX TEST REPORT v0.114.0-termux (Latest Suite, Corrected Rerun)

- Date: 2026-03-11 18:57:02 CET
- Device: asusrp3 (Termux)
- Repo: ~/Dev/codex-termux
- Global package under test: @mmmbuto/codex-cli-termux
- Suite reference: test-reports/suites/latest/termux.md

## Version Check Snapshot
- Global installed: ├── @mmmbuto/codex-cli-termux@0.114.0-termux
- Repo npm-package version: 3:  "version": "0.112.0-termux",

## TEST-100 - Install Guard: package installed

```bash
npm ls -g --depth=0 @mmmbuto/codex-cli-termux || true
```

Output:
```text
/data/data/com.termux/files/usr/lib
└── @mmmbuto/codex-cli-termux@0.114.0-termux
```
Result: PASS (exit 0)

## TEST-101 - Install Guard: global command paths

```bash
command -v codex; command -v codex-exec; ls -la "$(command -v codex)" "$(command -v codex-exec)"
```

Output:
```text
/data/data/com.termux/files/usr/bin/codex
/data/data/com.termux/files/usr/bin/codex-exec
lrwxrwxrwx. 1 termux_user termux_user 62 Mar 11 18:39 /data/data/com.termux/files/usr/bin/codex -> ../lib/node_modules/@mmmbuto/codex-cli-termux/bin/codex.js
lrwxrwxrwx. 1 termux_user termux_user 66 Mar 11 18:39 /data/data/com.termux/files/usr/bin/codex-exec -> ../lib/node_modules/@mmmbuto/codex-cli-termux/bin/codex-exec.js
```
Result: PASS (exit 0)

## TEST-200 - Version Guard

```bash
codex --version; codex-exec --version
```

Output:
```text
codex-cli 0.114.0
codex-exec 0.114.0
```
Result: PASS (exit 0)

## TEST-300 - Workspace setup

```bash
rm -rf ~/codex-test-workspace; mkdir -p ~/codex-test-workspace; cd ~/codex-test-workspace; pwd; ls -la
```

Output:
```text
~/codex-test-workspace
total 12
drwx------.  2 termux_user termux_user 3488 Mar 11 18:57 .
drwxr-xr-x. 42 termux_user termux_user 8192 Mar 11 18:57 ..
```
Result: PASS (exit 0)

## TEST-301 - Help: codex --help

```bash
codex --help | sed -n "1,40p"
```

Output:
```text
Codex CLI

If no subcommand is specified, options will be forwarded to the interactive CLI.

Usage: codex [OPTIONS] [PROMPT]
       codex [OPTIONS] <COMMAND> [ARGS]

Commands:
  exec        Run Codex non-interactively [aliases: e]
  review      Run a code review non-interactively
  login       Manage login
  logout      Remove stored authentication credentials
  mcp         Manage external MCP servers for Codex
  mcp-server  Start Codex as an MCP server (stdio)
  app-server  [experimental] Run the app server or related tooling
  completion  Generate shell completion scripts
  sandbox     Run commands within a Codex-provided sandbox
  debug       Debugging tools
  apply       Apply the latest diff produced by Codex agent as a `git apply` to your local working
              tree [aliases: a]
  resume      Resume a previous interactive session (picker by default; use --last to continue the
              most recent)
  fork        Fork a previous interactive session (picker by default; use --last to fork the most
              recent)
  cloud       [EXPERIMENTAL] Browse tasks from Codex Cloud and apply changes locally
  features    Inspect feature flags
  help        Print this message or the help of the given subcommand(s)

Arguments:
  [PROMPT]
          Optional user prompt to start the session

Options:
  -c, --config <key=value>
          Override a configuration value that would otherwise be loaded from `~/.codex/config.toml`.
          Use a dotted path (`foo.bar.baz`) to override nested values. The `value` portion is parsed
          as TOML. If it fails to parse as TOML, the raw string is used as a literal.
          
          Examples: - `-c model="o3"` - `-c 'sandbox_permissions=["disk-full-read-access"]'` - `-c
          shell_environment_policy.inherit=all`
```
Result: PASS (exit 0)

## TEST-302 - Help: codex exec --help

```bash
codex exec --help | sed -n "1,40p"
```

Output:
```text
Run Codex non-interactively

Usage: codex exec [OPTIONS] [PROMPT] [COMMAND]

Commands:
  resume  Resume a previous session by id or pick the most recent with --last
  review  Run a code review against the current repository
  help    Print this message or the help of the given subcommand(s)

Arguments:
  [PROMPT]
          Initial instructions for the agent. If not provided as an argument (or if `-` is used),
          instructions are read from stdin

Options:
  -c, --config <key=value>
          Override a configuration value that would otherwise be loaded from `~/.codex/config.toml`.
          Use a dotted path (`foo.bar.baz`) to override nested values. The `value` portion is parsed
          as TOML. If it fails to parse as TOML, the raw string is used as a literal.
          
          Examples: - `-c model="o3"` - `-c 'sandbox_permissions=["disk-full-read-access"]'` - `-c
          shell_environment_policy.inherit=all`

      --enable <FEATURE>
          Enable a feature (repeatable). Equivalent to `-c features.<name>=true`

      --disable <FEATURE>
          Disable a feature (repeatable). Equivalent to `-c features.<name>=false`

  -i, --image <FILE>...
          Optional image(s) to attach to the initial prompt

  -m, --model <MODEL>
          Model the agent should use

      --oss
          Use open-source provider

      --local-provider <OSS_PROVIDER>
          Specify which local provider to use (lmstudio or ollama). If not specified with --oss,
```
Result: PASS (exit 0)

## TEST-303 - Help: codex-exec --help

```bash
codex-exec --help | sed -n "1,40p"
```

Output:
```text
CLI option that captures arbitrary configuration overrides specified as `-c key=value`. It
intentionally keeps both halves **unparsed** so that the calling code can decide how to interpret
the right-hand side

Usage: codex-exec.bin [OPTIONS] [PROMPT] [COMMAND]

Commands:
  resume  Resume a previous session by id or pick the most recent with --last
  review  Run a code review against the current repository
  help    Print this message or the help of the given subcommand(s)

Arguments:
  [PROMPT]
          Initial instructions for the agent. If not provided as an argument (or if `-` is used),
          instructions are read from stdin

Options:
  -c, --config <key=value>
          Override a configuration value that would otherwise be loaded from `~/.codex/config.toml`.
          Use a dotted path (`foo.bar.baz`) to override nested values. The `value` portion is parsed
          as TOML. If it fails to parse as TOML, the raw string is used as a literal.
          
          Examples: - `-c model="o3"` - `-c 'sandbox_permissions=["disk-full-read-access"]'` - `-c
          shell_environment_policy.inherit=all`

  -i, --image <FILE>...
          Optional image(s) to attach to the initial prompt

  -m, --model <MODEL>
          Model the agent should use

      --oss
          Use open-source provider

      --local-provider <OSS_PROVIDER>
          Specify which local provider to use (lmstudio or ollama). If not specified with --oss,
          will use config default or show selection

  -s, --sandbox <SANDBOX_MODE>
          Select the sandbox policy to use when executing model-generated shell commands
```
Result: PASS (exit 0)

## TEST-400 - Non-interactive sanity: list files

```bash
cd ~/codex-test-workspace; codex-exec --sandbox workspace-write --skip-git-repo-check --json "print current directory and list files"
```

Output:
```text
{"type":"thread.started","thread_id":"<redacted>"}
{"type":"turn.started"}
{"type":"item.completed","item":{"id":"item_0","type":"agent_message","text":"Printing the working directory and listing files in `~/codex-test-workspace` now."}}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"/bin/sh -lc 'pwd && ls -la'","aggregated_output":"","exit_code":null,"status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_1","type":"command_execution","command":"/bin/sh -lc 'pwd && ls -la'","aggregated_output":"~/codex-test-workspace\ntotal 12\ndrwx------.  2 termux_user termux_user 3488 Mar 11 18:57 .\ndrwxr-xr-x. 42 termux_user termux_user 8192 Mar 11 18:57 ..\n","exit_code":0,"status":"completed"}}
{"type":"item.completed","item":{"id":"item_2","type":"agent_message","text":"`~/codex-test-workspace`\n\n```text\ntotal 12\ndrwx------.  2 termux_user termux_user 3488 Mar 11 18:57 .\ndrwxr-xr-x. 42 termux_user termux_user 8192 Mar 11 18:57 ..\n```"}}
{"type":"turn.completed","usage":{"input_tokens":16565,"cached_input_tokens":11648,"output_tokens":234}}
```
Result: PASS (exit 0)

## TEST-401 - Non-interactive sanity: create/read hello.txt

```bash
cd ~/codex-test-workspace; codex-exec --sandbox workspace-write --skip-git-repo-check --json "create hello.txt with content 'hello' and then read it"
```

Output:
```text
{"type":"thread.started","thread_id":"<redacted>"}
{"type":"turn.started"}
{"type":"item.completed","item":{"id":"item_0","type":"agent_message","text":"Creating `hello.txt` with the exact content and then reading it back to verify. I’ll run both steps now."}}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"/bin/sh -lc \"printf 'hello' > hello.txt && cat hello.txt\"","aggregated_output":"","exit_code":null,"status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_1","type":"command_execution","command":"/bin/sh -lc \"printf 'hello' > hello.txt && cat hello.txt\"","aggregated_output":"hello","exit_code":0,"status":"completed"}}
{"type":"item.completed","item":{"id":"item_2","type":"agent_message","text":"`hello.txt` created and read successfully.  \nContent:\n\n```text\nhello\n```"}}
{"type":"turn.completed","usage":{"input_tokens":16504,"cached_input_tokens":16256,"output_tokens":171}}
```
Result: PASS (exit 0)

## TEST-500 - Binary architecture guard

```bash
PKG_BIN_DIR="$(npm root -g)/@mmmbuto/codex-cli-termux/bin"; file "$PKG_BIN_DIR/codex"; file "$PKG_BIN_DIR/codex-exec"; file "$PKG_BIN_DIR/codex.bin"; file "$PKG_BIN_DIR/codex-exec.bin"
```

Output:
```text
/data/data/com.termux/files/usr/lib/node_modules/@mmmbuto/codex-cli-termux/bin/codex: a sh script, ASCII text executable
/data/data/com.termux/files/usr/lib/node_modules/@mmmbuto/codex-cli-termux/bin/codex-exec: a sh script, ASCII text executable
/data/data/com.termux/files/usr/lib/node_modules/@mmmbuto/codex-cli-termux/bin/codex.bin: ELF 64-bit LSB pie executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /system/bin/linker64, for Android 21, built by NDK r27 (12077973), stripped
/data/data/com.termux/files/usr/lib/node_modules/@mmmbuto/codex-cli-termux/bin/codex-exec.bin: ELF 64-bit LSB pie executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /system/bin/linker64, for Android 21, built by NDK r27 (12077973), stripped
```
Result: PASS (exit 0)

## TEST-600 - Network-path smoke (no panic)

```bash
cd ~/codex-test-workspace; codex-exec --sandbox workspace-write --skip-git-repo-check --json "run one network check with curl -I https://www.google.com and report the first HTTP status line only"
```

Output:
```text
{"type":"thread.started","thread_id":"<redacted>"}
{"type":"turn.started"}
{"type":"item.completed","item":{"id":"item_0","type":"agent_message","text":"Running a single `curl -I` request now and I’ll return only the first HTTP status line."}}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"/bin/sh -lc 'curl -I https://www.google.com | head -n 1'","aggregated_output":"","exit_code":null,"status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_1","type":"command_execution","command":"/bin/sh -lc 'curl -I https://www.google.com | head -n 1'","aggregated_output":"HTTP/2 200 \r\n\r  0      0   0      0   0      0      0      0                              0\r  0      0   0      0   0      0      0      0                              0\r  0      0   0      0   0      0      0      0                              0\n","exit_code":0,"status":"completed"}}
{"type":"item.completed","item":{"id":"item_2","type":"agent_message","text":"HTTP/2 200"}}
{"type":"turn.completed","usage":{"input_tokens":16624,"cached_input_tokens":11648,"output_tokens":121}}
```
Result: PASS (exit 0)

## TEST-700 - Installed binary linkage guard

```bash
PKG_BIN_DIR="$(npm root -g)/@mmmbuto/codex-cli-termux/bin"; READELF_BIN="$(command -v readelf || command -v llvm-readelf || true)"; if [ -n "$READELF_BIN" ]; then echo "Using: $READELF_BIN"; "$READELF_BIN" -d "$PKG_BIN_DIR/codex.bin" | rg "NEEDED|libc\+\+|OpenSLES|oboe" || true; "$READELF_BIN" -d "$PKG_BIN_DIR/codex-exec.bin" | rg "NEEDED|libc\+\+|OpenSLES|oboe" || true; else echo "SKIP: readelf/llvm-readelf not available"; fi
```

Output:
```text
Using: /data/data/com.termux/files/usr/bin/readelf
  0x0000000000000001 (NEEDED)       Shared library: [libz.so]
  0x0000000000000001 (NEEDED)       Shared library: [libdl.so]
  0x0000000000000001 (NEEDED)       Shared library: [libm.so]
  0x0000000000000001 (NEEDED)       Shared library: [libc.so]
  0x0000000000000001 (NEEDED)       Shared library: [libz.so]
  0x0000000000000001 (NEEDED)       Shared library: [libdl.so]
  0x0000000000000001 (NEEDED)       Shared library: [libm.so]
  0x0000000000000001 (NEEDED)       Shared library: [libc.so]
```
Result: PASS (exit 0)

## TEST-800 - Wrapper routing guard: fork/debug

```bash
PKG_BIN_DIR="$(npm root -g)/@mmmbuto/codex-cli-termux/bin"; node "$PKG_BIN_DIR/codex.js" fork --help | sed -n "1,6p"; node "$PKG_BIN_DIR/codex.js" debug --help | sed -n "1,6p"
```

Output:
```text
Fork a previous interactive session (picker by default; use --last to fork the most recent)

Usage: codex fork [OPTIONS] [SESSION_ID] [PROMPT]

Arguments:
  [SESSION_ID]
Debugging tools

Usage: codex debug [OPTIONS] <COMMAND>

Commands:
  app-server  Tooling: helps debug the app server
```
Result: PASS (exit 0)

## TEST-900 - Termux environment checks

```bash
uname -a; echo "$PREFIX"; node --version; npm --version; command -v termux-open-url || true
```

Output:
```text
Linux localhost 4.19.110-perf+ #1 SMP PREEMPT Thu Nov 16 20:10:09 CST 2023 aarch64 Android
/data/data/com.termux/files/usr
v25.8.0
11.11.0
/data/data/com.termux/files/usr/bin/termux-open-url
```
Result: PASS (exit 0)

## Summary
- PASS: 14
- FAIL: 0
- Report file: ~/Dev/codex-termux/test-reports/latest/0.114.0-termux/CODEX_TEST_REPORT_v0.114.0-termux_rerun_20260311-185702.md
