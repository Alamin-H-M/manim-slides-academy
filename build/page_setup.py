from common import page, pre

BODY = """
<h1>Setup: the most efficient offline toolchain</h1>
<p class="lead">Do this once (~20 minutes with a normal connection, then never again —
everything below works with the network cable unplugged). Windows commands shown;
macOS/Linux equivalents in each step.</p>

<div class="toc"><b>On this page</b>
<a href="#python">1 Python</a><a href="#manim">2 Manim + manim-slides</a>
<a href="#latex">3 LaTeX</a><a href="#vscode">4 VS Code</a>
<a href="#extension">5 One-keystroke workflow</a><a href="#verify">6 Verify everything</a>
<a href="#offline">7 Going fully offline</a>
</div>

<h2 id="python"><span class="tno">1</span>Python 3.9+</h2>
<p>Download from <code>python.org</code> → run the installer → <b>tick "Add python.exe to PATH"</b>
(the single most common setup mistake is skipping this box).</p>
""" + pre("""# check it worked (any terminal):
python --version        # Windows
python3 --version       # macOS / Linux""", "shell") + """
<div class="tip"><b>Tip</b> On Windows, if <code>python</code> opens the Microsoft Store instead of Python,
disable the alias: Settings → Apps → Advanced app settings → App execution aliases → turn off both python entries.</div>

<h2 id="manim"><span class="tno">2</span>Manim + manim-slides (one command)</h2>
""" + pre("""pip install manim "manim-slides[pyside6]"
# pyside6 gives you the native presenter window (GUI) — worth having.""", "shell") + """
<p>That's the entire animation stack. <code>manim-slides</code> pulls in everything it needs,
including <code>python-pptx</code> for PowerPoint export.</p>
<div class="note"><b>Which quality flag?</b> While learning use <code>-ql</code> (480p, fast).
Only your final render needs <code>-qh</code> (1080p60). Manim caches unchanged animations,
so re-renders after small edits are much faster than the first one.</div>

<h2 id="latex"><span class="tno">3</span>LaTeX (two valid strategies)</h2>
<table>
<tr><th></th><th>Strategy A — no install (start today)</th><th>Strategy B — full install (recommended eventually)</th></tr>
<tr><td><b>What</b></td><td>Use Manim's <code>Text()</code> and this site's live playgrounds; skip a LaTeX distribution entirely.</td><td>Install <b>MiKTeX</b> (Windows) or <b>TeX Live</b> / <b>MacTeX</b>.</td></tr>
<tr><td><b>Gets you</b></td><td>Everything except Manim's <code>MathTex/Tex</code> objects.</td><td>Beautiful math inside animations: <code>MathTex(r"e^{i\\pi}+1=0")</code>.</td></tr>
<tr><td><b>Size</b></td><td>0 MB</td><td>MiKTeX basic ≈ 250 MB (auto-installs packages on first use)</td></tr>
</table>
<div class="tip"><b>Efficient offline choice</b> MiKTeX with "install missing packages on-the-fly = yes",
then render one <code>MathTex</code> scene while still online — the handful of packages Manim needs get cached
and you're offline-ready forever.</div>

<h2 id="vscode"><span class="tno">4</span>VS Code</h2>
<p>Install VS Code, then just two extensions (more = slower, and defeats the lightweight goal):</p>
<table>
<tr><th>Extension</th><th>Why</th></tr>
<tr><td><b>Python</b> (Microsoft)</td><td>IntelliSense + running scripts. Nothing else needed for Manim.</td></tr>
<tr><td><b>Manim Slides Preview</b> (.vsix, offline)</td><td>The ▶-button → auto-preview workflow used in this course; installs from a local file, no marketplace/internet.</td></tr>
</table>
""" + pre("""# install a .vsix without internet:
code --install-extension manim-slides-preview-1.7.0.vsix""", "shell") + """

<h2 id="extension"><span class="tno">5</span>The one-keystroke workflow</h2>
<p>With the extension installed, the whole edit-render-preview loop collapses to:</p>
<table>
<tr><th>You do</th><th>What happens</th></tr>
<tr><td>Open your <code>.py</code>, press ▶</td><td>Scene rendered → converted to interactive HTML → opens in your browser (or VS Code tab, or the native GUI window — your pick)</td></tr>
<tr><td>Edit, press <kbd>Ctrl</kbd>+<kbd>S</kbd></td><td>Only <em>changed</em> animations re-render (cache), preview refreshes itself, staying on your current slide</td></tr>
<tr><td>Optional: enable <code>pptxExport</code></td><td>A .pptx of your deck is silently kept up to date in the background</td></tr>
</table>
<p>No terminal commands, no manual refreshing — your brain stays on the math, not the tooling.</p>

<h2 id="verify"><span class="tno">6</span>Verify everything (60 seconds)</h2>
""" + pre("""manim --version          # e.g. Manim Community v0.19.x
manim-slides --version   # e.g. 5.x
python -c "import pptx; print('pptx OK')"
latex --version          # only if you chose Strategy B""", "shell") + """
<p>Then render your very first animation:</p>
""" + pre('''# save as first.py, then:  manim render -ql -p first.py Hello
from manim import *

class Hello(Scene):
    def construct(self):
        self.play(Write(Text("It works!")))''') + """
<p><code>-p</code> means "play when done" — a video window should pop up. If it does, you're ready for
<a href="latex.html">Chapter 1</a>.</p>

<h2 id="offline"><span class="tno">7</span>Going fully offline</h2>
<ul>
<li><b>This site</b> is already offline — you're reading files from your own disk.</li>
<li><b>Manim &amp; manim-slides</b> never phone home. Rendering is fully local.</li>
<li><b>Slide exports:</b> always convert with <code>--offline</code> (bundles Reveal.js beside the HTML) so
presentations work in a lecture hall with no WiFi: <code>manim-slides convert --to html --offline MyScene out.html</code></li>
<li><b>pip on an air-gapped machine:</b> on a connected machine run
<code>pip download manim "manim-slides[pyside6]" -d wheelhouse/</code>, copy the folder, then
<code>pip install --no-index --find-links wheelhouse manim "manim-slides[pyside6]"</code>.</li>
</ul>

<div class="pager">
  <a href="index.html"><span class="dir">← Back</span>Home</a>
  <a href="latex.html" class="right"><span class="dir">Next chapter →</span>1 · LaTeX</a>
</div>
"""

def render():
    return page("setup.html", "Setup", BODY)
