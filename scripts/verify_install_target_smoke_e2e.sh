#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="$(bash "$ROOT_DIR/scripts/install_target_smoke.sh" --dry-run)"

echo "$OUTPUT" | grep -q "INSTALL_TARGET_SMOKE_DRY_RUN"
echo "$OUTPUT" | grep -q "findmnt -n -o FSTYPE /"
echo "$OUTPUT" | grep -q "systemctl is-enabled unattended-upgrades"
echo "$OUTPUT" | grep -q "/etc/apt/apt.conf.d/52unattended-upgrades-senior-zero"
echo "$OUTPUT" | grep -q "/etc/apt/preferences.d/90-senior-zero-security.pref"
echo "$OUTPUT" | grep -q "snapper-timeline.timer"
echo "$OUTPUT" | grep -q "snapper-cleanup.timer"
echo "$OUTPUT" | grep -q "/var/lib/senior-zero/rollback-bootstrap.done"
echo "$OUTPUT" | grep -q "de_DE.utf8"
echo "$OUTPUT" | grep -q "en_US.utf8"

echo "E2E PASS: install-target smoke dry-run is coherent"
