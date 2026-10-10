---
name: gateway-health-smoke
description: Smoke-test DeerFlow Gateway/Frontend/Nginx health endpoints. Use when verifying local or docker stack readiness.
---

# Gateway Health Smoke

## Checks
- GET Gateway /health
- Frontend root HTTP 200
- Nginx :2026 proxies /api/*

## Scripts
Prefer DeerFlow `.agent/skills/smoke-test` when available.

