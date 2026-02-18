#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/sbin/senior-zero-security-audit"
OUTPUT="$(bash "$SCRIPT" --dry-run)"

echo "$OUTPUT" | grep -q "SECURITY_AUDIT_DRY_RUN"
echo "$OUTPUT" | grep -q "systemctl is-enabled unattended-upgrades"
echo "$OUTPUT" | grep -q "52unattended-upgrades-senior-zero"
echo "$OUTPUT" | grep -q "90-senior-zero-security.pref"
echo "$OUTPUT" | grep -q "Allowed-Origins"
echo "$OUTPUT" | grep -q "Pin-Priority: 990"
echo "$OUTPUT" | grep -q "Pin-Priority: 500"

echo "E2E PASS: security audit dry-run is coherent"
