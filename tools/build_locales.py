#!/usr/bin/env python3
"""
Builds the ar / de / es / pt / it pages (home, privacy, terms, support) from
tools/i18n/<code>.py, patches the hand-written en/fr pages with the shared
language switcher + hreflang block, and regenerates sitemap.xml and the
locale lines of _redirects.

Run from the repo root:  python tools/build_locales.py
Idempotent: generated blocks in en/fr are wrapped in <!--lang-*--> markers and
replaced in place on every run.
"""
import importlib
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))

BASE = "https://watabook.devandrepair.com"
# code, hreflang/html lang, endonym
LANGS = [
    ("en", "en", "English"),
    ("fr", "fr", "Français"),
    ("ar", "ar", "العربية"),
    ("de", "de", "Deutsch"),
    ("es", "es", "Español"),
    ("pt", "pt-PT", "Português"),
    ("it", "it", "Italiano"),
]
GENERATED = ["ar", "de", "es", "pt", "it"]
PAGES = ["index", "privacy", "terms", "support"]
# Strings the en/fr patcher needs (their pages are hand-written, not generated).
PATCH_LABELS = {"en": "Language", "fr": "Langue"}

GLOBE = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/>'
    '<path d="M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>'
)
BACK_ARROW = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round"><path d="M19 12H5M11 18l-6-6 6-6"/></svg>'
)
MENU_ICON = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
    'stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>'
)
APPLE = (
    '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.53 4.08zM12.03 7.25c-.15-2.23 1.66-4.09 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/></svg>'
)
PLAY = (
    '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3.6 2.18c-.35.2-.6.58-.6 1.03v17.58c0 .45.25.83.6 1.03l9.7-9.82L3.6 2.18zM15.4 12l2.37-2.4 3.53 2.02c.6.35.6 1.2 0 1.55l-3.53 2.02L15.4 12zM4.7 2l9 5.15L15.9 5 5.6 1.1c-.32-.12-.66-.02-.9.2v.05v.65zM4.7 22l9-5.15L15.9 19l-10.3 3.9c-.32.12-.66.02-.9-.2v-.05v-.65z"/></svg>'
)
APP_STORE_URL = "https://apps.apple.com/us/app/watabook-car-log-fault-code/id6812091402"
PLAY_URL = "https://play.google.com/store/apps/details?id=com.devandrepair.watabook"
# Play listing language per site locale (Apple localises by storefront, not URL).
PLAY_HL = {"en": "en", "fr": "fr", "ar": "ar", "de": "de", "es": "es", "pt": "pt-PT", "it": "it"}


def play_url(code):
    return f"{PLAY_URL}&hl={PLAY_HL[code]}"


DOWNLOAD_ICON = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M12 4v11"/><path d="m7 10 5 5 5-5"/><path d="M5 20h14"/></svg>'
)


def download_btn(code, href, label):
    """Nav "Download" button: js/script.js sends phones straight to their
    store; everyone else lands on the hero's store badges (#download)."""
    return (
        f'<a class="btn btn-primary js-download" href="{href}" '
        f'data-ios="{APP_STORE_URL}" data-android="{esc_attr(play_url(code))}">'
        f'{DOWNLOAD_ICON}<span>{label}</span></a>'
    )


