from common import page

REF = [
    ("LaTeX — structure", [
        (r"\frac{a}{b}", "fraction"),
        (r"x^{2}", "superscript / power"),
        (r"x_{i}", "subscript / index"),
        (r"\sqrt{x} \quad \sqrt[3]{x}", "square root · nth root"),
        (r"\sum_{i=1}^{n} \quad \prod_{i=1}^{n}", "sum · product with limits"),
        (r"\int_a^b f(x)\,dx", "integral (\\, = thin space)"),
        (r"\lim_{x \to 0}", "limit"),
        (r"\left( \dots \right)", "auto-growing brackets"),
        (r"\begin{aligned} a &= b \\ &= c \end{aligned}", "aligned equations (& = align point)"),
        (r"\begin{cases} x & x>0 \\ 0 & x \le 0 \end{cases}", "piecewise"),
        (r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}", "matrix (b/v-matrix = [ ] / | |)"),
        (r"\text{words here}", "normal text inside math"),
    ]),
    ("LaTeX — symbols", [
        (r"\alpha \beta \gamma \delta \theta \lambda \pi \sigma \omega", "common Greek (lowercase)"),
        (r"\Gamma \Delta \Theta \Lambda \Pi \Sigma \Omega", "capital Greek (capitalize the command)"),
        (r"\le \ge \ne \approx \equiv \sim", "comparisons"),
        (r"\to \Rightarrow \Leftrightarrow \mapsto", "arrows"),
        (r"\in \notin \subset \cup \cap \emptyset", "sets"),
        (r"\forall \exists \neg \land \lor", "logic"),
        (r"\infty \partial \nabla \pm \cdot \times \div", "misc"),
        (r"\mathbb{R} \mathbb{Z} \mathbb{N} \mathcal{L} \mathbf{v}", "letter styles"),
        (r"\cdots \vdots \ddots \dots", "dots"),
        (r"\hat{x} \bar{x} \vec{v} \tilde{n} \dot{x}", "accents"),
    ]),
    ("LaTeX — decorations & calculus", [
        (r"\vec{v} \; \hat{x} \; \bar{y} \; \dot{x} \; \ddot{x}", "accents: vector · hat · bar · derivatives"),
        (r"\overline{x+y} \; \widehat{AB} \; \overrightarrow{PQ}", "wide accents (stretch over groups)"),
        (r"\underbrace{...}_{label} \; \overbrace{...}^{label}", "labeled braces under / over"),
        (r"\boxed{x = 2}", "box the final answer"),
        (r"f'(x) \; \frac{df}{dx} \; \frac{\partial f}{\partial x}", "derivative notations"),
        (r"\iint \; \iiint \; \oint", "double · triple · closed-loop integrals"),
        (r"\left. \frac{x^3}{3} \right|_0^1", "evaluation bar"),
        (r"\substack{a \\ b}", "stack lines under a sum"),
        (r"\! \, \; \quad \qquad", "spaces: negative · thin · medium · wide · double"),
        (r"\textcolor{orange}{...}", "color part of a formula"),
        (r"\displaystyle \; \textstyle", "force big / compact rendering"),
        (r"\operatorname{lcm}", "upright custom operator"),
    ]),
    ("Manim — mobjects", [
        ("Circle(radius=1, color=BLUE, fill_opacity=0.5)", "fill_opacity=0 by default!"),
        ("Square(side_length=2) / Rectangle(width=4, height=2)", "quads"),
        ("Line(A, B) / Arrow(A, B) / Dot(point)", "primitives"),
        ("Polygon(p1, p2, p3, ...)", "any shape from points"),
        ("Text(\"hi\", font_size=48, gradient=(BLUE, TEAL))", "plain text (no LaTeX needed)"),
        ("MathTex(r\"e^{i\\pi}+1=0\")", "LaTeX math — always r\"...\""),
        ("Axes(x_range=[-4,4], y_range=[-2,2])", "coordinate system"),
        ("axes.plot(lambda x: np.sin(x), color=YELLOW)", "function graph"),
        ("axes.c2p(x, y)", "math coords → screen point"),
        ("VGroup(a, b, c).arrange(RIGHT, buff=0.5)", "group + lay out"),
        ("group.arrange_in_grid(rows=3, cols=3)", "grid layout"),
        ("DecimalNumber(0) / Integer(0)", "animatable numbers"),
    ]),
    ("Manim — animations", [
        ("self.play(Create(shape))", "draw outline"),
        ("self.play(Write(text))", "handwriting reveal"),
        ("self.play(FadeIn(m, shift=UP), FadeOut(n))", "fades (optionally directional)"),
        ("self.play(GrowFromCenter(m))", "scale-in"),
        ("self.play(Transform(a, b))", "morph a into b's shape"),
        ("self.play(TransformMatchingTex(eq1, eq2))", "smart equation morph"),
        ("self.play(m.animate.shift(RIGHT).set_color(RED))", ".animate = animate any method chain"),
        ("self.play(LaggedStart(*anims, lag_ratio=0.1))", "staggered start"),
        ("self.play(anim, run_time=3, rate_func=linear)", "duration + speed curve"),
        ("rate_functions: linear, smooth, there_and_back, ease_in_quad", "common curves"),
        ("self.play(Indicate(m)) / Circumscribe(m)", "highlight attention"),
        ("self.wait(1)", "hold a frame"),
    ]),
    ("Manim — positioning", [
        ("m.shift(UP * 2 + RIGHT)", "move by offset"),
        ("m.move_to(point_or_mobject)", "move to absolute position"),
        ("m.next_to(other, DOWN, buff=0.5)", "relative placement"),
        ("m.to_edge(UP) / m.to_corner(UR)", "screen edges"),
        ("m.align_to(other, LEFT)", "align edges"),
        ("m.scale(2) / m.rotate(PI/4) / m.flip()", "transforms"),
        ("m.get_center() / get_top() / get_corner(UR)", "query points"),
        ("constants: UP DOWN LEFT RIGHT UL UR DL DR ORIGIN", "unit vectors"),
        ("screen ≈ 14.2 × 8 units, origin at center", "the canvas"),
    ]),
    ("Manim — updaters", [
        ("t = ValueTracker(0)", "animatable number"),
        ("self.play(t.animate.set_value(10))", "drive it"),
        ("m.add_updater(lambda m: m.set_value(t.get_value()))", "react every frame"),
        ("m.add_updater(lambda m, dt: m.rotate(dt))", "dt-updater: runs on wall time (even in wait)"),
        ("line = always_redraw(lambda: Line(a.get_center(), b.get_center()))", "rebuild each frame"),
        ("m.clear_updaters()", "stop reacting"),
    ]),
    ("Manim — camera, 3D & timing", [
        ("class S(MovingCameraScene):", "unlocks camera moves"),
        ("self.camera.frame.animate.scale(0.4).move_to(spot)", "zoom + pan"),
        ("self.camera.frame.save_state() / Restore(...)", "zoom back out"),
        ("self.camera.frame.add_updater(lambda f: f.move_to(obj))", "follow-cam"),
        ("class S(ThreeDScene):", "unlocks 3D"),
        ("self.set_camera_orientation(phi=70*DEGREES, theta=-45*DEGREES)", "tilt & spin the 3D camera"),
        ("self.begin_ambient_camera_rotation(rate=0.3)", "slow orbit while you talk"),
        ("self.add_fixed_in_frame_mobjects(title)", "HUD text that ignores 3D camera"),
        ("ThreeDAxes() · Sphere() · Surface(lambda u,v: ...)", "3D building blocks"),
        ("LaggedStart(*anims, lag_ratio=0.15)", "staggered entrances"),
        ("rate_func=linear / smooth / there_and_back / rush_into", "movement personalities"),
        ("TransformMatchingTex(eq1, eq2)", "morph equations, matching terms fly"),
        ("Brace(part, DOWN).get_text(\"label\")", "point at part of a formula"),
        ("SurroundingRectangle(part) + Indicate(part)", "spotlight a term"),
    ]),
    ("manim-slides", [
        ("self.add_to_canvas(header=h)", "pin mobjects across transitions"),
        ("self.mobjects_without_canvas", "everything except the canvas"),
        ("self.wipe(old, new) · self.zoom(old, new)", "slide transitions"),
        ("self.next_slide(notes=\"...\")", "speaker notes (press S in HTML deck)"),
        ("from manim_slides import Slide", "the import"),
        ("class Talk(Slide):", "Slide instead of Scene"),
        ("self.next_slide()", "pause point"),
        ("self.next_slide(loop=True)", "loop this segment until advance"),
        ("self.play(*[FadeOut(m) for m in self.mobjects])", "wipe between sections"),
        ("manim-slides render talk.py Talk", "render"),
        ("manim-slides present Talk", "native GUI presenter"),
        ("manim-slides convert --to html --offline Talk out.html", "offline HTML deck"),
        ("manim-slides convert --to pptx Talk out.pptx", "PowerPoint export"),
        ("hotkeys: → next · ← prev · F fullscreen · R replay · Q quit", "in the GUI"),
    ]),
    ("Terminal recipes", [
        ("manim render -ql -p file.py Scene", "fast 480p preview, play when done"),
        ("manim render -qh file.py Scene", "final 1080p60"),
        ("-ql / -qm / -qh / -qp / -qk", "480p15 / 720p30 / 1080p60 / 1440p60 / 4K"),
        ("pip install manim \"manim-slides[pyside6]\"", "the whole stack"),
        ("pip install -U manim manim-slides", "update"),
        ("manim --version && manim-slides --version", "health check"),
    ]),
]


