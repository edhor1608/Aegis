#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="$(bash "$ROOT_DIR/scripts/vm_runtime_smoke.sh" --dry-run)"

echo "$OUTPUT" | grep -q "VM_SMOKE_DRY_RUN"
echo "$OUTPUT" | grep -q "whoami | grep -qx 'user'"
echo "$OUTPUT" | grep -q "systemctl is-enabled unattended-upgrades | grep -qx 'enabled'"
echo "$OUTPUT" | grep -q "systemctl is-active NetworkManager | grep -qx 'active'"
echo "$OUTPUT" | grep -q "locale -a"
echo "$OUTPUT" | grep -q "de_DE.utf8"
echo "$OUTPUT" | grep -q "en_US.utf8"
echo "$OUTPUT" | grep -q "senior-zero-preflight-report"
echo "$OUTPUT" | grep -q "senior-zero-app-center-policy"
echo "$OUTPUT" | grep -q "senior-zero-acceptance-runner --dry-run"

echo "E2E PASS: VM runtime smoke dry-run is coherent"
