# M38 - Command Index Parity

## Drift fixed
`senior-zero-command-index` had drifted behind the actual helper command surface after M31-M37 additions.

## Goal
Bring command index output back in sync with current helper inventory.

## Delivered
- Expanded command-index planned list and runtime checks to include:
  - `senior-zero-session-report`
  - `senior-zero-support-bundle`
  - `senior-zero-daily-checklist`
  - `senior-zero-command-doctor`
  - `senior-zero-acceptance-runner`
- Updated command-index TDD coverage:
  - integration contract expectations
  - script snapshot
  - e2e verifier gate

## Verification
- `make test` passes with M38 included.

## Operator usage (inside VM)
- `senior-zero-command-index --dry-run`
- `SENIOR_ZERO_COMMAND_INDEX_FAKE=1 senior-zero-command-index`