def esc_attr(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")


# Device frame around the hero mock: status bar + dynamic island on top,
# icon-only tab bar + home indicator below. Purely decorative.
PHONE_TOP = (
    '<span class="phone-keys" aria-hidden="true"></span>\n'
    '          <div class="screen">\n'
    '            <div class="status-bar" aria-hidden="true"><span class="sb-time">9:41</span>'
    '<span class="island"></span><span class="sb-icons">'
    '<svg viewBox="0 0 18 12" fill="currentColor"><rect x="0" y="8" width="3" height="4" rx="1"/>'
    '<rect x="5" y="5.5" width="3" height="6.5" rx="1"/><rect x="10" y="3" width="3" height="9" rx="1"/>'
    '<rect x="15" y="0" width="3" height="12" rx="1"/></svg>'
    '<svg viewBox="0 0 16 12" fill="currentColor"><path d="M8 2.6c2.3 0 4.4.9 6 2.4l1.3-1.4A10.4 10.4 0 0 0 8 .7 10.4 10.4 0 0 0 .7 3.6L2 5c1.6-1.5 3.7-2.4 6-2.4Zm0 3.6c1.3 0 2.5.5 3.4 1.3l1.3-1.4A6.7 6.7 0 0 0 8 4.3a6.7 6.7 0 0 0-4.7 1.8l1.3 1.4C5.5 6.7 6.7 6.2 8 6.2Zm0 3.5a1.7 1.7 0 0 0-1.2.5L8 11.6l1.2-1.4a1.7 1.7 0 0 0-1.2-.5Z"/></svg>'
    '<svg class="sb-battery" viewBox="0 0 27 13" fill="none"><rect x=".5" y=".5" width="23" height="12" rx="3.5" stroke="currentColor" opacity=".4"/>'
    '<rect x="2" y="2" width="17" height="9" rx="2" fill="currentColor"/>'
    '<path d="M25 4.5v4c.8-.3 1.5-1.1 1.5-2s-.7-1.7-1.5-2Z" fill="currentColor" opacity=".45"/></svg>'
    '</span></div>'
)
PHONE_BOTTOM = (
    '            <div class="screen-foot" aria-hidden="true">\n'
    '              <div class="tabs">'
    '<span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/></svg></span>'
    '<span class="on"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 2 20h20L12 3Z"/><path d="M12 10v4"/><path d="M12 17h.01"/></svg></span>'
    '<span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></span>'
    '<span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 17h14v-5l-2-5H7l-2 5v5Z"/><path d="M5 12h14"/><circle cx="8" cy="17" r="1.6"/><circle cx="16" cy="17" r="1.6"/></svg></span>'
    '</div>\n'
    '              <span class="home-indicator"></span>\n'
    '            </div>\n'
)
FEAT_ICONS = [
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 2 20h20L12 3Z"/><path d="M12 10v4"/><path d="M12 17h.01"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M17 21H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7l5 5v11a2 2 0 0 1-2 2Z"/><path d="M9 13h6"/><path d="M9 17h6"/></svg>',
]


def path_of(code, page):
    base = "/" if code == "en" else f"/{code}/"
    return base if page == "index" else f"{base}{page}.html"


def url_of(code, page):
    return BASE + path_of(code, page)


def hreflang_block(page):
    out = []
    for code, hl, _ in LANGS:
        out.append(f'  <link rel="alternate" hreflang="{hl}" href="{url_of(code, page)}">')
    out.append(f'  <link rel="alternate" hreflang="x-default" href="{url_of("en", page)}">')
    return "\n".join(out)


def switcher_nav(cur, page, label):
    cur_name = next(n for c, _, n in LANGS if c == cur)
    items = []
    for code, hl, name in LANGS:
        aria = ' aria-current="true"' if code == cur else ""
        items.append(
            f'<li><a href="{path_of(code, page)}" hreflang="{hl}" lang="{hl}"{aria}>{name}</a></li>'
        )
    return (
        '<!--lang-nav--><li class="lang-switch"><details>'
        f'<summary aria-label="{label}">{GLOBE}{cur_name}</summary>'
        f'<ul>{"".join(items)}</ul></details></li><!--/lang-nav-->'
    )


def switcher_mobile(cur, page):
    links = []
    for code, hl, name in LANGS:
        aria = ' aria-current="true"' if code == cur else ""
        links.append(f'<a href="{path_of(code, page)}" hreflang="{hl}" lang="{hl}"{aria}>{name}</a>')
    return f'<!--lang-mobile--><div class="lang-row">{"".join(links)}</div><!--/lang-mobile-->'


def switcher_foot(cur, page):
    links = []
    for code, hl, name in LANGS:
        aria = ' aria-current="true"' if code == cur else ""
        links.append(f'<a href="{path_of(code, page)}" hreflang="{hl}" lang="{hl}"{aria}>{name}</a>')
    return f'<!--lang-foot--><div class="foot-langs">{"".join(links)}</div><!--/lang-foot-->'


# ---------------------------------------------------------------- generated pages

FONTS_LATIN = (
    "https://fonts.googleapis.com/css2?family=Spectral:wght@400;500;600"
    "&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500;600&display=swap"
)
FONTS_AR = (
    "https://fonts.googleapis.com/css2?family=Spectral:wght@400;500;600"
    "&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Sans+Arabic:wght@400;500;600"
    "&family=IBM+Plex+Mono:wght@500;600&display=swap"
)


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")


def head(L, page, title, description, extra=""):
    code = L["code"]
    fonts = FONTS_AR if L["dir"] == "rtl" else FONTS_LATIN
    return f"""<!DOCTYPE html>
<html lang="{L['htmllang']}" dir="{L['dir']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">

  <title>{title}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{url_of(code, page)}">
{hreflang_block(page)}
{extra}
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
  <link rel="apple-touch-icon" href="/assets/favicon-180.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{fonts}" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
"""


def nav(L, page, active=None, home_anchor=True):
    code = L["code"]
    n = L["nav"]
    home = path_of(code, "index")
    feat = ("" if page == "index" else home) + "#features"
    pric = ("" if page == "index" else home) + "#pricing"
    dl = ("" if page == "index" else home) + "#download"
    priv = path_of(code, "privacy")
    terms = path_of(code, "terms")

    def act(name):
        return ' class="active"' if active == name else ""

    return f"""  <nav class="nav" aria-label="{n['main_aria']}">
    <div class="container">
      <a class="wordmark" href="{home}" aria-label="{n['home_aria']}"><span class="mark">W</span>Watabook</a>
      <ul class="nav-links">
        <li><a href="{feat}">{n['features']}</a></li>
        <li><a href="{pric}">{n['pricing']}</a></li>
        <li><a href="{priv}"{act('privacy')}>{n['privacy']}</a></li>
        <li><a href="{terms}"{act('terms')}>{n['terms']}</a></li>
        {switcher_nav(code, page, n['language'])}
      </ul>
      <div class="nav-right">{download_btn(code, dl, n['download'])}</div>
      <button class="mobile-toggle" id="mobileToggle" aria-label="{n['menu_aria']}" aria-expanded="false">
        {MENU_ICON}
      </button>
    </div>
    <div class="mobile-sheet" id="mobileSheet">
      <a href="{feat}">{n['features']}</a>
      <a href="{pric}">{n['pricing']}</a>
      <a href="{priv}">{n['privacy']}</a>
      <a href="{terms}">{n['terms']}</a>
      {switcher_mobile(code, page)}
      {download_btn(code, dl, n['download'])}
    </div>
  </nav>
"""


def footer(L, page):
    code = L["code"]
    n = L["nav"]
    return f"""  <footer>
    <div class="container foot-row">
      <a class="wordmark" href="{path_of(code, 'index')}"><span class="mark">W</span>Watabook</a>
      <ul class="foot-links">
        <li><a href="{path_of(code, 'privacy')}">{n['privacy']}</a></li>
        <li><a href="{path_of(code, 'terms')}">{n['terms']}</a></li>
        <li><a href="{path_of(code, 'support')}">{n['support']}</a></li>
      </ul>
      <span class="foot-copy">&copy; 2026 DevAndRepair.</span>
      {switcher_foot(code, page)}
    </div>
  </footer>

  <script src="/js/script.js"></script>
</body>
</html>
"""


def render_index(L):
    code = L["code"]
    n = L["nav"]
    i = L["index"]
    ph = i["phone"]
    og = f"""
  <meta name="keywords" content="{esc(i['keywords'])}">
  <meta name="author" content="DevAndRepair">

  <meta property="og:type" content="website">
  <meta property="og:url" content="{url_of(code, 'index')}">
  <meta property="og:title" content="{esc(i['og_title'])}">
  <meta property="og:description" content="{esc(i['og_desc'])}">
  <meta property="og:image" content="{BASE}/assets/og-image.jpg">
  <meta property="og:site_name" content="Watabook">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(i['og_title'])}">
  <meta name="twitter:description" content="{esc(i['tw_desc'])}">
  <meta name="twitter:image" content="{BASE}/assets/og-image.jpg">
"""
    ld = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "MobileApplication",
    "name": "Watabook",
    "operatingSystem": "iOS, Android",
    "installUrl": ["{APP_STORE_URL}", "{play_url(code)}"],
    "applicationCategory": "UtilitiesApplication",
    "inLanguage": "{L['htmllang']}",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "EUR"
    }},
    "description": "{i['ld_desc'].replace('"', '&quot;')}"
  }}
  </script>
