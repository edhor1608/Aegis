# Milestone 29 Notes (Storage/Snapshot Readiness Check)

## Problem

Users and testers needed a quick check for storage prerequisites tied to rollback behavior.

## What Was Added

- New command:
  - `/usr/local/bin/senior-zero-storage-check`
- New desktop entry:
  - `/etc/skel/Desktop/Senior Zero Storage Check.desktop`

## Behavior

- `--dry-run` prints planned checks.
- Runtime mode checks:
  - `btrfs` command availability
  - `snapper` command availability
  - root filesystem type (Btrfs expectation)
  - root usage percentage
- Emits overall result marker (`OK` or `ATTENTION`).
- `SENIOR_ZERO_STORAGE_CHECK_FAKE=1` provides deterministic all-pass mode for tests.

## Manual VM Test

```bash
senior-zero-storage-check --dry-run
senior-zero-storage-check
```
