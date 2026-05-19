#!/usr/bin/env python3
"""Generate site at repo root from ./old/ with modern shell and verbatim content."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from bs4 import BeautifulSoup, Comment

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / "old"
SITE = ROOT
BASE_URL = "https://www.fibronet.in"

LINK_MAP = {
    "home.html": "",
    "index.html": "",
    "/": "/",
    "about-us.html": "about/",
    "business.html": "business/",
    "residential.html": "residential/",
    "contact-us.html": "contact/",
    "privacy-policy.html": "privacy-policy/",
    "terms-and-conditions.html": "terms-and-conditions/",
    "disclaimer.html": "disclaimer/",
    "fibronet-30-50.html": "fibronet-30-50/",
    "fibronet-40-75.html": "fibronet-40-75/",
    "fibronet-75-100.html": "fibronet-75-100/",
    "fibronet-100-600.html": "fibronet-100-600/",
    "fibronet-125-ul.html": "fibronet-125-ul/",
    "fibronet-125-900.html": "fibronet-125-900/",
    "fibronet-150-ul.html": "fibronet-150-ul/",
    "fibronet-150-1200.html": "fibronet-150-1200/",
    "fibronet-200-ul.html": "fibronet-200-ul/",
    "fibronet-200-1500.html": "fibronet-200-1500/",
}

PAGE_OUT = {
    "index.html": SITE / "index.html",
    "404.html": SITE / "404.html",
    "about-us.html": SITE / "about" / "index.html",
    "business.html": SITE / "business" / "index.html",
    "residential.html": SITE / "residential" / "index.html",
    "contact-us.html": SITE / "contact" / "index.html",
    "privacy-policy.html": SITE / "privacy-policy" / "index.html",
    "terms-and-conditions.html": SITE / "terms-and-conditions" / "index.html",
    "disclaimer.html": SITE / "disclaimer" / "index.html",
    "fibronet-30-50.html": SITE / "fibronet-30-50" / "index.html",
    "fibronet-40-75.html": SITE / "fibronet-40-75" / "index.html",
    "fibronet-75-100.html": SITE / "fibronet-75-100" / "index.html",
    "fibronet-100-600.html": SITE / "fibronet-100-600" / "index.html",
    "fibronet-125-ul.html": SITE / "fibronet-125-ul" / "index.html",
    "fibronet-125-900.html": SITE / "fibronet-125-900" / "index.html",
    "fibronet-150-ul.html": SITE / "fibronet-150-ul" / "index.html",
    "fibronet-150-1200.html": SITE / "fibronet-150-1200" / "index.html",
    "fibronet-200-ul.html": SITE / "fibronet-200-ul" / "index.html",
    "fibronet-200-1500.html": SITE / "fibronet-200-1500" / "index.html",
}

CONTACT_EMAIL = "avinashds@yahoo.com"

PRESTO_EMBED_SCRIPT = """<script type="text/javascript">
   (function(funcName, baseObj) {
    // The public function name defaults to window.docReady
    // but you can pass in your own object and own function name and those will be used
    // if you want to put them in a different namespace
    funcName = funcName || "docReady";
    baseObj = baseObj || window;
    var readyList = [];
    var readyFired = false;
    var readyEventHandlersInstalled = false;

    // call this when the document is ready
    // this function protects itself against being called more than once
    function ready() {
        if (!readyFired) {
            // this must be set to true before we start calling callbacks
            readyFired = true;
            for (var i = 0; i < readyList.length; i++) {
                // if a callback here happens to add new ready handlers,
                // the docReady() function will see that it already fired
                // and will schedule the callback to run right after
                // this event loop finishes so all handlers will still execute
                // in order and no new ones will be added to the readyList
                // while we are processing the list
                readyList[i].fn.call(window, readyList[i].ctx);
            }
            // allow any closures held by these functions to free
            readyList = [];
        }
    }

    function readyStateChange() {
        if ( document.readyState === "complete" ) {
            ready();
        }
    }

    // This is the one public interface
    // docReady(fn, context);
    // the context argument is optional - if present, it will be passed
    // as an argument to the callback
    baseObj[funcName] = function(callback, context) {
        if (typeof callback !== "function") {
            throw new TypeError("callback for docReady(fn) must be a function");
        }
        // if ready has already fired, then just schedule the callback
        // to fire asynchronously, but right away
        if (readyFired) {
            setTimeout(function() {callback(context);}, 1);
            return;
        } else {
            // add the function and context to the list
            readyList.push({fn: callback, ctx: context});
        }
        // if document already ready to go, schedule the ready function to run
        if (document.readyState === "complete") {
            setTimeout(ready, 1);
        } else if (!readyEventHandlersInstalled) {
            // otherwise if we don't have event handlers installed, install them
            if (document.addEventListener) {
                // first choice is DOMContentLoaded event
                document.addEventListener("DOMContentLoaded", ready, false);
                // backup is window load event
                window.addEventListener("load", ready, false);
            } else {
                // must be IE
                document.attachEvent("onreadystatechange", readyStateChange);
                window.attachEvent("onload", ready);
            }
            readyEventHandlersInstalled = true;
        }
    }
})("docReady", window);
docReady(function() {
    // code here
    if (window.location.href.indexOf("console") == -1) {

            var script = document.createElement('script');
            script.type = 'text/javascript';
            script.src = 'https://s3-ap-southeast-1.amazonaws.com/staging-websites/presto-shopping/presto_connections.js';
            document.getElementsByTagName('body')[0].appendChild(script);

            script.onload = function() {
                console.log( 'loaded presto shopping' );
                var initOptions = {
                  "controller": "/embed/presto-pay/",
                  "configParams": {
                    "merchant_id": "5cca8fc31e4cd66c8b00209f",
                    "app_id": "59d4cc24a4d34100046255b6",
                    "merchant_name": "Fibronet",
                    "merchant_logo": ""
                  },
                  "shoppingWindowOptions": {
                    "environment": "production",
                    "merchantType": "connections",
                    "currency": "rupee"
                  }
                }
                PrestoEmbedManager.init(initOptions);
            }
        }
});
  </script>"""


def contact_form_html() -> str:
    return """
