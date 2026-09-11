# watabook.devandrepair.com

Marketing site for [Watabook](https://github.com/Hassan-Boulhilt/watabook) —
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
fr/                     French versions of the above — the app's Wave-1 locale
css/style.css           Design tokens + all page styles
js/script.js            Mobile-nav toggle only — no scroll gimmicks
assets/                 Favicons, apple-touch-icon, OG/social image
                        (generated from store/icon/watabook-icon-1024.png
                        in the app repo)
```

Only `en` and `fr` exist so far, matching `store/screenshots.md`'s "Wave 1 =
fr/en" in the app repo. `ar`/`de`/`es`/`pt`/`it` are a natural fast-follow —
duplicate a locale folder, translate, add hreflang + sitemap entries.

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
