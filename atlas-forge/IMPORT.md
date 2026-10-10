# Atlas Forge cycle — GitHub import + NodeTool index

## Done
- Live public GitHub import at `/import` (owner/repo or URL).
- Imports persist in browser (`localStorage` via zustand) and appear under Projects.
- NodeTool Drive tree indexed (ARCHITECTURE, packages/* including huggingface, plugins, Electron, MCP).
- Services status updated for Drive / GitHub / Vercel / Hugging Face.

## Vercel
Write APIs fail with scope `echo-ec69` even when `team_kgQcPVmumwtmK3MdAGlxKJtg` is passed.
**Action required:** reconnect the Vercel connector in Grok (settings → connectors → Vercel → re-authenticate).
Read APIs (list teams, list projects, get auth user) work; create project / create_git_project do not.

## Team id (after reauth)
`team_kgQcPVmumwtmK3MdAGlxKJtg` (defaultTeamId for nevagetalong-1199)
