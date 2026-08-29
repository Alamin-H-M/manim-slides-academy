from common import page, pre, vid, example, quiz, exercise, topic, pretest, set_page, pychallenge, TOPIC_EXTRAS
set_page("manim.html")

# ---- "your turn to write" challenges: one per topic, appended inside it ----
TOPIC_EXTRAS.update({
"mnm-scene": pychallenge("pc-scene", "Your turn to write — your very first scene:",
    "Write a scene class called <code>MyFirst</code> that creates a <b>blue Circle</b> and plays <code>Create</code> on it.",
    [[r"class\s+MyFirst\s*\(\s*Scene\s*\)", "class MyFirst(Scene)"],
     [r"def\s+construct\s*\(\s*self\s*\)", "def construct(self)"],
     [r"Circle\s*\(", "makes a Circle"],
     [r"(color\s*=\s*BLUE|BLUE)", "colored BLUE"],
     [r"self\.play\s*\(\s*Create\s*\(", "plays Create(...)"]],
"""class MyFirst(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        self.play(Create(circle))""",
    "Subclass Scene, override construct(self), then self.play(Create(...))."),

"mnm-anim": pychallenge("pc-anim", "Your turn to write — three beats of animation:",
    "A <b>Square</b> appears with <code>Create</code>, <b>transforms</b> into a Circle, then <b>fades out</b>. Three plays.",
    [[r"Square\s*\(", "makes a Square"],
     [r"self\.play\s*\(\s*Create\s*\(", "plays Create(...)"],
     [r"Transform\s*\(", "uses Transform(...)"],
     [r"Circle\s*\(", "…into a Circle"],
     [r"FadeOut\s*\(", "ends with FadeOut(...)"]],
"""sq = Square()
self.play(Create(sq))
self.play(Transform(sq, Circle()))
self.play(FadeOut(sq))""",
    "Transform(old, new) morphs in place — then FadeOut the same variable."),

"mnm-pos": pychallenge("pc-pos", "Your turn to write — place things precisely:",
    "Make a Circle, put a <code>Text</code> label <b>below it</b> with <code>next_to</code>, then group both in a <code>VGroup</code> and <code>shift</code> the group 2 units LEFT.",
    [[r"next_to\s*\(", "label placed with next_to(...)"],
     [r"\bDOWN\b", "…below (DOWN)"],
     [r"VGroup\s*\(", "grouped in a VGroup"],
     [r"\.shift\s*\(", "group shifted"],
     [r"LEFT\s*\*\s*2|2\s*\*\s*LEFT", "…by 2 * LEFT"]],
"""c = Circle()
label = Text("a circle").next_to(c, DOWN)
group = VGroup(c, label)
group.shift(LEFT * 2)""",
    "next_to(mobject, DOWN) positions relative to another mobject; shift moves by a vector."),

"mnm-style": pychallenge("pc-style", "Your turn to write — style it like you mean it:",
    "Create a Square with <b>50% fill opacity</b>, then animate it turning <b>RED</b> using the <code>.animate</code> syntax.",
    [[r"Square\s*\(", "makes a Square"],
     [r"fill_opacity\s*=\s*0?\.5", "fill_opacity=0.5"],
     [r"\.animate\.", "uses .animate"],
     [r"set_color\s*\(\s*RED|set_fill\s*\(\s*RED", "…to RED"],
     [r"self\.play\s*\(", "inside self.play(...)"]],
"""sq = Square(fill_opacity=0.5)
self.add(sq)
self.play(sq.animate.set_color(RED))""",
    "fill_opacity is a constructor argument; .animate turns any setter into an animation."),

"mnm-updaters": pychallenge("pc-updaters", "Your turn to write — a number that counts:",
    "Make a <code>ValueTracker</code> starting at 0, a <code>DecimalNumber</code> that <b>follows it with an updater</b>, and animate the tracker to <b>100</b>.",
    [[r"ValueTracker\s*\(\s*0\s*\)", "ValueTracker(0)"],
     [r"DecimalNumber\s*\(", "a DecimalNumber"],
     [r"add_updater\s*\(|always_redraw\s*\(", "wired with an updater"],
     [r"get_value\s*\(\s*\)", "reads tracker.get_value()"],
     [r"\.animate\.set_value\s*\(\s*100\s*\)", "animates to set_value(100)"]],
"""t = ValueTracker(0)
num = DecimalNumber(0)
num.add_updater(lambda m: m.set_value(t.get_value()))
self.add(num)
self.play(t.animate.set_value(100))""",
    "The updater lambda runs every frame: m.set_value(tracker.get_value())."),

"mnm-graphs": pychallenge("pc-graphs", "Your turn to write — a real plot:",
    "Create <code>Axes</code>, plot <b>sin(x)</b> on them with a lambda, and play <code>Create</code> on both.",
    [[r"Axes\s*\(", "creates Axes"],
     [r"\.plot\s*\(", "calls axes.plot(...)"],
     [r"lambda\s+x\s*:", "with a lambda x:"],
     [r"np\.sin\s*\(\s*x\s*\)|sin\s*\(\s*x\s*\)", "…of sin(x)"],
     [r"self\.play\s*\(\s*Create\s*\(", "plays Create(...)"]],
"""ax = Axes()
curve = ax.plot(lambda x: np.sin(x))
self.play(Create(ax))
self.play(Create(curve))""",
    "axes.plot takes any function of x — a lambda is the shortest way."),

"mnm-tex-adv": pychallenge("pc-texadv", "Your turn to write — equation morphing:",
    "Write <code>MathTex</code> for <b>a²+b²=c²</b> split into <b>separate substrings</b> (so terms can move), then morph it into another MathTex with <code>TransformMatchingTex</code>.",
    [[r"MathTex\s*\(", "uses MathTex"],
     [r"MathTex\s*\([^)]*,[^)]*,", "…split into multiple substrings"],
     [r"a\^?2|a\^\{?2\}?", "contains a²"],
     [r"TransformMatchingTex\s*\(", "morphs with TransformMatchingTex"],
     [r"self\.play\s*\(", "inside self.play(...)"]],
"""eq1 = MathTex("a^2", "+", "b^2", "=", "c^2")
eq2 = MathTex("c^2", "=", "a^2", "+", "b^2")
self.play(Write(eq1))
self.play(TransformMatchingTex(eq1, eq2))""",
    "Every comma-separated string is a separately-animatable piece — that's the whole trick."),

"mnm-timing": pychallenge("pc-timing", "Your turn to write — choreography:",
    "Animate three squares appearing with <code>LaggedStart</code>, a <code>lag_ratio</code> of 0.3, a total <code>run_time</code> of 2, and a <code>rate_func</code> of your choice.",
    [[r"LaggedStart\s*\(", "uses LaggedStart"],
     [r"lag_ratio\s*=\s*0?\.3", "lag_ratio=0.3"],
     [r"run_time\s*=\s*2", "run_time=2"],
     [r"rate_func\s*=", "sets a rate_func"],
     [r"self\.play\s*\(", "inside self.play(...)"]],
"""squares = [Square().shift(LEFT*3), Square(), Square().shift(RIGHT*3)]
self.play(LaggedStart(*[Create(s) for s in squares],
                      lag_ratio=0.3),
          run_time=2, rate_func=smooth)""",
    "LaggedStart(*list_of_anims, lag_ratio=…) staggers them; run_time and rate_func go on play()."),

"mnm-camera": pychallenge("pc-camera", "Your turn to write — move the camera:",
    "In a <code>MovingCameraScene</code>, animate <code>self.camera.frame</code> to <b>scale to half size</b> and <b>move to</b> a dot.",
    [[r"MovingCameraScene", "class extends MovingCameraScene"],
     [r"self\.camera\.frame", "touches self.camera.frame"],
     [r"\.animate", "with .animate"],
     [r"scale\s*\(\s*0?\.5\s*\)", "scale(0.5)"],
     [r"move_to\s*\(", "and move_to(...)"]],
"""class ZoomIn(MovingCameraScene):
    def construct(self):
        dot = Dot(RIGHT * 3)
        self.add(dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(dot))""",
    "The camera frame is just a mobject — scale it and move it like anything else."),

"mnm-3d": pychallenge("pc-3d", "Your turn to write — enter the third dimension:",
    "A <code>ThreeDScene</code> that sets a camera orientation (<code>phi</code> and <code>theta</code>), creates <code>ThreeDAxes</code> and a <code>Sphere</code>.",
    [[r"ThreeDScene", "class extends ThreeDScene"],
     [r"set_camera_orientation\s*\(", "sets camera orientation"],
     [r"phi\s*=", "with phi=…"],
     [r"ThreeDAxes\s*\(", "creates ThreeDAxes"],
     [r"Sphere\s*\(", "and a Sphere"]],
"""class My3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()
        ball = Sphere()
        self.play(Create(axes), Create(ball))""",
    "phi tilts down from the pole, theta spins around — 70°/-45° is the classic view."),

"mnm-config": pychallenge("pc-config", "Your turn to write — the render command:",
    "Write the terminal command that renders <code>MyScene</code> from <code>talk.py</code> at <b>high quality</b> and <b>opens the result</b> when done.",
    [[r"\bmanim\b", "starts with manim"],
     [r"-p|--preview", "opens when done (-p)"],
     [r"-p?qh|-q\s*h|--quality", "high quality (-qh)"],
     [r"talk\.py", "the file: talk.py"],
     [r"MyScene", "the scene: MyScene"]],
"manim -pqh talk.py MyScene",
    "Flags combine: -pqh = preview + quality high. File before scene name."),
})

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

