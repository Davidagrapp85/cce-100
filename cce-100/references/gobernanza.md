# Gobernanza CCE-100 — Ciclo de evolución

**Versión del documento:** 1.1.0 · **Responsable de aprobación:** propietario del estándar (usuario).

## Principio rector

CCE-100 cambia con base en evidencia de mejor comunicación y menores errores de ejecución. No cambia porque una salida sea solamente más breve, formal o estética. No se permite la autoedición de las reglas por agentes sin aprobación.

## Capas

1. **CCE-100 Core:** reglas generales, excepciones, modos de salida y criterios de calidad.
2. **Perfiles:** convenciones de un producto, legal, riesgos, soporte, marketing o equipos específicos. Una excepción sectorial no debe cambiar el núcleo si solo afecta a un perfil.
3. **Integraciones:** ChatGPT, Codex, Claude Code, agentes de producto y documentación; cada entorno fija una versión verificable.

## Flujo obligatorio de cambio

1. **Capturar evidencia:** conservar ejemplo de entrada, salida original, problema e impacto. Evitar datos sensibles en el repositorio.
2. **Clasificar:** error crítico, inconsistencia, mejora de legibilidad o nueva necesidad sectorial.
3. **Proponer:** redactar regla alternativa, caso de prueba y criterio de aceptación.
4. **Comprobar:** ejecutar pruebas estructurales y revisar salidas con un conjunto estable de casos.
5. **Aprobar:** una persona responsable autoriza el cambio y su impacto.
6. **Publicar:** actualizar versión, changelog, tags y distribuciones; registrar entornos actualizados.
7. **Medir y revertir:** comprobar que la versión nueva no degrada claridad ni precisión; revertir si hay regresión.

## Cadencia

- **Continuo:** registrar fallas y propuestas cuando aparecen. No publicar cambios automáticamente.
- **Mensual:** revisar los casos recibidos, seleccionar cambios y decidir si ameritan una versión.
- **Trimestral:** revisar métricas de desempeño, adopción, excepciones y deuda editorial.
- **Urgente:** corregir fallas críticas de seguridad, cifras, riesgo o términos jurídicos con revisión inmediata.

## Severidades

- **Crítica:** cambia el significado de un dato, omite una condición material, alucina un resultado o genera una instrucción insegura. No se libera.
- **Alta:** cambia el responsable, secuencia, ámbito o conclusión de una instrucción.
- **Media:** crea ambigüedad evitable, inconsistencia terminológica o carga innecesaria de lectura.
- **Baja:** preferencia estilística sin impacto demostrado.

## Política de versiones

- **PATCH (1.1.1):** correcciones editoriales y de ejemplos, sin cambiar la conducta esperada.
- **MINOR (1.2.0):** reglas nuevas compatibles, nuevos perfiles o nuevas plantillas.
- **MAJOR (2.0.0):** cambios incompatibles que exigen adaptar agentes o documentos existentes.

El número de versión del estándar CCE-100 no debe confundirse con el número de edición de ASD-STE100.

## Controles de aprobación

Una versión solo es candidata a publicación si:

- La rúbrica de calidad alcanza al menos 9/10 en cada caso representativo o justifica la excepción.
- No hay pérdidas de contenido material, cifras o citas.
- Los casos críticos de riesgos, seguridad y privacidad cumplen sus invariantes.
- La revisión manual confirma que la respuesta mantiene utilidad y naturalidad.
- El changelog identifica el problema corregido y la justificación.
- Se establece un procedimiento para volver a la versión anterior.

La revisión estructural automatizada no sustituye la evaluación semántica de la salida.

## Registro de propuestas

Para cada mejora registra: `ID`, `fecha`, `entorno`, `tipo`, `entrada anonimizada`, `salida observada`, `salida deseada`, `motivo`, `severidad`, `regla afectada`, `caso de prueba`, `estado`, `versión objetivo` y `aprobador`.

Estados: `propuesta` → `en evaluación` → `en pruebas` → `aprobada` → `liberada` o `descartada`.

## Fuente de verdad y despliegue

Recomendación: repositorio independiente `cce-100` en GitHub, con tags firmados o protegidos y revisión por pull request. Los productos y los agentes consumen releases aprobadas. No usar cinco copias editadas de forma independiente. Mantener la versión instalada en cada entorno y actualizarla explícitamente después de revisar el diff.

**No autorizar despliegue automático a producción de un producto** por el mero hecho de aprobar una regla editorial. Requiere pruebas de producto y publicación propia.

## Gobierno de glosarios de perfil

Cada glosario de perfil tiene versión editorial independiente del Core CCE-100. La detección de **candidatos** puede ser automática. La aceptación de una definición exige responsable y evidencia. La publicación requiere comparar su efecto sobre prompts, reportes, alertas y documentación.

Si un término definido induce un error de identidad, puntaje, fuente, titularidad o riesgo, trátalo como incidente crítico y bloquea su liberación.
