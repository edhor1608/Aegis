#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DESKTOP="$ROOT_DIR/build/live-build/config/includes.chroot/etc/skel/Desktop/Senior Zero Acceptance Runner.desktop"

test -f "$DESKTOP"
grep -q "Type=Application" "$DESKTOP"
grep -q "Name=Senior Zero Acceptance Runner" "$DESKTOP"
grep -q "Exec=lxterminal -e senior-zero-acceptance-runner --dry-run" "$DESKTOP"

echo "E2E PASS: acceptance desktop entry is coherent"
