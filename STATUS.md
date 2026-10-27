# STATUS

Online Privacy Basics — beginner manual + static HTML site.

## What was built

- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — project overview, credits Asdale Dynamics, LLC, usage instructions
- `docs/privacy-manual.md` — full beginner manual covering five topics:
  1. Passwords (password manager, unique passwords, long main password)
  2. Two-factor authentication (authenticator app preferred, backup codes)
  3. Data-broker opt-outs (Whitepages, Spokeo, MyLife, Intelius, BeenVerified)
  4. Private browsing (what it does and doesn't do)
  5. Phone & email hygiene (carrier PIN, secondary number, separate emails)
  Each section ends with an action checklist. Plain English, no fear-mongering,
  education only.
- `site/` — static HTML site:
  - `index.html` — home with topic cards and suggested order
  - `passwords.html`, `two-factor.html`, `data-brokers.html`,
    `private-browsing.html`, `phone-email.html` — one page per topic
  - `style.css` — shared responsive stylesheet
- `verify_site.py` — build/link checker script
- `STATUS.md` — this file

## How to run

Open any HTML file directly in a web browser (no server, no install, no internet):

```bash
# From this folder
open site/index.html        # macOS
xdg-open site/index.html    # Linux
start site/index.html       # Windows
```

Or read the manual: `docs/privacy-manual.md`.

## Verification results

Ran `python3 verify_site.py`:

```
All verification checks passed.
HTML files: 6
CSS: style.css
Docs: docs/privacy-manual.md
```

All 6 HTML files exist, parse, reference `style.css`, and all internal links
resolve. `LICENSE` contains the exact copyright line. `README.md` credits
Asdale Dynamics, LLC. `docs/privacy-manual.md` contains all five topic sections
with checklists.

No build step required — static files only.

## Known gaps

- No automated HTML linting (e.g., htmlhint) configured; verification is a
  custom Python script covering existence, link resolution, CSS reference, and
  section presence.
- The manual and site duplicate content; kept in sync by hand.
- No search, dark mode, or print stylesheet beyond basic screen styles.
- Opt-out instructions name specific brokers; site-specific steps may change
  over time and should be re-checked periodically.
- Education only — not legal or professional security advice.

## Credit

Built for and credited to Asdale Dynamics, LLC (Indiana, formed October 2026).
© 2026 Asdale Dynamics, LLC. MIT License.
