#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt -r requirements-web.txt
python -m pytest -v --junitxml=resultados.xml
