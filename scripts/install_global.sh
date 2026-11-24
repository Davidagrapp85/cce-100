#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/cce-100"
BLOCK="$ROOT/integraciones/INSTRUCCIONES_PERSISTENTES.txt"
STAMP="$(date +%Y%m%d%H%M%S)"

python3 "$ROOT/scripts/validate_package.py"

install_skill() {
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  if [ -d "$dest" ]; then
    local backup="$HOME/.cce-100/backups/global/$(basename "$(dirname "$dest")")-cce-100.${STAMP}"
    mkdir -p "$(dirname "$backup")"
    cp -R "$dest" "$backup"
    rm -rf "$dest"
  fi
  cp -R "$SOURCE" "$dest"
  echo "Skill: $dest"
}

install_skill "$HOME/.agents/skills/cce-100"
install_skill "$HOME/.claude/skills/cce-100"
python3 "$ROOT/scripts/sync_instructions.py" "$HOME/.codex/AGENTS.md" "$BLOCK"
python3 "$ROOT/scripts/sync_instructions.py" "$HOME/.claude/CLAUDE.md" "$BLOCK"
echo 'Instalación local lista. Confirma versión al iniciar nuevas sesiones de los agentes.'
