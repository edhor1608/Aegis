# Milestone 11 Notes (In-Image Rollback Rehearsal)

## Problem

We validated rollback readiness and bootstrap state, but we did not yet have a direct installed-system rehearsal command to prove snapshot create/list/delete behavior in-place.

## What Was Added

- In-image command:
  - `/usr/local/sbin/senior-zero-rollback-rehearsal`
- Dry-run contract verifier:
  - `scripts/verify_rollback_rehearsal_in_image_e2e.sh`
- TDD coverage:
  - integration: `tests/integration/test_rollback_rehearsal_in_image_contract.py`
  - snapshot: `tests/snapshot/test_rollback_rehearsal_in_image_snapshot.py`
  - e2e: `tests/e2e/test_rollback_rehearsal_in_image_e2e.py`

## Manual VM Test

Run on installed btrfs-based VM:

```bash
sudo /usr/local/sbin/senior-zero-rollback-rehearsal
```

Expected key output:
- `PASS: created snapshot id=...`
- `PASS: snapshot visible in list`
- `PASS: snapshot cleanup complete`
- `ROLLBACK_REHEARSAL_PASS`

## Constraint

This rehearsal intentionally requires `btrfs` root and `snapper` root config; otherwise it fails fast.
