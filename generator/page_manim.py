from common import page, pre, vid, example, quiz, exercise, topic, pretest

T1 = topic(1, "mnm-scene", "Scenes & Mobjects — the two words that explain everything", """
A <b>Scene</b> is your canvas + timeline. A <b>Mobject</b> ("mathematical object") is anything drawable:
circles, text, formulas, graphs. You subclass <code>Scene</code>, override <code>construct()</code>,
and inside it you create mobjects and <code>play()</code> animations on them. That's the whole framework.""",
example("easy", "The smallest possible animation", vid("FirstCircle", '''from manim import *

class FirstCircle(Scene):
    def construct(self):
        circle = Circle(radius=1.5, color=BLUE)
        self.play(Create(circle))
        self.wait(0.5)''',
"Render it: <code>manim render -ql -p first.py FirstCircle</code>")) +
example("easy", "Two mobjects, two animations", vid("SquareAndLabel", '''class SquareAndLabel(Scene):
    def construct(self):
        square = Square(side_length=2, color=GREEN)
        label = Text("A square", font_size=36).next_to(square, DOWN)
        self.play(Create(square))
        self.play(Write(label))
        self.wait(0.5)''',
"Each <code>self.play(...)</code> is one beat of the timeline — they run in order.")) +
example("hard", "VGroup: treat many mobjects as one", vid("ShapeFamily", '''class ShapeFamily(Scene):
    def construct(self):
        shapes = VGroup(
            Circle(color=BLUE), Square(color=GREEN),
            Triangle(color=YELLOW), Star(color=RED),
        ).arrange(RIGHT, buff=0.8).scale(0.7)
        self.play(LaggedStart(*[Create(s) for s in shapes],
                              lag_ratio=0.3))''',
"<code>arrange</code> lays members out; <code>LaggedStart</code> staggers their animations.")) +
example("hard", "Transform: one mobject, many forms", vid("MorphingShapes", '''class MorphingShapes(Scene):
    def construct(self):
        shape = Circle(radius=1.5, color=BLUE)
        self.play(Create(shape))
        for target in [Square(side_length=2.5, color=GREEN),
                       Triangle(color=YELLOW).scale(1.5),
                       RegularPolygon(6, color=PURPLE).scale(1.5)]:
            self.play(Transform(shape, target))''',
"<code>Transform(a, b)</code> smoothly morphs a into b's shape.")))

T2 = topic(2, "mnm-anim", "The animation vocabulary", """
Manim ships dozens of animation classes, but you'll use about eight constantly:
<code>Create</code>, <code>Write</code>, <code>FadeIn/FadeOut</code>, <code>Transform</code>,
<code>GrowFromCenter</code>, <code>LaggedStart</code>, and the special <code>.animate</code> syntax.
Multiple animations passed to one <code>play()</code> run <b>simultaneously</b>.""",
example("easy", "Write — the classic for text", vid("HelloWrite", '''class HelloWrite(Scene):
    def construct(self):
        text = Text("Hello, Manim!", font_size=60,
                    gradient=(BLUE, TEAL))
        self.play(Write(text))''')) +
example("easy", "Parallel animations & directional fades", vid("FadeAndGrow", '''class FadeAndGrow(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5).shift(LEFT * 2.5)
        square = Square(color=GREEN, fill_opacity=0.5).shift(RIGHT * 2.5)
        self.play(FadeIn(circle), GrowFromCenter(square))  # together!
        self.wait(0.3)
        self.play(FadeOut(circle, shift=UP),
                  FadeOut(square, shift=DOWN))''',
"Two animations in one <code>play()</code> = simultaneous.")) +
example("hard", "TransformMatchingShapes — smart morphing", vid("WordMorph", '''class WordMorph(Scene):
    def construct(self):
        a = Text("mathematics", font_size=56)
        b = Text("animations", font_size=56, color=TEAL)
        self.play(Write(a))
        self.play(TransformMatchingShapes(a, b))''',
"Letters that exist in both words fly to their new positions.")) +
example("hard", "LaggedStart + rate functions", vid("RainDots", '''class RainDots(Scene):
    def construct(self):
        dots = VGroup(*[Dot(color=random_bright_color())
                        .move_to([x, 3.5, 0])
                        for x in np.linspace(-6, 6, 25)])
        self.play(LaggedStart(
            *[d.animate.shift(DOWN * 7) for d in dots],
            lag_ratio=0.05, run_time=2.5,
            rate_func=rate_functions.ease_in_quad))''',
"<code>rate_func</code> shapes the speed curve — ease_in_quad = accelerating, like gravity.")))