<form class="contact-form form-horizontal" id="contact-form" action="#" method="post" novalidate>
<div class="contact-form__grid">
<div class="contact-form__col">
<p class="contact-name">
<label class="visually-hidden" for="customerName">Name</label>
<input id="customerName" name="name" placeholder="Name" required type="text" autocomplete="name">
</p>
<p class="contact-email">
<label class="visually-hidden" for="customerEmail">Email Address</label>
<input id="customerEmail" name="email" placeholder="Email Address" required type="email" autocomplete="email">
</p>
<p class="contact-phone">
<label class="visually-hidden" for="customerPhone">Phone Number</label>
<input id="customerPhone" name="phone" placeholder="Phone Number" type="tel" autocomplete="tel">
</p>
</div>
<div class="contact-form__col">
<p class="contact-message">
<label class="visually-hidden" for="customerMessage">Message</label>
<textarea cols="40" id="customerMessage" name="message" placeholder="Message" required rows="8"></textarea>
</p>
<div class="contact-submit">
<input class="btn btn--brand" type="submit" value="SEND">
</div>
</div>
</div>
<div id="response" class="contact-form__status" role="status" aria-live="polite" hidden></div>
</form>
""".strip()


def map_embed_html(lat: float = 12.8859421, lng: float = 77.567846, zoom: int = 16) -> str:
    q = f"{lat},{lng}"
    src = f"https://maps.google.com/maps?q={q}&amp;z={zoom}&amp;output=embed"
    return f"""
