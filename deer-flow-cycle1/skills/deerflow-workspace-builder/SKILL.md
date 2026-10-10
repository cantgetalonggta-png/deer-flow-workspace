---
name: deerflow-workspace-builder
description: Rebuild ROOT_WORKSPACE skill trees, ontology, and encyclopedias from a DeerFlow monorepo extract. Trigger on FULL_LOGIC_CHAIN, ingest deer-flow zip, or rebuild skill engine.
---

# DeerFlow Workspace Builder

## Inputs
- Path to extracted deer-flow monorepo
- Optional catalog.json

## Process
1. Parse all production SKILL.md (exclude eval fixtures)
2. Enumerate harness tools, MCP, extensions
3. Emit skill-engine state.json + trees + dashboard
4. Package backup tar.gz and upload to Drive folder deer-flow-builds

