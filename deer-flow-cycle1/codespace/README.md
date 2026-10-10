# DeerFlow Codespace Workspace

Generated: 2026-10-10T13:43:47.390147Z

## Source
- DeerFlow 2.x monorepo extracted from Drive `deer-flow-main (1).zip`
- Full extract path on build host: `/tmp/deer-extract/deer-flow-main`
- Catalog: 4344 skills in encyclopedias/catalog.json

## Topology
| Service | Port | Role |
|---------|------|------|
| Nginx | 2026 | Entry proxy |
| Gateway | 8001 | FastAPI + agent runtime |
| Frontend | 3000 | Next.js |
| Provisioner | 8002 | Optional K8s sandbox |

## Quick start (local)
```bash
cd deer-flow-source   # or clone https://github.com/bytedance/deer-flow
make config
make install
# edit config.yaml with model keys
make dev
# open http://127.0.0.1:2026
```

## Workspace layout
See ROOT_WORKSPACE/ for skills, tools, plugins, ontology, encyclopedias, deployments.
