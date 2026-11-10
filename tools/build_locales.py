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

from i18n.web_sales import W  # noqa: E402
from i18n.web_legal import LEGAL  # noqa: E402

BASE = "https://watabook.devandrepair.com"

# Nav strings for the hand-written en/fr pages (used by /pro and /refund).
NAV_EN = dict(main_aria="Main navigation", home_aria="Watabook home", features="Features",
              privacy="Privacy", terms="Terms", support="Support", menu_aria="Toggle navigation",
              language="Language", back="Back to Watabook")
NAV_FR = dict(main_aria="Navigation principale", home_aria="Accueil Watabook", features="Fonctionnalités",
              privacy="Confidentialité", terms="Conditions", support="Assistance",
              menu_aria="Afficher la navigation", language="Langue", back="Retour à Watabook")
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
LEGACY_PAGES = ["index", "privacy", "terms", "support"]
SALES_PAGES = ["pro", "refund"]  # generated for every language, en and fr included
PAGES = LEGACY_PAGES + SALES_PAGES
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
  <link rel="icon" type="image/svg+xml" href="/assets/icon.svg">
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
    pro = path_of(code, "pro")
    pro_label = W[code]["nav_pro"]
    priv = path_of(code, "privacy")
    terms = path_of(code, "terms")

    def act(name):
        return ' class="active"' if active == name else ""

    return f"""  <nav class="nav" aria-label="{n['main_aria']}">
    <div class="container">
      <a class="wordmark" href="{home}" aria-label="{n['home_aria']}"><img class="mark" src="/assets/icon.svg" alt="" width="28" height="28">Watabook</a>
      <ul class="nav-links">
        <li><a href="{feat}">{n['features']}</a></li>
        <li><a href="{pro}"{act('pro')}>{pro_label}</a></li>
        <li><a href="{priv}"{act('privacy')}>{n['privacy']}</a></li>
        <li><a href="{terms}"{act('terms')}>{n['terms']}</a></li>
        {switcher_nav(code, page, n['language'])}
      </ul>
      <button class="mobile-toggle" id="mobileToggle" aria-label="{n['menu_aria']}" aria-expanded="false">
        {MENU_ICON}
      </button>
    </div>
    <div class="mobile-sheet" id="mobileSheet">
      <a href="{feat}">{n['features']}</a>
      <a href="{pro}">{pro_label}</a>
      <a href="{priv}">{n['privacy']}</a>
      <a href="{terms}">{n['terms']}</a>
      {switcher_mobile(code, page)}
    </div>
  </nav>
"""


def footer(L, page, scripts=("/js/script.js",)):
    code = L["code"]
    n = L["nav"]
    return f"""  <footer>
    <div class="container foot-row">
      <a class="wordmark" href="{path_of(code, 'index')}"><img class="mark" src="/assets/icon.svg" alt="" width="28" height="28">Watabook</a>
      <ul class="foot-links">
        <li><a href="{path_of(code, 'privacy')}">{n['privacy']}</a></li>
        <li><a href="{path_of(code, 'terms')}">{n['terms']}</a></li>
        <li><a href="{path_of(code, 'refund')}">{W[code]['nav_refunds']}</a></li>
        <li><a href="{path_of(code, 'support')}">{n['support']}</a></li>
      </ul>
      <span class="foot-copy">&copy; 2026 DevAndRepair.</span>
      {switcher_foot(code, page)}
    </div>
  </footer>

{"".join(f'  <script src="{src}"></script>{chr(10)}' for src in scripts)}</body>
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
          <span class="sec-num">0{k + 1}</span>
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
      <div class="sec-head"><span class="sec-num">01–04</span><span class="sec-label">{i['sec_features']}</span><span class="sec-rule"></span></div>
      <div class="feat-grid">
{feats}
      </div>
    </div>
  </section>

  <section class="pricing" id="pricing">
    <div class="container">
      <div class="sec-head"><span class="sec-num">05</span><span class="sec-label">{i['sec_pricing']}</span><span class="sec-rule"></span></div>
      <div class="price-grid">
        <div class="plan">
          <div class="plan-name">{i['free']['name']}</div>
          <div class="plan-price mono">{W[code]['home']['free_price']}</div>
          <div class="plan-sub">{i['free']['sub']}</div>
          <ul>
{free_items}
          </ul>
        </div>
        <div class="plan pro">
          <span class="badge">{i['pro']['badge']}</span>
          <div class="plan-name">{i['pro']['name']}</div>
          <div class="plan-price mono">{W[code]['home']['price']}<span>{W[code]['home']['per']}</span></div>
          <div class="plan-sub">{W[code]['home']['sub']}</div>
          <ul>
{pro_items}
          </ul>
          <a class="android-cta" href="{path_of(code, 'pro')}">{W[code]['home']['android_cta']} <span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
      <p class="price-note">{home_price_note(code, i['price_note'])}</p>
    </div>
  </section>

"""
    return h + body + footer(L, "index")


