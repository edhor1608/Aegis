#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-support-bundle"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Support Bundle.desktop"
TMP_HOME="$ROOT_DIR/out/tmp-support-bundle-home"

rm -rf "$TMP_HOME"
mkdir -p "$TMP_HOME"

DRY_OUTPUT="$(HOME="$TMP_HOME" bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_SUPPORT_BUNDLE_DRY_RUN"

echo "$DRY_OUTPUT" | grep -q "included_checks=preflight_report,security_audit,network_check,storage_check,update_check"

RUN_OUTPUT="$(HOME="$TMP_HOME" SENIOR_ZERO_SUPPORT_BUNDLE_FAKE=1 bash "$SCRIPT")"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_SUPPORT_BUNDLE_WRITTEN=$TMP_HOME/Documents/senior-zero-support-bundle.txt"
echo "$RUN_OUTPUT" | grep -q "SENIOR_ZERO_SUPPORT_BUNDLE_READY"

REPORT_FILE="$TMP_HOME/Documents/senior-zero-support-bundle.txt"
test -f "$REPORT_FILE"
grep -q "check_update_check=ready" "$REPORT_FILE"

grep -q "Exec=lxterminal -e senior-zero-support-bundle" "$DESKTOP"

echo "E2E PASS: support-bundle dry-run and fake execution are coherent"
