#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/cce-100"
BLOCK="$ROOT/integraciones/INSTRUCCIONES_PERSISTENTES.txt"
STAMP="$(date +%Y%m%d%H%M%S)"
python3 "$ROOT/scripts/validate_package.py"

if [ ! -d .git ]; then
  echo 'Aviso: no se detectó .git. Confirma la carpeta de instalación.' >&2
fi
for dest in '.agents/skills/cce-100' '.claude/skills/cce-100'; do
  mkdir -p "$(dirname "$dest")"
  if [ -d "$dest" ]; then
    b="$HOME/.cce-100/backups/repos/$(basename "$PWD")-$(basename "$(dirname "$dest")")-cce-100.${STAMP}"
    mkdir -p "$(dirname "$b")"
    cp -R "$dest" "$b"
    rm -rf "$dest"
  fi
  cp -R "$SOURCE" "$dest"
done
mkdir -p docs
if [ -e docs/CCE-100.md ]; then
  cp docs/CCE-100.md "docs/CCE-100.md.bak.${STAMP}"
fi
cp "$SOURCE/SKILL.md" docs/CCE-100.md
python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['version'])" "$ROOT/VERSION.json" > docs/CCE-100_VERSION.txt
for file in AGENTS.md CLAUDE.md; do
  python3 "$ROOT/scripts/sync_instructions.py" "$file" "$BLOCK"
done
echo 'Integración local lista. Revisa git diff y ejecuta pruebas de agentes antes de crear PR.'
