"""Shared template + tiny syntax highlighter for the Academy site generator.
Run build.py to regenerate site/*.html. No external dependencies.
"""
import html
import re

NAV = [
    ("index.html", "Home"),
    ("setup.html", "Setup"),
    ("latex.html", "1 · LaTeX"),
    ("manim.html", "2 · Manim"),
    ("slides.html", "3 · Slides"),
    ("practice.html", "🔁 Practice"),
    ("reference.html", "📖 Reference"),
]


def esc(s: str) -> str:
    return html.escape(s, quote=False)


# ---------------- tiny syntax highlighters (build-time, zero JS shipped) ----
_PY_KW = r"\b(def|class|import|from|return|for|while|if|elif|else|with|as|in|not|and|or|lambda|None|True|False|self|pass|try|except|raise|yield)\b"


def hl_python(code: str) -> str:
    out, i = [], 0
    token_re = re.compile(
        r"(#[^\n]*)|(\"\"\".*?\"\"\"|'''.*?'''|\"[^\"\n]*\"|'[^'\n]*'|r\"[^\"\n]*\"|r'[^'\n]*')"
        r"|(\b\d+\.?\d*\b)|" + _PY_KW, re.S)
    for m in token_re.finditer(code):
        out.append(esc(code[i:m.start()]))
        t = esc(m.group(0))
        if m.group(1):
            out.append(f'<span class="tok-c">{t}</span>')
        elif m.group(2):
            out.append(f'<span class="tok-s">{t}</span>')
        elif m.group(3):
            out.append(f'<span class="tok-n">{t}</span>')
        else:
            out.append(f'<span class="tok-k">{t}</span>')
        i = m.end()
    out.append(esc(code[i:]))
    s = "".join(out)
    # class names after 'class ' and calls to Capitalized names
    s = re.sub(r"(?<![\w>])([A-Z][A-Za-z0-9_]+)(?=\()", r'<span class="tok-cls">\1</span>', s)
    return s


def hl_latex(code: str) -> str:
    out, i = [], 0
    token_re = re.compile(r"(%[^\n]*)|(\\[a-zA-Z]+\*?)|([{}\[\]$&_^])")
    for m in token_re.finditer(code):
        out.append(esc(code[i:m.start()]))
        t = esc(m.group(0))
        if m.group(1):
            out.append(f'<span class="tok-c">{t}</span>')
        elif m.group(2):
            out.append(f'<span class="tok-cmd">{t}</span>')
        else:
            out.append(f'<span class="tok-brace">{t}</span>')
        i = m.end()
    out.append(esc(code[i:]))
    return "".join(out)


def hl_shell(code: str) -> str:
    out = []
    for line in code.split("\n"):
        e = esc(line)
        if line.strip().startswith("#"):
            out.append(f'<span class="tok-c">{e}</span>')
        else:
            e = re.sub(r"^(\s*)(\S+)", r'\1<span class="tok-f">\2</span>', e, count=1)
            out.append(e)
    return "\n".join(out)


def pre(code: str, lang: str = "python") -> str:
    code = code.strip("\n")
    body = {"python": hl_python, "latex": hl_latex, "shell": hl_shell,
            "text": esc}.get(lang, esc)(code)
    return f'<pre><code>{body}</code></pre>'


# ---------------- content building blocks ------------------------------
_play_n = 0


def texplay(latex: str, hint: str = "", display: bool = True) -> str:
    """Live KaTeX playground: textarea on the left, rendered output right."""
    global _play_n
    _play_n += 1
    mode = "" if display else ' data-display="inline"'
    hint_html = f'<p class="play-hint">💡 {hint}</p>' if hint else ""
    return (f'<div class="tex-play"{mode}>'
            f'<textarea spellcheck="false" aria-label="LaTeX input">{esc(latex)}</textarea>'
            f'<div class="tex-out"></div>{hint_html}</div>')


def example(level: str, title: str, body: str) -> str:
    cls = "easy" if level.startswith("e") else "hard"
    tag = "EASY" if cls == "easy" else "LEVEL UP"
    return (f'<div class="example"><div class="head">'
            f'<span class="lvl {cls}">{tag}</span><span class="t">{title}</span></div>'
            f'<div class="body">{body}</div></div>')


def vid(scene: str, code: str, note: str = "") -> str:
    """Video + code side by side. Click video to (re)play."""
    note_html = f'<p class="muted small">{note}</p>' if note else ""
    return (f'<div class="vid-split"><div>{pre(code)}</div>'
            f'<div><video muted playsinline controls preload="none" '
            f'data-src="assets/video/{scene}.mp4" '
            f'poster="assets/video/{scene}.jpg" '
            f'title="Click to play / replay"></video>'
            f'<p class="muted small" style="margin:6px 0 0">▶ click the video to play — click again to replay</p>'
            f'{note_html}</div></div>')


