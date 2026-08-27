# Contributing to Manim Slides Academy

Thanks for helping! This project is **AI-generated, human-maintained** — contributions of
any size are welcome, from a typo fix to a whole new chapter.

## Ground rules

1. **Every example must actually run.** If you add or change example code, render it and
   include the output (video for Manim, deck HTML for manim-slides).
2. **Keep it lightweight.** The whole site is ~2.5 MB. New videos: 854×480 @ 15 fps,
   re-encoded with x264 CRF 26 (see `build/` notes below), ideally < 50 KB each.
3. **Keep the teaching style.** One idea per topic; 2 easy examples, then 2 harder ones;
   plain language; no wall-of-text.
4. **No external network requests.** The site must stay 100% offline: no CDNs, no fonts
   from Google, no analytics.

## How the site is built

- `site/` — the deployable website (plain HTML/CSS/JS, committed).
- `build/` — Python generator: `common.py` (template + highlighter) and one
  `page_*.py` per page. Run `python3 build/build.py` to regenerate `site/*.html`.
- `examples/` — the Manim/manim-slides source for every animation on the site.

### Workflow for adding an example

```bash
# 1. add your Scene to examples/manim_examples.py
# 2. render it small:
cd examples
manim render -ql --fps 15 -r 854,480 --media_dir media manim_examples.py MyScene
# 3. compress + poster into the site (from repo root):
python3 build/encode_videos.py           # re-encodes media/videos/... into site/assets/video/
# 4. reference it in the right build/page_*.py via vid("MyScene", '''<code>''')
# 5. regenerate:
python3 build/build.py
```

### Workflow for adding a slide deck

```bash
cd examples
manim-slides render slides_examples.py MyDeck
manim-slides convert --to html --offline -ccontrols=true MyDeck /tmp/MyDeck.html
# merge its assets into site/assets/decks/shared_assets (content-hashed files never collide):
cp -n /tmp/MyDeck_assets/* ../site/assets/decks/shared_assets/
sed 's#MyDeck_assets/#shared_assets/#g' /tmp/MyDeck.html > ../site/assets/decks/MyDeck.html
```

## Submitting

- Small fixes: just open a PR.
- New topics/chapters: open an issue first so we can agree on scope.
- By contributing you agree your contribution is MIT-licensed like the rest.
