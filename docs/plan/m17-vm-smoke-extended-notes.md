# Milestone 17 Notes (Extended VM Smoke Script)

## Problem

VM smoke checks validated baseline services/locales but did not assert availability of the newly added in-image verification commands.

## What Was Added

- Extended host-side VM smoke helper:
  - `scripts/vm_runtime_smoke.sh`
- Extended dry-run verifier:
  - `scripts/verify_vm_runtime_smoke_e2e.sh`
- Updated TDD coverage:
  - integration: `tests/integration/test_live_build_pipeline_contract.py`
  - snapshot: `tests/snapshot/test_vm_runtime_smoke_snapshot.py`
  - e2e: `tests/e2e/test_vm_runtime_smoke_e2e.py`

## Runtime Behavior

VM smoke now also checks:
1. `senior-zero-preflight-report` exists
2. `senior-zero-app-center-policy` exists
3. `senior-zero-acceptance-runner --dry-run` returns `ACCEPTANCE_RUNNER_DRY_RUN`

## Manual VM Test

```bash
bash /usr/local/sbin/senior-zero-acceptance-runner --dry-run
```

And for host-side check helper:

```bash
bash scripts/vm_runtime_smoke.sh --dry-run
```
