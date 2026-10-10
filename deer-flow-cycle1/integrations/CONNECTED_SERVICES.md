# Connected Services Map — Cycle 2

Updated: 2026-10-10T13:47:15.360215Z

| Service | Status | Usage in this build |
|---------|--------|---------------------|
| Google Drive | connected | Ingest deer-flow zip; backup tarball to `deer-flow-builds/` |
| GitHub | connected as cantgetalonggta-png | Repo `deer-flow-workspace` |
| Vercel | connected team_kgQcPVmumwtmK3MdAGlxKJtg | Deploy skill-engine dashboard / frontend |
| Voice | available | Not wired this cycle |
| Automations | available | Optional schedule for skill-tree-cycle |
| HyperFrames | available | Media pipeline future |

## OAuth / Allowlist notes
- Drive downloads use connected tool OAuth (no gog CLI in sandbox).
- GitHub uses GH_TOKEN / MCP.
- Vercel deploys need teamId; frontend API base must point at Gateway, not local Next only.
