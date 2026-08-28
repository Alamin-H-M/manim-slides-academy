from common import page

BODY = """
<div class="hero">
  <h1>Learn <em>LaTeX</em>, <em>Manim</em> &amp; <em>manim-slides</em><br>completely offline</h1>
  <p class="sub">A free course that takes you from zero to animated math presentations —
  with live playgrounds, real rendered animations and click-through slide decks.
  No internet, no account, no installs needed to read it.</p>
  <div class="pillrow">
    <a class="pill" href="https://github.com/Alamin-H-M/manim-slides-academy/releases/latest/download/manim-slides-academy-offline.zip" style="border-color:var(--accent);color:var(--accent)">⬇ Download the whole course (~2 MB ZIP) — use it forever offline</a>
  </div>
  <div class="pillrow">
    <span class="pill">⚡ loads instantly</span>
    <span class="pill">📴 100% offline</span>
    <span class="pill">🧠 minimal brain-drain: one idea at a time</span>
    <span class="pill">🔓 open source · AI-generated</span>
  </div>
</div>


<div id="resume-strip" hidden style="max-width:760px;margin:0 auto 8px;padding:12px 18px;border:1px solid var(--line,#232a36);border-radius:12px;display:flex;align-items:center;gap:14px;flex-wrap:wrap">
  <span style="font-weight:600">▶ Pick up where you left off</span>
  <span id="resume-info" class="muted small"></span>
  <a id="resume-link" class="go" href="latex.html" style="margin-left:auto">Continue →</a>
</div>
<script>
(function(){
  function go(){
    if (!window.msaProgress) return setTimeout(go, 80);
    var p = window.msaProgress();
    if (!p || !p.done || !p.next || !p.next.p) return;
    document.getElementById("resume-strip").hidden = false;
    document.getElementById("resume-info").textContent = p.done + " of " + p.total + " items done (" + p.pct + "%)";
    document.getElementById("resume-link").href = p.next.p + "#" + p.next.k;
  }
  go();
})();
</script>

<div class="cards">
  <div class="card">
    <h3>🛠 Setup (once, ~20 min)</h3>
    <p>Python, Manim, manim-slides, LaTeX and VS Code — the most efficient fully-offline
    toolchain, with an installer-checklist you can tick off.</p>
    <a class="go" href="setup.html">Set up my machine →</a>
  </div>
  <div class="card">
    <h3>1 · LaTeX</h3>
    <p>The language of mathematical writing. <b>10 topics</b>, from first symbol to Maxwell's
    equations — every example is a <b>live playground</b>, every topic ends with a
    “your turn to write” challenge.</p>
    <a class="go" href="latex.html">Start LaTeX →</a>
  </div>
  <div class="card">
    <h3>2 · Manim</h3>
    <p>Programmatic animation. <b>11 topics, 32 real rendered animations</b> — from your first
    circle to camera work, 3D surfaces and production rendering flags.</p>
    <a class="go" href="manim.html">Start Manim →</a>
  </div>
  <div class="card">
    <h3>🔁 Practice</h3>
    <p>49 spaced-repetition flashcards across all three domains. 5 minutes a day —
    the single most evidence-backed way to make it stick.</p>
    <a class="go" href="practice.html">Review today's cards →</a>
  </div>
  <div class="card">
    <h3>📖 Reference</h3>
    <p>Every command from all three tools on one filterable, printable page. Your
    companion after the course.</p>
    <a class="go" href="reference.html">Look something up →</a>
  </div>
  <div class="card">
    <h3>3 · manim-slides</h3>
    <p>Turn animations into presentations. <b>6 topics</b> with click-through interactive decks —
    up to canvas headers, wipe/zoom transitions, speaker notes and every export target.</p>
    <a class="go" href="slides.html">Start manim-slides →</a>
  </div>
</div>

<h2>How this course keeps your brain fresh</h2>
<p class="lead">Learning three tools at once is usually overwhelming. This course is engineered against that:</p>
<table>
  <tr><th>Principle</th><th>How it's applied here</th></tr>
  <tr><td><b>One idea per topic</b></td><td>Each topic teaches exactly one concept. No topic depends on anything you haven't seen yet.</td></tr>
  <tr><td><b>2 easy → 2 harder</b></td><td>Every topic has two gentle examples, then two that stretch the same idea further. You always know which is which — look for the <span style="color:#4ade80">EASY</span> / <span style="color:#fbbf24">LEVEL UP</span> badge.</td></tr>
  <tr><td><b>Do, don't just read</b></td><td>LaTeX examples are editable live. Manim examples show the real video. Slide examples are decks you click through yourself.</td></tr>
  <tr><td><b>Test yourself</b></td><td>Every chapter ends with self-check exercises: quizzes that respond instantly, and open problems with hidden solutions.</td></tr>
  <tr><td><b>Track progress</b></td><td>The HUD on every page: XP, level, daily goal, 🔥 streak and overall course % — all stored only in your browser.</td></tr>
</table>


<h2>🎮 XP, levels, streaks — the game layer</h2>
<p class="lead">Everything you do earns (or costs) XP, stored only in your browser. The bar at the very
top of every page is your scoreboard.</p>
<table>
  <tr><th>Action</th><th>XP</th></tr>
  <tr><td>Finish a topic — <b>automatic</b>: read to its end and clear its exercises</td><td style="color:var(--accent2)"><b>+15 to +25</b></td></tr>
  <tr><td>Solve a “write this in LaTeX” challenge</td><td style="color:var(--accent2)"><b>+10</b></td></tr>
  <tr><td>Answer a quiz correctly (first time)</td><td style="color:var(--accent2)"><b>+5</b></td></tr>
  <tr><td>Remember a practice flashcard</td><td style="color:var(--accent2)"><b>+3</b> (every day — reviewing IS the work)</td></tr>
  <tr><td>Wrong quiz answer</td><td style="color:var(--danger)"><b>−2</b></td></tr>
  <tr><td>Forget a flashcard</td><td style="color:var(--danger)"><b>−1</b></td></tr>
  <tr><td>Give up on a challenge (“show solution”)</td><td style="color:var(--danger)"><b>−5</b></td></tr>
</table>
<p><b>🎯 Daily minimum: 30 XP.</b> Hit it and the day counts toward your <b>🔥 streak</b> — miss a day
and the streak resets. 30 XP is deliberately small: ten flashcards, or one topic — about 10 minutes.
Consistency beats bingeing; that is the entire science of spaced practice in one rule.</p>
<p><b>Levels</b> climb from <i>Newcomer</i> through <i>Formula Wrangler</i> and <i>Scene Director</i> to
<i>Academy Legend</i> (1400 XP). The green bar shows your <b>course progress %</b> — every trackable
item across every chapter, challenge and quiz. 80% completed means exactly that.</p>

<p class="muted small"><b>Backup:</b> progress lives only in this browser.
<button id="msa-export" class="copybtn" style="position:static">export progress</button>
<label class="copybtn" style="position:static;cursor:pointer">import progress<input id="msa-import" type="file" accept=".json" style="display:none"></label>
— export before clearing browser data or switching machines; import restores XP, streak, ticks, challenges and flashcards.</p>
<p class="muted small">Anti-cheat, sort of: each topic/challenge/quiz pays out once ever, and topics complete
themselves — only when you’ve actually scrolled to the end <i>and</i> solved everything inside, so there’s
nothing to tick (or to cheat). Flashcard XP repeats daily because re-reviewing genuinely is the work. Everything lives in
localStorage — use the export button above so your legend survives a browser reset.</p>
<h2>The path — a complete learning system</h2>
<p class="lead">This is not just reading material. It's a full loop based on how memory actually works:
<b>guess first</b> (pretests) → <b>learn by doing</b> (chapters) →
<b>keep it forever</b> (spaced practice) → <b>look things up</b> (reference).</p>
<pre><code>  Setup ──▶ LaTeX ──▶ Manim ──▶ manim-slides
 ~20 min    ~4 h      ~6 h        ~2.5 h
                │
   🔁 Practice (5 min/day, spaced cards) ──▶ 📖 Reference (forever)</code></pre>

<div class="note"><b>Honesty note</b>
This entire course was generated by an AI and packaged as open source (MIT). Every code
example was actually executed and every animation on these pages is the real render of the
code beside it — but treat it like any community resource: if something looks wrong,
<a href="https://github.com/Alamin-H-M/manim-slides-academy">open an issue or a pull request</a>. Contributions welcome!</div>
"""

def render():
    return page("index.html", "Home", BODY, desc='Learn LaTeX, Manim and manim-slides completely free and offline: live LaTeX playgrounds, 24 rendered Manim animation examples with source code, interactive slide decks, quizzes and exercises. Open-source beginner course.')