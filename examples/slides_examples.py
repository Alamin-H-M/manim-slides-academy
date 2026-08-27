"""manim-slides example scenes for the Academy website.
Each uses next_slide() pauses; the site embeds the rendered HTML export so
readers click through slides exactly like a real presentation.
"""
import numpy as np
from manim import *
from manim_slides import Slide


class FirstDeck(Slide):
    def construct(self):
        title = Text("My first deck", font_size=60)
        self.play(Write(title))
        self.next_slide()
        self.play(title.animate.scale(0.5).to_edge(UP))
        body = Text("Click / press \u2192 to advance", font_size=36, color=GREY)
        self.play(FadeIn(body))
        self.next_slide()
        self.play(FadeOut(title), FadeOut(body))


class TwoPoints(Slide):
    def construct(self):
        head = Text("Why animate slides?", font_size=48).to_edge(UP)
        p1 = Text("1. Motion guides attention", font_size=34, color=TEAL)
        p2 = Text("2. Steps appear when YOU decide", font_size=34, color=YELLOW)
        p1.shift(UP * 0.5)
        p2.next_to(p1, DOWN, buff=0.6)
        self.play(Write(head))
        self.next_slide()
        self.play(FadeIn(p1, shift=RIGHT))
        self.next_slide()
        self.play(FadeIn(p2, shift=RIGHT))
        self.next_slide()
        self.play(FadeOut(head), FadeOut(p1), FadeOut(p2))


class LoopingLogo(Slide):
    def construct(self):
        logo = RegularPolygon(6, color=TEAL, fill_opacity=0.4).scale(1.5)
        label = Text("loop=True keeps this spinning", font_size=30).to_edge(DOWN)
        self.play(Create(logo), FadeIn(label))
        self.next_slide(loop=True)
        self.play(Rotate(logo, TAU, run_time=3, rate_func=linear))
        self.next_slide()
        self.play(FadeOut(logo), FadeOut(label))


class MathLecture(Slide):
    def construct(self):
        title = Text("The derivative", font_size=54)
        self.play(Write(title))
        self.next_slide()
        self.play(title.animate.scale(0.55).to_edge(UP))

        definition = MathTex(
            r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}", font_size=54)
        self.play(Write(definition))
        self.next_slide()

        self.play(definition.animate.scale(0.7).shift(UP * 1.6))
        axes = Axes(x_range=[-2.5, 2.5], y_range=[-0.5, 4],
                    x_length=8, y_length=3.2).shift(DOWN * 1.2)
        curve = axes.plot(lambda x: 0.55 * x ** 2 + 0.3, color=YELLOW)
        self.play(Create(axes), Create(curve))
        self.next_slide()

        x = ValueTracker(-1.8)
        tangent = always_redraw(lambda: TangentLine(
            curve, alpha=(x.get_value() + 2.5) / 5, length=3.5, color=RED))
        self.add(tangent)
        self.play(x.animate.set_value(1.8), run_time=3, rate_func=linear)
        self.next_slide()
        self.play(*[FadeOut(m) for m in [title, definition, axes, curve, tangent]])


class ProDeck(Slide):
    """Advanced patterns: canvas (persistent header), wipe & zoom transitions,
    speaker notes on every slide."""
    def construct(self):
        header = Text("Advanced deck patterns", font_size=32).to_edge(UP)
        self.add_to_canvas(header=header)          # survives wipes!
        self.play(FadeIn(header))
        self.next_slide(notes="Canvas keeps the header on every slide.")

        p1 = Text("wipe() slides content sideways", font_size=30, color=TEAL)
        self.play(FadeIn(p1))
        self.next_slide(notes="Demonstrate wipe: old leaves left, new enters right.")

        p2 = Text("like a real slide change", font_size=30, color=YELLOW)
        self.wipe(self.mobjects_without_canvas, p2)
        self.next_slide(notes="Demonstrate zoom: focus attention by scaling in.")

        p3 = Text("zoom() scales the next idea in", font_size=30, color=GREEN)
        self.zoom(self.mobjects_without_canvas, p3)
        self.next_slide(notes="Wrap up — fade everything including canvas.")
        self.play(*[FadeOut(m) for m in self.mobjects])
