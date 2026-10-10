# GitHub Repository Structure

Recommended remote layout for this build:

```
deer-flow-workspace/
├── README.md
├── ROOT_WORKSPACE/          # generated ontology, encyclopedias, skill engine
├── deer-flow/               # vendor or submodule of bytedance/deer-flow
├── .github/workflows/
│   ├── skill-tree-cycle.yml
│   └── deploy-frontend.yml
└── docs/
```

Submodule option:
```bash
git submodule add https://github.com/bytedance/deer-flow.git deer-flow
```