"""
    h = head(L, "index", i["title"], i["description"], og) + ld + "</head>\n<body>\n\n"
    body = nav(L, "index")
    feats = "\n".join(
        f"""        <div class="feat">
          <div class="feat-icon">{FEAT_ICONS[k]}</div>
          <span class="sec-num">§ 0{k + 1}</span>
          <h3>{t}</h3>
          <p>{p}</p>
        </div>"""
        for k, (t, p) in enumerate(i["feats"])
    )
    free_items = "\n".join(f"            <li>{x}</li>" for x in i["free"]["items"])
    pro_items = "\n".join(f"            <li>{x}</li>" for x in i["pro"]["items"])
    body += f"""
  <section class="hero" id="download">
    <div class="container">
      <div>
        <p class="kicker">{i['kicker']}</p>
        <h1>{i['h1']}</h1>
        <p class="lead">{i['lead']}</p>
        <div class="store-row">
          <a class="store-btn" href="{APP_STORE_URL}" target="_blank" rel="noopener" aria-label="{esc(i['dl_on'])} App Store">
            {APPLE}
            <span><span class="l1">{i['dl_on']}</span><span class="l2">App Store</span></span>
          </a>
          <a class="store-btn" href="{esc_attr(play_url(code))}" target="_blank" rel="noopener" aria-label="{esc(i['get_on'])} Google Play">
            {PLAY}
            <span><span class="l1">{i['get_on']}</span><span class="l2">Google Play</span></span>
          </a>
        </div>
        <p class="free-note">{i['free_note']}</p>
      </div>
      <div class="phone-stage">
        <div class="phone">
          {PHONE_TOP}
            <div class="screen-bar"><span class="chip-code">P0301</span></div>
            <div class="screen-title">{ph['title']}</div>
            <p class="screen-body">{ph['body']}</p>
            <div class="meter"><div class="seg"></div><div class="seg on"></div><div class="seg"></div></div>
            <div class="meter-label"><span>{ph['safe']}</span><b>{ph['gentle']}</b><span>{ph['stop']}</span></div>
            <div class="row-card">
              <div class="row-title">{ph['row1']}</div>
              <div class="row-sub mono">{ph['row1_sub']}</div>
            </div>
            <div class="row-card">
              <div class="row-title">{ph['row2']}</div>
              <div class="row-sub mono">{ph['row2_sub']}</div>
            </div>
{PHONE_BOTTOM}          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="features" id="features">
    <div class="container">
      <div class="sec-head"><span class="sec-num">§ 01–04</span><span class="sec-label">{i['sec_features']}</span><span class="sec-rule"></span></div>
      <div class="feat-grid">
{feats}
      </div>
    </div>
  </section>

  <section class="pricing" id="pricing">
    <div class="container">
      <div class="sec-head"><span class="sec-num">§ 05</span><span class="sec-label">{i['sec_pricing']}</span><span class="sec-rule"></span></div>
      <div class="price-grid">
        <div class="plan">
          <div class="plan-name">{i['free']['name']}</div>
          <div class="plan-price mono">{i['free'].get('price', '&euro;0')}</div>
          <div class="plan-sub">{i['free']['sub']}</div>
          <ul>
{free_items}
          </ul>
        </div>
        <div class="plan pro">
          <span class="badge">{i['pro']['badge']}</span>
          <div class="plan-name">{i['pro']['name']}</div>
          <div class="plan-price mono">{i['pro'].get('price', '&euro;1.99')}<span>{i['pro']['per_month']}</span></div>
          <div class="plan-sub">{i['pro']['sub']}</div>
          <ul>
{pro_items}
          </ul>
        </div>
      </div>
      <p class="price-note">{i['price_note']}</p>
    </div>
  </section>