T3 = topic(3, "mnm-pos", "Positioning: shift, next_to, arrange, paths", """
The screen is a coordinate grid: origin at center, ~7 units left-right, ~4 up-down.
Constants <code>UP, DOWN, LEFT, RIGHT</code> are unit vectors you can scale and add:
<code>UP * 2 + RIGHT * 3</code> is just a point.""",
example("easy", "shift() — move by an offset", vid("ShiftAround", '''class ShiftAround(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).scale(2)
        self.play(FadeIn(dot))
        for direction in [UP * 2, RIGHT * 3, DOWN * 4,
                          LEFT * 6, UP * 2 + RIGHT * 3]:
            self.play(dot.animate.shift(direction), run_time=0.5)''',
"<code>.animate.shift()</code> animates the move; plain <code>.shift()</code> teleports before rendering.")) +
example("easy", "next_to() — position relative to another mobject", vid("NeighborLayout", '''class NeighborLayout(Scene):
    def construct(self):
        center = Square(color=BLUE)
        up = Text("above", font_size=30).next_to(center, UP)
        down = Text("below", font_size=30).next_to(center, DOWN)
        left = Text("left", font_size=30).next_to(center, LEFT)
        right = Text("right", font_size=30).next_to(center, RIGHT)
        self.play(Create(center))
        self.play(FadeIn(up), FadeIn(down),
                  FadeIn(left), FadeIn(right))''',
"Relative positioning survives refactors — move the square, labels follow (at creation time).")) +
example("hard", "arrange_in_grid & re-arranging live", vid("GridOfShapes", '''class GridOfShapes(Scene):
    def construct(self):
        grid = VGroup(*[
            Circle(radius=0.3, color=c, fill_opacity=0.8)
            for c in [RED, ORANGE, YELLOW, GREEN, TEAL,
                      BLUE, PURPLE, PINK, WHITE]
        ]).arrange_in_grid(rows=3, cols=3, buff=0.6)
        self.play(LaggedStart(*[GrowFromCenter(s) for s in grid],
                              lag_ratio=0.1))
        self.play(grid.animate.arrange(RIGHT, buff=0.25).scale(0.8))''',
"A VGroup can be re-arranged as an animation — the layout itself animates.")) +
example("hard", "MoveAlongPath — any mobject, any curve", vid("OrbitingMoon", '''class OrbitingMoon(Scene):
    def construct(self):
        planet = Circle(radius=0.6, color=BLUE, fill_opacity=1)
        orbit = Circle(radius=2.2, color=GREY).set_stroke(width=2)
        moon = Dot(color=WHITE).scale(1.5)
        moon.move_to(orbit.point_from_proportion(0))
        self.play(FadeIn(planet), Create(orbit), FadeIn(moon))
        self.play(MoveAlongPath(moon, orbit),
                  run_time=3, rate_func=linear)''',
"Any VMobject can be a path — circles, arcs, even hand-drawn Bezier curves.")))

