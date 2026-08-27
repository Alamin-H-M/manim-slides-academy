from common import page, pre, texplay, example, quiz, exercise, topic

T1 = topic(1, "ltx-what", "What LaTeX is (and the 60-second mental model)", """
LaTeX is not a text editor — it's a <b>language</b>: you type plain text with commands like
<code>\\frac{a}{b}</code>, and a program turns it into perfectly typeset output. Every command starts with
a backslash <code>\\</code>, arguments go in braces <code>{ }</code>. That's 90% of the mental model.""",
example("easy", "Your first formula — edit it!", """
<p>This playground renders as you type. Change the <code>2</code> to a <code>3</code>. Break it. Fix it.</p>
""" + texplay(r"E = mc^2", "^ makes a superscript (exponent). _ makes a subscript.")) +
example("easy", "Subscripts and superscripts", texplay(
    r"x_1^2 + x_2^2 = r^2",
    "Braces group things: try x_{10} vs x_10 to see why braces matter.")) +
example("hard", "Commands take arguments in braces", texplay(
    r"\frac{x+1}{x-1} \quad \sqrt{2} \quad \sqrt[3]{8}",
    r"\frac{top}{bottom} takes TWO arguments. \sqrt takes an optional [n] for nth roots.")) +
example("hard", "Nesting: commands inside commands", texplay(
    r"\frac{1}{1+\frac{1}{1+\frac{1}{x}}}",
    "Any argument can itself contain commands — that's how complex formulas are built.")))

T2 = topic(2, "ltx-symbols", "Greek letters & the symbols mathematicians actually use", """
Every Greek letter is a command: <code>\\alpha</code> → α. Capitalize the command for capitals:
<code>\\Delta</code> → Δ. You'll memorize the ~15 you use, and look up the rest.""",
example("easy", "The greatest hits", texplay(
    r"\alpha, \beta, \gamma, \Delta, \theta, \lambda, \pi, \sigma, \omega",
    "Try \\Omega, \\phi, \\varphi, \\epsilon, \\varepsilon.")) +
example("easy", "Comparison & arrows", texplay(
    r"a \le b \ne c \ge d \quad x \to \infty \quad p \Rightarrow q",
    r"\le ≤, \ge ≥, \ne ≠, \approx ≈, \to →, \Rightarrow ⇒, \infty ∞.")) +
example("hard", "Sets and logic", texplay(
    r"\forall x \in \mathbb{R}, \; \exists y \notin \mathbb{Q} : x \cdot y \in \mathbb{Z}",
    r"\mathbb{R} = blackboard bold. \in / \notin = set membership. \; adds a little space.")) +
example("hard", "Operators that size themselves", texplay(
    r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}\qquad \prod_{k=1}^{n} k = n!",
    r"On \sum and \prod, _ and ^ become the lower/upper limits automatically.")))

