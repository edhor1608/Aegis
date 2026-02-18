#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-health-summary"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Health Summary.desktop"

OUTPUT="$(bash "$SCRIPT" --dry-run)"

echo "$OUTPUT" | grep -q "SENIOR_ZERO_HEALTH_SUMMARY_DRY_RUN"
echo "$OUTPUT" | grep -q "networkmanager_active"
echo "$OUTPUT" | grep -q "language_switch_available"
grep -q "Exec=lxterminal -e senior-zero-health-summary" "$DESKTOP"

echo "E2E PASS: health summary dry-run and desktop entry are coherent"