<div class="contact-map" aria-label="Map showing office location">
<iframe title="Sherie's Fibronet office location" src="{src}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
</div>
""".strip()


def depth_for(out_path: Path) -> int:
    rel = out_path.relative_to(SITE)
    return len(rel.parts) - 1


def canonical_url(current_path: str) -> str:
    path = current_path.strip("/")
    if not path or path == "404":
        return f"{BASE_URL}/" if path != "404" else f"{BASE_URL}/404.html"
    return f"{BASE_URL}/{path}/"


def absolute_asset_url(relative: str, depth: int) -> str:
    if relative.startswith(("http://", "https://")):
        return relative
    return BASE_URL.rstrip("/") + "/" + rewrite_src(relative, depth).lstrip("./")


def json_ld_scripts(meta: dict, current_path: str) -> str:
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Sherie's Fibronet",
        "url": BASE_URL + "/",
        "logo": f"{BASE_URL}/imgs/logo-fibronet.webp",
        "email": CONTACT_EMAIL,
        "telephone": "+91-80-41488850",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "#13, 9th Cross, New Bank Colony, Chunchgatta Main Road, Konanakunte",
            "addressLocality": "Bangalore",
            "postalCode": "560062",
            "addressCountry": "IN",
        },
    }
    website = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": meta["title"].split("|")[0].strip(),
        "url": BASE_URL + "/",
        "publisher": {"@id": f"{BASE_URL}/#organization"},
    }
    org["@id"] = f"{BASE_URL}/#organization"
    blocks = [org, website]
    crumbs = []
    slug = current_path.strip("/")
    if slug and slug != "404":
        crumbs.append({"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"})
        label = meta["title"].split("|")[-1].strip() if "|" in meta["title"] else meta["title"]
        crumbs.append(
            {
                "@type": "ListItem",
                "position": 2,
                "name": label,
                "item": canonical_url(current_path),
            }
        )
        blocks.append(
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": crumbs,
            }
        )
    return "\n".join(
        f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>'
        for block in blocks
    )


def prefix(depth: int) -> str:
    return "../" * depth


def rewrite_href(href: str, depth: int) -> str:
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return href
    if href.startswith("http://") or href.startswith("https://"):
        return href
    clean = href.split("#")[0]
    frag = "#" + href.split("#", 1)[1] if "#" in href else ""
    for old, new in LINK_MAP.items():
        if clean == old or clean.endswith("/" + old):
            p = prefix(depth)
            return (new if new.startswith("/") else p + new.lstrip("/")) + frag
    if clean.endswith(".html"):
        slug = Path(clean).stem
        if slug in ("index", "home"):
            return prefix(depth) + ("" if depth else "") or "/"
        return prefix(depth) + slug + "/"
    return href


def rewrite_src(src: str, depth: int) -> str:
    if not src or src.startswith(("http://", "https://", "data:")):
        return src
    if src.startswith("imgs/"):
        return prefix(depth) + src
    return src


def extract_meta(soup: BeautifulSoup) -> dict:
    title = soup.title.get_text(strip=True) if soup.title else ""
    desc = ""
    m = soup.find("meta", attrs={"name": "description"})
    if m and m.get("content"):
        desc = m["content"]
    og_image = ""
    og = soup.find("meta", property="og:image")
    if og and og.get("content"):
        og_image = og["content"]
    return {"title": title, "description": desc, "og_image": og_image}


def extract_main_html(soup: BeautifulSoup) -> str:
    menu = soup.find(id=re.compile(r"viamagus_Menu"))
    footer = soup.find("footer", class_=re.compile(r"viamagus_footer"))
    if not menu or not footer:
        return ""
    parts = []
    sib = menu.find_parent(class_=re.compile(r"viamagus-component"))
    if sib:
        sib = sib.find_next_sibling()
    else:
        sib = menu.find_next_sibling()
    while sib and sib != footer and (getattr(sib, "name", None) != "footer"):
        parts.append(str(sib))
        sib = sib.find_next_sibling()
    return "\n".join(parts)


def transform_content(html: str, depth: int) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["script", "style", "link"]):
        tag.decompose()
    for form in soup.find_all("form"):
        form["class"] = list(dict.fromkeys([*(form.get("class") or []), "contact-form", "form-horizontal"]))
        form["id"] = form.get("id") or "contact-form"
        form["action"] = "#"
        form["method"] = "post"
        if "novalidate" in form.attrs:
            del form["novalidate"]
        form.attrs["novalidate"] = ""
        submit = form.find("input", attrs={"type": "submit"})
        if submit:
            submit["class"] = list(dict.fromkeys([*(submit.get("class") or []), "btn", "btn--brand"]))
        phone = form.find("input", id="customerPhone")
        if phone:
            phone["name"] = "phone"
            phone["type"] = "tel"
            phone["autocomplete"] = "tel"
    for comp in soup.find_all(attrs={"data-component-name": re.compile(r"^Address$")}):
        lat, lng, zoom = 12.8859421, 77.567846, 16
        latlng_el = comp.find(class_=re.compile(r"viamagus-google-latlng"))
        if latlng_el:
            m = re.search(r'"lat"\s*:\s*([-\d.]+).*"lng"\s*:\s*([-\d.]+)', latlng_el.get_text())
            if m:
                lat, lng = float(m.group(1)), float(m.group(2))
        zoom_in = comp.find("input", class_=re.compile(r"viamagus-google-mapzoom"))
        if zoom_in and zoom_in.get("value"):
            try:
                zoom = int(zoom_in["value"])
            except ValueError:
                pass
        embed = BeautifulSoup(map_embed_html(lat, lng, zoom), "html.parser")
        comp.replace_with(embed)
    for c in soup.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()
    for a in soup.find_all("a", href=True):
        a["href"] = rewrite_href(a["href"], depth)
    for img in soup.find_all("img"):
        if img.get("src"):
            img["src"] = rewrite_src(img["src"], depth)
            if not img.get("width") and "style" in img.attrs:
                w = re.search(r"width:\s*(\d+)", img["style"])
                h = re.search(r"height:\s*(\d+)", img["style"])
                if w:
                    img["width"] = w.group(1)
                if h:
                    img["height"] = h.group(1)
        if img.get("data-original"):
            img["data-original"] = rewrite_src(img["data-original"], depth)
        img["loading"] = "lazy"
        img["decoding"] = "async"
    for el in soup.find_all(style=True):
        style = el["style"]
        style = re.sub(
            r"url\(['\"]?(imgs/[^'\")]+)['\"]?\)",
            lambda m: f"url('{rewrite_src(m.group(1), depth)}')",
            style,
        )
        el["style"] = style
    for el in soup.find_all(attrs={"data-bkg-image": True}):
        if el["data-bkg-image"]:
            el["data-bkg-image"] = rewrite_src(el["data-bkg-image"], depth)
    for el in soup.find_all(attrs={"data-img-uri": True}):
        if el["data-img-uri"]:
            el["data-img-uri"] = rewrite_src(el["data-img-uri"], depth)
    # collapse headers -> details
    for header in soup.find_all(class_=re.compile(r"viamagus-collapse-header")):
        parent = header.parent
        content = parent.find(id=re.compile(r"-content$")) if parent else None
        if content and parent:
            label = header.get_text(strip=True)
            details = soup.new_tag("details", attrs={"class": "plan-period"})
            summary = soup.new_tag("summary")
            summary.string = label
            body = soup.new_tag("div", attrs={"class": "plan-period__body"})
            body.append(content.extract())
            details.append(summary)
            details.append(body)
            header.decompose()
            parent.replace_with(details)
    return str(soup)


def shell(
    meta: dict,
    body: str,
    depth: int,
    current_path: str = "",
) -> str:
    p = prefix(depth)
    og = meta.get("og_image") or "imgs/logo-fibronet-2.webp"
    og_url = absolute_asset_url(og, depth)
    canonical = canonical_url(current_path)
    ld_json = json_ld_scripts(meta, current_path)
    esc_title = meta["title"].replace('"', "&quot;")
    esc_desc = meta["description"].replace('"', "&quot;")
    critical = (
        "body{margin:0;background:#050a14;color:#f0f4fc}"
        ".site-header{position:sticky;top:0;z-index:100;height:72px;"
        "background:#fff;border-bottom:1px solid rgba(7,25,77,.12)}"
    )
    cur_path = current_path.strip("/")
    nav_items = [
        ("", "HOME"),
        ("about/", "ABOUT US"),
    ]
    nav_html = ""
    for href, label in nav_items:
        full = f"{p}{href}" if href else (p or "./")
        slug = href.rstrip("/") if href else ""
        cur = ' aria-current="page"' if (slug == cur_path or (not slug and not cur_path)) else ""
        nav_html += f'<li><a href="{full}"{cur}>{label}</a></li>\n'
    res_href = f"{p}residential/"
    biz_href = f"{p}business/"
    plans_open = cur_path in ("residential", "business")
    plans_cur = ' aria-current="true"' if plans_open else ""
    plans_open_class = " is-open" if plans_open else ""
    nav_html += f"""<li class="nav-item nav-item--has-submenu{plans_open_class}">