def render_legal(L, page):
    n = L["nav"]
    d = dict(L[page])
    if page in ("privacy", "terms"):
        lg = LEGAL[L["code"]][page]
        d["body"] = apply_privacy(d["body"], lg) if page == "privacy" else apply_terms(d["body"], lg)
        d["updated"] = lg["updated"]
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


# ---------------------------------------------------------------- web sales (Pro on the web)

def home_price_note(code, note):
    """Swap the first line of the price note (currency/store) for the USD one; keep the AI line."""
    rest = note.split("<br>", 1)[1] if "<br>" in note else ""
    first = W[code]["home"]["price_note_first"]
    return first + ("<br>" + rest if rest else "")


def _sections(body):
    """Split a legal body into (start, end) spans per <h2>."""
    starts = [m.start() for m in re.finditer(r"<h2[ >]", body)]
    return [(a, starts[k + 1] if k + 1 < len(starts) else len(body)) for k, a in enumerate(starts)]


def apply_privacy(body, lg):
    """Web-sales edits to a privacy body (same section order in every language)."""
    if 'id="web-purchase"' in body or 'id="achat-web"' in body:
        return body
    sec = _sections(body)
    # work from the end so earlier offsets stay valid
    # 4th section (children): replace its <p>
    a, b = sec[3]
    part = re.sub(r"<p>.*?</p>", lambda m: lg["children"], body[a:b], count=1, flags=re.S)
    body = body[:a] + part + body[b:]
    # 3rd section (control): replace its 3rd <li>
    sec = _sections(body)
    a, b = sec[2]
    lis = list(re.finditer(r"<li>.*?</li>", body[a:b], flags=re.S))
    li = lis[2]
    body = body[:a + li.start()] + lg["control_li"] + body[a + li.end():]
    # new section before the 3rd <h2>
    sec = _sections(body)
    a, _ = sec[2]
    body = body[:a] + lg["section"] + body[a:]
    # 2nd section (internet): insert after its 3rd <li>
    sec = _sections(body)
    a, b = sec[1]
    lis = list(re.finditer(r"<li>.*?</li>", body[a:b], flags=re.S))
    li = lis[2]
    body = body[:a + li.end()] + "\n          " + lg["license_li"] + body[a + li.end():]
    # 1st section (collect): replace its first <p>
    sec = _sections(body)
    a, b = sec[0]
    part = re.sub(r"<p>.*?</p>", lambda m: lg["collect"], body[a:b], count=1, flags=re.S)
    return body[:a] + part + body[b:]


def apply_terms(body, lg):
    """Replace section 4 (subscriptions) and its TOC entry."""
    if "PayPal" in body:
        return body
    sec = _sections(body)
    a, b = sec[3]
    body = body[:a] + lg["section4"] + body[b:]
    # 4th TOC entry text
    m = re.search(r'(<div class="toc">.*?</ol>)', body, re.S)
    if m:
        toc = m.group(1)
        items = list(re.finditer(r'(<li><a href="#[^"]*">)(.*?)(</a></li>)', toc))
        if len(items) >= 4:
            it = items[3]
            toc2 = toc[:it.start(2)] + lg["toc4"] + toc[it.end(2):]
            body = body[:m.start(1)] + toc2 + body[m.end(1):]
    return body


def nav_for(code):
    if code == "en":
        return NAV_EN
    if code == "fr":
        return NAV_FR
    return importlib.import_module(f"i18n.{code}").L["nav"]


