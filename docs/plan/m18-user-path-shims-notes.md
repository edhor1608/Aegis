# Milestone 18 Notes (User PATH Command Shims)

## Problem

The in-image verification commands were installed in `/usr/local/sbin`, which was not on the default non-root user PATH in the VM. Commands worked only with full paths.

## What Was Added

- Added `/usr/local/bin` wrappers for all current `senior-zero-*` commands:
  - `senior-zero-acceptance-runner`
  - `senior-zero-app-center-policy`
  - `senior-zero-install-target-smoke`
  - `senior-zero-preflight-report`
  - `senior-zero-rollback-bootstrap`
  - `senior-zero-rollback-rehearsal`
  - `senior-zero-security-audit`
- Wrapper behavior:
  - Prefer `/usr/local/sbin/<cmd>`
  - Fallback to sibling `../sbin/<cmd>` for repository-side e2e tests

## TDD Coverage

- integration:
  - `tests/integration/test_user_path_shims_in_image_contract.py`
- snapshot:
  - `tests/snapshot/test_user_path_shims_in_image_snapshot.py`
- e2e:
  - `tests/e2e/test_user_path_shims_in_image_e2e.py`
  - `scripts/verify_user_path_shims_in_image_e2e.sh`

## Manual VM Test

Run as normal user (without full path):

```bash
senior-zero-preflight-report --dry-run
senior-zero-app-center-policy --dry-run
senior-zero-acceptance-runner --dry-run
```