<button type="button" class="nav-submenu-toggle" aria-expanded="{"true" if plans_open else "false"}" aria-haspopup="true"{plans_cur}>PLANS</button>
<ul class="nav-submenu">
<li><a href="{res_href}"{" aria-current=\"page\"" if cur_path == "residential" else ""}>RESIDENTIAL</a></li>
<li><a href="{biz_href}"{" aria-current=\"page\"" if cur_path == "business" else ""}>BUSINESS</a></li>
</ul>
</li>
"""
    contact_href = f"{p}contact/"
    contact_cur = ' aria-current="page"' if cur_path == "contact" else ""
    nav_html += f'<li><a href="{contact_href}"{contact_cur}>CONTACT US</a></li>\n'
    login_href = "https://login.fibronet.in/customer_portal"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{meta["title"]}</title>
<meta name="description" content="{esc_desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Sherie's Fibronet">
<meta property="og:title" content="{esc_title}">
<meta property="og:description" content="{esc_desc}">
<meta property="og:image" content="{og_url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_title}">
<meta name="twitter:description" content="{esc_desc}">
<meta name="twitter:image" content="{og_url}">
<link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="shortcut icon" href="/favicon.ico">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">
{ld_json}
<style>{critical}</style>
<link rel="preload" href="{p}css/site.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="{p}css/site.css"></noscript>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
<div class="site-header__inner">
<a class="brand" href="{p or './'}"><img src="{p}imgs/logo-fibronet.webp" alt="logo" width="160" height="44" fetchpriority="high"></a>
<button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
<nav class="site-nav" aria-label="Main">
<ul>
{nav_html}<li><a class="nav-cta" href="{login_href}" target="_blank" rel="noopener noreferrer">LOGIN</a></li>
</ul>
</nav>
</div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
<div class="container site-footer__inner">
<p>© 2026. Sherie's fibronet. All Rights Reserved.</p>
<nav class="footer-links" aria-label="Legal">
<a href="{p}terms-and-conditions/">Terms &amp; Conditions</a>
<a href="{p}disclaimer/">Disclaimer</a>
<a href="{p}privacy-policy/">Privacy Policy</a>
</nav>
<p class="footer-meta"><a href="https://propage.in" target="_blank" rel="noopener noreferrer">powered by propage.in</a></p>
</div>
</footer>
{PRESTO_EMBED_SCRIPT}
<script type="module" src="{p}js/main.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-160601521-43"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag("js", new Date());
gtag("config", "UA-160601521-43");
</script>
</body>
</html>"""


