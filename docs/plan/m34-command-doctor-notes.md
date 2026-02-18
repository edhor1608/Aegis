# M34 - Command Doctor

## Goal
Add a quick command-readiness doctor for core support helper commands.

## Delivered
- `senior-zero-command-doctor` in image includes.
- Desktop entry: `Senior Zero Command Doctor.desktop`.
- TDD coverage:
  - integration contract tests
  - snapshot tests
  - e2e dry-run and fake-runtime gate

## Verification
- `make test` passes with M34 tests included.

## Operator usage (inside VM)
- Terminal: `/usr/local/bin/senior-zero-command-doctor --dry-run`
- Fake execution for deterministic output:
  - `SENIOR_ZERO_COMMAND_DOCTOR_FAKE=1 senior-zero-command-doctor`
- Desktop: click `Senior Zero Command Doctor` icon
