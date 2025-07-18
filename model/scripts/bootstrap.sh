#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pre-commit install || true
python model/train.py
echo "Bootstrap complete."
