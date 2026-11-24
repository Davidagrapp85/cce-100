#!/usr/bin/env python3
"""Instalar dos veces no produce cambios y conserva las instrucciones existentes."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILE = {'skills': ['.claude/skills/cce-100', '.agents/skills/cce-100'], 'instructions': ['AGENTS.md']}


def install(target):
    cmd = [sys.executable, '-I', str(ROOT / 'scripts/install_target.py'), '--source', str(ROOT), '--target', str(target),
           '--profile', json.dumps(PROFILE), '--source-repo', 'local/cce-100', '--source-ref', 'v0', '--source-sha', '0' * 40]
    return json.loads(subprocess.run(cmd, check=True, capture_output=True, text=True).stdout)['changes']


def main():
    with tempfile.TemporaryDirectory() as d:
        t = Path(d)
        (t / 'AGENTS.md').write_text('# Reglas locales\n\nNo borrar esto.\n', encoding='utf-8')
        first = install(t)
        assert first, 'La primera instalación debe generar cambios'
        agents = (t / 'AGENTS.md').read_text(encoding='utf-8')
        assert agents.startswith('# Reglas locales\n\nNo borrar esto.') and agents.count('CCE-100:START') == 1
        assert (t / '.claude/skills/cce-100/references/gobernanza.md').is_file(), 'Skill incompleta'
        assert install(t) == [], 'La reinstalación no es idempotente'
        assert not (t / 'CLAUDE.md').exists(), 'Creó un archivo fuera del perfil'
    print('OK: instalación idempotente; conserva instrucciones existentes; skill completa.')


if __name__ == '__main__':
    main()
