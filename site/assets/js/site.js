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
        window.dispatchEvent(new CustomEvent("msa-xp", { detail: { delta: 10, key: key } }));
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
        if (!ch.classList.contains("won") && !won[key])
          window.dispatchEvent(new CustomEvent("msa-xp", { detail: { delta: -5, key: "rev-" + key, label: "gave up" } }));
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

  /* ---------- quizzes (right = +5 XP once, wrong = -2 XP) ---------- */
  document.querySelectorAll(".quiz").forEach(function (q) {
    var verdict = q.querySelector(".verdict");
    var qkey = q.getAttribute("data-key") || "";
    q.querySelectorAll("label").forEach(function (lab) {
      lab.addEventListener("click", function () {
        var wasWrong = lab.classList.contains("wrong");
        q.querySelectorAll("label").forEach(function (l) { l.classList.remove("right", "wrong"); });
        var ok = lab.hasAttribute("data-right");
        lab.classList.add(ok ? "right" : "wrong");
        if (verdict) {
          verdict.textContent = ok
            ? "✓ Correct — " + (q.getAttribute("data-why") || "nice.")
            : "✗ Not quite (−2 XP) — think again.";
          verdict.style.color = ok ? "var(--accent2)" : "var(--danger)";
        }
        if (ok) {
          q.querySelectorAll("label").forEach(function (l) {
            if (l.hasAttribute("data-right")) l.classList.add("right");
          });
          if (qkey) window.dispatchEvent(new CustomEvent("msa-xp", { detail: { delta: 5, key: qkey } }));
        } else if (!wasWrong) {
          window.dispatchEvent(new CustomEvent("msa-xp", { detail: { delta: -2 } }));
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
    var xp = parseInt(cb.getAttribute("data-xp") || "15", 10);
    cb.checked = !!store[key];
    cb.addEventListener("change", function () {
      store[key] = cb.checked;
      try { localStorage.setItem(LS, JSON.stringify(store)); } catch (_) {}
      window.dispatchEvent(new CustomEvent("msa-xp", { detail: { delta: cb.checked ? xp : -xp } }));
    });
  });

  /* ---------- highlight current nav entry ---------- */
  var here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("nav.main a").forEach(function (a) {
    if (a.getAttribute("href") === here) a.classList.add("here");
  });

  /* ================================================================
   * GAME ENGINE — XP, levels, daily goal, streak, course progress %.
   * One localStorage key ("msa-game"), zero network, zero dependencies.
   * ================================================================ */
  var G_LS = "msa-game";
  var LEVELS = [
    [0, "Newcomer"], [50, "Apprentice"], [125, "Tinkerer"], [225, "Animator"],
    [350, "Formula Wrangler"], [500, "Scene Director"], [675, "Slide Smith"],
    [875, "Presenter"], [1100, "Motion Master"], [1400, "Academy Legend"]];
  var DAILY_GOAL = 30;

  function gload() {
    var g = { xp: 0, aw: {}, days: {} };
    try {
      var raw = JSON.parse(localStorage.getItem(G_LS) || "{}");
      if (typeof raw.xp === "number") g.xp = raw.xp;
      if (raw.aw) g.aw = raw.aw;
      if (raw.days) g.days = raw.days;
    } catch (_) {}
    return g;
  }
  function gsave(g) { try { localStorage.setItem(G_LS, JSON.stringify(g)); } catch (_) {} }
  function today() {
    var d = new Date();
    return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2);
  }
  function dayBefore(iso) {
    var p = iso.split("-");
    var d = new Date(+p[0], +p[1] - 1, +p[2]);
    d.setDate(d.getDate() - 1);
    return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2);
  }
  function levelOf(xp) {
    var i = 0;
    while (i + 1 < LEVELS.length && xp >= LEVELS[i + 1][0]) i++;
    return i;
  }
  function streakOf(g) {
    // consecutive days (ending today or yesterday) that met the daily goal
    var n = 0, d = today();
    if ((g.days[d] || 0) < DAILY_GOAL) d = dayBefore(d); // today not done yet? streak still alive from yesterday
    while ((g.days[d] || 0) >= DAILY_GOAL) { n++; d = dayBefore(d); }
    return n;
  }

  /* course progress % from the page-embedded registry + the stores */
  function courseProgress() {
    var reg = window.MSA_COURSE || [];
    if (!reg.length) return null;
    var boxes = {}, chs = {};
    try { boxes = JSON.parse(localStorage.getItem("msa-progress") || "{}"); } catch (_) {}
    try { chs = JSON.parse(localStorage.getItem("msa-challenges") || "{}"); } catch (_) {}
    var g = gload();
    var done = 0;
    reg.forEach(function (it) {
      if (it.t === "box" && boxes[it.k]) done++;
      else if (it.t === "ch" && chs[it.k]) done++;
      else if (it.t === "qz" && g.aw[it.k]) done++;
    });
    return { done: done, total: reg.length, pct: Math.round(100 * done / reg.length) };
  }

  /* ---------- HUD ---------- */
  var hud = document.getElementById("game-hud");
  function renderHUD() {
    if (!hud) return;
    var g = gload();
    var li = levelOf(g.xp);
    var cur = LEVELS[li][0];
    var nxt = li + 1 < LEVELS.length ? LEVELS[li + 1][0] : null;
    var lvlPct = nxt === null ? 100 : Math.round(100 * (g.xp - cur) / (nxt - cur));
    var tXP = g.days[today()] || 0;
    var goalPct = Math.min(100, Math.round(100 * tXP / DAILY_GOAL));
    var st = streakOf(g);
    var cp = courseProgress();
    hud.hidden = false;
    hud.innerHTML =
      '<div class="hud-inner">' +
      '<span class="hud-lvl" title="' + g.xp + ' XP total">Lv ' + (li + 1) + " · " + LEVELS[li][1] + "</span>" +
      '<span class="hud-bar" title="' + (nxt === null ? "max level!" : (nxt - g.xp) + " XP to level " + (li + 2)) + '">' +
      '<i style="width:' + lvlPct + '%"></i><b>' + g.xp + " XP</b></span>" +
      '<span class="hud-goal ' + (tXP >= DAILY_GOAL ? "met" : "") + '" title="daily minimum: ' + DAILY_GOAL + ' XP">' +
      "🎯 today " + tXP + "/" + DAILY_GOAL +
      '<span class="hud-mini"><i style="width:' + goalPct + '%"></i></span></span>' +
      '<span class="hud-streak" title="days in a row you hit the daily goal">🔥 ' + st + "</span>" +
      (cp ? '<span class="hud-bar course" title="' + cp.done + " of " + cp.total + ' items completed">' +
        '<i style="width:' + cp.pct + '%"></i><b>' + cp.pct + "% course</b></span>" : "") +
      "</div>";
  }

  function toast(delta, label) {
    var t = document.createElement("div");
    t.className = "xp-toast " + (delta >= 0 ? "gain" : "lose");
    t.textContent = (delta >= 0 ? "+" : "") + delta + " XP" + (label ? " · " + label : "");
    document.body.appendChild(t);
    setTimeout(function () { t.classList.add("show"); }, 10);
    setTimeout(function () { t.classList.remove("show"); }, 1800);
    setTimeout(function () { t.remove(); }, 2300);
  }

  window.addEventListener("msa-xp", function (ev) {
    var d = ev.detail || {};
    var delta = d.delta | 0;
    if (!delta) return;
    var g = gload();
    // keyed positive awards are one-time (stops farming by re-doing the same item)
    if (d.key && delta > 0) {
      if (g.aw[d.key]) return;
      g.aw[d.key] = 1;
    }
    if (d.key && delta < 0 && g.aw[d.key]) return; // penalty already taken for this key
    if (d.key && delta < 0) g.aw[d.key] = 1;
    g.xp = Math.max(0, g.xp + delta);
    var t = today();
    g.days[t] = Math.max(0, (g.days[t] || 0) + delta);
    // prune day log > 400 entries (years of use) to stay tiny
    var keys = Object.keys(g.days);
    if (keys.length > 400) keys.sort().slice(0, keys.length - 400).forEach(function (k) { delete g.days[k]; });
    gsave(g);
    var before = levelOf(Math.max(0, g.xp - delta)), after = levelOf(g.xp);
    renderHUD();
    toast(delta, d.label);
    if (after > before) {
      var lt = document.createElement("div");
      lt.className = "xp-toast gain lvlup show";
      lt.textContent = "⬆ LEVEL UP! You are now Lv " + (after + 1) + " — " + LEVELS[after][1];
      document.body.appendChild(lt);
      setTimeout(function () { lt.classList.remove("show"); }, 3500);
      setTimeout(function () { lt.remove(); }, 4000);
    }
  });

  /* checkbox / challenge state changed in another tab → refresh HUD */
  window.addEventListener("storage", function (e) {
    if (e.key === G_LS || e.key === "msa-progress" || e.key === "msa-challenges") renderHUD();
  });

  renderHUD();
})();
