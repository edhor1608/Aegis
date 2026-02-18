# M35 - Acceptance Runner Expansion

## Goal
Extend the acceptance runner chain so it also validates newly introduced support-facing helper commands.

## Delivered
- Updated in-image acceptance runner command chain to include:
  - `senior-zero-support-bundle`
  - `senior-zero-daily-checklist`
  - `senior-zero-command-doctor`
- Updated test coverage:
  - integration contract expectations
  - snapshot of acceptance runner script
  - e2e dry-run gate expectations

## Verification
- `make test` passes with expanded acceptance-runner checks.

## Operator usage (inside VM)
- `senior-zero-acceptance-runner --dry-run`
