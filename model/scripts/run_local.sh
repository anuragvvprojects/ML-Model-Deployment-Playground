#!/usr/bin/env bash
set -euo pipefail
export MODEL_PATH=${MODEL_PATH:-model/artifacts/model.joblib}
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
