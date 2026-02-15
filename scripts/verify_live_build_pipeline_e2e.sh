#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="$(bash "$ROOT_DIR/scripts/live_build_pipeline.sh" --dry-run)"

echo "$OUTPUT" | grep -q "lb clean --purge"
echo "$OUTPUT" | grep -q "lb config noauto"
echo "$OUTPUT" | grep -q "lb build"
echo "$OUTPUT" | grep -q "VM_READY_INSTRUCTION:"

echo "E2E PASS: live-build pipeline dry-run is coherent"
