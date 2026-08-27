/* Manim Slides Academy — one tiny script, zero dependencies (KaTeX loaded only
 * on pages that use it). Everything works from file:// — no server needed. */
(function () {
  "use strict";

  /* ---------- live LaTeX playgrounds (KaTeX) ---------- */
  function initTexPlaygrounds() {
    var plays = document.querySelectorAll(".tex-play");
    if (!plays.length) return;
    plays.forEach(function (p) {
      var ta = p.querySelector("textarea");
      var out = p.querySelector(".tex-out");
      var display = p.getAttribute("data-display") !== "inline";
      function render() {
        if (!window.katex) { out.textContent = ta.value; return; }
        try {
          katex.render(ta.value, out, {
            displayMode: display,
            throwOnError: true,
            trust: false,
            strict: "ignore",
          });
        } catch (e) {
          out.innerHTML = '<span class="tex-err">' +
            String(e.message || e).replace(/[<>&]/g, function (c) {
              return { "<": "&lt;", ">": "&gt;", "&": "&amp;" }[c];
            }) + "</span>";
        }
      }
      ta.addEventListener("input", render);
      render();
    });
  }
  // KaTeX is loaded with defer before this script; but guard for slow disks
  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", initTexPlaygrounds);
  else initTexPlaygrounds();

  /* ---------- "write this in LaTeX" challenges ---------- */
  function initChallenges() {
    var chs = document.querySelectorAll(".tex-challenge");
    if (!chs.length || !window.katex) { if (chs.length) setTimeout(initChallenges, 150); return; }
    var LSW = "msa-challenges";
    var won = {};
    try { won = JSON.parse(localStorage.getItem(LSW) || "{}"); } catch (_) {}

    chs.forEach(function (ch, idx) {
      var target = ch.getAttribute("data-target");
      var key = ch.getAttribute("data-key") || ("ch" + idx);
      var targetBox = ch.querySelector(".target");
      var ta = ch.querySelector("textarea");
      var out = ch.querySelector(".yours");
      var status = ch.querySelector(".ch-status");
      var hintBtn = ch.querySelector(".ch-hint");
      var revealBtn = ch.querySelector(".ch-reveal");
      var title = ch.querySelector(".ch-q");

      // Compare RENDERED output, not keystrokes — so spacing differences don't
      // matter, but any real difference does. KaTeX embeds the literal source
      // in an <annotation> tag; strip it before comparing.
      function norm(html) {
        return html.replace(/<annotation[^>]*>[\s\S]*?<\/annotation>/g, "");
      }
      var targetHTML = "";
      try {
        var raw = katex.renderToString(target, { displayMode: true, throwOnError: true });
        targetHTML = norm(raw);
        targetBox.innerHTML = raw;
      } catch (e) { targetBox.textContent = target; }

      function celebrate() {
        ch.classList.add("won");
        status.textContent = "✓ Perfect — your LaTeX renders exactly like the goal!";
        status.style.color = "var(--accent2)";
        if (title && !title.querySelector(".badge-won")) {
          var b = document.createElement("span");
          b.className = "badge-won"; b.textContent = "SOLVED";
          title.appendChild(b);
        }
        won[key] = true;
        try { localStorage.setItem(LSW, JSON.stringify(won)); } catch (_) {}
      }

      function check() {
        var v = ta.value.trim();
        if (!v) { out.innerHTML = '<span class="muted small">your rendering appears here…</span>'; status.textContent = ""; return; }
        var html;
        try {
          html = katex.renderToString(v, { displayMode: true, throwOnError: true });
          out.innerHTML = html;
        } catch (e) {
          out.innerHTML = '<span class="tex-err">' + String(e.message || e).replace(/[<>&]/g, function (c) {
            return { "<": "&lt;", ">": "&gt;", "&": "&amp;" }[c];
          }) + "</span>";
          status.textContent = "…keep typing (LaTeX error)";
          status.style.color = "var(--muted)";
          return;
        }
        if (norm(html) === targetHTML) celebrate();
        else if (!ch.classList.contains("won")) {
          status.textContent = "Renders fine — but doesn't match the goal yet. Compare closely!";
          status.style.color = "var(--warn)";
        }
      }
      ta.addEventListener("input", check);

      if (hintBtn) hintBtn.addEventListener("click", function () {
        status.textContent = "💡 " + (ch.getAttribute("data-hint") || "Look at the structure: what is the outermost shape?");
        status.style.color = "var(--accent)";
      });
      if (revealBtn) revealBtn.addEventListener("click", function () {
        ta.value = target; check();
        status.textContent = "Solution shown — now clear the box and try from memory!";
        status.style.color = "var(--muted)";
      });

      if (won[key]) { ta.value = target; check(); }
      else check();
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initChallenges);
  else initChallenges();

  /* ---------- copy buttons on every <pre> ---------- */
  document.querySelectorAll("pre").forEach(function (pre) {
    var btn = document.createElement("button");
    btn.className = "copybtn";
    btn.textContent = "copy";
    btn.addEventListener("click", function () {
      var text = pre.querySelector("code")
        ? pre.querySelector("code").innerText : pre.innerText;
      function done() { btn.textContent = "copied!"; setTimeout(function () { btn.textContent = "copy"; }, 1400); }
      if (navigator.clipboard && navigator.clipboard.writeText)
        navigator.clipboard.writeText(text).then(done, function () { fallback(text); done(); });
      else { fallback(text); done(); }
      function fallback(t) {
        var ta = document.createElement("textarea");
        ta.value = t; document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy"); } catch (_) {}
        document.body.removeChild(ta);
      }
    });
    pre.appendChild(btn);
  });

  /* ---------- videos: click-to-play poster style, replay on click ---------- */
  document.querySelectorAll("video[data-src]").forEach(function (v) {
    // Lazy: real src attached when scrolled near, keeps initial load tiny.
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          v.src = v.getAttribute("data-src");
          io.unobserve(v);
        }
      });
    }, { rootMargin: "400px" });
    io.observe(v);
    v.addEventListener("click", function () {
      if (v.paused) v.play(); else { v.currentTime = 0; v.play(); }
    });
  });

  /* ---------- slide decks: placeholder that swaps to iframe on click ---------- */
  document.querySelectorAll(".deck-launch").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.className = "deck-frame";
      f.src = btn.getAttribute("data-deck");
      f.setAttribute("allow", "autoplay");
      f.setAttribute("loading", "lazy");
      btn.replaceWith(f);
      setTimeout(function () { try { f.contentWindow.focus(); } catch (_) {} }, 400);
    });
  });

  /* ---------- quizzes ---------- */
  document.querySelectorAll(".quiz").forEach(function (q) {
    var verdict = q.querySelector(".verdict");
    q.querySelectorAll("label").forEach(function (lab) {
      lab.addEventListener("click", function () {
        q.querySelectorAll("label").forEach(function (l) { l.classList.remove("right", "wrong"); });
        var ok = lab.hasAttribute("data-right");
        lab.classList.add(ok ? "right" : "wrong");
        if (verdict) {
          verdict.textContent = ok
            ? "✓ Correct — " + (q.getAttribute("data-why") || "nice.")
            : "✗ Not quite — try again.";
          verdict.style.color = ok ? "var(--accent2)" : "var(--danger)";
        }
        if (ok) {
          q.querySelectorAll("label").forEach(function (l) {
            if (l.hasAttribute("data-right")) l.classList.add("right");
          });
        }
      });
    });
  });

  /* ---------- per-topic "done" checkboxes persisted in localStorage ---------- */
  var LS = "msa-progress";
  var store = {};
  try { store = JSON.parse(localStorage.getItem(LS) || "{}"); } catch (_) {}
  document.querySelectorAll(".donebox input").forEach(function (cb) {
    var key = cb.getAttribute("data-key");
    cb.checked = !!store[key];
    cb.addEventListener("change", function () {
      store[key] = cb.checked;
      try { localStorage.setItem(LS, JSON.stringify(store)); } catch (_) {}
    });
  });

  /* ---------- highlight current nav entry ---------- */
  var here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("nav.main a").forEach(function (a) {
    if (a.getAttribute("href") === here) a.classList.add("here");
  });
})();
