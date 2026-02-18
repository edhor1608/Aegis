#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/sbin/senior-zero-install-target-smoke"
OUTPUT="$(bash "$SCRIPT" --dry-run)"

echo "$OUTPUT" | grep -q "INSTALL_TARGET_SMOKE_DRY_RUN"
echo "$OUTPUT" | grep -q "command -v snapper"
echo "$OUTPUT" | grep -q "findmnt -n -o FSTYPE /"
echo "$OUTPUT" | grep -q "systemctl is-enabled unattended-upgrades"
echo "$OUTPUT" | grep -q "/etc/apt/apt.conf.d/52unattended-upgrades-senior-zero"
echo "$OUTPUT" | grep -q "/etc/apt/preferences.d/90-senior-zero-security.pref"
echo "$OUTPUT" | grep -q "snapper-timeline.timer"
echo "$OUTPUT" | grep -q "snapper-cleanup.timer"
echo "$OUTPUT" | grep -q "/var/lib/senior-zero/rollback-bootstrap.done"
echo "$OUTPUT" | grep -Fq "de_DE\\.(utf8|utf-8)"
echo "$OUTPUT" | grep -Fq "en_US\\.(utf8|utf-8)"

echo "E2E PASS: in-image install-target smoke dry-run is coherent"
