#!/usr/bin/env python3
"""Build the Manim Slides Academy static site: python3 generator/build.py
Regenerates site/*.html from the page_*.py content modules. No dependencies."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import page_index, page_setup, page_latex, page_manim, page_slides, page_practice, page_reference  # noqa: E402

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")

PAGES = {
    "index.html": page_index.render,
    "setup.html": page_setup.render,
    "latex.html": page_latex.render,
    "manim.html": page_manim.render,
    "slides.html": page_slides.render,
    "practice.html": page_practice.render,
    "reference.html": page_reference.render,
}

for name, fn in PAGES.items():
    out = os.path.join(SITE, name)
    html = fn()
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{name}: {len(html) // 1024} KB")

# ---- assets: minify generator/src/site.{js,css} -> site/assets/ ------------
# Sources of truth live in generator/src/. If esbuild is available it minifies
# them (~45% smaller); otherwise the readable sources are copied verbatim so
# the build never breaks. Never edit site/assets/js|css directly.
import shutil, subprocess
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
esbuild = None
for cand in ("esbuild", "/tmp/esb/node_modules/.bin/esbuild"):
    if shutil.which(cand) or os.path.exists(cand):
        esbuild = cand
        break
for src_name, dst_rel, flags in (
        ("site.js",  os.path.join("assets", "js",  "site.js"),  ["--minify", "--target=es2017", "--legal-comments=none"]),
        ("site.css", os.path.join("assets", "css", "site.css"), ["--minify"])):
    src = os.path.join(SRC, src_name)
    dst = os.path.join(SITE, dst_rel)
    if not os.path.exists(src):
        continue
    if esbuild:
        subprocess.run([esbuild, src] + flags + ["--outfile=" + dst],
                       check=True, capture_output=True)
        print(f"{dst_rel}: minified ({os.path.getsize(dst) // 1024} KB)")
    else:
        shutil.copyfile(src, dst)
        print(f"{dst_rel}: copied unminified (install esbuild to minify)")
print("done.")