def fix_shell_typos(html: str) -> str:
    return html.replace("</div>", "</div>").replace("<div ", "<div ")


def build_index(depth: int = 0) -> str:
    p = prefix(depth)
    meta = extract_meta(BeautifulSoup((OLD / "index.html").read_text(encoding="utf-8"), "html.parser"))
    body = f"""
<section class="hero-carousel" aria-roledescription="carousel" aria-label="Featured">
<div class="hero-carousel__viewport" tabindex="0">
<button type="button" class="hero-carousel__control hero-carousel__control--prev" aria-label="Previous slide">
<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M15.41 7.41 14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
</button>
<div class="hero-carousel__slides" aria-live="polite">
<div class="hero-carousel__slide is-active" style="background-image:url('{p}imgs/619d6acb460a55abe34e53ee7bca0875.webp')" aria-hidden="false"></div>
<div class="hero-carousel__slide" style="background-image:url('{p}imgs/b0cbb92f967f94635c0a4f7780d577ef.webp')" aria-hidden="true"></div>
<div class="hero-carousel__slide" style="background-image:url('{p}imgs/97434a6affbb8dc935784c9b8dce431a.webp')" aria-hidden="true"></div>
</div>
<button type="button" class="hero-carousel__control hero-carousel__control--next" aria-label="Next slide">
<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M8.59 16.59 13.17 12 8.59 7.41 10 6l6 6-6 6z"/></svg>
</button>
</div>
<div class="hero-carousel__copy">
<p class="eyebrow">Fiber to the home</p>
<h1 class="visually-hidden">Sherie's Fibronet | Internet Service Provider | Home</h1>
<h2>BLAZING FAST INTERNET</h2>
<p class="lead">Sherie’s Fibronet provides “ Fiber to the home”(FTTH) that means faster downloads, less buffering, and an ultra-reliable internet connection for all the devices in your home or office . FTTH as a technology, enables the optical fiber to perform as a neutral-cum-independent network to carry multiple services to enhance &amp; ensure higher level of subscriber satisfaction. More than 1000’s of homes are already connected to our cutting edge fiber network. Enjoy faster service. Connect now.</p>
<p style="margin-top:1.5rem"><a class="btn btn--brand" href="{p}about/">MORE ABOUT US</a></p>
</div>
</section>
<section class="section bg-image-section" style="background-image:url('{p}imgs/c30fadc888d3e8a99843bec2153e2084.webp')">
<div class="container text-center">
<h2>INTERNET SERVICE PROVIDER</h2>
<p style="font-size:1.15rem;max-width:52rem;margin:0 auto">Sherie’s fibronet Internet is a leading Internet Service Provider. We specialize in providing ultra-fast, ultra-reliable High-Speed Broadband Internet to Residential, Small Business and Enterprises. We have the expertise needed to build and maintain carrier-grade networks to deliver the best services of any provider. Sherie’s fibronet Internet builds, maintains and controls 100% of our network, with absolutely zero reliance on "the telephone company" or any other third party providers.<br><br>Since our network is 100% fiber network run directly to your home, it’s the only one that delivers consistently fast speeds, 24/7, with no connection sharing and no slowdowns — whether you’re downloading or uploading.<br><br>Here at Sherie’s fibronet Internet, we are able to provide our customers with symmetrical internet speeds of up to 1 Gbps per second.</p>
</div>
</section>
<section class="section">
<div class="container split">
<div><img src="{p}imgs/benefits.webp" alt="BENEFITS | Bandwidth upto 1Gbps | Symmetrical connection | Secure transmission | Reliability" width="480" height="360" loading="lazy" decoding="async"></div>
<div>
<h2>BENEFITS</h2>
<ul class="benefits-list">
<li><strong>1. Bandwidth upto 1Gbps:</strong> Optical Fiber really have almost no limits how fast and how much information can be sent through it.</li>
<li><strong>2. Symmetrical connection:</strong> The term “symmetrical” means that the download and upload speeds are the same.</li>
<li><strong>3. Secure transmission:</strong> fiber-optic internet is touted as a cost effective way of instantly increasing your Internet security.</li>
<li><strong>4. Reliability:</strong> The fiber is amazingly reliable. Nothing hurts it except a physical cut.</li>
</ul>
</div>
</div>
</section>
<section class="section bg-image-section" style="background-image:url('{p}imgs/b6b2fe6b9814930b37241e7f380e195b.webp')">
<div class="container text-center">
<h2>For Complaints please call 7997006889</h2>
<p class="lead" style="margin:0 auto">From 8AM to 9PM</p>
</div>
</section>
<section class="section section--tight" id="contact">
<div class="container">
<h2 class="text-center">Get In Touch</h2>
<div class="contact-grid contact-grid--home" style="margin-top:2rem">
{contact_form_html()}
<ul class="contact-details panel">
<li><b>Address</b><div>#13, 9th Cross, New Bank Colony, Chunchgatta Main Road, Konanakunte, Bangalore - 560062</div></li>
<li><b>Phone</b><div>080 41488850</div></li>
<li><b>Email</b><a href="mailto:avinashds@yahoo.com">avinashds@yahoo.com</a></li>
</ul>
</div>
</div>
</section>
"""
    return fix_shell_typos(shell(meta, body, depth, "/"))


