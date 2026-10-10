---
name: catalog-navigator
description: Navigate and search the 4344-skill catalog.json by category, completeness, and keywords. Use when user asks to find a skill in the catalog, list categories, or install candidates.
---

# Catalog Navigator

## Workflow
1. Load `encyclopedias/catalog.json` or external catalog path.
2. Filter by `category`, `status`, `completeness`.
3. Return top-N matches with id, description, pack.
4. Optionally propose install list (do not bulk install).

