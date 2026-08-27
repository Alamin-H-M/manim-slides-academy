from common import page, pre, deck, example, quiz, exercise, topic

T1 = topic(1, "sld-first", "From Scene to Slide — one import, one call", """
Change <code>Scene</code> to <code>Slide</code> (from manim_slides) and call
<code>self.next_slide()</code> wherever the presentation should <b>pause and wait for you</b>.
Everything you know from Chapter 2 still works — a Slide <em>is</em> a Scene.""",
example("easy", "Your first deck (this one is real — click through it!)", deck("FirstDeck", '''from manim import *
from manim_slides import Slide

class FirstDeck(Slide):
    def construct(self):
        title = Text("My first deck", font_size=60)
        self.play(Write(title))
        self.next_slide()          # ⏸ waits for your click

        self.play(title.animate.scale(0.5).to_edge(UP))
        body = Text("Click / press → to advance",
                    font_size=36, color=GREY)
        self.play(FadeIn(body))
        self.next_slide()          # ⏸ waits again

        self.play(FadeOut(title), FadeOut(body))''',
"Render + convert: <code>manim-slides render deck.py FirstDeck</code> then <code>manim-slides convert --to html --offline FirstDeck out.html</code> — or press ▶ with the VS Code extension and it's all automatic.")) +
example("easy", "Bullet points that appear on YOUR click", deck("TwoPoints", '''class TwoPoints(Slide):
    def construct(self):
        head = Text("Why animate slides?", font_size=48).to_edge(UP)
        p1 = Text("1. Motion guides attention",
                  font_size=34, color=TEAL).shift(UP * 0.5)
        p2 = Text("2. Steps appear when YOU decide",
                  font_size=34, color=YELLOW).next_to(p1, DOWN, buff=0.6)
        self.play(Write(head))
        self.next_slide()
        self.play(FadeIn(p1, shift=RIGHT))
        self.next_slide()
        self.play(FadeIn(p2, shift=RIGHT))
        self.next_slide()
        self.play(FadeOut(head), FadeOut(p1), FadeOut(p2))''',
"The pattern for every talk: reveal → pause → reveal → pause.")) +
example("hard", "Looping slides — ambient motion while you talk", deck("LoopingLogo", '''class LoopingLogo(Slide):
    def construct(self):
        logo = RegularPolygon(6, color=TEAL,
                              fill_opacity=0.4).scale(1.5)
        label = Text("loop=True keeps this spinning",
                     font_size=30).to_edge(DOWN)
        self.play(Create(logo), FadeIn(label))

        self.next_slide(loop=True)   # ⟳ loops until you advance
        self.play(Rotate(logo, TAU, run_time=3,
                         rate_func=linear))

        self.next_slide()
        self.play(FadeOut(logo), FadeOut(label))''',
"loop=True replays that segment forever — perfect for title slides while the audience settles.")) +
example("hard", "A real mini-lecture: LaTeX + graph + updater, as slides", deck("MathLecture", '''class MathLecture(Slide):
    def construct(self):
        title = Text("The derivative", font_size=54)
        self.play(Write(title))
        self.next_slide()

        self.play(title.animate.scale(0.55).to_edge(UP))
        definition = MathTex(
            r"f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}",
            font_size=54)
        self.play(Write(definition))
        self.next_slide()

        self.play(definition.animate.scale(0.7).shift(UP * 1.6))
        axes = Axes(x_range=[-2.5, 2.5], y_range=[-0.5, 4],
                    x_length=8, y_length=3.2).shift(DOWN * 1.2)
        curve = axes.plot(lambda x: 0.55 * x**2 + 0.3,
                          color=YELLOW)
        self.play(Create(axes), Create(curve))
        self.next_slide()

        x = ValueTracker(-1.8)
        tangent = always_redraw(lambda: TangentLine(
            curve, alpha=(x.get_value() + 2.5) / 5,
            length=3.5, color=RED))
        self.add(tangent)
        self.play(x.animate.set_value(1.8), run_time=3,
                  rate_func=linear)
        self.next_slide()
        self.play(*[FadeOut(m) for m in
                    [title, definition, axes, curve, tangent]])''',
"All three chapters in one deck: Chapter-1 LaTeX, Chapter-2 graphs & updaters, Chapter-3 pauses.")))

