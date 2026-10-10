# Full Build Instructions (Future Runs)

Generated: 2026-10-10T13:43:47.390147Z

## 1. Ingest
1. Download `deer-flow-main*.zip` from Google Drive via `google_drive_download_artifact`.
2. Extract with Python zipfile to `/tmp/deer-extract` (artifacts FS is slow for many files).
3. Load `catalog.json` and `skill-atlas.html` if present.

## 2. Distill
1. Parse all `SKILL.md` → atoms.
2. Cluster catalog by category.
3. Enumerate harness tools, MCP servers, extension examples.
4. Run skill-tree-engine cycle → state.json + reports.

## 3. Workspace
1. Write under `/tmp/deer-build` then copy small generated artifacts to `/workspace/artifacts`.
2. Keep source extract in `/tmp`; do not bulk-copy into artifacts.

## 4. Implement / Connect
- GitHub: push ROOT_WORKSPACE + optional submodule.
- Vercel: frontend only.
- Drive: upload backup ZIP of encyclopedias + state.

## 5. Test
- Unit: backend pytest / frontend rstest (in full DeerFlow env).
- Smoke: `.agent/skills/smoke-test` scripts when Docker available.
- Skill review: `skills/public/skill-reviewer`.

## 6. Deploy
- `make up` Docker stack or Helm chart under `deploy/helm`.
- Frontend can go to Vercel with API pointed at Gateway.

## 7. Backup
- Bundle ROOT_WORKSPACE encyclopedias + skill-engine into ZIP.
- Upload via `google_drive_upload_artifact`.
