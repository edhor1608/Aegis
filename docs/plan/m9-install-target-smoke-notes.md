# Milestone 9 Notes (Install-Target Smoke Gate)

## Problem

We had live-session smoke coverage, but no dedicated gate for validating a disk-installed system after first boot.

## What Was Added

- `scripts/install_target_smoke.sh`
  - Validates install-target baseline for rollback-ready systems.
  - Checks unattended upgrades + Senior Zero apt policy files.
  - Checks snapper timers/state and bootstrap completion marker.
  - Checks DE/EN locale baseline.
- `scripts/verify_install_target_smoke_e2e.sh`
  - Dry-run coherence gate for CI/TDD.
- TDD coverage layers:
  - integration: `tests/integration/test_install_target_smoke_contract.py`
  - snapshot: `tests/snapshot/test_install_target_smoke_snapshot.py`
  - e2e: `tests/e2e/test_install_target_smoke_e2e.py`

## Manual VM Test (Installed System)

1. Install ISO to disk with root filesystem set to `btrfs`.
2. Boot into installed system.
3. Run:

```bash
sudo bash /path/to/repo/scripts/install_target_smoke.sh
```

4. Expected tail output:
- `PASS: snapper root config present`
- `PASS: snapper-timeline.timer active`
- `PASS: snapper-cleanup.timer active`
- `INSTALL_TARGET_SMOKE_PASS`

## Current Constraint

- The gate is intentionally strict: if root is not `btrfs`, it fails (rollback-capable install is required baseline).
