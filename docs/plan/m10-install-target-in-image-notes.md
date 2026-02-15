# Milestone 10 Notes (In-Image Install-Target Smoke)

## Problem

Install-target smoke checks existed in the repository, but were not embedded into the generated ISO. VM users could not run them directly after install without extra repo setup.

## What Was Added

- In-image smoke script included via live-build chroot includes:
  - `/usr/local/sbin/senior-zero-install-target-smoke`
- E2E dry-run verifier for the in-image script contract:
  - `scripts/verify_install_target_in_image_e2e.sh`
- New TDD layers:
  - integration: `tests/integration/test_install_target_in_image_contract.py`
  - snapshot: `tests/snapshot/test_install_target_in_image_snapshot.py`
  - e2e: `tests/e2e/test_install_target_in_image_e2e.py`

## Manual VM Validation (Installed System)

Run on installed VM:

```bash
sudo /usr/local/sbin/senior-zero-install-target-smoke
```

Expected successful tail lines:
- `PASS: snapper root config present`
- `PASS: snapper-timeline.timer active`
- `PASS: snapper-cleanup.timer active`
- `INSTALL_TARGET_SMOKE_PASS`

## Constraint

The smoke gate intentionally fails when root is not `btrfs`; this preserves rollback-capable baseline requirements.
