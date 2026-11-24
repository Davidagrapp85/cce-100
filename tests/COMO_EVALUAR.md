# Pruebas de regresión CCE-100

**Importante:** `scripts/validate_package.py` valida la estructura del paquete, no la calidad de las respuestas del modelo.

## Proceso de evaluación semántica

1. Selecciona un conjunto fijo de 10–20 entradas representativas, con datos reales anonimizados.
2. Ejecuta las mismas entradas con la versión actual y la candidata, usando el mismo modelo y contexto.
3. Puntúa cada salida con `cce-100/references/evaluacion.md` (0–10).
4. Verifica los criterios de `tests/casos_regresion.json`. Registra fallas críticas de manera separada.
5. Solicita revisión humana para casos jurídicos, financieros y operativos sensibles.
6. Publica un reporte de comparación antes de aprobar la nueva versión.

### Indicadores

- Calidad por caso: objetivo al menos 9/10.
- Errores críticos: 0.
- Regresiones frente a versión anterior: 0 en precisión y seguridad.
- Tiempo o longitud de lectura: observar, pero nunca optimizar a costa de sentido.
- Cobertura de versiones: porcentaje de entornos que confirman la versión aprobada.

**No declares cumplimiento ni mejora de calidad hasta correr estas pruebas con salidas reales.**