T3 = topic(3, "ltx-structure", "Fractions, roots, integrals, limits — building real formulas", """
Real formulas are just the pieces you've seen, combined. The skill is reading a formula
outside-in: find the outermost structure first, then fill the slots.""",
example("easy", "The quadratic formula, step by step", """
<p>Outer structure: a fraction. Top slot: <code>-b \\pm \\sqrt{...}</code>. Bottom slot: <code>2a</code>.</p>
""" + texplay(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", r"\pm gives the ± sign.")) +
example("easy", "A definite integral", texplay(
    r"\int_0^1 x^2 \, dx = \frac{1}{3}",
    r"\int works like \sum: _ lower limit, ^ upper limit. \, is a thin space before dx.")) +
example("hard", "Limits and derivatives", texplay(
    r"f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}",
    r"\lim_{...} puts its argument underneath in display mode.")) +
example("hard", "Putting it all together", texplay(
    r"\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt",
    "Read it outside-in: an integral, with limits, of a product of two powers.")))

T4 = topic(4, "ltx-brackets", "Brackets that grow & multi-line math", """
Plain parentheses stay small around tall content — ugly. <code>\\left(</code> and <code>\\right)</code>
grow to fit. For multi-line derivations, <code>aligned</code> lines up the <code>=</code> signs:
<code>&amp;</code> marks the alignment column, <code>\\\\</code> ends a line.""",
example("easy", "Small vs growing brackets", texplay(
    r"( \frac{1}{2} ) \quad \text{vs} \quad \left( \frac{1}{2} \right)",
    r"Every \left needs a matching \right. Use \left. or \right. for an invisible side.")) +
example("easy", "All the bracket families", texplay(
    r"\left[ \frac{a}{b} \right] \; \left\{ \frac{a}{b} \right\} \; \left| \frac{a}{b} \right|",
    r"Braces must be escaped: \{ \}. Try \left\langle ... \right\rangle too.")) +
example("hard", "A two-line derivation with aligned", texplay(
    "\\begin{aligned}\n(x+1)^2 &= x^2 + 2x + 1 \\\\\n        &= x(x+2) + 1\n\\end{aligned}",
    "& marks where lines align (before the =). \\\\ starts a new line.")) +
example("hard", "Cases (piecewise functions)", texplay(
    "|x| = \\begin{cases}\n x & \\text{if } x \\ge 0 \\\\\n -x & \\text{if } x < 0\n\\end{cases}",
    r"\text{...} switches to normal words inside math mode.")))

T5 = topic(5, "ltx-matrices", "Matrices & vectors", """
Matrices are grids: <code>&amp;</code> separates columns, <code>\\\\</code> separates rows.
The environment name picks the brackets: <code>pmatrix</code> ( ), <code>bmatrix</code> [ ],
<code>vmatrix</code> | |.""",
example("easy", "A 2×2 matrix", texplay(
    "A = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}",
    "Change pmatrix to bmatrix or vmatrix and watch the brackets change.")) +
example("easy", "Column vectors", texplay(
    "\\vec{v} = \\begin{pmatrix} x \\\\ y \\\\ z \\end{pmatrix}",
    r"\vec{v} draws the arrow. One column = no & needed, just \\\\ between rows.")) +
example("hard", "Matrix × vector", texplay(
    "\\begin{bmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{bmatrix}"
    "\\begin{bmatrix} x \\\\ y \\end{bmatrix}",
    "This is the 2D rotation matrix — you'll animate exactly this in the Manim chapter.")) +
example("hard", "A determinant with dots", texplay(
    "\\det(A) = \\begin{vmatrix} a_{11} & \\cdots & a_{1n} \\\\ \\vdots & \\ddots & \\vdots \\\\ a_{n1} & \\cdots & a_{nn} \\end{vmatrix}",
    r"\cdots horizontal, \vdots vertical, \ddots diagonal dots.")))

T6 = topic(6, "ltx-docs", "Complete documents (the part Manim does for you)", """
Everything so far was <em>math mode</em> — which is all Manim needs. But a standalone LaTeX
<em>document</em> wraps that math in a small skeleton. Learn the skeleton once, mostly so
error messages make sense.""",
example("easy", "The minimal document", """
<p>This is a full compilable <code>.tex</code> file (paste into any LaTeX editor — this one
isn't live because it's a document, not a formula):</p>
""" + pre(r"""\documentclass{article}
\begin{document}
Hello, \LaTeX!  Inline math: $E = mc^2$.
\end{document}""", "latex")) +
example("easy", "Inline vs display math", pre(r"""Euler proved that $e^{i\pi} + 1 = 0$   % inline: flows with text
\[ e^{i\pi} + 1 = 0 \]                  % display: own centered line""", "latex") +
"<p class='muted small'>Same formula, two contexts. In Manim you'll only ever write the math part.</p>") +
example("hard", "Sections, packages, labels", pre(r"""\documentclass{article}
\usepackage{amsmath}          % better math environments
\begin{document}
\section{The identity}
As shown in equation~\eqref{eq:euler}:
\begin{equation}\label{eq:euler}
  e^{i\pi} + 1 = 0
\end{equation}
\end{document}""", "latex")) +
example("hard", "How Manim uses this", pre(r'''# Manim writes the document FOR you. When you type:
MathTex(r"e^{i\pi} + 1 = 0")
# ...Manim generates a tiny document around your math,
# compiles it, and turns the result into animatable shapes.
# The r"" (raw string) stops Python from eating your backslashes!''') +
"<p class='muted small'>This is why the math-mode skills above transfer 1:1 to Manim.</p>"))

EXERCISES = """
<h2 id="ltx-ex">Self-examination</h2>
<p class="lead">No peeking at the topics above — that's the exam part. Solutions are one click away.</p>
""" + quiz("Which of these renders a fraction one-half?",
    [(r"\frac{1}{2}", True), (r"\fraction{1}{2}", False), (r"1 \over{2} \frac", False), (r"\div{1}{2}", False)],
    r"\frac takes two brace arguments: numerator, then denominator.") + \
quiz("What does the & symbol do inside an aligned or matrix environment?",
    [("Makes the next character bold", False), ("Marks the column/alignment point", True),
     ("Starts a comment", False), ("Inserts extra space", False)],
    "& separates columns (matrices) or marks where lines line up (aligned).") + \
quiz(r"Why must Python strings for Manim's MathTex be written as r\"...\"?",
    [("It renders faster", False), ("It makes the text red", False),
     (r"So Python doesn't treat backslashes as escapes (\t, \n...)", True), ("It's just tradition", False)],
    r"Without r, Python turns \theta into a tab + 'heta'.") + \
exercise(r"Write the LaTeX for: the sum from k = 0 to n of (n choose k) x^k = (1+x)^n. "
         r"(Binomial coefficient is \binom{n}{k}.) Try it in any playground above first!",
         pre(r"\sum_{k=0}^{n} \binom{n}{k} x^k = (1+x)^n", "latex")) + \
exercise("Typeset a 3×3 identity matrix with square brackets.",
         pre("I = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix}", "latex")) + \
exercise(r"Typeset the piecewise sign function: sgn(x) = -1 if x < 0, 0 if x = 0, 1 if x > 0.",
         pre("\\operatorname{sgn}(x) = \\begin{cases} -1 & x < 0 \\\\ 0 & x = 0 \\\\ 1 & x > 0 \\end{cases}", "latex"))

BODY = f"""
<h1>Chapter 1 · LaTeX</h1>
<p class="lead">Everything below is a <b>live playground</b> — edit the left side, the math re-renders
instantly. You cannot break anything; errors show in red and vanish when fixed.
Total time: about 2 hours, best split over 2–3 sittings.</p>
<div class="toc"><b>Topics</b>
<a href="#ltx-what">1 Mental model</a><a href="#ltx-symbols">2 Symbols</a>
<a href="#ltx-structure">3 Real formulas</a><a href="#ltx-brackets">4 Brackets &amp; multi-line</a>
<a href="#ltx-matrices">5 Matrices</a><a href="#ltx-docs">6 Documents</a>
<a href="#ltx-ex">✅ Self-exam</a></div>
{T1}{T2}{T3}{T4}{T5}{T6}{EXERCISES}
<div class="pager">
  <a href="setup.html"><span class="dir">← Previous</span>Setup</a>
  <a href="manim.html" class="right"><span class="dir">Next chapter →</span>2 · Manim</a>
</div>
"""

def render():
    return page("latex.html", "LaTeX", BODY, katex=True, desc='LaTeX tutorial for beginners with live editable examples: fractions, Greek letters, integrals, matrices, aligned equations and full documents — rendered instantly in your browser, works offline.')