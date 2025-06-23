# Security Policy
We take security seriously and appreciate responsible disclosure.

## Reporting a Vulnerability
- Please report suspected vulnerabilities privately to **security@example.com**.
- Include a clear description, reproduction steps, logs (redacted), and potential impact.
- Do **not** open a public issue for undisclosed vulnerabilities.

## Scope
- Application endpoints: `/predict`, `/health`, `/ready`, `/version`, `/metrics`
- Container and deployment artifacts under `infra/`
- Training and model artifacts under `model/`

## Handling Sensitive Data
- Do not log PII or raw payloads in production logs.
- Prefer environment variables and/or a secrets manager for credentials.
- Rotate secrets regularly and restrict access on a least-privilege basis.

## Hardening Checklist (Summary)
- Input validation with Pydantic (types & bounds)
- JSON structured logging with redaction of sensitive fields
- Rate limiting & authentication at the gateway (reverse proxy / API gateway)
- Dependency updates & vulnerability scanning (e.g., Dependabot, Trivy)
- Readiness & liveness probes for safe rollouts and automated recovery