def lang_ctx(code):
    """Minimal L-like dict so head()/nav()/footer() work for every language."""
    hl = next(h for c, h, _ in LANGS if c == code)
    return dict(code=code, htmllang=hl, dir="rtl" if code == "ar" else "ltr", nav=nav_for(code))


TICK = '<svg class="tick" viewBox="0 0 16 16" aria-label="{label}" role="img"><path d="M3 8.5l3 3 7-7"/></svg>'


def render_pro(code):
    import json
    L = lang_ctx(code)
    t = W[code]["pro"]
    refund = path_of(code, "refund")
    og = f"""  <meta property="og:title" content="{esc(t['og_title'])}">
  <meta property="og:description" content="{esc(t['og_desc'])}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url_of(code, 'pro')}">
  <meta property="og:image" content="{BASE}/assets/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">"""
    h = head(L, "pro", t["title"], t["description"], og) + "</head>\n<body>\n\n"
    tick = TICK.format(label=esc(t["included"]))
    dash = f'<span class="dash" aria-label="{esc(t["not_included"])}">&mdash;</span>'
    r = t["rows"]
    rows = [
        (r["vehicles"], '<td class="mono">1</td>', f'<td class="mono">{t["unlimited"]}</td>'),
        (r["entries"], f'<td class="mono">{t["unlimited"]}</td>', f'<td class="mono">{t["unlimited"]}</td>'),
        (r["dictionary"], f"<td>{tick}</td>", f"<td>{tick}</td>"),
        (r["lights"], '<td class="mono">36</td>', '<td class="mono">36</td>'),
        (r["reminders"], f"<td>{t['rem_free']}</td>", f"<td>{t['rem_pro']}</td>"),
        (r["ai"], f"<td>{dash}</td>", f"<td>{tick}</td>"),
        (r["vault"], f"<td>{dash}</td>", f"<td>{tick}</td>"),
        (r["pdf"], f"<td>{dash}</td>", f"<td>{tick}</td>"),
        (r["csv"], f"<td>{tick}</td>", f"<td>{tick}</td>"),
    ]
    rows_html = "\n".join(f'              <tr><th scope="row">{a}</th>{b}{c}</tr>' for a, b, c in rows)
    plate_rows = "\n".join(
        f'            <div><dt>{k}</dt><dd class="mono">{v}</dd></div>' for k, v in t["plate_rows"]
    )
    steps = "\n".join(
        f'            <li><span class="step-n mono">{k + 1}</span><span>{s_}</span></li>'
        for k, s_ in enumerate(t["steps"])
    )
    faq = "\n".join(
        f"          <div>\n            <h3>{f['q']}</h3>\n            <p>{f['a'].format(refund=refund)}</p>\n          </div>"
        for f in t["faq"]
    )
    strings = json.dumps(t["js"], ensure_ascii=False).replace("</", "<\\/")
    body = nav(L, "pro", active="pro")
    body += f"""
  <div class="test-banner" id="testBanner" hidden>
    <div class="container">{t['test_banner']}</div>
  </div>

  <main class="pro-page">

    <section class="pro-intro">
      <div class="container">
        <div class="pro-intro-text">
          <h1>{t['h1']}</h1>
          <p class="lead">{t['lead']}</p>
          <p class="ios-note">{t['ios_note']}</p>
        </div>

        <figure class="key-plate" aria-label="{esc(t['plate_aria'])}">
          <div class="key-plate-head">
            <span>Watabook Pro</span>
            <span class="mono">{t['plate_label']}</span>
          </div>
          <p class="key-plate-key mono" dir="ltr">WATA-<wbr>7K3QD-<wbr>XM2PA-<wbr>0N4RT-<wbr>9BZ1C</p>
          <dl class="key-plate-rows">
{plate_rows}
          </dl>
          <figcaption>{t['plate_caption']}</figcaption>
        </figure>
      </div>
    </section>

    <section class="pro-plans" id="plans" aria-labelledby="plansTitle">
      <div class="container">
        <h2 id="plansTitle" class="pro-h2">{t['plans_title']}</h2>

        <div class="plan-row" id="planRow">
          <article class="plan pro buy-plan" data-sku="watabook_pro_yearly" aria-labelledby="yearlyName">
            <span class="badge">{t['badge']}</span>
            <h3 class="plan-name" id="yearlyName">{t['yearly']}</h3>
            <p class="plan-price mono"><bdi dir="ltr">$7.99</bdi><span>{t['yearly_per']}</span></p>
            <p class="plan-sub">{t['yearly_sub']}</p>
            <div class="pay-slot" id="paySlotYearly" aria-live="polite">
              <p class="pay-loading">{t['loading']}</p>
            </div>
          </article>

          <article class="plan buy-plan" data-sku="watabook_pro_lifetime" aria-labelledby="lifetimeName">
            <h3 class="plan-name" id="lifetimeName">{t['lifetime']}</h3>
            <p class="plan-price mono"><bdi dir="ltr">$19.99</bdi><span>{t['lifetime_per']}</span></p>
            <p class="plan-sub">{t['lifetime_sub']}</p>
            <div class="pay-slot" id="paySlotLifetime" aria-live="polite">
              <p class="pay-loading">{t['loading']}</p>
            </div>
          </article>
        </div>

        <div class="key-result" id="keyResult" hidden tabindex="-1" aria-live="polite">
          <div class="key-result-status" id="keyStatus"></div>
          <div class="key-result-box" id="keyBox" hidden>
            <p class="key-result-key mono" id="keyValue" dir="ltr"></p>
            <button type="button" class="btn btn-secondary" id="copyKey">{t['copy']}</button>
          </div>
          <p class="key-result-mail" id="keyMail" hidden></p>
          <ol class="steps">
{steps}
          </ol>
        </div>

        <p class="plan-fine" id="planFine">{t['fine'].format(refund=refund)}</p>
      </div>
    </section>

    <section class="pro-compare" aria-labelledby="compareTitle">
      <div class="container">
        <h2 id="compareTitle" class="pro-h2">{t['compare_title']}</h2>
        <div class="spec-wrap">
          <table class="spec">
            <thead>
              <tr><th scope="col"><span class="sr">{t['th_feature']}</span></th><th scope="col">{t['th_free']}</th><th scope="col">{t['th_pro']}</th></tr>
            </thead>
            <tbody>
{rows_html}
            </tbody>
          </table>
        </div>
        <p class="plan-fine">{t['ai_note']}</p>
      </div>
    </section>

    <section class="pro-faq" aria-labelledby="faqTitle">
      <div class="container">
        <h2 id="faqTitle" class="pro-h2">{t['faq_title']}</h2>
        <div class="faq-grid">
{faq}
        </div>

        <form class="lost-key" id="lostKey" novalidate>
          <h3>{t['lost_title']}</h3>
          <p>{t['lost_text']}</p>
          <div class="lost-key-row">
            <label class="sr" for="lostEmail">{t['lost_label']}</label>
            <input id="lostEmail" name="email" type="email" autocomplete="email" placeholder="{esc(t['lost_placeholder'])}" dir="ltr" required>
            <button type="submit" class="btn btn-secondary">{t['lost_button']}</button>
          </div>
          <p class="lost-key-msg" id="lostMsg" aria-live="polite"></p>
        </form>
      </div>
    </section>

  </main>

  <script type="application/json" id="proStrings">{strings}</script>
"""
    return h + body + footer(L, "pro", scripts=("/js/script.js", "/js/pro.js"))


