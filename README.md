# CCE-100 · Comunicación Clara y Estructurada

Un estándar de redacción clara para personas **y para agentes de IA**, instalable como skill en Claude Code y Codex, con gobierno de versiones y pruebas de regresión contra modelos reales.

**Versión:** 1.2.0 · **Estado:** candidata (no alcanzó el umbral de aprobación; ver [resultados](tests/resultados/2026-11-07-v1.2.0/README.md)).

CCE-100 es una adaptación original inspirada en los principios de ASD-STE100. No es ASD-STE100 oficial, no reproduce su diccionario y no certifica conformidad.

## Por qué existe

Los agentes de IA escriben rápido, pero cometen errores de redacción con consecuencias operativas: agregan requisitos que un contrato no exige, renombran funciones al explicar código o convierten un dato ausente en «sin riesgo». CCE-100 fija 12 reglas verificables para evitarlos y un proceso para cambiarlas con evidencia, no por gusto.

## Las 12 reglas, en una línea cada una

1. Respuesta primero.
2. Una idea principal por oración.
3. Una acción por paso.
4. Voz activa y sujeto identificable.
5. Verbos concretos.
6. Longitud proporcionada.
7. Terminología constante.
8. Referencias explícitas.
9. Separar hechos, hipótesis, riesgos y decisiones.
10. Datos intactos: fechas, cifras, códigos y citas no se tocan.
11. Formato al servicio de la tarea.
12. No rellenar vacíos: si falta evidencia, se dice.

El texto completo, las excepciones y los modos de salida están en [`cce-100/SKILL.md`](cce-100/SKILL.md).

## Lo que lo hace distinto: se prueba contra modelos reales

La v1.2.0 se evaluó con 10 casos de regresión (legal, financiero, código, riesgo, procedimientos) en **Claude Code** y **Codex CLI**, con calificación ciega A/B y verificación mecánica de cifras.

| Agente | Promedio | Casos que pasan | Fallas críticas |
|---|---|---|---|
| Codex CLI | 9,3 | 8/10 | 0 confirmadas |
| Claude Code | 8,6 | 6/10 | 3 |

La evaluación encontró tres fallas críticas reales; por ejemplo, un agente convirtió un conteo nulo en «Sin hallazgos». Por eso la versión **sigue como candidata**: el proceso bloquea la publicación hasta que las reglas corrijan esas fallas. Detalle completo en [`tests/resultados/`](tests/resultados/2026-11-07-v1.2.0/README.md).

## Estructura

```
cce-100/                  Skill portátil: reglas, plantillas, evaluación y gobernanza
integraciones/            Bloque para AGENTS.md / CLAUDE.md, ChatGPT, GPT y auditor mensual
scripts/                  Instaladores idempotentes y validador del paquete
tests/                    Casos de regresión, guía de evaluación y resultados
docs/ROLLBACK.md          Cómo revertir una versión
```

## Instalar

**Global (Claude Code y Codex, macOS/Linux):**

```bash
bash scripts/install_global.sh
```

Copia la skill a `~/.claude/skills/cce-100` y `~/.agents/skills/cce-100`, y actualiza solo el bloque `CCE-100:START/END` en `~/.claude/CLAUDE.md` y `~/.codex/AGENTS.md`. Respalda la versión anterior.

**En un repositorio** (desde su raíz):

```bash
bash /ruta/a/cce-100/scripts/install_repo.sh
```

Revisa el `git diff` y abre un PR; nada se publica solo.

**ChatGPT:** copia [`integraciones/CHATGPT_INSTRUCCIONES_GLOBALES.md`](integraciones/CHATGPT_INSTRUCCIONES_GLOBALES.md) en las instrucciones personalizadas.

## Pruebas

```bash
bash scripts/run_tests.sh
```

Valida la estructura del paquete y la idempotencia de la instalación. No evalúa la calidad del lenguaje: esa evaluación es semántica y sigue [`tests/COMO_EVALUAR.md`](tests/COMO_EVALUAR.md).

## Gobierno

Un agente puede detectar fallas y proponer cambios, pero **no puede aprobarlos**. Cada versión exige evidencia, casos de prueba, revisión humana y un camino de reversa. Ver [`gobernanza.md`](cce-100/references/gobernanza.md) y [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Perfiles

El Core es transversal. Las reglas de un sector o producto (por ejemplo, un glosario de términos de riesgo) viven en perfiles separados que no se publican aquí.

## Referencia

ASD-STE100 Simplified Technical English, Issue 9 (2025): https://www.asd-ste100.org/

## Licencia

[MIT](LICENSE) © 2026 David Duarte.
