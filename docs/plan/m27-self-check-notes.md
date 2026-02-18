# Milestone 27 Notes (Self-Check Runner)

## Problem

Users needed a single command that summarizes whether core Senior Zero maintenance tools are callable.

## What Was Added

- New command:
  - `/usr/local/bin/senior-zero-self-check`
- New desktop entry:
  - `/etc/skel/Desktop/Senior Zero Self Check.desktop`

## Behavior

- `--dry-run` prints the planned checks.
- Runtime mode executes dry-run checks for:
  - preflight report
  - update check
  - runtime profile
  - diagnostics report
- Writes `~/Documents/senior-zero-self-check.txt` with pass/fail results.
- Emits overall result marker (`OK` or `ATTENTION`).
- `SENIOR_ZERO_SELF_CHECK_FAKE=1` provides deterministic all-pass mode for tests.

## Manual VM Test

```bash
senior-zero-self-check --dry-run
senior-zero-self-check
cat ~/Documents/senior-zero-self-check.txt
```
