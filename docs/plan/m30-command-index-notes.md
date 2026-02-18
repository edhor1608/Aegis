# Milestone 30 Notes (Command Index)

## Problem

Users and testers needed a quick visibility command to confirm which core Senior Zero helper commands are available.

## What Was Added

- New command:
  - `/usr/local/bin/senior-zero-command-index`
- New desktop entry:
  - `/etc/skel/Desktop/Senior Zero Command Index.desktop`

## Behavior

- `--dry-run` prints the planned command inventory.
- Runtime mode reports availability for:
  - preflight report
  - update check
  - runtime profile
  - network check
  - storage check
  - self-check
- Emits overall readiness marker (`READY` or `PARTIAL`).
- `SENIOR_ZERO_COMMAND_INDEX_FAKE=1` provides deterministic all-available mode for tests.

## Manual VM Test

```bash
senior-zero-command-index --dry-run
senior-zero-command-index
```