def build_404() -> str:
    meta = {"title": "Page Not Found | Sherie's Fibronet", "description": "404", "og_image": "imgs/logo-fibronet-2.webp"}
    body = """
<section class="error-page">
<h1>404</h1>
<h2>Page Not Found</h2>
<p><a class="btn" href="/">Return to homepage</a></p>
</section>
"""
    return fix_shell_typos(shell(meta, body, 0, "/404"))


def build_page(old_name: str, out_path: Path) -> None:
    if old_name == "index.html":
        html = build_index(0)
    elif old_name == "404.html":
        html = build_404()
    else:
        raw = (OLD / old_name).read_text(encoding="utf-8")
        soup = BeautifulSoup(raw, "html.parser")
        meta = extract_meta(soup)
        depth = depth_for(out_path)
        content = extract_main_html(soup)
        content = transform_content(content, depth)
        current = "/" + "/".join(out_path.relative_to(SITE).parts[:-1]) + "/"
        if current == "//":
            current = "/"
        wrapped = f'<div class="page-content"><div class="container">{content}</div></div>'
        wrapped = fix_shell_typos(wrapped)
        html = fix_shell_typos(shell(meta, wrapped, depth, current))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")


def copy_root_files() -> None:
    shutil.copy(OLD / "robots.txt", SITE / "robots.txt")
    sitemap = (OLD / "sitemap.xml").read_text(encoding="utf-8")
    sitemap = re.sub(
        r"https://www\.fibronet\.in/([^<]+)\.html",
        lambda m: f"https://www.fibronet.in/{m.group(1)}/" if m.group(1) != "index" else "https://www.fibronet.in/",
        sitemap,
    )
    sitemap = sitemap.replace("/about-us/", "/about/").replace("/contact-us/", "/contact/")
    (SITE / "sitemap.xml").write_text(sitemap, encoding="utf-8")