T7 = topic(7, "mnm-tex-adv", "MathTex mastery: transforms, braces & spotlights", """
The killer feature for math talks: split a formula into parts, then <b>morph one equation into
another</b> while matching terms fly to their new places. This is why you learned LaTeX first.""",
vid("TexTransform", '''class TexTransform(Scene):
    def construct(self):
        eq1 = MathTex("a^2", "+", "b^2", "=", "c^2",
                      font_size=72)
        eq2 = MathTex("c^2", "=", "a^2", "+", "b^2",
                      font_size=72)
        self.play(Write(eq1))
        self.wait(0.6)
        self.play(TransformMatchingTex(eq1, eq2),
                  run_time=1.5)
        self.wait(0.6)''',
    "Each string argument becomes a separately-animatable part. TransformMatchingTex moves identical parts to their new positions.") +
vid("BraceAnnotate", '''class BraceAnnotate(Scene):
    def construct(self):
        eq = MathTex("(", "x+1", ")", "^2", "=",
                     "x^2+2x+1", font_size=60)
        self.play(Write(eq))
        brace = Brace(eq[1], DOWN, color=YELLOW)
        note = brace.get_text("this part gets squared")
        note.set_color(YELLOW)
        box = SurroundingRectangle(eq[5], color=TEAL,
                                   buff=0.15)
        self.play(GrowFromCenter(brace), FadeIn(note))
        self.play(Create(box), Indicate(eq[5]))''',
    "eq[1] indexes the parts you split. Brace points at anything; SurroundingRectangle + Indicate = instant spotlight.") +
quiz("You wrote MathTex(r'a^2 + b^2 = c^2') as ONE string. Why can't you animate just the 'b^2'?",
     [("Manim renders one string as one indivisible mobject \u2014 split it into parts to address them", True),
      ("You can \u2014 eq['b^2'] always works", False),
      ("MathTex doesn't support animation at all", False)],
     "splitting into separate string arguments is exactly what makes per-term animation possible."),
xp=20)