def render_refund(code):
    L = lang_ctx(code)
    t = W[code]["refund"]
    h = head(L, "refund", t["title"], t["description"]) + "</head>\n<body>\n\n"
    secs = "\n\n".join(
        f'        <h2 id="{sid}">{h2}</h2>\n        <p>{p}</p>' for sid, h2, p in t["sections"]
    )
    prevails = f'\n\n        <p class="translation-note"><em>{t["prevails"]}</em></p>' if t["prevails"] else ""
    body = nav(L, "refund")
    body += f"""
  <main class="legal-page">
    <div class="container">
      <a href="{path_of(code, 'pro')}" class="back-nav">{BACK_ARROW}{t['back']}</a>

      <div class="legal-header">
        <h1>{t['h1']}</h1>
        <div class="meta">
          <span>{t['effective']}</span>
          <span>{t['updated']}</span>
          <span>DevAndRepair</span>
        </div>
      </div>

      <div class="legal-body">
        <div class="note-box">
          <p>{t['note']}</p>
        </div>

{secs}{prevails}
      </div>
    </div>
  </main>

"""
    return h + body + footer(L, "refund")


NAV_PRICING_RE = re.compile(r'<a href="(/(?:fr/)?)#pricing">(?:Pricing|Tarifs)</a>|<a href="#pricing">(?:Pricing|Tarifs)</a>')


