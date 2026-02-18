#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BASE="$ROOT_DIR/build/live-build/config/includes.chroot"

test -f "$BASE/etc/skel/Desktop/Senior Zero Browser.desktop"
test -f "$BASE/etc/skel/Desktop/Senior Zero Documents.desktop"
test -f "$BASE/etc/skel/Desktop/Senior Zero Help.desktop"
test -f "$BASE/etc/skel/Desktop/Senior Zero Health.desktop"
test -f "$BASE/usr/share/senior-zero/help/welcome.txt"

grep -q "Exec=firefox-esr" "$BASE/etc/skel/Desktop/Senior Zero Browser.desktop"
grep -q "Exec=libreoffice" "$BASE/etc/skel/Desktop/Senior Zero Documents.desktop"
grep -q "Exec=lxterminal -e less /usr/share/senior-zero/help/welcome.txt" "$BASE/etc/skel/Desktop/Senior Zero Help.desktop"
grep -q "Exec=lxterminal -e senior-zero-preflight-report" "$BASE/etc/skel/Desktop/Senior Zero Health.desktop"
grep -q "Senior Zero Linux" "$BASE/usr/share/senior-zero/help/welcome.txt"

echo "E2E PASS: desktop baseline assets are coherent"
