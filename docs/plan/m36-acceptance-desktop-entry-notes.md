# M36 - Acceptance Desktop Entry

## Goal
Surface acceptance dry-run directly in the desktop UI so testers can launch it without typing commands.

## Delivered
- Added desktop entry: `Senior Zero Acceptance Runner.desktop`
- Added TDD coverage:
  - integration contract test
  - snapshot test
  - e2e gate script

## Verification
- `make test` passes with M36 tests included.

## Operator usage (inside VM)
- Click `Senior Zero Acceptance Runner` on desktop
- Equivalent terminal command:
  - `senior-zero-acceptance-runner --dry-run`
