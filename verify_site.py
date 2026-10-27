#!/usr/bin/env python3
"""Verify the static privacy site builds correctly.

Checks:
- All HTML files exist and parse
- All internal links resolve to existing files
- CSS file is referenced and exists
- No placeholder URLs or secrets present
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"

HTML_FILES = [
    "index.html",
    "passwords.html",
    "two-factor.html",
    "data-brokers.html",
    "private-browsing.html",
    "phone-email.html",
]

CSS_FILE = "style.css"
DOCS_FILE = "docs/privacy-manual.md"


def fail(msg):
    print(f"FAIL: {msg}")
    return False


def main():
    errors = 0

    # Site directory exists
    if not SITE.is_dir():
        print(f"FAIL: site directory missing: {SITE}")
        return 1

    # CSS exists and is referenced
    css_path = SITE / CSS_FILE
    if not css_path.is_file():
        errors += 1
        print(f"FAIL: missing CSS file: {css_path}")

    # Docs manual exists
    docs_path = ROOT / DOCS_FILE
    if not docs_path.is_file():
        errors += 1
        print(f"FAIL: missing docs file: {docs_path}")

    # Every HTML file exists, parses, references CSS, and links resolve
    for name in HTML_FILES:
        path = SITE / name
        if not path.is_file():
            errors += 1
            print(f"FAIL: missing HTML file: {path}")
            continue

        text = path.read_text(encoding="utf-8")

        # CSS reference
        if CSS_FILE not in text:
            errors += 1
            print(f"FAIL: {name} does not reference {CSS_FILE}")

        # Basic well-formedness
        if "<html" not in text or "</html>" not in text:
            errors += 1
            print(f"FAIL: {name} missing html tags")

        # Internal href links resolve
        hrefs = re.findall(r'href="([^"]+)"', text)
        for href in hrefs:
            if href.startswith("#") or href.startswith("http://") or href.startswith("https://") or href.startswith("mailto:"):
                continue
            target = (SITE / href).resolve()
            if not target.exists():
                target = (ROOT / href).resolve()
            if not target.exists():
                errors += 1
                print(f"FAIL: {name} links to missing file: {href}")

        # No obvious placeholder/secrets
        for bad in ["API_KEY", "SECRET", "password=", "example.com/api"]:
            if bad.lower() in text.lower():
                errors += 1
                print(f"FAIL: {name} contains suspicious token: {bad}")

    # Check links from docs manual to site files (manual references site CSS? no)
    if docs_path.is_file():
        dtext = docs_path.read_text(encoding="utf-8")
        for required in ["Passwords", "Two-factor", "Data-broker", "Private browsing", "Phone and email", "checklist"]:
            if required.lower() not in dtext.lower():
                errors += 1
                print(f"FAIL: docs manual missing section: {required}")

    # LICENSE present with exact copyright line
    license_path = ROOT / "LICENSE"
    if not license_path.is_file():
        errors += 1
        print("FAIL: missing LICENSE")
    else:
        lic = license_path.read_text(encoding="utf-8")
        if "Copyright (c) 2026 Asdale Dynamics, LLC" not in lic:
            errors += 1
            print("FAIL: LICENSE missing exact copyright line")

    # README present and credits Asdale Dynamics
    readme_path = ROOT / "README.md"
    if not readme_path.is_file():
        errors += 1
        print("FAIL: missing README.md")
    else:
        readme = readme_path.read_text(encoding="utf-8")
        if "Asdale Dynamics" not in readme:
            errors += 1
            print("FAIL: README does not credit Asdale Dynamics, LLC")

    if errors:
        print(f"\n{errors} verification error(s)")
        return 1

    print("All verification checks passed.")
    print(f"HTML files: {len(HTML_FILES)}")
    print(f"CSS: {CSS_FILE}")
    print(f"Docs: {DOCS_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