T8 = topic(8, "mnm-timing", "Timing & choreography: LaggedStart, rate functions", """
Amateur animations play everything at once at constant speed. Professional ones stagger entrances
and ease movements. Two tools give you 90% of that polish.""",
vid("LaggedShapes", '''class LaggedShapes(Scene):
    def construct(self):
        dots = VGroup(*[Dot(radius=0.14, color=TEAL)
                        for _ in range(12)])
        dots.arrange(RIGHT, buff=0.35)
        self.play(LaggedStart(
            *[GrowFromCenter(d) for d in dots],
            lag_ratio=0.15))
        self.play(dots.animate.set_color(YELLOW),
                  run_time=1.5)''',
    "lag_ratio=0.15: each dot starts when the previous one is 15% done \u2014 a wave instead of a blob.") +
vid("RateFuncs", '''class RateFuncs(Scene):
    def construct(self):
        labels = ["linear", "smooth",
                  "there_and_back", "rush_into"]
        funcs = [linear, smooth,
                 there_and_back, rush_into]
        rows = VGroup(*[
            VGroup(Text(n, font_size=24), Dot(color=ORANGE))
            .arrange(RIGHT, buff=0.5)
            for n in labels])
        rows.arrange(DOWN, aligned_edge=LEFT,
                     buff=0.5).to_edge(LEFT)
        self.add(rows)
        self.play(*[row[1].animate(rate_func=fn,
                                   run_time=2.5)
                    .shift(RIGHT * 8)
                    for row, fn in zip(rows, funcs)])''',
    "Same shift, four personalities. smooth is the default; there_and_back returns home \u2014 great for 'pulse' effects.") +
quiz("You want 20 stars to appear one after another, overlapping slightly. Best tool?",
     [("LaggedStart(*[GrowFromCenter(s) for s in stars], lag_ratio=0.1)", True),
      ("20 separate self.play calls", False),
      ("AnimationGroup with lag_ratio=1", False)],
     "lag_ratio < 1 overlaps them; 20 self.play calls would be strictly sequential (and slow)."),
xp=20)

