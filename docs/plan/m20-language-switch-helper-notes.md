# Milestone 20 Notes (DE/EN Language Switch Helper)

## Problem

DE/EN baseline existed, but there was no simple user-facing command to switch session language intent without manual config edits.

## What Was Added

- New in-image helper:
  - `/usr/local/bin/senior-zero-language-switch`

## Behavior

- `--print-current`: prints current `LANG` value.
- `--to en`: sets session intent to `en_US.UTF-8`.
- `--to de`: sets session intent to `de_DE.UTF-8`.
- Writes language exports to:
  - `~/.xsessionrc`
- Returns:
  - `SENIOR_ZERO_LANGUAGE_SWITCH_APPLIED: ...`
  - `RELOGIN_REQUIRED`
- Supports dry-run mode:
  - `SENIOR_ZERO_LANGUAGE_SWITCH_DRY_RUN`

## Manual VM Test

```bash
senior-zero-language-switch --to de --dry-run
senior-zero-language-switch --to en --dry-run
senior-zero-language-switch --print-current --dry-run
```
