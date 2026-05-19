#!/usr/bin/env bash
# Standards checks for fibronet.in — see docs/static-site-standards.md
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

ERRORS=0
WARNINGS=0

error() {
  echo "ERROR: $*" >&2
  ERRORS=$((ERRORS + 1))
}

warn() {
  echo "WARN: $*" >&2
  WARNINGS=$((WARNINGS + 1))
}

collect_html_files() {
  case "${1:-}" in
    --staged)
      git diff --cached --name-only --diff-filter=ACM | grep -E '\.html?$' || true
      ;;
    --changed)
      if git rev-parse --verify HEAD~1 >/dev/null 2>&1; then
        git diff --name-only --diff-filter=ACM HEAD~1 HEAD | grep -E '\.html?$' || true
      else
        find . -name '*.html' ! -path './.git/*' ! -path './old/*' ! -path './new/*' | sort
      fi
      ;;
    --pr)
      local base="${PR_BASE:-origin/main}"
      if git rev-parse --verify "$base" >/dev/null 2>&1; then
        git diff --name-only --diff-filter=ACM "$base"...HEAD | grep -E '\.html?$' || true
      else
        git diff --name-only --diff-filter=ACM HEAD~1 HEAD 2>/dev/null | grep -E '\.html?$' || true
      fi
      ;;
    *)
      find . -name '*.html' ! -path './.git/*' ! -path './old/*' ! -path './new/*' | sort
      ;;
  esac
}

check_html_file() {
  local file="$1"
  local content
  content="$(cat "$file")"

  if ! grep -qiE '<html[^>]*\blang=' <<<"$content"; then
    error "$file: missing lang on <html> (docs/static-site-standards.md — HTML5)"
  fi

  if ! grep -qiE '<meta[^>]+charset=["'\'']?utf-8' <<<"$content" \
    && ! grep -qi 'http-equiv=["'\'']Content-Type["'\'']' <<<"$content"; then
    error "$file: missing UTF-8 charset meta"
  fi

  if ! grep -qi 'name=["'\'']viewport["'\'']' <<<"$content"; then
    error "$file: missing viewport meta"
  fi

  local title_text
  title_text="$(sed -n '/<title>/,/<\/title>/p' "$file" | sed '1d;$d' | tr -d '[:space:]')"
  if ! grep -qi '<title>' <<<"$content" || [[ -z "$title_text" ]]; then
    error "$file: missing or empty <title>"
  fi

  if ! grep -qi 'name=["'\'']description["'\'']' <<<"$content"; then
    warn "$file: missing meta description (SEO)"
  fi

  # External target=_blank must use noopener
  while IFS= read -r line_num; do
    [[ -z "$line_num" ]] && continue
    local start end chunk
    start=$((line_num > 3 ? line_num - 3 : 1))
    end=$((line_num + 3))
    chunk="$(sed -n "${start},${end}p" "$file" | tr '\n' ' ')"
    if grep -qi 'target=["'\'']_blank["'\'']' <<<"$chunk" \
      && ! grep -qi 'noopener' <<<"$chunk"; then
      error "$file:$line_num: target=_blank without rel noopener noreferrer"
    fi
  done < <(grep -n 'target=["'\'']_blank["'\'']' "$file" 2>/dev/null | cut -d: -f1 || true)
}

main() {
  if [[ ! -f docs/static-site-standards.md ]]; then
    error "docs/static-site-standards.md is missing"
  fi

  local mode="${1:-}"
  local files=()
  while IFS= read -r f; do
    [[ -n "$f" ]] && files+=("$f")
  done < <(collect_html_files "$mode")

  if [[ ${#files[@]} -eq 0 ]]; then
    if [[ "$mode" == "--staged" || "$mode" == "--changed" || "$mode" == "--pr" ]]; then
      echo "No HTML files to check for mode '$mode' — skipping."
      exit 0
    fi
    warn "No HTML files found to check."
    exit 0
  fi

  echo "Checking ${#files[@]} HTML file(s) against static-site-standards…"
  for f in "${files[@]}"; do
    check_html_file "$f"
  done

  echo ""
  echo "Done: $ERRORS error(s), $WARNINGS warning(s)."
  if [[ $ERRORS -gt 0 ]]; then
    echo "See docs/static-site-standards.md and .cursor/rules/"
    exit 1
  fi
  exit 0
}

main "$@"
