# Milestone 16 Notes (Extended Acceptance Runner)

## Problem

Acceptance validation still required separate manual execution for the new preflight and app-center policy checks.

## What Was Added

- Extended in-image runner:
  - `/usr/local/sbin/senior-zero-acceptance-runner`
- Updated dry-run verifier:
  - `scripts/verify_acceptance_runner_in_image_e2e.sh`
- Updated TDD coverage:
  - integration: `tests/integration/test_acceptance_runner_in_image_contract.py`
  - snapshot: `tests/snapshot/test_acceptance_runner_in_image_snapshot.py`
  - e2e: `tests/e2e/test_acceptance_runner_in_image_e2e.py`

## Runtime Behavior

The runner now executes, in order:
1. `/usr/local/sbin/senior-zero-install-target-smoke`
2. `/usr/local/sbin/senior-zero-security-audit`
3. `/usr/local/sbin/senior-zero-rollback-rehearsal`
4. `/usr/local/sbin/senior-zero-preflight-report`
5. `/usr/local/sbin/senior-zero-app-center-policy`

It fails fast on first error and returns `ACCEPTANCE_RUNNER_PASS` only when all stages pass.

## Manual VM Test

```bash
sudo /usr/local/sbin/senior-zero-acceptance-runner
```

Expected final line:
- `ACCEPTANCE_RUNNER_PASS`