T4 = topic(4, "mnm-style", "Color & styling", """
Every mobject has a <b>stroke</b> (outline) and a <b>fill</b>. <code>color=</code> sets both;
<code>fill_opacity=</code> reveals the fill (default 0!). Gradients work on both text and shapes.""",
example("easy", "Stroke, fill, and both", vid("FillAndStroke", '''class FillAndStroke(Scene):
    def construct(self):
        s1 = Square(color=BLUE).shift(LEFT * 3)   # stroke only
        s2 = Square(color=BLUE, fill_opacity=1)   # filled
        s3 = Square(fill_color=YELLOW, fill_opacity=1,
                    stroke_color=RED, stroke_width=8).shift(RIGHT * 3)
        self.play(Create(s1), Create(s2), Create(s3))''',
"The #1 beginner surprise: shapes are hollow until you set fill_opacity.")) +
example("easy", "Gradients", vid("GradientTitle", '''class GradientTitle(Scene):
    def construct(self):
        title = Text("Gradients!", font_size=72,
                     gradient=(RED, YELLOW, GREEN))
        underline = Line(LEFT * 3, RIGHT * 3).next_to(title, DOWN)
        underline.set_color_by_gradient(RED, YELLOW, GREEN)
        self.play(Write(title), Create(underline))''')) +
example("hard", "Dashed lines & opacity for de-emphasis", vid("DashAndOpacity", '''class DashAndOpacity(Scene):
    def construct(self):
        solid = Circle(radius=1.2, color=TEAL).shift(LEFT * 3)
        dashed = DashedVMobject(Circle(radius=1.2, color=TEAL))
        ghost = Circle(radius=1.2, color=TEAL, fill_opacity=0.25,
                       stroke_opacity=0.4).shift(RIGHT * 3)
        self.play(Create(solid), Create(dashed), FadeIn(ghost))''',
"Low opacity = 'this is context, not the point' — a key visual-communication trick.")) +
example("hard", "Gradient across a whole group + there_and_back", vid("StyleWave", '''class StyleWave(Scene):
    def construct(self):
        squares = VGroup(*[Square(side_length=0.7, fill_opacity=0.9)
                           for _ in range(10)]).arrange(RIGHT, buff=0.15)
        squares.set_color_by_gradient(PURPLE, TEAL, YELLOW)
        self.play(LaggedStart(*[GrowFromCenter(s) for s in squares],
                              lag_ratio=0.08))
        self.play(LaggedStart(
            *[s.animate.shift(UP * 0.8).set_fill(WHITE)
              for s in squares],
            lag_ratio=0.1, rate_func=there_and_back, run_time=2))''',
"<code>there_and_back</code> plays the animation forward then in reverse — great for waves and pulses.")))

T5 = topic(5, "mnm-updaters", "Updaters & ValueTracker — animations that react", """
So far every animation was pre-scripted. <b>Updaters</b> are little functions that run
<em>every frame</em>: "keep this line attached to that dot", "keep this number equal to that value".
<code>ValueTracker</code> holds a number you can animate; <code>always_redraw</code> rebuilds
a mobject each frame. This combination is Manim's superpower.""",
example("easy", "A number that counts to 100", vid("LiveCounter", '''class LiveCounter(Scene):
    def construct(self):
        value = ValueTracker(0)
        number = DecimalNumber(0, num_decimal_places=1,
                               font_size=96)
        number.add_updater(
            lambda m: m.set_value(value.get_value()))
        self.add(number)
        self.play(value.animate.set_value(100),
                  run_time=3, rate_func=linear)''',
"You animate the tracker; the updater drags the number along every frame.")) +
example("easy", "A rope that never lets go", vid("DotChaser", '''class DotChaser(Scene):
    def construct(self):
        anchor = Dot(LEFT * 4, color=BLUE).scale(1.5)
        runner = Dot(RIGHT * 4 + UP * 2, color=YELLOW).scale(1.5)
        rope = always_redraw(lambda: Line(
            anchor.get_center(), runner.get_center(), color=GREY))
        self.add(anchor, runner, rope)
        self.play(runner.animate.move_to(RIGHT * 4 + DOWN * 2))
        self.play(runner.animate.move_to(UP * 2.5))''',
"<code>always_redraw</code> rebuilds the line every frame from live positions.")) +
example("hard", "dt-updaters: perpetual motion", vid("TickingClock", '''class TickingClock(Scene):
    def construct(self):
        face = Circle(radius=2, color=WHITE)
        hand = Line(ORIGIN, UP * 1.6, color=YELLOW,
                    stroke_width=6)
        hand.add_updater(lambda m, dt:
            m.rotate(-dt * PI / 2, about_point=ORIGIN))
        self.play(Create(face))
        self.add(hand)
        self.wait(4)   # the hand keeps turning by itself!''',
"An updater taking <code>(mobject, dt)</code> runs on wall-clock time — even during wait().")) +
example("hard", "A live progress bar (three updaters cooperating)", vid("GrowingBar", '''class GrowingBar(Scene):
    def construct(self):
        progress = ValueTracker(0)
        track = Rectangle(width=8, height=0.6, color=GREY)
        bar = always_redraw(lambda: Rectangle(
            width=max(progress.get_value() * 8, 0.001), height=0.6,
            fill_color=TEAL, fill_opacity=1, stroke_width=0,
        ).align_to(track, LEFT))
        pct = always_redraw(lambda: Integer(
            int(progress.get_value() * 100), unit=r"\\%",
            font_size=40).next_to(track, UP))
        self.add(track, bar, pct)
        self.play(progress.animate.set_value(1), run_time=3,
                  rate_func=rate_functions.ease_in_out_sine)''',
"One tracker drives both the bar's width and the percentage — single source of truth.")))

