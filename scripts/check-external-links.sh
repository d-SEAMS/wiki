#!/usr/bin/env bash
# Check third-party URLs in the wiki markdown with lychee.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
exec lychee --config "$root/lychee.toml" --no-progress "$root/docs" "$root/README.md"
