# Milestone 22 Notes (First-Boot Onboarding Autostart)

## Problem

The image included help content but did not actively surface onboarding on first login.

## What Was Added

- New command:
  - `/usr/local/bin/senior-zero-onboarding`
- New autostart entry:
  - `/etc/xdg/autostart/senior-zero-onboarding.desktop`

## Behavior

- First run:
  - Creates `~/.config/senior-zero/onboarding.done`
  - Opens welcome help text when `xdg-open` is available
  - Prints `SENIOR_ZERO_ONBOARDING_SHOWN`
- Subsequent runs:
  - Prints `SENIOR_ZERO_ONBOARDING_ALREADY_DONE`
- Dry-run:
  - Prints `SENIOR_ZERO_ONBOARDING_DRY_RUN`

## Manual VM Test

```bash
senior-zero-onboarding --dry-run
senior-zero-onboarding
senior-zero-onboarding
```
