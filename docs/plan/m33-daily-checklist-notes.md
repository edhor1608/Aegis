# M33 - Daily Checklist

## Goal
Provide a single daily checklist command for quick “is everything basic-ready” verification.

## Delivered
- `senior-zero-daily-checklist` in image includes.
- Desktop entry: `Senior Zero Daily Checklist.desktop`.
- TDD coverage:
  - integration contract tests
  - snapshot tests
  - e2e dry-run and fake-runtime gate

## Verification
- `make test` passes with M33 tests included.

## Operator usage (inside VM)
- Terminal: `/usr/local/bin/senior-zero-daily-checklist --dry-run`
- Fake execution for deterministic output:
  - `SENIOR_ZERO_DAILY_CHECKLIST_FAKE=1 senior-zero-daily-checklist`
- Desktop: click `Senior Zero Daily Checklist` icon
