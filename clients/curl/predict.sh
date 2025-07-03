#!/usr/bin/env bash
set -euo pipefail
curl -s http://127.0.0.1:8000/predict   -H 'content-type: application/json'   -d '{"features":[5.1,3.5,1.4,0.2]}' | jq .
