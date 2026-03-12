#!/bin/bash
# Generates spooler-manual.pdf from MDX sources
# Requirements: pandoc, typst  (brew install pandoc typst)

set -e
DOCS="$(cd "$(dirname "$0")/.." && pwd)"

python3 "$DOCS/scripts/merge-mdx.py"

pandoc /tmp/spooler-manual.md \
  --pdf-engine=typst \
  --toc --toc-depth=2 \
  --metadata title="Spooler — Uživatelský manuál" \
  --metadata author="Snail Rollers" \
  --metadata date="$(date +%Y)" \
  -o "$DOCS/spooler-manual.pdf"

echo "✓ $DOCS/spooler-manual.pdf"
