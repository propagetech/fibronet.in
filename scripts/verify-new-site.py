#!/usr/bin/env python3
"""Self-check: images + text coverage old vs new."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / "old"
SITE = ROOT


def normalize_text(s: str) -> str:
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def collect_text(path: Path) -> set[str]:
    if not path.exists():
        return set()
    raw = path.read_text(encoding="utf-8", errors="ignore")
    raw = re.sub(r"<script[\s\S]*?</script>", " ", raw, flags=re.I)
    raw = re.sub(r"<style[\s\S]*?</style>", " ", raw, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", raw)
    chunks = set()
    for part in re.split(r"[.!?]\s+", text):
        part = normalize_text(part)
        if len(part) >= 40:
            chunks.add(part)
    return chunks


def collect_images(dir_path: Path) -> set[str]:
    if not dir_path.exists():
        return set()
    return {p.name for p in dir_path.iterdir() if p.is_file()}


def page_pairs() -> list[tuple[Path, Path]]:
    pairs = [(OLD / "index.html", SITE / "index.html")]
    for old_html in OLD.glob("*.html"):
        name = old_html.name
        if name == "index.html":
            continue
        slug = old_html.stem
        if name == "404.html":
            new_p = SITE / "404.html"
        elif slug == "about-us":
            new_p = SITE / "about" / "index.html"
        elif slug == "contact-us":
            new_p = SITE / "contact" / "index.html"
        else:
            new_p = SITE / slug / "index.html"
        pairs.append((old_html, new_p))
    return pairs


def estimate_page_weight(html_path: Path, base: Path) -> int:
    html = html_path.read_text(encoding="utf-8")
    total = len(html.encode("utf-8"))
    for m in re.finditer(r"""href=["']([^"']+\.css)["']""", html):
        css = base / m.group(1).lstrip("/")
        if css.exists():
            total += css.stat().st_size
    for m in re.finditer(r"""src=["']([^"']+\.js)["']""", html):
        js = base / m.group(1).lstrip("/")
        if js.exists():
            total += js.stat().st_size
    return total


def main() -> int:
    old_imgs = collect_images(OLD / "imgs")
    new_imgs = collect_images(SITE / "imgs")
    missing_imgs = old_imgs - new_imgs
    extra_imgs = new_imgs - old_imgs

    print("## Images")
    print(f"old/imgs: {len(old_imgs)} files")
    print(f"imgs/: {len(new_imgs)} files")
    if missing_imgs:
        print("MISSING in site imgs:", sorted(missing_imgs))
    else:
        print("All old images present in imgs/ ✓")
    if extra_imgs:
        print("Extra in imgs:", sorted(extra_imgs))

    print("\n## Text coverage (chunks ≥40 chars)")
    missing_all: list[str] = []
    for old_p, new_p in page_pairs():
        if not new_p.exists():
            print(f"MISSING PAGE: {new_p.relative_to(ROOT)}")
            continue
        old_chunks = collect_text(old_p)
        new_chunks = collect_text(new_p)
        missing = []
        for c in old_chunks:
            if not any(c in n or n in c for n in new_chunks):
                missing.append(c)
        if missing:
            print(f"\n{old_p.name} -> {new_p.relative_to(ROOT)}: {len(missing)} possibly missing chunks")
            for m in missing[:5]:
                print(f"  - {m[:120]}...")
            missing_all.extend(missing)
        else:
            print(f"{old_p.name}: OK")

    print("\n## Estimated transfer (HTML + site.css + main.js, no fonts/images)")
    for label, path in [
        ("index", SITE / "index.html"),
        ("about", SITE / "about" / "index.html"),
        ("plan", SITE / "fibronet-30-50" / "index.html"),
    ]:
        if path.exists():
            kb = estimate_page_weight(path, SITE) / 1024
            if path.parent != SITE:
                kb = len(path.read_text().encode()) / 1024
                kb += (SITE / "css" / "site.css").stat().st_size / 1024
                kb += (SITE / "js" / "main.js").stat().st_size / 1024
            print(f"  {label}: ~{kb:.1f} KB (shell only)")

    return 1 if missing_imgs or missing_all else 0


if __name__ == "__main__":
    sys.exit(main())
