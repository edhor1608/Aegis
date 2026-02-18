#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/sbin/senior-zero-preflight-report"
OUTPUT="$(bash "$SCRIPT" --dry-run)"

echo "$OUTPUT" | grep -q "SENIOR_ZERO_PREFLIGHT_REPORT_DRY_RUN"
echo "$OUTPUT" | grep -q "networkmanager_active"
echo "$OUTPUT" | grep -q "unattended_upgrades_enabled"
echo "$OUTPUT" | grep -q "locale_en_us_present"
echo "$OUTPUT" | grep -q "locale_de_de_present"
echo "$OUTPUT" | grep -q "snapper_available"
echo "$OUTPUT" | grep -q "btrfs_available"

echo "E2E PASS: preflight report dry-run is coherent"
