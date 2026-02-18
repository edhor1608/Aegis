# Milestone 15 Notes (In-Image App Center Policy Baseline)

## Problem

The app-center decision (curated defaults + explicit warning for "More Apps") existed only in docs. We needed image-level policy artifacts and a single verification command.

## What Was Added

- In-image policy command:
  - `/usr/local/sbin/senior-zero-app-center-policy`
- In-image policy data:
  - `/etc/senior-zero/app-center/curated-default-packages.txt`
  - `/etc/senior-zero/app-center/more-apps-warning.txt`
- Dry-run verifier:
  - `scripts/verify_app_center_policy_in_image_e2e.sh`
- TDD coverage:
  - integration: `tests/integration/test_app_center_policy_in_image_contract.py`
  - snapshot: `tests/snapshot/test_app_center_policy_in_image_snapshot.py`
  - e2e: `tests/e2e/test_app_center_policy_in_image_e2e.py`

## Runtime Behavior

The policy command validates the two policy files, enforces seed-curated packages, then prints policy content and:
- `SENIOR_ZERO_APP_CENTER_POLICY_PASS`

## Manual VM Test

```bash
sudo /usr/local/sbin/senior-zero-app-center-policy
```

Expected final line:
- `SENIOR_ZERO_APP_CENTER_POLICY_PASS`
