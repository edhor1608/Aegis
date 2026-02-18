# M32 - Support Bundle

## Goal
Add a single helper that produces a compact support readiness bundle file from core system checks.

## Delivered
- `senior-zero-support-bundle` in image includes.
- Desktop entry: `Senior Zero Support Bundle.desktop`.
- TDD coverage:
  - integration contract tests
  - snapshot tests
  - e2e dry-run and fake-runtime gate

## Verification
- `make test` passes with M32 tests included.

## Operator usage (inside VM)
- Terminal: `/usr/local/bin/senior-zero-support-bundle --dry-run`
- Run fake mode in VM test shell:
  - `SENIOR_ZERO_SUPPORT_BUNDLE_FAKE=1 senior-zero-support-bundle`
- Desktop: click `Senior Zero Support Bundle` icon
