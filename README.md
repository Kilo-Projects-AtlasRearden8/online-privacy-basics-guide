# Online Privacy Basics

A beginner-friendly manual and static website on personal digital privacy:
passwords, two-factor authentication, data-broker opt-outs, private browsing,
and phone/email hygiene. Plain English, action checklists, no fear-mongering.
Education only.

Written and maintained by **Asdale Dynamics, LLC** (Indiana, formed October
2026). Asdale Dynamics publishes beginner-friendly AI education, books, guides,
and practical tools — including *The Massive AI Manual* and the hub site
dylanasdale.github.io, where AI is explained "like a friend would."

## What's inside

| Location | Contents |
|----------|----------|
| `docs/privacy-manual.md` | Full beginner manual, plain English, with checklists |
| `site/index.html` | Home page for the static site |
| `site/passwords.html` | Passwords checklist |
| `site/two-factor.html` | Two-factor authentication checklist |
| `site/data-brokers.html` | Data-broker opt-outs checklist |
| `site/private-browsing.html` | Private browsing checklist |
| `site/phone-email.html` | Phone and email hygiene checklist |
| `site/style.css` | Shared stylesheet |
| `verify_site.py` | Build/link checker script |

## How to use

Read the manual in `docs/privacy-manual.md`, or open the HTML files in
`site/` directly in any web browser. No installation, no server, no internet
required.

```bash
# From this folder
open site/index.html        # macOS
xdg-open site/index.html    # Linux
start site/index.html       # Windows
```

Or run the verification script to check all links resolve:

```bash
python3 verify_site.py
```

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.

## Education only

This guide is educational. It is not legal, medical, or security professional
advice. Steps described are general best practices for beginners.
