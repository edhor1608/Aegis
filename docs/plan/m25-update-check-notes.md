# Milestone 25 Notes (Security Update Check Entry)

## Problem

Users had no simple one-click way to verify that the security update policy wiring is active.

## What Was Added

- New command:
  - `/usr/local/bin/senior-zero-update-check`
- New desktop entry:
  - `/etc/skel/Desktop/Senior Zero Update Check.desktop`

## Behavior

- `--dry-run` prints policy targets and scope marker.
- Runtime mode reports:
  - security pin file presence
  - unattended-upgrades enabled state
  - attention/ok summary marker
- `SENIOR_ZERO_UPDATE_CHECK_FAKE=1` provides deterministic output for verification.

## Manual VM Test

```bash
senior-zero-update-check --dry-run
senior-zero-update-check
```
