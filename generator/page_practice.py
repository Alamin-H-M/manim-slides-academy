from common import page

# ---------------------------------------------------------------------------
# Card deck: retrieval practice across ALL THREE domains, interleaved.
# type: "latex" -> front is rendered math (KaTeX), answer is the source
#       "qa"    -> plain question/answer (answer may contain <code>/<pre>)
# ---------------------------------------------------------------------------
CARDS = [
    # ---- LaTeX ----
    {"d": "LaTeX", "t": "latex", "f": r"\frac{a}{b}", "q": "Write the LaTeX for this:", "a": r"\frac{a}{b}"},
    {"d": "LaTeX", "t": "latex", "f": r"x_1^2", "q": "Write the LaTeX for this:", "a": r"x_1^2"},
    {"d": "LaTeX", "t": "latex", "f": r"\sqrt[3]{8}", "q": "Write the LaTeX for this:", "a": r"\sqrt[3]{8}"},
    {"d": "LaTeX", "t": "latex", "f": r"\sum_{n=1}^{\infty} \frac{1}{n^2}", "q": "Write the LaTeX for this:", "a": r"\sum_{n=1}^{\infty} \frac{1}{n^2}"},
    {"d": "LaTeX", "t": "latex", "f": r"\int_0^1 x^2 \, dx", "q": "Write the LaTeX for this:", "a": r"\int_0^1 x^2 \, dx"},
    {"d": "LaTeX", "t": "latex", "f": r"\lim_{h \to 0} \frac{f(x+h)-f(x)}{h}", "q": "Write the LaTeX for this:", "a": r"\lim_{h \to 0} \frac{f(x+h)-f(x)}{h}"},
    {"d": "LaTeX", "t": "latex", "f": r"\forall x \in \mathbb{R}", "q": "Write the LaTeX for this:", "a": r"\forall x \in \mathbb{R}"},
    {"d": "LaTeX", "t": "latex", "f": r"\left( \frac{1}{2} \right)", "q": "Write the LaTeX for this (brackets must grow):", "a": r"\left( \frac{1}{2} \right)"},
    {"d": "LaTeX", "t": "qa", "q": "What symbol separates COLUMNS in a matrix or aligns lines in <code>aligned</code>?", "a": "<code>&amp;</code> — and <code>\\\\</code> ends a row/line."},
    {"d": "LaTeX", "t": "qa", "q": "Which matrix environment gives square brackets [ ]?", "a": "<code>bmatrix</code> (p = parentheses, v = vertical bars)."},
    {"d": "LaTeX", "t": "qa", "q": "How do you write normal words inside math mode?", "a": "<code>\\text{...}</code> — e.g. <code>\\text{if } x &gt; 0</code>."},
    {"d": "LaTeX", "t": "qa", "q": "Greek: which commands give α, Δ, λ, π?", "a": "<code>\\alpha</code>, <code>\\Delta</code> (capitalized command = capital letter), <code>\\lambda</code>, <code>\\pi</code>."},
    {"d": "LaTeX", "t": "qa", "q": "≤, ≥, ≠, ≈, → in LaTeX?", "a": "<code>\\le \\ge \\ne \\approx \\to</code>"},
    {"d": "LaTeX", "t": "qa", "q": "What does a piecewise function use?", "a": "<code>\\begin{cases} x &amp; x \\ge 0 \\\\ -x &amp; x &lt; 0 \\end{cases}</code>"},

    # ---- Manim ----
    {"d": "Manim", "t": "qa", "q": "What are the TWO core concepts of Manim, and what does each mean?", "a": "<b>Scene</b> = canvas + timeline (subclass it, override <code>construct()</code>). <b>Mobject</b> = anything drawable (Circle, Text, MathTex…)."},
    {"d": "Manim", "t": "qa", "q": "Why is a default <code>Circle()</code> just an outline?", "a": "<code>fill_opacity</code> defaults to 0 — pass <code>fill_opacity=1</code> to see the fill."},
    {"d": "Manim", "t": "qa", "q": "Difference: <code>sq.shift(UP)</code> vs <code>sq.animate.shift(UP)</code> inside <code>play()</code>?", "a": "Plain call = instant teleport (before rendering). <code>.animate</code> = smooth animation of the change."},
    {"d": "Manim", "t": "qa", "q": "How do you run two animations at the SAME time?", "a": "Pass both to one play: <code>self.play(FadeIn(a), Create(b))</code>."},
    {"d": "Manim", "t": "qa", "q": "Which animation is the classic for revealing text?", "a": "<code>Write(text)</code> — draws it like handwriting. <code>FadeIn</code> works too."},
    {"d": "Manim", "t": "qa", "q": "Position a label under a square — which method?", "a": "<code>label.next_to(square, DOWN)</code> — relative positioning."},
    {"d": "Manim", "t": "qa", "q": "How do you make a mobject FOLLOW another for the whole scene?", "a": "An updater: <code>always_redraw(lambda: Line(a.get_center(), b.get_center()))</code> or <code>mob.add_updater(...)</code> — runs every frame."},
    {"d": "Manim", "t": "qa", "q": "What does <code>ValueTracker</code> do?", "a": "Holds a number you can animate: <code>self.play(t.animate.set_value(100))</code>; updaters read it with <code>t.get_value()</code> every frame."},
    {"d": "Manim", "t": "qa", "q": "Recite the recipe for plotting sin(x).", "a": "<pre>axes = Axes(x_range=[-4,4], y_range=[-2,2])\ncurve = axes.plot(lambda x: np.sin(x))\nself.play(Create(axes), Create(curve))</pre>"},
    {"d": "Manim", "t": "qa", "q": "Why must MathTex strings start with <code>r</code>?", "a": "Raw string: stops Python eating backslashes — <code>\"\\theta\"</code> would become TAB + 'heta'."},
    {"d": "Manim", "t": "qa", "q": "Stagger 10 animations one after another with overlap — which wrapper?", "a": "<code>LaggedStart(*anims, lag_ratio=0.1)</code>"},
    {"d": "Manim", "t": "qa", "q": "Which rate_func plays an animation forward then in reverse?", "a": "<code>rate_func=there_and_back</code> — great for pulses."},
    {"d": "Manim", "t": "qa", "q": "Render command for fast 480p preview of scene Hello in first.py?", "a": "<code>manim render -ql -p first.py Hello</code>"},
    {"d": "Manim", "t": "qa", "q": "What does <code>VGroup</code> give you?", "a": "Treat many mobjects as one: <code>.arrange(RIGHT)</code>, <code>.scale()</code>, animate the whole group."},

    # ---- manim-slides ----
    {"d": "Slides", "t": "qa", "q": "Turn a Manim Scene into a presentation — what TWO changes?", "a": "1) <code>class X(Slide)</code> (from manim_slides) instead of Scene. 2) call <code>self.next_slide()</code> at every pause point."},
    {"d": "Slides", "t": "qa", "q": "What exactly does <code>self.next_slide()</code> mark?", "a": "A pause boundary: everything between two calls plays as one segment, then waits for the presenter."},
    {"d": "Slides", "t": "qa", "q": "Make a title slide loop its animation until you advance?", "a": "<code>self.next_slide(loop=True)</code> before the looping play()."},
    {"d": "Slides", "t": "qa", "q": "The three present/export targets and when to use each?", "a": "<b>Native GUI</b> (<code>manim-slides present</code>) in person · <b>HTML</b> (<code>convert --to html --offline</code>) to share · <b>pptx</b> (<code>--to pptx</code>) for PowerPoint venues."},
    {"d": "Slides", "t": "qa", "q": "Why is <code>--offline</code> essential for talks?", "a": "It bundles Reveal.js locally — without it the HTML fetches from a CDN and shows a BLANK page without internet."},
    {"d": "Slides", "t": "qa", "q": "Wipe everything between sections — the one-liner?", "a": "<code>self.play(*[FadeOut(m) for m in self.mobjects])</code>"},
    {"d": "Slides", "t": "qa", "q": "Render + convert commands for deck.py, scene Talk, offline HTML?", "a": "<pre>manim-slides render deck.py Talk\nmanim-slides convert --to html --offline Talk out.html</pre>"},
    {"d": "Slides", "t": "qa", "q": "Presenter hotkeys in the native GUI?", "a": "<kbd>→</kbd>/<kbd>Space</kbd> next · <kbd>←</kbd> prev · <kbd>F</kbd> fullscreen · <kbd>R</kbd> replay · <kbd>Q</kbd> quit."},
    # ---- new advanced-topic cards ----
    {"d": "LaTeX", "t": "latex", "f": r"\vec{v} \cdot \hat{n}", "q": "Write the LaTeX for this:", "a": r"\vec{v} \cdot \hat{n}"},
    {"d": "LaTeX", "t": "latex", "f": r"\underbrace{a + b}_{\text{sum}}", "q": "Write the LaTeX for this:", "a": r"\underbrace{a + b}_{\text{sum}}"},
    {"d": "LaTeX", "t": "latex", "f": r"\frac{\partial f}{\partial x}", "q": "Write the LaTeX for this:", "a": r"\frac{\partial f}{\partial x}"},
    {"d": "LaTeX", "t": "latex", "f": r"\oint_C \vec{F} \cdot d\vec{r}", "q": "Write the LaTeX for this:", "a": r"\oint_C \vec{F} \cdot d\vec{r}"},
    {"d": "LaTeX", "t": "qa", "q": "Thin space vs wide space in math mode?", "a": "<code>\\,</code> is thin (before dx), <code>\\quad</code> is wide, <code>\\qquad</code> double. <code>\\!</code> is negative."},
    {"d": "Manim", "t": "qa", "q": "Morph <code>a²+b²=c²</code> into <code>c²=a²+b²</code> with terms flying to their new spots. Which animation?", "a": "<code>TransformMatchingTex(eq1, eq2)</code> — split each MathTex into per-term string arguments first."},
    {"d": "Manim", "t": "qa", "q": "Make 12 dots appear one-after-another with overlap. Which wrapper?", "a": "<code>LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.15)</code>"},
    {"d": "Manim", "t": "qa", "q": "Which Scene subclass lets you zoom & pan the viewport, and what do you animate?", "a": "<code>MovingCameraScene</code>; animate <code>self.camera.frame</code> (scale = zoom, move_to = pan, save_state/Restore to return)."},
    {"d": "Manim", "t": "qa", "q": "In a ThreeDScene, what do phi and theta control?", "a": "<code>phi</code> = tilt down from vertical, <code>theta</code> = spin around the z-axis: <code>self.set_camera_orientation(phi=70*DEGREES, theta=-45*DEGREES)</code>"},
    {"d": "Manim", "t": "qa", "q": "Render ONLY the last animation of a long scene while polishing it?", "a": "<code>manim render -ql -n -1 scene.py MyScene</code>"},
    {"d": "Slides", "t": "qa", "q": "Keep a header visible across wipe() transitions. What's the feature called?", "a": "The <b>canvas</b>: <code>self.add_to_canvas(header=header)</code>, then wipe <code>self.mobjects_without_canvas</code>."},
    {"d": "Slides", "t": "qa", "q": "Export one self-contained HTML file that works with zero installs?", "a": "<code>manim-slides convert --to html --offline --one-file MyTalk talk.html</code>"},
    {"d": "Slides", "t": "qa", "q": "You edited the .py and converted, but the .pptx shows old animations. Why?", "a": "convert packages the <b>last render</b> — re-render first (the ▶ button in the VS Code extension does both)."},
]

