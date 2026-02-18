#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-command-doctor"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Command Doctor.desktop"
TMP_HOME="$ROOT_DIR/out/tmp-command-doctor-home"

rm -rf "$TMP_HOME"
mkdir -p "$TMP_HOME"

DRY_OUTPUT="$(HOME="$TMP_HOME" bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_COMMAND_DOCTOR_DRY_RUN"

echo "$DRY_OUTPUT" | grep -q "required_commands=senior-zero-preflight-report,senior-zero-security-audit,senior-zero-network-check,senior-zero-storage-check,senior-zero-self-check,senior-zero-support-bundle,senior-zero-daily-checklist"

RUN_OUTPUT="$(HOME="$TMP_HOME" SENIOR_ZERO_COMMAND_DOCTOR_FAKE=1 bash "$SCRIPT")"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_COMMAND_DOCTOR_WRITTEN=$TMP_HOME/Documents/senior-zero-command-doctor.txt"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_COMMAND_DOCTOR_READY"

REPORT_FILE="$TMP_HOME/Documents/senior-zero-command-doctor.txt"
test -f "$REPORT_FILE"
grep -q "command_senior_zero_support_bundle=ready" "$REPORT_FILE"

grep -q "Exec=lxterminal -e senior-zero-command-doctor" "$DESKTOP"

echo "E2E PASS: command-doctor dry-run and fake execution are coherent"
