# watabook.devandrepair.com

Marketing site for [Watabook](https://github.com/Hassan-Boulhilt/watabook_site) —
the offline car-maintenance logbook & fault-code app. Vanilla HTML5 / CSS3 /
JS, deployed as a static site to Cloudflare Pages (same pattern as the other
`*.devandrepair.com` sites — no build step, no framework).

## Design system

Visual identity matches the app's own signed-off **"Service Manual"** system
(`DESIGN.md` in the app repo) exactly — same tokens, not a reinterpretation:
paper ground `#E7E9E5`, blueprint-blue accent `#1F4B75`, Spectral serif
headings, IBM Plex Sans body, IBM Plex Mono for every number/code/price. See
`css/style.css` for the full token set.

A sign-off mockup of the home page lives in `design-canvas/` (a Claude Design
canvas — see `Main.dc.html` + `canvas.json`; the large seeded/published
`.html` is git-ignored and regenerable from those two files).

## Structure

```
index.html            Home (en) — hero, features, pricing
privacy.html           Privacy policy (en)
terms.html             Terms of service (en)
support.html           Support / FAQ (en)
fr/                     French versions of the above (hand-written)
ar/ de/ es/ pt/ it/     Generated — do not edit by hand (see "Languages")
css/style.css           Design tokens + all page styles (logical properties, so RTL works)
js/script.js            Mobile-nav toggle + language dropdown — no scroll gimmicks
tools/                  build_locales.py + i18n/<code>.py (the translations)
assets/                 Favicons, apple-touch-icon, OG/social image
                        (generated from store/icon/watabook-icon-1024.png
                        in the app repo)
```

## Languages

All 7 app locales are covered: en and fr (hand-written pages), and ar, de, es,
pt (pt-PT) and it (generated). Edit a translation in `tools/i18n/<code>.py`, then:

```bash
python tools/build_locales.py        # all five generated languages
python tools/build_locales.py de     # or just one
```

That rewrites `<code>/*.html`, re-applies the shared language switcher and the
`hreflang` block to the hand-written en/fr pages, and regenerates
`sitemap.xml` and the locale lines of `_redirects`. It is idempotent. Arabic
renders right-to-left (`dir="rtl"`, IBM Plex Sans Arabic).

The privacy/terms/support translations are AI drafts of the English originals
and carry an "English prevails" note — have a native / legal reader review
them before relying on them. To change wording in en/fr, edit those pages
directly; to add a section everywhere, edit all seven.

## Local preview

```bash
npx wrangler pages dev . --port 8788
```

## Deploy

Not yet connected. To ship it:

1. Create a GitHub repo (e.g. `Hassan-Boulhilt/watabook.devandrepair.com`,
   matching the sibling sites' naming) and push this folder to it.
2. In the Cloudflare dashboard, create a Pages project connected to that repo
   — framework preset "None", build command empty, output directory `/`.
3. Add a custom domain `watabook.devandrepair.com` to the Pages project (it
   walks you through the DNS record; `devandrepair.com` is already on
   Cloudflare, so this is usually just a CNAME).
4. Update `store/privacy-policy.md` and `store/app-privacy.md` in the app repo
   to point at the live privacy-policy URL for App Store Connect / Play
   Console.
