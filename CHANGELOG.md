# Changelog de CCE-100

Se usa versionado semántico: MAJOR.MINOR.PATCH. Las fechas siguen ISO 8601.

## [1.2.0] — 2026-11-07 — Candidata

### Añadido
- `scripts/install_target.py`: instalación idempotente por perfil; no duplica bloques.
- Workflow de validación en cada push y pull request.
- `docs/ROLLBACK.md` y prueba de idempotencia de reinstalación.
- Mecanismo de glosario de perfil: detección de términos candidatos sin convertirlos en definiciones vigentes.
- Primera evaluación semántica con Claude Code y Codex (`tests/resultados/2026-11-07-v1.2.0/`).

### Resultado de la evaluación
- No alcanza el umbral (9/10 por caso y 0 pérdidas materiales). Tres fallas críticas en Claude Code.
- Se proponen tres reglas más explícitas: resúmenes legales sin requisitos inventados, símbolos de código citados exactamente y datos ausentes como «No disponible».

### Pendiente
- Aprobar las tres reglas propuestas y repetir la evaluación.

## [1.1.0] — 2026-11-07 — Paquete candidato

### Añadido
- Política de mejora continua, revisión mensual, clasificación de incidentes y aprobación humana.
- Separación explícita entre núcleo CCE-100 y perfiles sectoriales.
- Registro de casos de prueba y guía de evaluación de regresión.
- Instalación con bloque persistente administrado e idempotente.
- Comprobador local de integridad del paquete.

### Conservado
- Doce reglas centrales de claridad, precisión y trazabilidad de 1.0.0.
- Aclaración de que no certifica conformidad oficial ASD-STE100.

## [1.0.0] — 2026-11-07 — Piloto inicial

- Skill base, plantillas, evaluación e integraciones propuestas.
