#!/usr/bin/env bash
# Ejecuta todas las pruebas del repositorio canónico. Solo biblioteca estándar.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
python3 -I scripts/validate_package.py
python3 -I tests/test_install_idempotencia.py
python3 -I -c "import json;[json.load(open(p,encoding='utf-8')) for p in ('VERSION.json','tests/casos_regresion.json')];print('OK: JSON válidos.')"
