#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-update-check"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Update Check.desktop"

DRY_OUTPUT="$(bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_UPDATE_CHECK_DRY_RUN"
echo "$DRY_OUTPUT" | grep -q "policy_file=/etc/apt/preferences.d/90-senior-zero-security.pref"
echo "$DRY_OUTPUT" | grep -q "unattended_service=unattended-upgrades"

RUN_OUTPUT="$(SENIOR_ZERO_UPDATE_CHECK_FAKE=1 bash "$SCRIPT")"
echo "$RUN_OUTPUT" | grep -q "security_pin_present=yes"
echo "$RUN_OUTPUT" | grep -q "unattended_upgrades_enabled=yes"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_UPDATE_CHECK_OK"

grep -q "Exec=lxterminal -e senior-zero-update-check" "$DESKTOP"

echo "E2E PASS: update-check dry-run and runtime behavior are coherent"
