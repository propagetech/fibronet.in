# Static site standards (fibronet.in)

Authoritative tech spec for this project. Cursor rules summarize and enforce this document; when in doubt, follow every section here.

**Stack:** Vanilla HTML5, CSS (no preprocessor), ES modules JavaScript. No frameworks unless explicitly requested.

**Legacy note:** Existing `js/bundle-*.js` and `css/main-*.css` are legacy. New features use ES modules under `js/` and consolidated CSS; migrate bundles only when asked.

---

## HTML5

- Semantic elements: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`
- `<picture>`, `<source>`, `<figure>`, `<figcaption>`
- `<dialog>`, `<details>`, `<summary>`
- `<template>`, `<slot>`
- `<time>`, `<mark>`, `<abbr>`
- Microdata / `itemprop`
- `lang` attribute on `<html>`
- Viewport meta
- Charset UTF-8 (`<meta charset="utf-8">`)
- Open Graph meta
- Twitter Cards meta
- JSON-LD schema.org

---

## CSS (vanilla, no preprocessor)

- Custom properties (CSS variables)
- Cascade layers (`@layer`)
- Flexbox, Grid, Subgrid
- Container queries (`@container`)
- Media queries
- `prefers-color-scheme`, `prefers-reduced-motion`, `prefers-contrast`
- Logical properties (`margin-inline`, `padding-block`)
- `clamp()`, `min()`, `max()`
- `:has()`, `:is()`, `:where()`, `:not()`
- `:focus-visible`, `:focus-within`
- Nesting (`&`)
- View Transitions API
- CSS animations / transitions / keyframes
- `aspect-ratio`
- `gap`
- `scroll-snap`, `scroll-behavior`
- `backdrop-filter`
- `color-mix()`, `oklch()`, `lch()`
- Anchor positioning
- `content-visibility`

---

## Vanilla JS (ES modules)

- `<script type="module">`
- `defer`, `async`
- IntersectionObserver (lazy load / scroll effects)
- MutationObserver
- ResizeObserver
- Fetch API (load JSON / partials)
- Web Components / Custom Elements / Shadow DOM
- HTML `<template>`
- Event delegation
- `addEventListener`, `AbortController`
- `localStorage`, `sessionStorage`
- History API, `pushState`, `popstate`
- Clipboard API
- `matchMedia`
- `requestAnimationFrame`, `requestIdleCallback`
- `structuredClone`
- Optional chaining, nullish coalescing
- ES2020+ syntax

---

## Theming

- Light / Dark mode
- `color-scheme` meta
- `prefers-color-scheme`
- CSS variables (design tokens)
- `localStorage` persistence
- System sync

---

## SEO

- `<title>`, `<meta name="description">`
- Canonical URL
- Open Graph (`og:title`, `og:image`, etc.)
- Twitter Cards
- `sitemap.xml`
- `robots.txt`
- JSON-LD (Article, BreadcrumbList, Organization, Person, WebSite)
- Hreflang (if multilingual)
- Clean folder URLs (`/about/`)
- OG image 1200×630

---

## Accessibility

- Semantic HTML
- ARIA roles / states / properties
- `aria-label`, `aria-labelledby`, `aria-describedby`
- `aria-live`, `aria-hidden`, `aria-expanded`
- Landmark regions
- Heading hierarchy (h1→h6)
- Skip link
- Keyboard navigation
- `:focus-visible` styles
- Tab order, `tabindex`
- Alt text
- WCAG 2.2 AA contrast
- Reduced motion respect
- Screen reader testing (NVDA, VoiceOver)

---

## Performance

- Lighthouse 100% (target)
- Core Web Vitals (LCP, INP, CLS)
- Inline critical CSS
- Preload critical assets
- Preconnect, dns-prefetch
- `loading="lazy"` (img, iframe)
- `decoding="async"`
- `fetchpriority`
- Async/defer scripts
- Minimal JS payload
- No render-blocking resources
- Font subsetting
- `font-display: swap`
- HTTP/2, HTTP/3 (via Cloudflare)

---

## Images / media

- WebP, AVIF with `<picture>` fallback
- Responsive: `srcset`, `sizes`
- Inline SVG (icons, logos)
- SVG sprites
- Native lazy loading
- Compression (Squoosh, ImageOptim)
- Width / height attributes (prevent CLS)
- `<video>` poster, `preload="none"`

---

## PWA (optional)

- `manifest.json`
- Service Worker (Cache API)
- Offline fallback
- Install prompt
- Maskable icons
- `theme-color` meta
- `apple-touch-icon`

---

## Browser APIs (no library required)

- IntersectionObserver
- Fetch
- localStorage
- Web Animations API
- Web Storage
- History API
- Clipboard API
- Share API (`navigator.share`)
- Wake Lock API
- View Transitions API

---

## File structure

Target layout (migrate toward this; current `imgs/` may map to `/images/` or `/assets/`):

- `index.html` per folder (clean URLs)
- `/assets/`, `/images/`, `/css/`, `/js/`
- `404.html`
- `robots.txt`
- `sitemap.xml`
- `humans.txt`
- `manifest.json`
- `sw.js`
- `favicon.ico`, `favicon.svg`, apple-touch-icon
- `.well-known/security.txt`
- `CNAME` (custom domain)
- `.nojekyll`

---

## Link safety

- `rel="noopener noreferrer"` on external `target="_blank"`
- `rel="nofollow"` (where appropriate)
- `rel="me"` (verified profiles)

---

## Validation / testing tools

- W3C HTML Validator
- W3C CSS Validator
- Lighthouse (Chrome DevTools)
- PageSpeed Insights
- WebPageTest
- axe DevTools
- WAVE
- securityheaders.com
- SSL Labs (ssllabs.com)
- Mozilla Observatory
- Rich Results Test (Google)
- Schema Markup Validator
- Open Graph debugger (Facebook, Twitter)
- Lychee / linkchecker (broken links)

---

## Browser DevTools

- Elements / Inspector
- Network panel (waterfall, sizes)
- Performance panel
- Lighthouse panel
- Coverage (unused CSS/JS)
- Rendering (paint flashing, FPS)
- Application (storage, SW, manifest)
- Accessibility tree

---

## Version control

- Git
- `.gitignore`
- Conventional commits
- Branches (`main`, `dev`)
- Tags / releases

---

## Code style

- 2 or 4 space indent (match `.editorconfig` when present)
- `.editorconfig`
- Consistent quotes
- Semantic naming (BEM optional for CSS)
- File-per-component (if using web components)

---

## Misc

- Favicon generator (realfavicongenerator.net)
- OG image generator
- RSS feed (hand-written XML, optional)
- Sitemap generator
- Reading time (JS calc)
- Smooth anchor scroll
- Back-to-top button
- Print stylesheet (`@media print`)

---

## Fonts & icons (Google + system fallback)

### Fonts

- System font stack as fallback in `font-family`
- Preconnect to `fonts.googleapis.com` + `fonts.gstatic.com` (`crossorigin`)
- `&display=swap` in URL (FOUT acceptable)
- woff2 only (no woff/ttf fallback for modern browsers)
- Pick only used weights / styles
- Prefer variable fonts when available
- Single `<link>` for multiple families
- `<link>` in `<head>` (not `@import` in CSS)
- Preload critical woff2: `<link rel="preload" as="font" type="font/woff2" crossorigin>`
- Max 2 font families (body + display)
- `&text=` param for logo-only / hero text (exact glyph subset)
- Optional self-host woff2 for Lighthouse 100 + privacy

### Icons (Material Symbols)

- Material Symbols (variable) over legacy Material Icons
- Variants: Outlined / Rounded / Sharp
- Axes: FILL, wght, GRAD, opsz
- Usage: `<span class="material-symbols-outlined">home</span>`
- `&display=block` (avoid ligature flash)
- Specify only axes you need (smaller file)
- `font-variation-settings` for fill/weight
- Size via `font-size`, color via `color`
- ARIA: `aria-hidden="true"` on decorative
- ARIA: `aria-label` on icon-only buttons
- Alternative: inline SVG from fonts.google.com/icons → zero network, better perf/a11y