T2 = topic(2, "sld-run", "Rendering, presenting, exporting", """
Three commands cover the whole lifecycle — and if you use the VS Code extension,
the first two happen automatically every time you save.""",
pre("""# 1. RENDER — runs Manim + records where the pauses are
manim-slides render lecture.py MathLecture

# 2. PRESENT — three ways to show it:
manim-slides present MathLecture              # native window (PySide6) — best in-person
manim-slides convert --to html --offline MathLecture out.html   # browser deck — best to share
# ...or the VS Code extension's live preview          — best while authoring

# 3. EXPORT — hand it to PowerPoint people:
manim-slides convert --to pptx MathLecture lecture.pptx""", "shell") + """
<table>
<tr><th>Target</th><th>Best for</th><th>Offline?</th></tr>
<tr><td>Native GUI (<code>present</code>)</td><td>Presenting in person — instant start, presenter hotkeys</td><td>always</td></tr>
<tr><td>HTML (<code>convert --to html --offline</code>)</td><td>Sharing a link/file; works on any machine with a browser</td><td>with <code>--offline</code></td></tr>
<tr><td>PowerPoint (<code>--to pptx</code>)</td><td>Venues that demand .pptx; embeds auto-playing videos</td><td>always</td></tr>
</table>
<div class="tip"><b>Presenter hotkeys (native GUI)</b> <kbd>→</kbd>/<kbd>Space</kbd> next ·
<kbd>←</kbd> previous · <kbd>F</kbd> fullscreen · <kbd>R</kbd> replay current · <kbd>Q</kbd> quit.
In the HTML version: same arrows, plus <kbd>Esc</kbd> for slide overview.</div>""")

T3 = topic(3, "sld-craft", "Slide craft — patterns that make decks feel professional", """
Four battle-tested patterns. None require new API — just discipline in how you use
<code>next_slide()</code> and FadeOut.""",
"""<h3>Pattern 1 — Clean between sections</h3>""" +
pre('''self.next_slide()
self.play(*[FadeOut(m) for m in self.mobjects])   # wipe everything
# ...start the next section on a clean canvas''') + """
<h3>Pattern 2 — Title that shrinks into a header</h3>""" +
pre('''title = Text("Big opening title", font_size=64)
self.play(Write(title))
self.next_slide()
self.play(title.animate.scale(0.5).to_edge(UP))   # becomes the header''') + """
<h3>Pattern 3 — The loop-while-talking title slide</h3>""" +
pre('''self.next_slide(loop=True)     # ambient motion, zero pressure
self.play(Rotate(star, TAU, run_time=4, rate_func=linear))
self.next_slide()              # advances when YOU are ready''') + """
<h3>Pattern 4 — Highlight, then un-highlight</h3>""" +
pre('''self.play(formula[2].animate.set_color(YELLOW))   # spotlight one term
self.next_slide()
self.play(formula[2].animate.set_color(WHITE))    # release attention''') + """
<div class="note"><b>Rule of thumb</b> One idea per slide segment; if you're saying "and also" twice
about the same screen, split it with another <code>next_slide()</code>. Pauses are free — confusion isn't.</div>""")

EXERCISES = """
<h2 id="sld-ex">Self-examination</h2>
""" + quiz("What does self.next_slide() actually do?",
    [("Renders the next scene file", False),
     ("Marks a pause point: playback stops there until the presenter advances", True),
     ("Creates a new blank slide", False), ("Skips the next animation", False)],
    "It records a boundary — everything between two next_slide() calls plays as one segment.") + \
quiz("Your talk venue has no internet. Which export is safest?",
    [("convert --to html (default)", False), ("convert --to html --offline", True),
     ("A YouTube link", False), ("Any of them", False)],
    "--offline bundles Reveal.js locally; the default fetches it from a CDN and shows a blank page without internet.") + \
quiz("What happens between self.next_slide(loop=True) and the following next_slide()?",
    [("The whole deck restarts", False), ("Nothing renders", False),
     ("That segment replays forever until the presenter advances", True), ("The video plays backwards", False)],
    "loop=True makes just that segment cycle — ideal for ambient title slides.") + \
