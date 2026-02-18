# Milestone 24 Notes (Runtime Profile Baseline)

## Problem

Low-end hardware checks were manual and inconsistent; there was no dedicated profile command for 4 GB / legacy i3 targets.

## What Was Added

- New command:
  - `/usr/local/bin/senior-zero-runtime-profile`
- New desktop entry:
  - `/etc/skel/Desktop/Senior Zero Runtime Profile.desktop`

## Behavior

- `--dry-run` prints the expected profile schema and baseline labels
- Runtime mode prints:
  - baseline RAM target
  - target CPU class label
  - boot time
  - memory totals/usage/available
  - CPU model
- Status output:
  - `SENIOR_ZERO_RUNTIME_PROFILE_OK` when RAM baseline is met
  - `SENIOR_ZERO_RUNTIME_PROFILE_WARN` otherwise
- `SENIOR_ZERO_RUNTIME_PROFILE_FAKE=1` provides deterministic output for tests

## Manual VM Test

```bash
senior-zero-runtime-profile --dry-run
senior-zero-runtime-profile
```
