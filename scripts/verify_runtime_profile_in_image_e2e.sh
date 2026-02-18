#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-runtime-profile"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Runtime Profile.desktop"

DRY_OUTPUT="$(bash "$SCRIPT" --dry-run)"
echo "$DRY_OUTPUT" | grep -q "SENIOR_ZERO_RUNTIME_PROFILE_DRY_RUN"
echo "$DRY_OUTPUT" | grep -q "baseline_ram_mb=4096"
echo "$DRY_OUTPUT" | grep -q "target_cpu_class=i3_legacy"

FAKE_OUTPUT="$(SENIOR_ZERO_RUNTIME_PROFILE_FAKE=1 bash "$SCRIPT")"
echo "$FAKE_OUTPUT" | grep -q "memory_total_mb=4096"
echo "$FAKE_OUTPUT" | grep -q "SENIOR_ZERO_RUNTIME_PROFILE_OK"

grep -q "Exec=lxterminal -e senior-zero-runtime-profile" "$DESKTOP"

echo "E2E PASS: runtime profile dry-run and fake execution are coherent"
