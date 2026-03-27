# Termux Text-to-Speech Skill

## Description
This skill enables text-to-speech functionality on Termux devices using the `termux-tts-speak` command from Termux:API package.

## Requirements
- Termux:API app installed on Android device
- `termux-tts-speak` command available in PATH
- Text-to-speech permissions granted to Termux

## Usage
Use `/speak <text>` to have the text spoken aloud via Android's text-to-speech engine.

## Command Definition
```yaml
name: speak
description: Speak text using Android's text-to-speech engine
arguments:
  - name: text
    type: string
    description: Text to speak
    required: true
```

## Implementation
```bash
#!/bin/bash
# Check if termux-tts-speak is available
if command -v termux-tts-speak >/dev/null 2>&1; then
    # Execute the text-to-speech command
    termux-tts-speak "$1"
    echo "Speaking: $1"
else
    echo "Error: termux-tts-speak not available. Please install Termux:API app."
    exit 1
fi
```

## Notes
- This skill is only effective on Termux-enabled devices
- No modifications to core Codex code required
- Safe to use with future Codex updates
