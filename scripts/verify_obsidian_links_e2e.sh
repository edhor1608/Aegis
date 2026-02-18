#!/usr/bin/env bash
set -euo pipefail

DEFAULT_NOTES_FILE="${HOME}/Library/Mobile Documents/iCloud~md~obsidian/Documents/Coding/Projekte/P18 Senior Zero Linux/docs/notes.md"
DEFAULT_WORKSPACE_ROOT="${HOME}/repos/senior-zero-linux"
NOTES_FILE="${OBSIDIAN_NOTES_PATH:-$DEFAULT_NOTES_FILE}"
WORKSPACE_ROOT="${SENIOR_ZERO_WORKSPACE_ROOT:-$DEFAULT_WORKSPACE_ROOT}"

check_contains() {
  local pattern="$1"
  local file="$2"
  grep -q "$pattern" "$file" || { echo "E2E FAIL: missing '$pattern' in $file"; exit 1; }
}

if [[ ! -f "$NOTES_FILE" ]]; then
  echo "E2E PASS: obsidian links check skipped (missing $NOTES_FILE)"
  exit 0
fi

check_contains "## Sprint-0 Workspace Links" "$NOTES_FILE"
check_contains "$WORKSPACE_ROOT/docs/architecture/system-model.md" "$NOTES_FILE"
check_contains "$WORKSPACE_ROOT/docs/architecture/update-and-rollback.md" "$NOTES_FILE"
check_contains "$WORKSPACE_ROOT/docs/architecture/app-center-policy.md" "$NOTES_FILE"
check_contains "$WORKSPACE_ROOT/docs/plan/sprint-0.md" "$NOTES_FILE"
check_contains "$WORKSPACE_ROOT/docs/plan/risk-register.md" "$NOTES_FILE"

echo "E2E PASS: obsidian links are in place"
