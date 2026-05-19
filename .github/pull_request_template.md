## Summary

<!-- What changed and why -->

## Standards

Full spec: [docs/static-site-standards.md](../docs/static-site-standards.md)

Run locally before opening PR:

```bash
./scripts/check-standards.sh
git config core.hooksPath .githooks   # once per clone — enables pre-commit checks
```

## Checklist

### HTML & structure
- [ ] `<html lang="…">`, UTF-8 charset, viewport meta
- [ ] Semantic landmarks (`header`, `nav`, `main`, `footer`, …)
- [ ] One `<h1>`; heading levels do not skip
- [ ] Skip link; external `target="_blank"` uses `rel="noopener noreferrer"`

### SEO
- [ ] Unique `<title>` and meta description
- [ ] Canonical URL; valid Open Graph + Twitter Cards
- [ ] OG image 1200×630 where applicable
- [ ] JSON-LD updated if page type changed
- [ ] `sitemap.xml` / `robots.txt` updated for new routes

### CSS
- [ ] Design tokens / CSS variables; dark mode via `prefers-color-scheme` (+ storage if toggled)
- [ ] `:focus-visible` styles; `prefers-reduced-motion` respected
- [ ] No `@import` for Google Fonts (use `<link>` in HTML)

### JavaScript
- [ ] New code is ES modules (`type="module" defer`) — not added to `js/bundle-*.js`
- [ ] Event listeners cleaned up (`AbortController`) where needed

### Accessibility (WCAG 2.2 AA target)
- [ ] Alt text on images; ARIA only where semantics fall short
- [ ] Keyboard operable; icon-only buttons have `aria-label`
- [ ] Contrast checked on new UI

### Performance & media
- [ ] LCP image: dimensions set, `fetchpriority` if hero
- [ ] Below-fold images: `loading="lazy"`; `<picture>` for WebP/AVIF where used
- [ ] Scripts non-blocking; minimal JS added

### Manual verification (major changes)
- [ ] [Lighthouse](https://developer.chrome.com/docs/lighthouse) / PageSpeed Insights
- [ ] [W3C HTML Validator](https://validator.w3.org/)
- [ ] [axe](https://www.deque.com/axe/) or WAVE
- [ ] [Rich Results Test](https://search.google.com/test/rich-results) if schema changed
