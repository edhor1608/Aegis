# Milestone 14 Notes (In-Image Preflight Report)

## Problem

Manual VM verification still required remembering multiple commands. We needed one command that reports key baseline readiness checks in a single output.

## What Was Added

- In-image command:
  - `/usr/local/sbin/senior-zero-preflight-report`
- Dry-run verifier:
  - `scripts/verify_preflight_report_in_image_e2e.sh`
- TDD coverage:
  - integration: `tests/integration/test_preflight_report_in_image_contract.py`
  - snapshot: `tests/snapshot/test_preflight_report_in_image_snapshot.py`
  - e2e: `tests/e2e/test_preflight_report_in_image_e2e.py`

## Runtime Behavior

The report runs and prints PASS/FAIL for:
1. `networkmanager_active`
2. `unattended_upgrades_enabled`
3. `locale_en_us_present`
4. `locale_de_de_present`
5. `snapper_available`
6. `btrfs_available`

It returns `SENIOR_ZERO_PREFLIGHT_REPORT_PASS` only when all checks pass.

## Manual VM Test

```bash
sudo /usr/local/sbin/senior-zero-preflight-report
```

Expected final line:
- `SENIOR_ZERO_PREFLIGHT_REPORT_PASS`