T9 = topic(9, "mnm-camera", "Camera work: zoom, pan, follow", """
Switch <code>Scene</code> \u2192 <code>MovingCameraScene</code> and the viewport itself becomes an animatable
object. Zooming into detail and following motion are the two moves you'll actually use.""",
vid("CameraZoom", '''class CameraZoom(MovingCameraScene):
    def construct(self):
        dots = VGroup(*[Dot(color=BLUE)
                        for _ in range(9)])
        dots.arrange_in_grid(3, 3, buff=1.2)
        target = dots[4].set_color(YELLOW)
        self.play(Create(dots))
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate
                  .scale(0.35).move_to(target))
        self.wait(0.4)
        self.play(Restore(self.camera.frame))''',
    "self.camera.frame is a rectangle mobject: scale it (zoom), move_to it (pan), Restore brings it back.") +
vid("CameraFollow", '''class CameraFollow(MovingCameraScene):
    def construct(self):
        path = Line(LEFT * 5, RIGHT * 5).shift(DOWN)
        car = Triangle(color=RED, fill_opacity=1)
        car.scale(0.3).rotate(-PI / 2)
        car.move_to(path.get_start())
        self.add(path, car)
        self.camera.frame.scale(0.6).move_to(car)
        self.camera.frame.add_updater(
            lambda f: f.move_to(car.get_center()))
        self.play(car.animate.move_to(path.get_end()),
                  run_time=3, rate_func=linear)''',
    "An updater on the camera frame = a follow-cam. Same updater idea from Topic 5, applied to the camera.") +
quiz("Zoom into the top-right corner of a diagram. Which line?",
     [("self.play(self.camera.frame.animate.scale(0.4).move_to(corner))", True),
      ("self.play(diagram.animate.scale(2.5))", False),
      ("config.zoom = 2.5", False)],
     "scaling the diagram distorts layout & positions; moving the camera frame is non-destructive."),
xp=20)

T10 = topic(10, "mnm-3d", "3D scenes: axes, spheres, surfaces", """
<code>ThreeDScene</code> unlocks the third axis. You position the camera with two angles \u2014
<code>phi</code> (tilt down from vertical) and <code>theta</code> (spin around) \u2014 and can set it
slowly orbiting while you present.""",
vid("First3D", '''class First3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-4, 4],
                          y_range=[-4, 4],
                          z_range=[-3, 3])
        sphere = Sphere(radius=1,
                        resolution=(18, 18))
        sphere.set_color(BLUE)
        self.set_camera_orientation(
            phi=70 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes))
        self.play(Create(sphere))
        self.begin_ambient_camera_rotation(rate=0.4)
        self.wait(2.5)''',
    "phi=70\u00b0 tilts you above the plane; ambient rotation keeps the scene alive while you talk over it.") +
vid("Surface3D", '''class Surface3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-3, 3],
                          y_range=[-3, 3],
                          z_range=[-2, 2])
        surface = Surface(
            lambda u, v: axes.c2p(
                u, v, np.sin(u) * np.cos(v)),
            u_range=[-3, 3], v_range=[-3, 3],
            resolution=(24, 24), fill_opacity=0.8)
        surface.set_fill_by_value(axes=axes,
            colorscale=[(BLUE, -1), (GREEN, 0),
                        (YELLOW, 1)])
        self.set_camera_orientation(
            phi=65 * DEGREES, theta=-50 * DEGREES)
        self.play(Create(axes), Create(surface),
                  run_time=2)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(2)''',
    "Surface takes a function (u,v) \u2192 3D point; set_fill_by_value colors by height like a heat map.") +
quiz("Your 3D text looks skewed because the camera tilts. The fix Manim provides?",
     [("self.add_fixed_in_frame_mobjects(text) \u2014 pins it to the screen like a HUD", True),
      ("Rotate the text by -phi", False),
      ("3D scenes cannot contain text", False)],
     "fixed-in-frame mobjects ignore the 3D camera \u2014 perfect for titles and labels over 3D content."),
xp=25)

