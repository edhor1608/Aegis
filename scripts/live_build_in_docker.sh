#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE_TAG="senior-zero-live-build:bookworm"
DOCKERFILE="docker/live-build-builder.Dockerfile"
OUT_DIR="$ROOT_DIR/out/live-build"
BUILD_CMD=(docker build --platform linux/amd64 -f "$DOCKERFILE" -t "$IMAGE_TAG" .)
RUN_CMD=(docker run --rm --platform linux/amd64 --privileged -v "$ROOT_DIR:/src:ro" -v "$OUT_DIR:/out" -w /tmp "$IMAGE_TAG" bash -lc "set -euo pipefail; rm -rf /tmp/repo; mkdir -p /tmp/repo; cp -a /src/. /tmp/repo/; cd /tmp/repo; ./scripts/live_build_pipeline.sh; cp build/live-build/live-image-amd64.hybrid.iso /out/")
RUN_DRY_CMD=(docker run --rm --platform linux/amd64 --privileged -v "$ROOT_DIR:/src:ro" -v "$OUT_DIR:/out" -w /tmp "$IMAGE_TAG" bash -lc "set -euo pipefail; rm -rf /tmp/repo; mkdir -p /tmp/repo; cp -a /src/. /tmp/repo/; cd /tmp/repo; ./scripts/live_build_pipeline.sh --dry-run")

mkdir -p "$OUT_DIR"

if [[ "${1:-}" == "--dry-run" ]]; then
  echo "${BUILD_CMD[*]}"
  echo "${RUN_DRY_CMD[*]}"
  exit 0
fi

(
  cd "$ROOT_DIR"
  "${BUILD_CMD[@]}"
)
"${RUN_CMD[@]}"