def deck(name: str, code: str, note: str = "") -> str:
    """manim-slides deck: code + click-to-load interactive Reveal.js iframe."""
    note_html = f'<p class="muted small">{note}</p>' if note else ""
    return (f'<div>{pre(code)}'
            f'<button class="deck-launch" data-deck="assets/decks/{name}.html" type="button">'
            f'<span class="big">🎬</span><span>Click to open the interactive deck '
            f'— then use <b>&nbsp;→&nbsp;</b> / click to advance</span></button>'
            f'{note_html}</div>')


def quiz(question: str, options, why: str) -> str:
    import hashlib
    digest = hashlib.md5(question.encode()).hexdigest()
    qkey = "qz-" + digest[:8]
    register_box(qkey, 5, "qz")
    # Deterministic shuffle so the right answer isn't always in the same slot
    # (but the build stays reproducible).
    options = sorted(options, key=lambda o: hashlib.md5((digest + o[0]).encode()).hexdigest())
    opts = "".join(
        f'<label{" data-right" if right else ""}><input type="radio" name="{qkey}">{esc(t)}</label>'
        for t, right in options)
    return (f'<div class="exercise" id="{qkey}"><div class="q">{question}</div>'
            f'<div class="quiz" data-key="{qkey}" data-why="{esc(why)}">{opts}<div class="verdict"></div></div></div>')


def exercise(question: str, answer_html: str) -> str:
    return (f'<div class="exercise"><div class="q">{question}</div>'
            f'<details class="answer"><summary>show solution</summary>'
            f'<div class="inner">{answer_html}</div></details></div>')


# Every checkable unit of the course registers here (during module import).
# page() then embeds the full list so any page can compute overall progress %.
TOPIC_REGISTRY = []  # list of (key, xp, kind, page)  kind: box | ch | qz
CURRENT_PAGE = ""    # set by each page module via set_page() before content
TOPIC_EXTRAS = {}    # topic key -> extra HTML appended to that topic's body
                     # (page modules fill this BEFORE defining their topics)


def set_page(filename: str) -> None:
    global CURRENT_PAGE
    CURRENT_PAGE = filename


def register_box(key: str, xp: int, kind: str = "box") -> None:
    if key not in [k for k, _, _, _ in TOPIC_REGISTRY]:
        TOPIC_REGISTRY.append((key, xp, kind, CURRENT_PAGE))


def topic(n: int, key: str, title: str, intro: str, body: str, xp: int = 15) -> str:
    register_box(key, xp)
    body = body + TOPIC_EXTRAS.get(key, "")
    return (f'<h2 id="{key}"><span class="tno">{n}</span>{title}</h2>'
            f'<p class="lead">{intro}</p>{body}'
            f'<div class="topic-end"><label class="donebox auto"><input type="checkbox" disabled data-key="{key}" data-xp="{xp}">'
            f' <span class="done-msg">Topic {n} completes automatically — read to the end and clear its exercises</span>'
            f' <span class="xp-tag">+{xp} XP</span></label></div>')


