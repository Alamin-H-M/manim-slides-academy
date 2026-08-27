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
    opts = "".join(
        f'<label{" data-right" if right else ""}><input type="radio" name="q{abs(hash(question)) % 99999}">{esc(t)}</label>'
        for t, right in options)
    return (f'<div class="exercise"><div class="q">{question}</div>'
            f'<div class="quiz" data-why="{esc(why)}">{opts}<div class="verdict"></div></div></div>')


def exercise(question: str, answer_html: str) -> str:
    return (f'<div class="exercise"><div class="q">{question}</div>'
            f'<details class="answer"><summary>show solution</summary>'
            f'<div class="inner">{answer_html}</div></details></div>')


def topic(n: int, key: str, title: str, intro: str, body: str) -> str:
    return (f'<h2 id="{key}"><span class="tno">{n}</span>{title}'
            f'<label class="donebox"><input type="checkbox" data-key="{key}"> mark done</label></h2>'
            f'<p class="lead">{intro}</p>{body}')


def page(filename: str, title: str, body: str, katex: bool = False) -> str:
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    katex_head = ('<link rel="stylesheet" href="assets/katex/katex.min.css">'
                  '<script defer src="assets/katex/katex.min.js"></script>') if katex else ""
    return f"""<!DOCTYPE html>
<html lang="en" class="auto">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — Manim Slides Academy</title>
<meta name="description" content="A free, offline, open-source course: LaTeX, Manim and manim-slides from zero — with interactive examples.">
<link rel="stylesheet" href="assets/css/site.css">
{katex_head}
<script defer src="assets/js/site.js"></script>
</head>
<body>
<header class="site"><div class="inner">
  <a class="logo" href="index.html">Manim Slides <b>Academy</b></a>
  <nav class="main">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site">
  <p>Manim Slides Academy — open source (MIT), <b>AI-generated</b> content, human-reviewed examples that all actually render.<br>
  Works 100% offline · No trackers, no cookies, no network requests ·
  <a href="https://github.com/Alamin-H-M/manim-slides-academy">Contribute on GitHub</a></p>
</footer>
</body>
</html>"""
