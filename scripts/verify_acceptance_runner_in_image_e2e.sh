#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/sbin/senior-zero-acceptance-runner"
OUTPUT="$(bash "$SCRIPT" --dry-run)"

echo "$OUTPUT" | grep -q "ACCEPTANCE_RUNNER_DRY_RUN"
echo "$OUTPUT" | grep -q "senior-zero-install-target-smoke"
echo "$OUTPUT" | grep -q "senior-zero-security-audit"
echo "$OUTPUT" | grep -q "senior-zero-rollback-rehearsal"
echo "$OUTPUT" | grep -q "senior-zero-preflight-report"
echo "$OUTPUT" | grep -q "senior-zero-app-center-policy"

echo "E2E PASS: acceptance runner dry-run is coherent"
