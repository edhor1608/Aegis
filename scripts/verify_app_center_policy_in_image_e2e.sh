#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT_DIR/build/live-build/config/includes.chroot/usr/local/sbin/senior-zero-app-center-policy"
OUTPUT="$(bash "$SCRIPT" --dry-run)"

echo "$OUTPUT" | grep -q "SENIOR_ZERO_APP_CENTER_POLICY_DRY_RUN"
echo "$OUTPUT" | grep -q "curated-default-packages.txt"
echo "$OUTPUT" | grep -q "more-apps-warning.txt"
echo "$OUTPUT" | grep -q "firefox-esr"
echo "$OUTPUT" | grep -q "thunderbird"

echo "E2E PASS: app-center policy dry-run is coherent"
