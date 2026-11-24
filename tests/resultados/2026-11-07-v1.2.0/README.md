# Evaluación semántica de CCE-100 v1.2.0 — 2026-11-07

**Resultado:** v1.2.0 **no alcanza** el umbral de aprobación (9/10 por caso y 0 pérdidas materiales). La versión sigue en estado `candidate`.

| Agente | Promedio | Casos que pasan | Fallas críticas |
|---|---|---|---|
| Codex CLI 0.155.1 (`gpt-6-astra`, esfuerzo bajo) | 9,3 | 8/10 | 0 confirmadas (1 discutida) |
| Claude Code 2.1.311 (`opus[1m]`) | 8,6 | 6/10 | 3 |

Un caso pasa si obtiene al menos 9/10, cumple todos sus criterios y no tiene falla crítica.

## Método

1. **Entradas.** Los 10 casos de `tests/casos_regresion.json` describen la tarea, no el texto. Cada caso se fijó como una entrada concreta y ficticia (`casos/`), con las trampas que el caso debe detectar: cifras, excepciones, fuentes que no respondieron y símbolos de código.
2. **Generación.** Cada entrada se envió sin mencionar CCE-100 a los dos agentes instalados, para comprobar la activación automática:
   - Claude Code: `claude -p`, herramientas de solo lectura.
   - Codex: `codex exec -s read-only`.
   - Los casos 002 y 009 corrieron dentro del repositorio privado de un producto de inteligencia de riesgo, con su glosario de perfil; el resto, en un directorio vacío. Sus entradas y salidas no se publican porque contienen detalles de ese producto; sus puntajes sí.
3. **Calificación ciega.** Las 20 salidas se anonimizaron como A/B con orden aleatorio (`clave.json`). Cinco subagentes calificadores puntuaron dos casos cada uno con `cce-100/references/evaluacion.md` (10 controles), los criterios del caso y una lista de fallas críticas. Cada 0 y cada falla lleva su cita (`calificaciones/`).
4. **Verificación.** Una revisión mecánica confirmó que las cifras de las entradas están en las 20 salidas. Cuatro salidas cambiaron el formato de una fecha (ISO a formato largo) sin cambiar el valor. Las fallas críticas se verificaron contra el texto original.

## Resultados por caso

| Caso | Categoría | Claude Code | Codex |
|---|---|---|---|
| CCE-001 | procedimiento | 9 | 8 · falla discutida |
| CCE-002 | riesgo | 9 | 10 |
| CCE-003 | financiero | 9 | 10 |
| CCE-004 | legal | 8 · **falla crítica** | 10 |
| CCE-005 | mensaje | 9 | 10 |
| CCE-006 | código | 8 · **falla crítica** | 10 |
| CCE-007 | investigación | 9 | 9 |
| CCE-008 | explicación | 8 | 9 |
| CCE-009 | agente | 8 · **falla crítica** | 9 |
| CCE-010 | resumen ejecutivo | 9 | 8 |

## Fallas críticas

1. **CCE-004 (Claude Code).** La respuesta agrega un requisito que la cláusula no tiene: «Ese incumplimiento debe notificarse por escrito». La cláusula dice «debidamente notificado». También pierde el inicio del plazo de 15 días hábiles («siguientes a la notificación»).
2. **CCE-006 (Claude Code).** La respuesta llama `riskScore` a la función `getRiskScore`. También inventa significados que el código no define: «ficticias (de demo o de prueba)» y «por ejemplo las verdes».
3. **CCE-009 (Claude Code).** El prompt para un agente que consulta un registro público de multas instruye: «Si ese campo es nulo, `n = 0`». Un conteo nulo termina como «Sin hallazgos» y «Sin multas pendientes». Eso contradice su propia regla («Si falta un dato, escribe "No disponible"») y la regla del glosario: «No disponible» no es «Sin hallazgos». El agente reprodujo un defecto que existía en el código del producto (un conteo nulo tratado como 0); la evaluación lo detectó.
4. **Discutida: CCE-001 (Codex).** La respuesta remite a «el procedimiento de aislamiento y bloqueo específico del equipo», que la nota no menciona. El calificador lo cuenta como referencia inventada. Es una precaución de seguridad sin nombre de documento. El caso no pasa de todos modos: 8/10 y la secuencia no es verificable.

## Observaciones

- **Activación.** Codex leyó la skill completa en 3 de 10 casos (001, 002 y 009). En los demás aplicó solo el bloque de `~/.codex/AGENTS.md`. No se registró si Claude Code cargó la skill: `claude -p` en modo texto no muestra las herramientas usadas.
- **CCE-009 (Claude Code)** escribió el prompt en un archivo de su scratchpad y entregó solo un resumen. El archivo se evaluó; no se publica (ver Método).
- **Defectos frecuentes que no llegan a falla crítica:** formato o largo que excede lo pedido (CCE-004-B, CCE-007-B, CCE-010), referentes ambiguos (CCE-008, CCE-010) y consecuencias no dadas en la entrada (CCE-005, CCE-008).

## Límites

- Una corrida por caso y agente; un calificador por caso. Los calificadores son modelos, no personas.
- No hay línea base sin el estándar: el bloque CCE-100 está en las instrucciones globales de ambos agentes. Esta evaluación mide el cumplimiento absoluto, no la mejora frente a no tener el estándar.
- Es la primera versión desplegada, así que no aplica la regresión frente a la versión anterior.
- Los casos 002, 004 y 009 tocan temas jurídicos y de riesgo: requieren revisión humana (`tests/COMO_EVALUAR.md`, paso 5).

## Propuestas para la próxima versión (requieren aprobación humana)

Las tres fallas críticas violan reglas que la skill ya tiene. Se proponen tres reglas más explícitas, para revisar según `cce-100/references/gobernanza.md`:

1. **Resúmenes de textos legales:** no agregues requisitos de forma (escrito, firmado, certificado) que el texto no exige. Conserva el punto de inicio de cada plazo.
2. **Código:** cita cada símbolo exactamente como aparece. No atribuyas significados a valores que el código no muestra.
3. **Datos ausentes:** un dato nulo o ausente es «No disponible». Nunca lo conviertas en 0, «sin registros» ni «sin hallazgos».
