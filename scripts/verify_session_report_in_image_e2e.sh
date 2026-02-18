#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-session-report"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Session Report.desktop"
TMP_HOME="$ROOT_DIR/out/tmp-session-report-home"

rm -rf "$TMP_HOME"
mkdir -p "$TMP_HOME"

DRY_OUTPUT="$(HOME="$TMP_HOME" bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_SESSION_REPORT_DRY_RUN"

echo "$DRY_OUTPUT" | grep -q "planned_sections=update_check,network_check,storage_check,runtime_profile,self_check"

RUN_OUTPUT="$(HOME="$TMP_HOME" SENIOR_ZERO_SESSION_REPORT_FAKE=1 bash "$SCRIPT")"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_SESSION_REPORT_WRITTEN=$TMP_HOME/Documents/senior-zero-session-report.txt"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_SESSION_REPORT_READY"

REPORT_FILE="$TMP_HOME/Documents/senior-zero-session-report.txt"
test -f "$REPORT_FILE"
grep -q "section_network_check=ready" "$REPORT_FILE"

grep -q "Exec=lxterminal -e senior-zero-session-report" "$DESKTOP"

echo "E2E PASS: session-report dry-run and fake execution are coherent"
