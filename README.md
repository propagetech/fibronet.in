# fibronet.in

Static ISP marketing site (vanilla HTML, CSS, ES modules).

- **Site (vanilla HTML/CSS/ES modules):** repo root — `index.html`, `css/site.css`, `js/main.js`, `imgs/`
- **Legacy snapshot:** [`old/`](old/) — source HTML for regeneration
- Generate/regenerate: `python3 scripts/generate-new-site.py`
- Verify assets + copy: `python3 scripts/verify-new-site.py`

- **Full tech spec:** [docs/static-site-standards.md](docs/static-site-standards.md)
- **Cursor AI rules:** `.cursor/rules/` (summaries + enforcement; always read the doc for the complete checklist)

## Quality checks

```bash
./scripts/check-standards.sh          # audit all HTML
./scripts/check-standards.sh --pr     # only HTML changed vs origin/main
git config core.hooksPath .githooks   # pre-commit: staged HTML only
```

CI: PRs check changed HTML vs base branch; pushes check HTML in the latest commit (`.github/workflows/quality.yml`).