exercise("Convert this Chapter-2 scene into a 3-pause deck: Write a title → pause → draw a sine curve on axes → pause → fade everything out. Use the sine example from Chapter 2 as your starting point.",
    pre('''from manim import *
from manim_slides import Slide

class SineDeck(Slide):
    def construct(self):
        title = Text("The sine wave", font_size=56)
        self.play(Write(title))
        self.next_slide()

        self.play(title.animate.scale(0.5).to_edge(UP))
        axes = Axes(x_range=[-4, 4], y_range=[-2, 2],
                    x_length=10, y_length=5)
        curve = axes.plot(lambda x: np.sin(x), color=YELLOW)
        self.play(Create(axes))
        self.play(Create(curve), run_time=2)
        self.next_slide()

        self.play(*[FadeOut(m) for m in self.mobjects])''')) + \
exercise("Make a deck whose first slide loops a pulsing circle (scale up and back, there_and_back) until you advance. (Hint: next_slide(loop=True).)",
    pre('''class PulseTitle(Slide):
    def construct(self):
        c = Circle(radius=1.5, color=TEAL, fill_opacity=0.4)
        title = Text("Ready?", font_size=48).next_to(c, DOWN)
        self.play(Create(c), Write(title))
        self.next_slide(loop=True)
        self.play(c.animate.scale(1.25), rate_func=there_and_back,
                  run_time=1.6)
        self.next_slide()
        self.play(FadeOut(c), FadeOut(title))''')) + \
exercise("Final project: build a 5-slide deck teaching the quadratic formula — title (looping), the formula (Chapter 1 LaTeX), a parabola plot with its roots marked (Chapter 2), highlight the discriminant in yellow, clean fade-out. Then export it to BOTH offline HTML and pptx.",
    pre('''class QuadraticTalk(Slide):
    def construct(self):
        # 1 — looping title
        title = Text("The Quadratic Formula", font_size=54)
        self.play(Write(title))
        self.next_slide(loop=True)
        self.play(title.animate.set_color(TEAL),
                  rate_func=there_and_back, run_time=2)
        self.next_slide()
        self.play(title.animate.scale(0.5).to_edge(UP))

        # 2 — the formula
        f = MathTex(r"x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}",
                    font_size=64)
        self.play(Write(f))
        self.next_slide()

        # 3 — parabola with roots
        self.play(f.animate.scale(0.6).shift(UP * 1.8))
        ax = Axes(x_range=[-4, 2], y_range=[-3, 5],
                  x_length=8, y_length=3.4).shift(DOWN * 1.2)
        curve = ax.plot(lambda x: x**2 + 2*x - 2, color=YELLOW)
        roots = VGroup(*[Dot(ax.c2p(r, 0), color=RED)
            for r in (-1 - 3**0.5, -1 + 3**0.5)])
        self.play(Create(ax), Create(curve))
        self.play(FadeIn(roots, scale=3))
        self.next_slide()

        # 4 — highlight the discriminant b²-4ac
        self.play(Indicate(f, color=YELLOW))
        self.next_slide()

        # 5 — clean exit
        self.play(*[FadeOut(m) for m in self.mobjects])

# terminal:
#   manim-slides render talk.py QuadraticTalk
#   manim-slides convert --to html --offline QuadraticTalk talk.html
#   manim-slides convert --to pptx QuadraticTalk talk.pptx'''))

BODY = f"""
<h1>Chapter 3 · manim-slides</h1>
<p class="lead">The payoff chapter: your animations become presentations. The decks below are
<b>real interactive presentations</b> — click one open, then click / press <kbd>→</kbd> inside it
to advance, exactly like your audience would.</p>
<div class="toc"><b>Topics</b>
<a href="#sld-first">1 Scene → Slide</a><a href="#sld-run">2 Render, present, export</a>
<a href="#sld-craft">3 Slide craft</a><a href="#sld-ex">✅ Self-exam</a></div>
{T1}{T2}{T3}{EXERCISES}
<div class="pager">
  <a href="manim.html"><span class="dir">← Previous</span>2 · Manim</a>
  <a href="index.html" class="right"><span class="dir">Finish 🎉</span>Back to Home</a>
</div>
"""

def render():
    return page("slides.html", "manim-slides", BODY)
