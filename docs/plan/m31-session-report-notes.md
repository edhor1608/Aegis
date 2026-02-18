# M31 - Session Report

## Goal
Add a one-command session report helper for current desktop session triage, available from terminal and desktop.

## Delivered
- `senior-zero-session-report` in image includes.
- Desktop entry: `Senior Zero Session Report.desktop`.
- TDD coverage:
  - integration contract tests
  - snapshot tests
  - e2e dry-run and fake-runtime gate

## Verification
- `make test` passes with M31 tests included.

## Operator usage (inside VM)
- Terminal: `/usr/local/sbin/senior-zero-session-report --dry-run`
- Desktop: click `Senior Zero Session Report` icon