import json


def render():
    deck = json.dumps(CARDS, ensure_ascii=False)
    body = """
<h1>🔁 Practice — spaced repetition</h1>
<p class="lead">This is the part most courses skip, and it's the most effective thing on this site.
Two findings dominate learning research: <b>testing yourself beats re-reading</b> (retrieval practice)
and <b>short sessions spread over days beat one long session</b> (spacing). This page does both for you:
49 cards across all three chapters, interleaved, scheduled with a Leitner system that hides
what you know and repeats what you miss. All progress stays in your browser.</p>

<div class="note"><b>How to use it</b>
Come here for <b>5 minutes a day</b> after (or during) the chapters. Read the card, answer
<em>out loud or on paper first</em>, then flip. Be honest with the buttons — "Again" is not failure,
it's scheduling. Cards you know keep moving to longer intervals: 1 → 3 → 7 → 21 days.</div>

<div id="deck-stats" class="toc" style="display:flex;gap:24px;flex-wrap:wrap"></div>

<div id="flash-area"></div>

<div class="tip"><b>Why interleaved?</b> Cards from LaTeX, Manim and manim-slides are shuffled
together on purpose. Mixing related-but-different material feels harder — and measurably improves
your ability to pick the right tool later. The difficulty is the point.</div>
""" + f"""
<script id="deck-data" type="application/json">{deck}</script>
""" + """
<script>
(function(){
"use strict";
var CARDS = JSON.parse(document.getElementById("deck-data").textContent);
var LS = "msa-srs-v1";
var DAY = 86400000;
var INTERVALS = [0, 1 * DAY, 3 * DAY, 7 * DAY, 21 * DAY]; // per box
var state = {};
try { state = JSON.parse(localStorage.getItem(LS) || "{}"); } catch (e) {}

function save() { try { localStorage.setItem(LS, JSON.stringify(state)); } catch (e) {} }
function card(i) { return state[i] || { box: 0, due: 0 }; }
function isDue(i) { return Date.now() >= card(i).due; }

function dueList() {
  var due = [];
  for (var i = 0; i < CARDS.length; i++) if (isDue(i)) due.push(i);
  // interleave: shuffle (Fisher-Yates, seeded by nothing — fresh each session)
  for (var j = due.length - 1; j > 0; j--) {
    var k = Math.floor(Math.random() * (j + 1));
    var t = due[j]; due[j] = due[k]; due[k] = t;
  }
  return due;
}

var area = document.getElementById("flash-area");
var statsEl = document.getElementById("deck-stats");
var queue = dueList();

function stats() {
  var boxes = [0,0,0,0,0];
  for (var i = 0; i < CARDS.length; i++) boxes[card(i).box]++;
  var mastered = boxes[3] + boxes[4];
  statsEl.innerHTML =
    "<span><b>" + queue.length + "</b> due now</span>" +
    "<span><b>" + mastered + "</b>/" + CARDS.length + " mastered (box 4-5)</span>" +
    "<span class='muted'>boxes: " + boxes.join(" · ") + "</span>" +
    "<span style='margin-left:auto'><button class='copybtn' style='position:static' id='reset-deck'>reset deck</button></span>";
  var rb = document.getElementById("reset-deck");
  if (rb) rb.onclick = function () {
    if (confirm("Reset all card progress?")) { state = {}; save(); queue = dueList(); next(); }
  };
}

function renderMath(el) {
  if (!window.katex) return;
  el.querySelectorAll(".kx").forEach(function (n) {
    try { katex.render(n.getAttribute("data-tex"), n, { displayMode: true, throwOnError: false }); } catch (e) {}
  });
}

function esc(s){ return s.replace(/[&<>"]/g, function(c){ return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]; }); }

function next() {
  stats();
  if (!queue.length) {
    var soonest = Infinity;
    for (var i = 0; i < CARDS.length; i++) soonest = Math.min(soonest, card(i).due);
    var hrs = Math.max(0, Math.round((soonest - Date.now()) / 3600000));
    area.innerHTML = "<div class='exercise' style='text-align:center'><div class='q'>🎉 All done for now!</div>" +
      "<p class='muted'>Next cards due in about " + (hrs < 24 ? hrs + " hours" : Math.round(hrs/24) + " days") +
      ". Spacing only works if you actually leave — go build something with what you know.</p></div>";
    return;
  }
  var idx = queue[0];
  var c = CARDS[idx];
  var front = c.t === "latex"
    ? "<div class='q'>" + esc(c.q) + "</div><div class='target' style='margin:12px 0'><span class='kx' data-tex='" + esc(c.f) + "'></span></div>"
    : "<div class='q'>" + c.q + "</div>";
  var back = c.t === "latex" ? "<pre><code>" + esc(c.a) + "</code></pre>" : "<div>" + c.a + "</div>";
  area.innerHTML =
    "<div class='exercise'>" +
    "<div class='muted small' style='margin-bottom:6px'>" + esc(c.d) + " · card " + (idx + 1) + " · box " + (card(idx).box + 1) + "/5</div>" +
    front +
    "<div id='fc-back' style='display:none;margin-top:12px;border-top:1px solid var(--border);padding-top:12px'>" + back +
    "<div class='ch-btns' style='margin-top:12px'>" +
    "<button id='fc-again' style='border-color:var(--danger);color:var(--danger)'>✗ Again (tomorrow)</button>" +
    "<button id='fc-good' style='border-color:var(--accent2);color:var(--accent2)'>✓ Got it</button>" +
    "</div></div>" +
    "<div class='ch-btns'><button id='fc-flip'>show answer</button></div>" +
    "</div>";
  renderMath(area);
  document.getElementById("fc-flip").onclick = function () {
    document.getElementById("fc-back").style.display = "block";
    this.parentNode.style.display = "none";
  };
  document.getElementById("fc-again").onclick = function () { grade(idx, false); };
  document.getElementById("fc-good").onclick = function () { grade(idx, true); };
}

function grade(idx, ok) {
  var c = card(idx);
  c.box = ok ? Math.min(c.box + 1, 4) : 0;
  c.due = Date.now() + (ok ? INTERVALS[c.box] : DAY);
  state[idx] = c; save();
  // XP: +3 per remembered card (repeatable — reviewing IS the work), -1 per miss
  window.dispatchEvent(new CustomEvent("msa-xp", { detail: { delta: ok ? 3 : -1 } }));
  queue.shift();
  next();
}

next();
})();
</script>

<div class="pager">
  <a href="slides.html"><span class="dir">← Chapters</span>3 · manim-slides</a>
  <a href="reference.html" class="right"><span class="dir">Look things up →</span>📖 Reference</a>
</div>
"""
    return page("practice.html", "Practice", body, katex=True,
                desc="Spaced-repetition flashcards for LaTeX, Manim and manim-slides: 49 interleaved retrieval-practice cards with a Leitner scheduling system — the evidence-based way to make the course stick.")
