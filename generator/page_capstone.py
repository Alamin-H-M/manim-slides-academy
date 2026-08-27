from common import page, pre, milestone

BODY = """
<h1>🏆 Capstone — build a real animated talk</h1>
<p class="lead">Everything before this was practice; this is the performance. You'll build
<b>"The Pythagorean Theorem, animated"</b> — a complete presentation combining all three chapters —
through five milestones. The scaffolding fades: milestone 1 hands you the code, milestone 5 is yours alone.
When you finish, you will have done everything this stack was made for. Budget: one afternoon.</p>

<div class="note"><b>The fading rule (read once)</b>
Research on worked examples says the fastest route to competence is: study a full example →
complete partially-solved problems → solve alone. That's exactly the structure below.
<b>Type everything by hand</b> — no copy-paste. Typing is where the learning happens; the copy
buttons are for checking, not for skipping.</div>

{M1}
<p>Create <code>pythagoras.py</code>. Type this, render it, watch it. It's the whole presentation
in miniature: one title slide that pauses.</p>
""" + pre('''from manim import *
from manim_slides import Slide

class Pythagoras(Slide):
    def construct(self):
        title = Text("The Pythagorean Theorem", font_size=56)
        subtitle = MathTex(r"a^2 + b^2 = c^2", font_size=72, color=TEAL)
        subtitle.next_to(title, DOWN, buff=0.6)
        self.play(Write(title))
        self.play(Write(subtitle))
        self.next_slide()
        self.play(title.animate.scale(0.5).to_edge(UP), FadeOut(subtitle))
        self.next_slide()''') + """
<p>Render + present it:</p>
""" + pre("""manim-slides render pythagoras.py Pythagoras
manim-slides present Pythagoras     # -> or convert to HTML, your choice""", "shell") + """
<div class="tip"><b>Checkpoint</b> You should see the title, the formula below it, then (on your click)
the title shrinking to the top edge. If yes — milestone 1 done. If the render fails on MathTex,
revisit <a href="setup.html#latex">Setup §3</a> (LaTeX strategy B).</div>

{M2}
<p>Append before the final <code>next_slide()</code>. One line is missing — the label for side <code>b</code>.
You've seen <code>next_to</code> with directions; fill the gap.</p>
""" + pre('''        # right triangle: legs a=3, b=4 -> hypotenuse c=5
        A = [-2.5, -1.5, 0]   # right-angle corner
        B = [ 1.5, -1.5, 0]   # along the bottom (b = 4 units)
        C = [-2.5,  1.5, 0]   # up the left side (a = 3 units)
        tri = Polygon(A, B, C, color=WHITE, fill_opacity=0.15)

        la = MathTex("a").next_to(Line(A, C), LEFT)
        lb = # ??? — label "b" under the bottom edge Line(A, B)
        lc = MathTex("c").next_to(Line(B, C).get_center(), UR, buff=0.15)

        self.play(Create(tri))
        self.play(Write(la), Write(lb), Write(lc))
        self.next_slide()''') + """
<details class="answer"><summary>stuck? show the missing line</summary><div class="inner">
""" + pre('''lb = MathTex("b").next_to(Line(A, B), DOWN)''') + """
</div></details>

{M3}
<p>The classic visual: a square on each side, areas a², b², c². You get the recipe and the first
square; build the other two yourself.</p>
""" + pre('''        # recipe for a square attached to an edge P->Q:
        #   1. edge = Line(P, Q)
        #   2. sq = Square(side_length=edge.get_length())
        #   3. rotate it to the edge angle:  sq.rotate(edge.get_angle())
        #   4. move its center OUTWARD from the triangle:
        #      sq.move_to(edge.get_center() + offset)
        # first one (on leg a, pointing left) is done for you:
        edge_a = Line(A, C)
        sq_a = Square(side_length=3, color=BLUE, fill_opacity=0.4)
        sq_a.move_to(edge_a.get_center() + LEFT * 1.5)
        area_a = MathTex("a^2").move_to(sq_a)

        # YOUR TURN:
        # sq_b: side 4, GREEN, below edge Line(A, B), label b^2
        # sq_c: side 5, RED, on the hypotenuse Line(B, C) — build it, rotate
        #       by Line(B, C).get_angle(), then shift it outward (UR direction),
        #       label c^2. (Perfect placement is fiddly — close is fine!)

        self.play(FadeIn(sq_a), Write(area_a))
        self.play(FadeIn(sq_b), Write(area_b))
        self.play(FadeIn(sq_c), Write(area_c))
        self.next_slide()''') + """
<details class="answer"><summary>show a working version</summary><div class="inner">
""" + pre('''        sq_b = Square(side_length=4, color=GREEN, fill_opacity=0.4)
        sq_b.move_to(Line(A, B).get_center() + DOWN * 2)
        area_b = MathTex("b^2").move_to(sq_b)

        edge_c = Line(B, C)
        sq_c = Square(side_length=5, color=RED, fill_opacity=0.4)
        sq_c.rotate(edge_c.get_angle())
        sq_c.move_to(edge_c.get_center() + (UP + RIGHT) * 1.8)
        area_c = MathTex("c^2").move_to(sq_c)''') + """
<p class="muted small">Your numbers may differ — if the squares sit roughly on their sides, you've won.
This fiddliness is real Manim life.</p></div></details>

{M4}
<p>New segment: fade everything out, then tell the algebra story — the equation appears,
the numbers substitute in, the result gets a box. Your tools: <code>MathTex</code>,
<code>TransformMatchingTex</code> (or plain <code>Transform</code>), <code>SurroundingRectangle</code>, <code>Indicate</code>.</p>
<ul>
<li>Step 1: <code>eq1 = MathTex(r"a^2 + b^2 = c^2")</code> — Write it, pause.</li>
<li>Step 2: transform into <code>3^2 + 4^2 = c^2</code>, then into <code>9 + 16 = 25</code>, pause between each.</li>
<li>Step 3: <code>c = 5</code> appears beneath, with <code>SurroundingRectangle(..., color=YELLOW)</code> drawn around it via <code>Create</code>.</li>
</ul>
<details class="answer"><summary>show a working version</summary><div class="inner">
""" + pre('''        self.play(*[FadeOut(m) for m in self.mobjects])
        eq1 = MathTex(r"a^2 + b^2 = c^2", font_size=64)
        self.play(Write(eq1))
        self.next_slide()

        eq2 = MathTex(r"3^2 + 4^2 = c^2", font_size=64)
        self.play(TransformMatchingTex(eq1, eq2))
        self.next_slide()

        eq3 = MathTex(r"9 + 16 = 25", font_size=64)
        self.play(TransformMatchingTex(eq2, eq3))
        self.next_slide()

        result = MathTex(r"c = 5", font_size=72, color=YELLOW)
        result.next_to(eq3, DOWN, buff=0.8)
        box = SurroundingRectangle(result, color=YELLOW, buff=0.25)
        self.play(Write(result))
        self.play(Create(box))
        self.next_slide()''') + """
</div></details>

{M5}
<p>Alone now — you know everything you need:</p>
<ol>
<li>Add a <b>looping</b> end slide: "Thanks! Questions?" with some ambient motion (<code>next_slide(loop=True)</code>… you know this).</li>
<li>Clean fade-out at the very end.</li>
<li>Export <b>both</b> deliverables:
""" + pre("""manim-slides convert --to html --offline Pythagoras talk.html
manim-slides convert --to pptx Pythagoras talk.pptx""", "shell") + """
</li>
<li>Open <code>talk.html</code>, disconnect your WiFi, and present it start to finish. Out loud. Yes, really.</li>
</ol>

<div class="tip"><b>🎓 Done?</b> Then you have: written LaTeX inside animations, built and positioned
mobjects, animated transforms, structured a deck with pauses and loops, and shipped offline HTML + PowerPoint.
That is the complete workflow — there is no chapter 4 because there is nothing left to teach.
The <a href="reference.html">Reference</a> is your companion from here; the
<a href="practice.html">Practice deck</a> keeps it all in memory.</div>

<h2 id="next">Where to go from here (choose your adventure)</h2>
<table>
<tr><th>If you want…</th><th>Do this next</th></tr>
<tr><td>A talk on YOUR topic</td><td>Copy pythagoras.py as a template; swap content, keep the structure (title → visual → algebra → loop-out). Structure is reusable, content isn't.</td></tr>
<tr><td>Prettier math typography</td><td>Chapter 1's playgrounds accept everything KaTeX supports — experiment with <code>\\underbrace</code>, <code>\\overset</code>, <code>\\mathcal</code>.</td></tr>
<tr><td>3D scenes, camera moves, voiceovers</td><td>These are Manim plugins/classes beyond this course's scope — by design. You now read Manim code fluently; the official docs' examples will make sense. (Honest scope note, not a sales pitch.)</td></tr>
<tr><td>To help others learn this</td><td>Contribute an example or translation to this site — see the GitHub repo. Teaching is the strongest retrieval practice there is.</td></tr>
</table>

<div class="pager">
  <a href="practice.html"><span class="dir">← Keep it fresh</span>🔁 Practice</a>
  <a href="reference.html" class="right"><span class="dir">Look things up →</span>📖 Reference</a>
</div>
"""


# substitute milestone headings (BODY is a plain string; code samples contain braces)
BODY = BODY.replace('{M1}', milestone(1, "cap-m1", "Milestone 1 — the skeleton", "full worked example", 25))
BODY = BODY.replace('{M2}', milestone(2, "cap-m2", "Milestone 2 — draw the triangle", "worked example, one gap", 30))
BODY = BODY.replace('{M3}', milestone(3, "cap-m3", "Milestone 3 — the squares on the sides", "half scaffold", 35))
BODY = BODY.replace('{M4}', milestone(4, "cap-m4", "Milestone 4 — the algebra, animated", "hints only", 40))
BODY = BODY.replace('{M5}', milestone(5, "cap-m5", "Milestone 5 — ship it", "no scaffold", 50))

def render():
    return page("capstone.html", "Capstone", BODY,
                desc="Capstone project: build a complete animated Pythagorean-theorem presentation with LaTeX, Manim and manim-slides — five milestones with fading scaffolding, from worked example to independent work.")
