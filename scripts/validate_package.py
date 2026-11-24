#!/usr/bin/env python3
"""Validación estructural CCE-100. No evalúa semántica ni conformidad ASD."""
import json
import pathlib
import re
import sys
root=pathlib.Path(__file__).resolve().parent.parent
manifest=json.loads((root/'VERSION.json').read_text(encoding='utf-8'))
required=[
 'README.md','CHANGELOG.md','CONTRIBUTING.md',
 'cce-100/SKILL.md','cce-100/references/gobernanza.md',
 'cce-100/references/evaluacion.md','cce-100/references/plantillas.md',
 'integraciones/INSTRUCCIONES_PERSISTENTES.txt','tests/casos_regresion.json',
 'scripts/install_global.sh','scripts/install_repo.sh','LICENSE']
errors=[f'Falta {p}' for p in required if not (root/p).is_file()]
skill=(root/'cce-100/SKILL.md').read_text(encoding='utf-8')
if f'version: {manifest["version"]}' not in skill:
 errors.append('Versión diferente entre manifest y skill')
if 'ASD-STE100' not in skill or 'no certifica' not in skill:
 errors.append('Falta declaración de límites')
block=(root/'integraciones/INSTRUCCIONES_PERSISTENTES.txt').read_text(encoding='utf-8')
if block.count('<!-- CCE-100:START -->')!=1 or block.count('<!-- CCE-100:END -->')!=1:
 errors.append('Delimitadores no válidos')
tests=json.loads((root/'tests/casos_regresion.json').read_text(encoding='utf-8'))
if len(tests)<10 or len({x['id'] for x in tests})!=len(tests):
 errors.append('Casos de regresión insuficientes o duplicados')
if errors:
 print('ERROR:\n'+'\n'.join(errors),file=sys.stderr)
 raise SystemExit(1)
print(f'OK: CCE-100 v{manifest["version"]}; {len(required)} archivos obligatorios; {len(tests)} casos de prueba. Evaluación semántica pendiente.')
