# fibronet.in

Static ISP marketing site (vanilla HTML, CSS, ES modules).

- **Full tech spec:** [docs/static-site-standards.md](docs/static-site-standards.md)
- **Cursor AI rules:** `.cursor/rules/` (summaries + enforcement; always read the doc for the complete checklist)

## Quality checks

```bash
./scripts/check-standards.sh          # all HTML in repo root
git config core.hooksPath .githooks   # enable pre-commit (once per clone)
```

CI runs the same script on pull requests and pushes to `main` / `dev` (see `.github/workflows/quality.yml`).