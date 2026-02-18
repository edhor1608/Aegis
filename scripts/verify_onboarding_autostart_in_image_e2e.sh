#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-onboarding"
AUTOSTART="$ROOT_DIR/build/live-build/config/includes.chroot/etc/xdg/autostart/senior-zero-onboarding.desktop"
TMP_HOME="$ROOT_DIR/out/tmp-onboarding-home"

cleanup() {
  rm -rf "$TMP_HOME"
}

trap cleanup EXIT INT TERM

rm -rf "$TMP_HOME"
mkdir -p "$TMP_HOME"

DRY_OUTPUT="$(HOME="$TMP_HOME" "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_ONBOARDING_DRY_RUN"

FIRST_OUTPUT="$(HOME="$TMP_HOME" SENIOR_ZERO_ONBOARDING_NO_OPEN=1 "$SCRIPT")"
echo "$FIRST_OUTPUT" | grep -q "SENIOR_ZERO_ONBOARDING_SHOWN"

SECOND_OUTPUT="$(HOME="$TMP_HOME" SENIOR_ZERO_ONBOARDING_NO_OPEN=1 "$SCRIPT")"
echo "$SECOND_OUTPUT" | grep -q "SENIOR_ZERO_ONBOARDING_ALREADY_DONE"

grep -q "Exec=senior-zero-onboarding" "$AUTOSTART"

echo "E2E PASS: onboarding autostart behavior is coherent"
