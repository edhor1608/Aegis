#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BIN_DIR="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin"

check_dry_run() {
  local cmd="$1"
  local marker="$2"
  local output
  output="$("$BIN_DIR/$cmd" --dry-run)"
  echo "$output" | grep -q "$marker"
}

check_dry_run "senior-zero-preflight-report" "SENIOR_ZERO_PREFLIGHT_REPORT_DRY_RUN"
check_dry_run "senior-zero-app-center-policy" "SENIOR_ZERO_APP_CENTER_POLICY_DRY_RUN"
check_dry_run "senior-zero-acceptance-runner" "ACCEPTANCE_RUNNER_DRY_RUN"
check_dry_run "senior-zero-install-target-smoke" "INSTALL_TARGET_SMOKE_DRY_RUN"
check_dry_run "senior-zero-rollback-rehearsal" "ROLLBACK_REHEARSAL_DRY_RUN"
check_dry_run "senior-zero-rollback-bootstrap" "ROLLBACK_BOOTSTRAP_DRY_RUN"
check_dry_run "senior-zero-security-audit" "SECURITY_AUDIT_DRY_RUN"

echo "E2E PASS: user-path shims forward to in-image commands"
