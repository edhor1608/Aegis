# M37 - Launcher Acceptance Action

## Goal
Expose acceptance dry-run through the simplified launcher action catalog.

## Delivered
- Extended `senior-zero-launcher` with a new action:
  - `acceptance -> senior-zero-acceptance-runner --dry-run`
- Updated launcher TDD coverage:
  - integration contract expectations
  - script snapshot
  - e2e action flow checks

## Verification
- `make test` passes with M37 launcher updates.

## Operator usage (inside VM)
- `senior-zero-launcher --dry-run` (lists `action_acceptance`)
- `senior-zero-launcher --action acceptance`
