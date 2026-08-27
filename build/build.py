#!/usr/bin/env python3
"""Build the Manim Slides Academy static site: python3 build/build.py
Regenerates site/*.html from the page_*.py content modules. No dependencies."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import page_index, page_setup, page_latex, page_manim, page_slides  # noqa: E402

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")

PAGES = {
    "index.html": page_index.render,
    "setup.html": page_setup.render,
    "latex.html": page_latex.render,
    "manim.html": page_manim.render,
    "slides.html": page_slides.render,
}

for name, fn in PAGES.items():
    out = os.path.join(SITE, name)
    html = fn()
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{name}: {len(html) // 1024} KB")
print("done.")
