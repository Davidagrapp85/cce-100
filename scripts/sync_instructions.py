#!/usr/bin/env python3
"""Añade o actualiza solo el bloque CCE-100; no modifica otras instrucciones."""
import sys
from pathlib import Path

if len(sys.argv) != 3:
    raise SystemExit('Uso: sync_instructions.py <archivo_objetivo> <bloque>')

target=Path(sys.argv[1]).expanduser()
source=Path(sys.argv[2]).read_text(encoding='utf-8').strip()
start='<!-- CCE-100:START -->'
end='<!-- CCE-100:END -->'
assert source.startswith(start) and source.endswith(end), 'Bloque sin delimitadores'
target.parent.mkdir(parents=True, exist_ok=True)
old=target.read_text(encoding='utf-8') if target.exists() else ''
if start in old or end in old:
    if old.count(start) != 1 or old.count(end) != 1 or old.index(start)>old.index(end):
        raise SystemExit(f'Bloque CCE-100 ambiguo en {target}; revisión manual requerida.')
    i=old.index(start); j=old.index(end)+len(end)
    new=old[:i]+source+old[j:]
else:
    # El paquete v1.0 agregaba un bloque sin delimitadores.
    legacy="""## CCE-100 — Comunicación Clara y Estructurada\n\nAplica CCE-100 como estándar por defecto para respuestas, documentación e instrucciones a agentes. Da la respuesta principal primero. Escribe una idea por oración y una acción por paso. Utiliza verbos concretos, voz activa y terminología consistente. Preserva todos los datos, fuentes, términos legales, matices y excepciones. Distingue hechos, hipótesis y límites de información. Adapta el formato a la tarea. No confundas esta adaptación con cumplimiento oficial ASD-STE100. Para revisión detallada, utiliza la skill `cce-100`."""
    if legacy in old:
        new=old.replace(legacy, source, 1)
    elif '## CCE-100 — Comunicación Clara y Estructurada' in old:
        raise SystemExit(f'Hay una instrucción CCE-100 no identificada en {target}; revisión manual requerida.')
    else:
        new=old.rstrip()+ ('\n\n' if old.strip() else '')+source+'\n'
if new!=old:
    target.write_text(new, encoding='utf-8')
    print(f'Actualizado: {target}')
else:
    print(f'Sin cambios: {target}')