T11 = topic(11, "mnm-config", "Production settings: quality, format, partial renders", """
The last mile: rendering the same scene for a quick check, a slide deck, or a final video are
just different flags. These are the ones that matter in real work.""",
pre('''# fast draft while iterating (480p @ 15fps)
manim render -ql --fps 15 scene.py MyScene

# full quality for the final export (1080p60)
manim render -qh scene.py MyScene

# render a transparent-background overlay (for OBS / video editors)
manim render -qh -t --format=mov scene.py MyScene

# just the LAST play() call \u2014 lifesaver when polishing an ending
manim render -ql -n -1 scene.py MyScene

# save the final frame as PNG (thumbnails!)
manim render -qh -s scene.py MyScene''', "shell") +
pre('''# per-project defaults: put a manim.cfg next to your scene file
[CLI]
quality = medium_quality
preview = True
background_color = #101418''', "shell") +
quiz("Your 3-minute scene's ending is wrong. Fastest way to iterate on just the ending?",
     [("manim render -ql -n -1 (render only the last animation)", True),
      ("Render everything at -ql each time", False),
      ("Comment out all earlier self.play calls", False)],
     "-n start,end (or -n -1) skips straight to the animations you're fixing \u2014 commenting code out breaks positions."),
xp=20)

PRETEST = pretest([
    ("Guess: in an animation library, what might a 'Scene' be?", "Your canvas + timeline. You subclass it and describe what happens in <code>construct()</code> — Topic 1."),
    ("How do you think you'd make two animations happen at once?", "Pass both to one <code>play()</code> call. Sequential = separate calls — Topic 2."),
    ("What could make a label FOLLOW a moving dot?", "A function that runs every frame — an <em>updater</em>. That's Topic 5, the superpower one."),
])

BODY = f"""
<h1>Chapter 2 · Manim</h1>
<p class="lead">Every example below shows the <b>exact code</b> on the left and the <b>real video it
rendered</b> on the right — click any video to play it, click again to replay. Eleven topics from first circle to 3D camera work — about 6 hours total;
each topic stands alone, so stop whenever you like.</p>
<div class="toc"><b>Topics</b>
<a href="#mnm-scene">1 Scenes &amp; Mobjects</a><a href="#mnm-anim">2 Animations</a>
<a href="#mnm-pos">3 Positioning</a><a href="#mnm-style">4 Color &amp; styling</a>
<a href="#mnm-updaters">5 Updaters</a><a href="#mnm-graphs">6 Graphs &amp; MathTex</a>
<a href="#mnm-tex-adv">7 MathTex mastery</a><a href="#mnm-timing">8 Timing</a>
<a href="#mnm-camera">9 Camera</a><a href="#mnm-3d">10 3D</a>
<a href="#mnm-config">11 Production</a>
<a href="#mnm-ex">✅ Self-exam</a></div>
{PRETEST}{T1}{T2}{T3}{T4}{T5}{T6}{T7}{T8}{T9}{T10}{T11}{EXERCISES}
<div class="pager">
  <a href="latex.html"><span class="dir">← Previous</span>1 · LaTeX</a>
  <a href="slides.html" class="right"><span class="dir">Next chapter →</span>3 · manim-slides</a>
</div>
"""

def render():
    return page("manim.html", "Manim", BODY, desc='Manim tutorial for beginners: Scenes, Mobjects, animations, positioning, updaters, ValueTracker, graphs and MathTex — 24 real rendered example videos next to their exact Python source code.')