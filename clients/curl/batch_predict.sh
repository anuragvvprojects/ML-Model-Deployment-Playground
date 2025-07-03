#!/usr/bin/env bash
set -euo pipefail
curl -s http://127.0.0.1:8000/predict/batch   -H 'content-type: application/json'   -d '{"rows":[[5.1,3.5,1.4,0.2],[6.2,3.4,5.4,2.3]]}' | jq .
