#!/usr/bin/env python3
"""Instala CCE-100 en un repositorio según su perfil del manifiesto. Idempotente.

- Copia la skill completa a las rutas del perfil (Claude Code y Codex).
- Actualiza solo el bloque CCE-100:START/END en los archivos de instrucciones del perfil.
- Escribe .cce-100/install.json sin marcas de tiempo, para que una reinstalación igual no genere cambios.

Uso: install_target.py --source <árbol de la versión> --target <repo> --profile '<json>' \
        --source-repo <owner>/cce-100 --source-ref v1.2.0 --source-sha <sha>
"""
import argparse
import filecmp
import json
import shutil
import subprocess
import sys
from pathlib import Path


def same_tree(a, b):
    if not b.is_dir():
        return False
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return False
    _, mismatch, errors = filecmp.cmpfiles(a, b, cmp.common_files, shallow=False)
    return not mismatch and not errors and all(same_tree(a / d, b / d) for d in cmp.common_dirs)


def put_tree(src, dest, log):
    if same_tree(src, dest):
        return
    if dest.exists():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dest)
    log.append(f'skill: {dest}')


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument('--source', required=True, type=Path)
    a.add_argument('--target', required=True, type=Path)
    a.add_argument('--profile', required=True)
    a.add_argument('--source-repo', required=True)
    a.add_argument('--source-ref', required=True)
    a.add_argument('--source-sha', required=True)
    args = a.parse_args()
    src, tgt, prof = args.source.resolve(), args.target.resolve(), json.loads(args.profile)
    version = json.loads((src / 'VERSION.json').read_text(encoding='utf-8'))['version']
    log = []
    for rel in prof.get('skills', []):
        put_tree(src / 'cce-100', tgt / rel, log)
    block = src / 'integraciones/INSTRUCCIONES_PERSISTENTES.txt'
    for rel in prof.get('instructions', []):
        out = subprocess.run([sys.executable, '-I', str(src / 'scripts/sync_instructions.py'), str(tgt / rel), str(block)],
                             capture_output=True, text=True)
        if out.returncode:
            raise SystemExit(out.stderr or out.stdout)
        if out.stdout.startswith('Actualizado'):
            log.append(f'instrucciones: {rel}')
    record = {'standard': 'CCE-100', 'version': version, 'source_repo': args.source_repo,
              'source_ref': args.source_ref, 'source_sha': args.source_sha, 'profile': prof,
              'managed_by': f'{args.source_repo} (no editar a mano; usar el sincronizador)'}
    rec_path = tgt / '.cce-100/install.json'
    new = json.dumps(record, ensure_ascii=False, indent=2) + '\n'
    if not rec_path.exists() or rec_path.read_text(encoding='utf-8') != new:
        rec_path.parent.mkdir(parents=True, exist_ok=True)
        rec_path.write_text(new, encoding='utf-8')
        log.append('registro: .cce-100/install.json')
    print(json.dumps({'target': str(tgt), 'version': version, 'changes': log}, ensure_ascii=False))


if __name__ == '__main__':
    main()
