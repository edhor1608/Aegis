#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-branding-apply"
AUTOSTART="$ROOT_DIR/build/live-build/config/includes.chroot/etc/xdg/autostart/senior-zero-branding.desktop"
ISSUE="$ROOT_DIR/build/live-build/config/includes.chroot/etc/issue"
HOOK="$ROOT_DIR/build/live-build/config/hooks/normal/6100-brand-os-release.hook.chroot"

DRY_OUTPUT="$(bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_BRANDING_DRY_RUN"
echo "$DRY_OUTPUT" | grep -q "wallpaper=/usr/share/senior-zero/branding/aegis-wallpaper.svg"

echo "$DRY_OUTPUT" | grep -q "pcmanfm --set-wallpaper"
grep -q "Exec=senior-zero-branding-apply" "$AUTOSTART"
grep -q "Aegis Linux" "$ISSUE"
grep -q "PRETTY_NAME=\"Aegis Linux\"" "$HOOK"

echo "E2E PASS: branding shell dry-run is coherent"