def page(filename: str, title: str, body: str, katex: bool = False, desc: str = "") -> str:
    desc = desc or ("Free offline course: learn LaTeX, Manim and manim-slides from zero "
                    "with live playgrounds, rendered animations and interactive slide decks.")
    esc_title = esc(title)
    import json as _json
    course_json = _json.dumps([{"k": k, "x": x, "t": t, "p": p} for k, x, t, p in TOPIC_REGISTRY],
                              separators=(",", ":"))
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    katex_head = ('<link rel="stylesheet" href="assets/katex/katex.min.css">'
                  '<script defer src="assets/katex/katex.min.js"></script>') if katex else ""
    return f"""<!DOCTYPE html>
<html lang="en" class="auto">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0d1117">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230d1117'/%3E%3Ccircle cx='16' cy='16' r='9' fill='none' stroke='%2360a5fa' stroke-width='2.5'/%3E%3Cpath d='M16 7v9l6.5 5' fill='none' stroke='%2334d399' stroke-width='2.5' stroke-linecap='round'/%3E%3C/svg%3E">
<meta name="google-site-verification" content="G9nUhiPGHB-PRAzOsDSdJxR47JKmGOSKM3EP1jkNtdk" />
<title>{esc(title)} — Manim Slides Academy</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://alamin-h-m.github.io/manim-slides-academy/site/{filename}">
<meta property="og:title" content="{esc_title} — Manim Slides Academy">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://alamin-h-m.github.io/manim-slides-academy/site/{filename}">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Course","name":"Manim Slides Academy","description":"Free offline course teaching LaTeX, Manim and manim-slides with interactive examples.","provider":{{"@type":"Organization","name":"Manim Slides Academy","sameAs":"https://github.com/Alamin-H-M/manim-slides-academy"}},"isAccessibleForFree":true,"inLanguage":"en","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}},"hasCourseInstance":{{"@type":"CourseInstance","courseMode":"online","courseWorkload":"PT13H"}}}}</script>
<link rel="stylesheet" href="assets/css/site.css">
{katex_head}
<script defer src="assets/js/site.js"></script>
</head>
<body>
<header class="site"><div class="inner">
  <a class="logo" href="index.html">Manim Slides <b>Academy</b></a>
  <nav class="main">{nav}</nav>
</div></header>
<div id="game-hud" hidden></div>
<noscript><div style="max-width:1060px;margin:8px auto;padding:8px 20px;color:#fbbf24;font-size:.85rem">
JavaScript is off — the course text still works, but playgrounds, challenges, XP and progress tracking need it.</div></noscript>
<script>window.MSA_COURSE={course_json};</script>
<main>
{body}
</main>
<footer class="site">
  <p>Manim Slides Academy — open source (MIT), <b>AI-generated</b> content, human-reviewed examples that all actually render.<br>
  Works 100% offline · <a href="https://github.com/Alamin-H-M/manim-slides-academy/releases/latest/download/manim-slides-academy-offline.zip">Download the site as a ZIP</a> · No trackers, no cookies ·
  <a href="https://github.com/Alamin-H-M/manim-slides-academy">Contribute on GitHub</a></p>
</footer>
</body>
</html>"""


def challenge(key: str, prompt: str, target: str, hint: str = "") -> str:
    """'Write this in LaTeX' game: shows rendered math, user types LaTeX,
    live-checks whether their rendering matches the goal exactly."""
    register_box(key, 10, "ch")
    return (f'<div class="tex-challenge" id="{key}" data-key="{key}" data-target="{esc(target)}" data-hint="{esc(hint)}">'
            f'<div class="ch-q">🎯 {prompt}</div>'
            f'<div class="target">{esc(target)}</div>'
            f'<div class="attempt">'
            f'<textarea spellcheck="false" placeholder="type your LaTeX here…" aria-label="LaTeX attempt"></textarea>'
            f'<div class="yours"></div></div>'
            f'<div class="ch-status"></div>'
            f'<div class="ch-btns"><button type="button" class="ch-hint">hint</button>'
            f'<button type="button" class="ch-reveal">give up — show solution</button></div>'
            f'</div>')


def pychallenge(key: str, prompt: str, goal: str, musts, solution: str, hint: str = "") -> str:
    """'Your turn to write' game for Python/CLI code: shows the goal in words,
    user types code, live checklist shows which requirements pass (regexes are
    tested against the whitespace-stripped input)."""
    import json as _json
    register_box(key, 10, "ch")
    aesc = lambda t: html.escape(t, quote=True)
    musts_json = aesc(_json.dumps(musts, separators=(",", ":")))
    return (f'<div class="tex-challenge py-challenge" id="{key}" data-key="{key}" '
            f'data-musts="{musts_json}" data-solution="{aesc(solution)}" data-hint="{aesc(hint)}">'
            f'<div class="ch-q">🎯 {prompt}</div>'
            f'<div class="target goal-text">{goal}</div>'
            f'<div class="attempt">'
            f'<textarea class="code" spellcheck="false" placeholder="write your code here…" aria-label="code attempt"></textarea>'
            f'<div class="ck-list"></div></div>'
            f'<div class="ch-status"></div>'
            f'<div class="ch-btns"><button type="button" class="ch-hint">hint</button>'
            f'<button type="button" class="ch-reveal">give up — show solution</button></div>'
            f'</div>')


def pretest(qas) -> str:
    """Pre-test box: try to answer BEFORE learning (boosts retention even when wrong)."""
    items = "".join(
        f'<details class="answer" style="margin:6px 0"><summary>{esc(q)}</summary>'
        f'<div class="inner muted">{a}</div></details>' for q, a in qas)
    return ('<div class="note"><b>🧠 Before you start (30 seconds)</b>'
            "Try to answer these from intuition — being wrong is fine, guessing first "
            "is proven to make the real answers stick better:" + items + "</div>")
