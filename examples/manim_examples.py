"""All Manim example scenes for the Academy website.
Rendered at -ql (854x480 @15fps) to keep the offline site lightweight.
Each scene is intentionally SHORT (2-6 s) and matches the code shown on the site.
"""
from manim import *


# ---------- Topic 1: Scenes & Mobjects ----------
class FirstCircle(Scene):
    def construct(self):
        circle = Circle(radius=1.5, color=BLUE)
        self.play(Create(circle))
        self.wait(0.5)


class SquareAndLabel(Scene):
    def construct(self):
        square = Square(side_length=2, color=GREEN)
        label = Text("A square", font_size=36).next_to(square, DOWN)
        self.play(Create(square))
        self.play(Write(label))
        self.wait(0.5)


class ShapeFamily(Scene):
    def construct(self):
        shapes = VGroup(
            Circle(color=BLUE), Square(color=GREEN),
            Triangle(color=YELLOW), Star(color=RED),
        ).arrange(RIGHT, buff=0.8).scale(0.7)
        self.play(LaggedStart(*[Create(s) for s in shapes], lag_ratio=0.3))
        self.wait(0.5)


class MorphingShapes(Scene):
    def construct(self):
        shape = Circle(radius=1.5, color=BLUE)
        self.play(Create(shape))
        for target in [Square(side_length=2.5, color=GREEN),
                       Triangle(color=YELLOW).scale(1.5),
                       RegularPolygon(6, color=PURPLE).scale(1.5)]:
            self.play(Transform(shape, target))
        self.wait(0.5)


# ---------- Topic 2: Animations ----------
class HelloWrite(Scene):
    def construct(self):
        text = Text("Hello, Manim!", font_size=60, gradient=(BLUE, TEAL))
        self.play(Write(text))
        self.wait(0.5)


class FadeAndGrow(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5)
        square = Square(color=GREEN, fill_opacity=0.5).shift(RIGHT * 2.5)
        circle.shift(LEFT * 2.5)
        self.play(FadeIn(circle), GrowFromCenter(square))
        self.wait(0.3)
        self.play(FadeOut(circle, shift=UP), FadeOut(square, shift=DOWN))


class WordMorph(Scene):
    def construct(self):
        a = Text("mathematics", font_size=56)
        b = Text("animations", font_size=56, color=TEAL)
        self.play(Write(a))
        self.wait(0.3)
        self.play(TransformMatchingShapes(a, b))
        self.wait(0.5)


class RainDots(Scene):
    def construct(self):
        dots = VGroup(*[Dot(color=random_bright_color()).move_to(
            [x, 3.5, 0]) for x in np.linspace(-6, 6, 25)])
        self.play(LaggedStart(
            *[d.animate.shift(DOWN * 7) for d in dots],
            lag_ratio=0.05, run_time=2.5, rate_func=rate_functions.ease_in_quad))
        self.wait(0.3)


# ---------- Topic 3: Positioning ----------
class ShiftAround(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).scale(2)
        self.play(FadeIn(dot))
        for direction in [UP * 2, RIGHT * 3, DOWN * 4, LEFT * 6, UP * 2 + RIGHT * 3]:
            self.play(dot.animate.shift(direction), run_time=0.5)
        self.wait(0.3)


class NeighborLayout(Scene):
    def construct(self):
        center = Square(color=BLUE)
        up = Text("above", font_size=30).next_to(center, UP)
        down = Text("below", font_size=30).next_to(center, DOWN)
        left = Text("left", font_size=30).next_to(center, LEFT)
        right = Text("right", font_size=30).next_to(center, RIGHT)
        self.play(Create(center))
        self.play(*[FadeIn(t, shift=0.3 * d) for t, d in
                    [(up, DOWN), (down, UP), (left, RIGHT), (right, LEFT)]])
        self.wait(0.5)


class GridOfShapes(Scene):
    def construct(self):
        grid = VGroup(*[
            Circle(radius=0.3, color=c, fill_opacity=0.8)
            for c in [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK, WHITE]
        ]).arrange_in_grid(rows=3, cols=3, buff=0.6)
        self.play(LaggedStart(*[GrowFromCenter(s) for s in grid], lag_ratio=0.1))
        self.play(grid.animate.arrange(RIGHT, buff=0.25).scale(0.8))
        self.wait(0.5)


class OrbitingMoon(Scene):
    def construct(self):
        planet = Circle(radius=0.6, color=BLUE, fill_opacity=1)
        orbit = Circle(radius=2.2, color=GREY).set_stroke(width=2)
        moon = Dot(color=WHITE).scale(1.5).move_to(orbit.point_from_proportion(0))
        self.play(FadeIn(planet), Create(orbit), FadeIn(moon))
        self.play(MoveAlongPath(moon, orbit), run_time=3, rate_func=linear)
        self.wait(0.3)


# ---------- Topic 4: Color & styling ----------
class FillAndStroke(Scene):
    def construct(self):
        s1 = Square(color=BLUE).shift(LEFT * 3)                      # stroke only
        s2 = Square(color=BLUE, fill_opacity=1)                      # filled
        s3 = Square(fill_color=YELLOW, fill_opacity=1,
                    stroke_color=RED, stroke_width=8).shift(RIGHT * 3)
        self.play(Create(s1), Create(s2), Create(s3))
        self.wait(0.7)