"""
    return h + body + footer(L, "index")


def render_legal(L, page):
    n = L["nav"]
    d = L[page]
    if page == "privacy":
        meta = f"<span>{d['updated']}</span>\n          <span>DevAndRepair</span>"
    elif page == "terms":
        meta = (
            f"<span>{d['effective']}</span>\n          <span>{d['updated']}</span>\n"
            "          <span>DevAndRepair</span>"
        )
    else:
        meta = f"<span>{d['reply']}</span>"
    h = head(L, page, d["title"], d["description"]) + "</head>\n<body>\n\n"
    body = nav(L, page, active=page if page in ("privacy", "terms") else None)
    body += f"""
  <main class="legal-page">
    <div class="container">
      <a href="{path_of(L['code'], 'index')}" class="back-nav">{BACK_ARROW}{n['back']}</a>

      <div class="legal-header">
        <h1>{d['h1']}</h1>
        <div class="meta">
          {meta}
        </div>
      </div>

      <div class="legal-body">
{d['body']}
      </div>
    </div>
  </main>

"""
    return h + body + footer(L, page)


# ---------------------------------------------------------------- patch en / fr

def _patch_block(s, block_re, tag, new, old_link_re, place):
    """Replace/insert one generated block inside one region of the page."""
    m = block_re.search(s)
    if not m:
        raise SystemExit(f"region for {tag} not found")
    head_, inner, tail = m.groups()
    inner = re.sub(rf"[ \t]*\n?[ \t]*<!--{tag}-->.*?<!--/{tag}-->", "", inner, flags=re.S)
    inner = re.sub(old_link_re, "", inner)
    return s[: m.start()] + head_ + place(inner, new) + tail + s[m.end():]


NAV_BLOCK = re.compile(r'(<ul class="nav-links">)(.*?)(</ul>\s*<div class="nav-right")', re.S)
MOB_BLOCK = re.compile(r'(<div class="mobile-sheet" id="mobileSheet">)(.*?)(</div>\s*</nav>)', re.S)
FOOT_BLOCK = re.compile(r"(<footer>)(.*?)(</footer>)", re.S)
OLD_LI = r'\s*<li><a href="[^"]*">(?:Français|English)</a></li>'
OLD_A = r'[ \t]*<a href="[^"]*">(?:Français|English)</a>\n?'


def _place_nav(inner, new):
    return inner.rstrip() + "\n        " + new + "\n      "


def _place_mobile(inner, new):
    idx = inner.find('<a class="btn')
    if idx == -1:
        return inner.rstrip() + "\n      " + new + "\n    "
    return inner[:idx] + new + "\n      " + inner[idx:]


def _place_foot(inner, new):
    m = re.search(r'<span class="foot-copy">.*?</span>', inner, re.S)
    return inner[: m.end()] + "\n      " + new + inner[m.end():]


def patch_existing(code, page):
    path = os.path.join(ROOT, ("" if code == "en" else code), f"{page}.html")
    s = open(path, encoding="utf-8", newline="").read().replace("\r\n", "\n")

    # hreflang: drop every alternate line, re-insert the full set where the first was.
    lines = s.split("\n")
    existing = [k for k, l in enumerate(lines) if 'rel="alternate" hreflang=' in l]
    if existing:
        first = existing[0]
    else:  # e.g. the support pages never had any: anchor after the canonical
        first = next(k for k, l in enumerate(lines) if 'rel="canonical"' in l) + 1
    kept = [l for l in lines if 'rel="alternate" hreflang=' not in l]
    kept.insert(first - len([k for k in existing if k < first]), hreflang_block(page))
    s = "\n".join(kept)

    s = _patch_block(s, NAV_BLOCK, "lang-nav", switcher_nav(code, page, PATCH_LABELS[code]), OLD_LI, _place_nav)
    s = _patch_block(s, MOB_BLOCK, "lang-mobile", switcher_mobile(code, page), OLD_A, _place_mobile)
    s = _patch_block(s, FOOT_BLOCK, "lang-foot", switcher_foot(code, page), OLD_LI, _place_foot)
    open(path, "w", encoding="utf-8", newline="").write(s)
    open(path, "w", encoding="utf-8", newline="").write(s)


# ---------------------------------------------------------------- sitemap / redirects

def write_sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for page in PAGES:
        for code, _, _ in LANGS:
            out.append("  <url>")
            out.append(f"    <loc>{url_of(code, page)}</loc>")
            for c2, hl, _ in LANGS:
                out.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{url_of(c2, page)}"/>')
            out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url_of("en", page)}"/>')
            out.append("  </url>")
    out.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="").write("\n".join(out) + "\n")


def write_redirects():
    lines = [
        "# Cloudflare Pages redirects.",
        "# Collapse /index.html to the clean directory form (matches <link rel=\"canonical\">)",
        "/index.html        /       301",
    ]
    for code, _, _ in LANGS:
        if code != "en":
            lines.append(f"/{code}/index.html".ljust(19) + f" /{code}/".ljust(7) + " 301")
    open(os.path.join(ROOT, "_redirects"), "w", encoding="utf-8", newline="").write("\n".join(lines) + "\n")


def main():
    only = [c for c in sys.argv[1:] if c in GENERATED] or GENERATED
    for code in only:
        L = importlib.import_module(f"i18n.{code}").L
        assert L["code"] == code
        os.makedirs(os.path.join(ROOT, code), exist_ok=True)
        for page in PAGES:
            html = render_index(L) if page == "index" else render_legal(L, page)
            open(os.path.join(ROOT, code, f"{page}.html"), "w", encoding="utf-8", newline="").write(html)
        print("generated", code)
    for code in ("en", "fr"):
        for page in PAGES:
            patch_existing(code, page)
        print("patched", code)
    write_sitemap()
    write_redirects()
    print("sitemap + redirects written")


if __name__ == "__main__":
    main()
