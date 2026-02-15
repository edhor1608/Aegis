#!/usr/bin/env bash
set -euo pipefail

NOTES_FILE="/Users/jonas/Library/Mobile Documents/iCloud~md~obsidian/Documents/Coding/Projekte/P18 Senior Zero Linux/docs/notes.md"

[[ -f "$NOTES_FILE" ]] || { echo "E2E FAIL: missing $NOTES_FILE"; exit 1; }

grep -q "## Sprint-0 Workspace Links" "$NOTES_FILE"
grep -q "/Users/jonas/repos/senior-zero-linux/docs/architecture/system-model.md" "$NOTES_FILE"
grep -q "/Users/jonas/repos/senior-zero-linux/docs/architecture/update-and-rollback.md" "$NOTES_FILE"
grep -q "/Users/jonas/repos/senior-zero-linux/docs/architecture/app-center-policy.md" "$NOTES_FILE"
grep -q "/Users/jonas/repos/senior-zero-linux/docs/plan/sprint-0.md" "$NOTES_FILE"
grep -q "/Users/jonas/repos/senior-zero-linux/docs/plan/risk-register.md" "$NOTES_FILE"

echo "E2E PASS: obsidian links are in place"