class GradientTitle(Scene):
    def construct(self):
        title = Text("Gradients!", font_size=72, gradient=(RED, YELLOW, GREEN))
        underline = Line(LEFT * 3, RIGHT * 3).next_to(title, DOWN)
        underline.set_color_by_gradient(RED, YELLOW, GREEN)
        self.play(Write(title), Create(underline))
        self.wait(0.7)


class DashAndOpacity(Scene):
    def construct(self):
        solid = Circle(radius=1.2, color=TEAL).shift(LEFT * 3)
        dashed = DashedVMobject(Circle(radius=1.2, color=TEAL))
        ghost = Circle(radius=1.2, color=TEAL, fill_opacity=0.25,
                       stroke_opacity=0.4).shift(RIGHT * 3)
        self.play(Create(solid), Create(dashed), FadeIn(ghost))
        self.wait(0.7)


class StyleWave(Scene):
    def construct(self):
        squares = VGroup(*[Square(side_length=0.7, fill_opacity=0.9)
                           for _ in range(10)]).arrange(RIGHT, buff=0.15)
        squares.set_color_by_gradient(PURPLE, TEAL, YELLOW)
        self.play(LaggedStart(*[GrowFromCenter(s) for s in squares], lag_ratio=0.08))
        self.play(LaggedStart(
            *[s.animate.shift(UP * 0.8).set_fill(WHITE) for s in squares],
            lag_ratio=0.1, rate_func=there_and_back, run_time=2))
        self.wait(0.3)


# ---------- Topic 5: Updaters & ValueTracker ----------
class LiveCounter(Scene):
    def construct(self):
        value = ValueTracker(0)
        number = DecimalNumber(0, num_decimal_places=1, font_size=96)
        number.add_updater(lambda m: m.set_value(value.get_value()))
        self.add(number)
        self.play(value.animate.set_value(100), run_time=3, rate_func=linear)
        self.wait(0.5)


class DotChaser(Scene):
    def construct(self):
        anchor = Dot(LEFT * 4, color=BLUE).scale(1.5)
        runner = Dot(RIGHT * 4 + UP * 2, color=YELLOW).scale(1.5)
        rope = always_redraw(lambda: Line(
            anchor.get_center(), runner.get_center(), color=GREY))
        self.add(anchor, runner, rope)
        self.play(runner.animate.move_to(RIGHT * 4 + DOWN * 2), run_time=1.5)
        self.play(runner.animate.move_to(UP * 2.5), run_time=1.5)
        self.wait(0.3)


class TickingClock(Scene):
    def construct(self):
        face = Circle(radius=2, color=WHITE)
        hand = Line(ORIGIN, UP * 1.6, color=YELLOW, stroke_width=6)
        hand.add_updater(lambda m, dt: m.rotate(-dt * PI / 2, about_point=ORIGIN))
        self.play(Create(face))
        self.add(hand)
        self.wait(4)


class GrowingBar(Scene):
    def construct(self):
        progress = ValueTracker(0)
        track = Rectangle(width=8, height=0.6, color=GREY)
        bar = always_redraw(lambda: Rectangle(
            width=max(progress.get_value() * 8, 0.001), height=0.6,
            fill_color=TEAL, fill_opacity=1, stroke_width=0,
        ).align_to(track, LEFT))
        pct = always_redraw(lambda: Integer(
            int(progress.get_value() * 100), unit=r"\%", font_size=40
        ).next_to(track, UP))
        self.add(track, bar, pct)
        self.play(progress.animate.set_value(1), run_time=3,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.5)


# ---------- Topic 6: Graphs & MathTex ----------
class SinePlot(Scene):
    def construct(self):
        axes = Axes(x_range=[-4, 4], y_range=[-2, 2], x_length=10, y_length=5)
        curve = axes.plot(lambda x: np.sin(x), color=YELLOW)
        self.play(Create(axes))
        self.play(Create(curve), run_time=2)
        self.wait(0.5)


class EulerFormula(Scene):
    def construct(self):
        formula = MathTex(r"e^{i\pi} + 1 = 0", font_size=96)
        name = Text("Euler's identity", font_size=32, color=GREY).next_to(formula, DOWN)
        self.play(Write(formula))
        self.play(FadeIn(name))
        self.wait(0.7)


class RiemannIntro(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 4], y_range=[0, 9], x_length=9, y_length=5)
        curve = axes.plot(lambda x: x ** 2 * 0.55 + 0.5, color=TEAL)
        rects = axes.get_riemann_rectangles(curve, x_range=[0, 4], dx=0.5,
                                            fill_opacity=0.7)
        fine = axes.get_riemann_rectangles(curve, x_range=[0, 4], dx=0.125,
                                           fill_opacity=0.7)
        self.play(Create(axes), Create(curve))
        self.play(FadeIn(rects))
        self.play(Transform(rects, fine))
        self.wait(0.5)


class TangentSlide(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3], y_range=[-1, 8], x_length=10, y_length=5.5)
        curve = axes.plot(lambda x: 0.6 * x ** 2 + 0.4, color=YELLOW)
        x = ValueTracker(-2.2)
        tangent = always_redraw(lambda: TangentLine(
            curve, alpha=(x.get_value() + 3) / 6, length=4, color=RED))
        dot = always_redraw(lambda: Dot(color=RED).move_to(
            axes.c2p(x.get_value(), 0.6 * x.get_value() ** 2 + 0.4)))
        self.play(Create(axes), Create(curve))
        self.add(tangent, dot)
        self.play(x.animate.set_value(2.2), run_time=3, rate_func=linear)
        self.wait(0.3)
