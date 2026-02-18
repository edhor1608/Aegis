# Milestone 26 Notes (Local Diagnostics Report)

## Problem

There was no simple built-in way for users to generate a local diagnostics snapshot for troubleshooting.

## What Was Added

- New command:
  - `/usr/local/bin/senior-zero-diagnostics-report`
- New desktop entry:
  - `/etc/skel/Desktop/Senior Zero Diagnostics Report.desktop`

## Behavior

- `--dry-run` prints report output path and expected schema fields.
- Runtime mode writes `~/Documents/senior-zero-diagnostics.txt` with:
  - timestamp
  - user
  - locale
  - NetworkManager active state
  - unattended-upgrades enabled state
  - memory total/available
- `SENIOR_ZERO_DIAGNOSTICS_REPORT_FAKE=1` provides deterministic output for tests.

## Manual VM Test

```bash
senior-zero-diagnostics-report --dry-run
senior-zero-diagnostics-report
cat ~/Documents/senior-zero-diagnostics.txt
```
