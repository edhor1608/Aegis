# Milestone 13 Notes (In-Image Acceptance Runner)

## Problem

Post-install verification required manually running multiple separate commands. We needed one top-level runner for a single acceptance pass.

## What Was Added

- In-image runner:
  - `/usr/local/sbin/senior-zero-acceptance-runner`
- Dry-run verifier:
  - `scripts/verify_acceptance_runner_in_image_e2e.sh`
- TDD coverage:
  - integration: `tests/integration/test_acceptance_runner_in_image_contract.py`
  - snapshot: `tests/snapshot/test_acceptance_runner_in_image_snapshot.py`
  - e2e: `tests/e2e/test_acceptance_runner_in_image_e2e.py`

## Runtime Behavior

The runner executes, in order:
1. `/usr/local/sbin/senior-zero-install-target-smoke`
2. `/usr/local/sbin/senior-zero-security-audit`
3. `/usr/local/sbin/senior-zero-rollback-rehearsal`

It fails fast on first error and returns `ACCEPTANCE_RUNNER_PASS` only when all stages pass.

## Manual VM Test

```bash
sudo /usr/local/sbin/senior-zero-acceptance-runner
```

Expected final line:
- `ACCEPTANCE_RUNNER_PASS`
