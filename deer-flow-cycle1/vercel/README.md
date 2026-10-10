# Vercel Deployment Plan

Generated: 2026-10-10T13:43:47.390147Z

1. Frontend is Next.js under `frontend/`.
2. Use skill `vercel-deploy` from DeerFlow public skills.
3. Gateway/API must be hosted separately (Docker/K8s); set API base URL env.
4. Do not deploy secrets in client bundle — model keys stay on Gateway.

## Checklist
- [ ] Create Vercel project linked to GitHub repo
- [ ] Set env: NEXT_PUBLIC_API_BASE
- [ ] Build from `frontend/`
- [ ] Verify chat SSE streaming through proxy
- [ ] Verify skills market loads
