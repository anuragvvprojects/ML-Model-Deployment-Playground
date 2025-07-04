# Examples

Sample payloads to try against the Minimal Deployment Pipeline API.

## Files
- `payloads/single.json` — Single prediction payload
- `payloads/batch.json` — Batch prediction payload

## Usage
```bash
# Single
curl -s http://127.0.0.1:8000/predict \  -H 'content-type: application/json' \  -d @examples/payloads/single.json | jq .

# Batch
curl -s http://127.0.0.1:8000/predict/batch \  -H 'content-type: application/json' \  -d @examples/payloads/batch.json | jq .
```
