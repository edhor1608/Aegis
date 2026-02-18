# Milestone 12 Notes (In-Image Security Audit)

## Problem

We had security policy files configured in image build, but no explicit installed-system command to validate policy integrity quickly.

## What Was Added

- In-image command:
  - `/usr/local/sbin/senior-zero-security-audit`
- Dry-run verifier:
  - `scripts/verify_security_audit_in_image_e2e.sh`
- TDD coverage:
  - integration: `tests/integration/test_security_audit_in_image_contract.py`
  - snapshot: `tests/snapshot/test_security_audit_in_image_snapshot.py`
  - e2e: `tests/e2e/test_security_audit_in_image_e2e.py`

## Runtime Checks Performed

- `unattended-upgrades` enabled
- Senior Zero unattended-upgrades policy file exists and includes `Allowed-Origins` + `security`
- APT pinning policy file exists and includes priorities `990` (security) and `500` (stable)
- automatic reboot remains disabled

## Manual VM Test

```bash
sudo /usr/local/sbin/senior-zero-security-audit
```

Expected tail output:
- `PASS: automatic reboot stays disabled`
- `SECURITY_AUDIT_PASS`
