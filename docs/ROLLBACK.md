# Rollback de CCE-100

## Repositorio consumidor
1. Revierte el PR que instaló o actualizó CCE-100 con `git revert <sha>` o el botón «Revert» del PR.
2. Para fijar una versión anterior: `git checkout vX.Y.Z` en este repositorio y vuelve a ejecutar `scripts/install_repo.sh` en el consumidor.

## Instalación global (Claude Code y Codex)
1. Borra el bloque entre `<!-- CCE-100:START -->` y `<!-- CCE-100:END -->` en `~/.claude/CLAUDE.md` y `~/.codex/AGENTS.md`.
2. Borra `~/.claude/skills/cce-100` y `~/.agents/skills/cce-100`. Las copias previas, si existían, están en `~/.cce-100/backups/`.
3. Para reinstalar otra versión: `git checkout vX.Y.Z && bash scripts/install_global.sh`.

## Prueba de idempotencia
`python3 -I tests/test_install_idempotencia.py` debe confirmar que una segunda instalación no produce cambios.
