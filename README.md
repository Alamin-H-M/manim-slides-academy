# Manim Slides Academy

**A free, 100% offline documentation website that teaches LaTeX, Manim and manim-slides from zero** — with live LaTeX playgrounds, real rendered animations beside their exact source code, and click-through interactive slide decks.

> 🤖 **Honesty first: this project is AI-generated.**
> The course content, examples, website and build system were produced by an AI assistant
> (at a user's request), then published as open source. Every code example was actually
> executed and every animation on the site is the real render of the code shown next to it —
> but review it with the same healthy skepticism you'd apply to any community resource.
> Found an error? Please [open an issue](https://github.com/Alamin-H-M/manim-slides-academy/issues) or a pull request!

## ✨ What's inside

| Chapter | Topics | Interactive format |
|---|---|---|
| **Setup** | The most efficient offline toolchain: Python, Manim, manim-slides, LaTeX, VS Code | Copy-paste checklists |
| **1 · LaTeX** | Mental model · symbols · real formulas · brackets & multi-line · matrices · documents | **Live KaTeX playgrounds** — edit the math, it re-renders instantly |
| **2 · Manim** | Scenes & Mobjects · animations · positioning · styling · updaters · graphs & MathTex | **24 real rendered videos** next to their exact source |
| **3 · manim-slides** | Scene→Slide · render/present/export · slide craft patterns | **4 embedded interactive decks** you click through |

Each topic follows the same low-brain-drain recipe: **2 easy examples → 2 progressively harder ones → self-exam** (instant-feedback quizzes + open exercises with hidden solutions).

## 🚀 Use it

No install, no server, no internet:

1. Download / clone this repository.
2. Open `site/index.html` in any browser. Done.

(Optionally serve it — `python -m http.server -d site` — but `file://` works fully.)

## ⚡ Fast & lightweight by design

- **~2.5 MB total** including all 24 videos, 4 slide decks and the complete KaTeX math engine
- Zero frameworks, zero trackers, zero network requests — plain HTML/CSS + one 6 KB script
- Videos lazy-load (only when scrolled near) and decks load only when clicked
- Reveal.js is shared across all four decks instead of being bundled four times

## 🛠 Rebuilding the site

The HTML is generated from Python content modules (no dependencies):

```bash
python3 build/build.py          # regenerates site/*.html
```

To re-render the example animations (needs `manim` + `manim-slides`):

```bash
cd examples
manim render -ql --fps 15 -r 854,480 --media_dir media manim_examples.py <SceneName>
manim-slides render slides_examples.py <SlideName>
manim-slides convert --to html --offline <SlideName> ../site/assets/decks/<SlideName>.html
```

## 🤝 Contributing

Anyone can contribute — see [CONTRIBUTING.md](CONTRIBUTING.md). Good first contributions:

- Fix typos / clarify explanations
- Add translations
- Add a new example (please include the rendered video and keep it < 50 KB)
- Add new topics (3D scenes, camera movement, manim-voiceover…)

## 🧩 Companion tool

This course's one-keystroke workflow (▶ → live preview on every save) is powered by the
**[Manim Slides Preview](https://github.com/Alamin-H-M/manim-slides-preview)** VS Code extension — offline installable, zero dependencies,
with browser / VS Code tab / native GUI preview targets and background .pptx export.

## 📄 License

[MIT](LICENSE) — use it, teach with it, fork it, sell courses based on it, whatever helps people learn.
