#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/bin/senior-zero-language-switch"

OUTPUT_EN="$(HOME="$ROOT_DIR/out/tmp-lang-en" "$SCRIPT" --to en --dry-run)"
OUTPUT_DE="$(HOME="$ROOT_DIR/out/tmp-lang-de" "$SCRIPT" --to de --dry-run)"
OUTPUT_CUR="$(HOME="$ROOT_DIR/out/tmp-lang-cur" "$SCRIPT" --print-current --dry-run)"

echo "$OUTPUT_EN" | grep -q "SENIOR_ZERO_LANGUAGE_SWITCH_DRY_RUN"
echo "$OUTPUT_EN" | grep -q "LANG=en_US.UTF-8"
echo "$OUTPUT_DE" | grep -q "LANG=de_DE.UTF-8"
echo "$OUTPUT_CUR" | grep -q "SENIOR_ZERO_LANGUAGE_SWITCH_DRY_RUN"

echo "E2E PASS: language switch helper dry-run is coherent"