def copy_assets() -> None:
    """Sync imgs, CSS, JS, favicon from old / template paths."""
    src_imgs = OLD / "imgs"
    dst_imgs = SITE / "imgs"
    if dst_imgs.exists():
        shutil.rmtree(dst_imgs)
    shutil.copytree(src_imgs, dst_imgs)

    css_src = ROOT / "new" / "css" / "site.css"
    if not css_src.exists():
        css_src = SITE / "css" / "site.css"
    (SITE / "css").mkdir(parents=True, exist_ok=True)
    shutil.copy2(css_src, SITE / "css" / "site.css")

    for legacy in (SITE / "css").glob("main-*.css"):
        legacy.unlink()
    if (SITE / "css" / "internal-styles.css").exists():
        (SITE / "css" / "internal-styles.css").unlink()

    (SITE / "js").mkdir(parents=True, exist_ok=True)
    for legacy_js in (SITE / "js").glob("bundle-*.js"):
        legacy_js.unlink()

    favicon_dir = ROOT / "favicon"
    if favicon_dir.is_dir():
        for name in (
            "favicon-96x96.png",
            "favicon.svg",
            "favicon.ico",
            "apple-touch-icon.png",
            "web-app-manifest-192x192.png",
            "web-app-manifest-512x512.png",
        ):
            src = favicon_dir / name
            if src.exists():
                shutil.copy2(src, SITE / name)
        manifest_src = favicon_dir / "site.webmanifest"
        if manifest_src.exists():
            shutil.copy2(manifest_src, SITE / "site.webmanifest")
    elif (ROOT / "new" / "favicon.svg").exists():
        shutil.copy2(ROOT / "new" / "favicon.svg", SITE / "favicon.svg")

    js_main = SITE / "js" / "main.js"
    if not js_main.exists():
        template_js = ROOT / "new" / "js" / "main.js"
        if template_js.exists():
            shutil.copy2(template_js, js_main)


def main() -> None:
    copy_assets()
    for old_name, out_path in PAGE_OUT.items():
        print(f"Build {old_name} -> {out_path.relative_to(ROOT)}")
        build_page(old_name, out_path)
    copy_root_files()
    print("Done.")


if __name__ == "__main__":
    main()