def patch_sales(code, page, s):
    """Pro link in the menu, Refunds in the footer, and (fr) the legal + price edits. Idempotent."""
    pro = path_of(code, "pro")
    s = NAV_PRICING_RE.sub(f'<a href="{pro}">{W[code]["nav_pro"]}</a>', s)
    if path_of(code, "refund") not in s.split("<footer>")[1]:
        s = re.sub(
            r'(<li><a href="[^"]*terms\.html">[^<]*</a></li>)(\s*<li><a href="[^"]*support\.html">)',
            lambda m: m.group(1) + f'\n        <li><a href="{path_of(code, "refund")}">{W[code]["nav_refunds"]}</a></li>' + m.group(2),
            s, count=1,
        )
    if code == "fr" and page in ("privacy", "terms"):
        lg = LEGAL["fr"][page]
        m = re.search(r'(<div class="legal-body">)(.*?)(\n      </div>\n    </div>\n  </main>)', s, re.S)
        inner = m.group(2)
        inner = apply_privacy(inner, lg) if page == "privacy" else apply_terms(inner, lg)
        s = s[:m.start(2)] + inner + s[m.end(2):]
        s = re.sub(r"Dernière mise à jour(?: |&nbsp;): [^<]*", "Dernière mise à jour&nbsp;: 10 novembre 2026", s, count=1)
    if page == "index":
        h = W[code]["home"]
        s = re.sub(r'(<div class="plan">\s*<div class="plan-name">[^<]*</div>\s*<div class="plan-price mono">)[^<]*(</div>)',
                   lambda m: m.group(1) + h["free_price"] + m.group(2), s, count=1)
    if page == "index" and 'class="android-cta"' not in s:
        h = W[code]["home"]
        s = re.sub(r'(<div class="plan pro">.*?<div class="plan-price mono">).*?(</div>\s*<div class="plan-sub">).*?(</div>)',
                   lambda m: m.group(1) + f'{h["price"]}<span>{h["per"]}</span>' + m.group(2) + h["sub"] + m.group(3), s, count=1, flags=re.S)
        s = re.sub(r'(<div class="plan pro">.*?</ul>)',
                   lambda m: m.group(1) + f'\n          <a class="android-cta" href="{pro}">{h["android_cta"]} <span aria-hidden="true">&rarr;</span></a>', s, count=1, flags=re.S)
        s = re.sub(r'(<p class="price-note">)(.*?)(</p>)', lambda m: m.group(1) + home_price_note(code, m.group(2)) + m.group(3), s, count=1, flags=re.S)
    return s


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


NAV_BLOCK = re.compile(r'(<ul class="nav-links">)(.*?)(</ul>\s*<button class="mobile-toggle")', re.S)
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
    s = patch_sales(code, page, s)
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
        for page in LEGACY_PAGES:
            html = render_index(L) if page == "index" else render_legal(L, page)
            open(os.path.join(ROOT, code, f"{page}.html"), "w", encoding="utf-8", newline="").write(html)
        print("generated", code)
    for code in ("en", "fr"):
        for page in LEGACY_PAGES:
            patch_existing(code, page)
        print("patched", code)
    for code, _, _ in LANGS:
        os.makedirs(os.path.join(ROOT, "" if code == "en" else code), exist_ok=True)
        for page, render in (("pro", render_pro), ("refund", render_refund)):
            dest = os.path.join(ROOT, "" if code == "en" else code, f"{page}.html")
            open(dest, "w", encoding="utf-8", newline="").write(render(code))
    print("pro + refund written for", ", ".join(c for c, _, _ in LANGS))
    write_sitemap()
    write_redirects()
    print("sitemap + redirects written")


if __name__ == "__main__":
    main()