T6 = topic(6, "mnm-graphs", "Graphs & MathTex — where LaTeX pays off", """
<code>Axes</code> gives you a coordinate system; <code>.plot()</code> draws functions on it;
<code>MathTex</code> renders any LaTeX from Chapter 1 as an animatable mobject.
This is the toolkit of every math explainer video you've ever watched.""",
example("easy", "Plot a sine wave", vid("SinePlot", '''class SinePlot(Scene):
    def construct(self):
        axes = Axes(x_range=[-4, 4], y_range=[-2, 2],
                    x_length=10, y_length=5)
        curve = axes.plot(lambda x: np.sin(x), color=YELLOW)
        self.play(Create(axes))
        self.play(Create(curve), run_time=2)''',
"<code>plot()</code> takes any Python function of x.")) +
example("easy", "Your LaTeX, animated", vid("EulerFormula", '''class EulerFormula(Scene):
    def construct(self):
        formula = MathTex(r"e^{i\\pi} + 1 = 0", font_size=96)
        name = Text("Euler's identity", font_size=32,
                    color=GREY).next_to(formula, DOWN)
        self.play(Write(formula))
        self.play(FadeIn(name))''',
"Everything from Chapter 1 works inside MathTex — always with the r prefix.")) +
example("hard", "Riemann rectangles refining themselves", vid("RiemannIntro", '''class RiemannIntro(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 4], y_range=[0, 9],
                    x_length=9, y_length=5)
        curve = axes.plot(lambda x: x**2 * 0.55 + 0.5, color=TEAL)
        rects = axes.get_riemann_rectangles(
            curve, x_range=[0, 4], dx=0.5, fill_opacity=0.7)
        fine = axes.get_riemann_rectangles(
            curve, x_range=[0, 4], dx=0.125, fill_opacity=0.7)
        self.play(Create(axes), Create(curve))
        self.play(FadeIn(rects))
        self.play(Transform(rects, fine))''',
"Transforming coarse rectangles into fine ones IS the idea of integration, visually.")) +
example("hard", "A tangent line sliding along a curve", vid("TangentSlide", '''class TangentSlide(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-1, 8],
                    x_length=10, y_length=5.5)
        curve = axes.plot(lambda x: 0.6 * x**2 + 0.4, color=YELLOW)
        x = ValueTracker(-2.2)
        tangent = always_redraw(lambda: TangentLine(
            curve, alpha=(x.get_value() + 3) / 6,
            length=4, color=RED))
        dot = always_redraw(lambda: Dot(color=RED).move_to(
            axes.c2p(x.get_value(),
                     0.6 * x.get_value()**2 + 0.4)))
        self.play(Create(axes), Create(curve))
        self.add(tangent, dot)
        self.play(x.animate.set_value(2.2), run_time=3,
                  rate_func=linear)''',
"Updaters (topic 5) + graphs (topic 6) = the derivative, animated. This exact scene becomes a slide deck in Chapter 3.")))

EXERCISES = """
<h2 id="mnm-ex">Self-examination</h2>
""" + quiz("Why does a Circle appear as just an outline by default?",
    [("Manim only draws outlines", False), ("fill_opacity defaults to 0", True),
     ("You forgot Create()", False), ("The fill color defaults to black", False)],
    "Shapes have fill_opacity=0 by default — set it to see the fill.") + \
