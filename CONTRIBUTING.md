# Proponer una mejora a CCE-100

No modifiques la skill directamente en producción. Usa una propuesta reproducible.

## Plantilla de solicitud de cambio

```markdown
ID: CCE-YYYY-NNN
Problema: [una oración]
Entorno afectado: [ChatGPT / Codex / Claude / agente de producto / documentos]
Severidad: [crítica / alta / media / baja]
Entrada anonimizada: [texto]
Salida observada: [texto]
Salida esperada: [texto]
Regla que cambiaría: [sección o número]
Beneficio esperado: [cómo lo mediríamos]
Posibles efectos secundarios: [qué puede empeorar]
Prueba de regresión: [entrada + criterio de aceptación]
Estado: propuesta
Versión sugerida: [SemVer]
```

## Criterios editoriales

- Una regla solo entra al Core si beneficia más de un contexto.
- Las excepciones de un sector o producto van a su perfil, no al Core.
- La brevedad no justifica eliminar excepciones, incertidumbre o trazabilidad.
- Las nuevas reglas deben admitir evaluación con ejemplos observables.
- Evitar reproducir el texto o el diccionario de ASD-STE100.