def render():
    import html as h
    sections = []
    for title, rows in REF:
        trs = "".join(
            f'<tr><td><code>{h.escape(code)}</code></td><td class="muted">{h.escape(what)}</td></tr>'
            for code, what in rows)
        key = title.split(" — ")[0].lower() + "-" + (title.split(" — ")[1] if " — " in title else "x")
        key = key.replace(" ", "-").lower()
        sections.append(f'<h2 id="{h.escape(key)}">{h.escape(title)}</h2>'
                        f'<table class="ref-table">{trs}</table>')
    body = """
<h1>📖 Reference — everything on one page</h1>
<p class="lead">The lookup companion for daily work: every command taught in this course
(plus the ones you'll want next week), organized and filterable. <kbd>Ctrl</kbd>+<kbd>F</kbd> works too —
it's one page on purpose. Printable: this page strips its chrome when printed.</p>

<p><input id="ref-filter" type="search" placeholder="filter… e.g. 'matrix', 'fade', 'updater', 'pptx'"
   style="width:100%;padding:12px 14px;border-radius:8px;border:1px solid var(--border);
          background:var(--bg2);color:var(--fg);font-size:1rem;outline:none"></p>
<p class="muted small" id="ref-count"></p>
""" + "".join(sections) + """
<script>
(function(){
var inp = document.getElementById("ref-filter");
var count = document.getElementById("ref-count");
var rows = [].slice.call(document.querySelectorAll(".ref-table tr"));
var heads = [].slice.call(document.querySelectorAll("h2"));
function apply() {
  var q = inp.value.trim().toLowerCase();
  var shown = 0;
  rows.forEach(function (r) {
    var hit = !q || r.textContent.toLowerCase().indexOf(q) >= 0;
    r.style.display = hit ? "" : "none";
    if (hit) shown++;
  });
  heads.forEach(function (hd) {
    var t = hd.nextElementSibling;
    if (t && t.classList.contains("ref-table")) {
      var any = [].slice.call(t.rows).some(function (r) { return r.style.display !== "none"; });
      hd.style.display = any ? "" : "none";
      t.style.display = any ? "" : "none";
    }
  });
  count.textContent = q ? shown + " matching entries" : rows.length + " entries";
}
inp.addEventListener("input", apply);
apply();
})();
</script>

<div class="pager">
  <a href="capstone.html"><span class="dir">← Build</span>🏆 Capstone</a>
  <a href="index.html" class="right"><span class="dir">Start</span>Home</a>
</div>
"""
    return page("reference.html", "Reference", body,
                desc="One-page searchable reference for LaTeX math commands, Manim mobjects/animations/positioning/updaters, and every manim-slides command — filterable and printable.")