quiz("What's the difference between circle.shift(UP) and circle.animate.shift(UP) inside play()?",
    [("No difference", False), ("The first is faster", False),
     (".animate produces a smooth animation; the plain call moves it instantly", True),
     (".animate moves it twice as far", False)],
    "Plain method calls change state immediately; .animate turns the change into an animation.") + \
quiz("You want a label to follow a moving dot for the whole scene. Best tool?",
    [("Call next_to() once before play()", False), ("An updater / always_redraw", True),
     ("Transform the label every frame manually", False), ("A VGroup", False)],
    "Updaters run every frame — that's exactly what 'follow' means. (A VGroup works only if you move the group itself.)") + \
exercise("Write a scene where a red square grows from the center, slides right 3 units, then fades out upward. (Three plays, or fewer!)",
    pre('''class Ex1(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=0.8)
        self.play(GrowFromCenter(sq))
        self.play(sq.animate.shift(RIGHT * 3))
        self.play(FadeOut(sq, shift=UP))''')) + \
exercise("Make a DecimalNumber that counts DOWN from 10 to 0 in 5 seconds while turning from white to red. (Hint: two updaters or one updater + .animate.set_color.)",
    pre('''class Countdown(Scene):
    def construct(self):
        t = ValueTracker(10)
        num = DecimalNumber(10, num_decimal_places=1, font_size=96)
        num.add_updater(lambda m: m.set_value(t.get_value()))
        self.add(num)
        self.play(t.animate.set_value(0),
                  num.animate.set_color(RED),
                  run_time=5, rate_func=linear)''')) + \
exercise("Plot y = x³ − 3x on axes from −3 to 3 and animate a dot moving along the curve from left to right. (Hint: ValueTracker + always_redraw + axes.c2p.)",
    pre('''class CubicDot(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-4, 4],
                    x_length=10, y_length=5.5)
        f = lambda x: x**3 - 3 * x
        curve = axes.plot(f, color=TEAL)
        x = ValueTracker(-2.2)
        dot = always_redraw(lambda: Dot(color=YELLOW).move_to(
            axes.c2p(x.get_value(), f(x.get_value()))))
        self.play(Create(axes), Create(curve))
        self.add(dot)
        self.play(x.animate.set_value(2.2), run_time=4)'''))

PRETEST = pretest([
    ("Guess: in an animation library, what might a 'Scene' be?", "Your canvas + timeline. You subclass it and describe what happens in <code>construct()</code> — Topic 1."),
    ("How do you think you'd make two animations happen at once?", "Pass both to one <code>play()</code> call. Sequential = separate calls — Topic 2."),
    ("What could make a label FOLLOW a moving dot?", "A function that runs every frame — an <em>updater</em>. That's Topic 5, the superpower one."),
])

BODY = f"""
<h1>Chapter 2 · Manim</h1>
<p class="lead">Every example below shows the <b>exact code</b> on the left and the <b>real video it
rendered</b> on the right — click any video to play it, click again to replay. About 3 hours total;
each topic stands alone, so stop whenever you like.</p>
<div class="toc"><b>Topics</b>
<a href="#mnm-scene">1 Scenes &amp; Mobjects</a><a href="#mnm-anim">2 Animations</a>
<a href="#mnm-pos">3 Positioning</a><a href="#mnm-style">4 Color &amp; styling</a>
<a href="#mnm-updaters">5 Updaters</a><a href="#mnm-graphs">6 Graphs &amp; MathTex</a>
<a href="#mnm-ex">✅ Self-exam</a></div>
{PRETEST}{T1}{T2}{T3}{T4}{T5}{T6}{EXERCISES}
<div class="pager">
  <a href="latex.html"><span class="dir">← Previous</span>1 · LaTeX</a>
  <a href="slides.html" class="right"><span class="dir">Next chapter →</span>3 · manim-slides</a>
</div>
"""

def render():
    return page("manim.html", "Manim", BODY, desc='Manim tutorial for beginners: Scenes, Mobjects, animations, positioning, updaters, ValueTracker, graphs and MathTex — 24 real rendered example videos next to their exact Python source code.')