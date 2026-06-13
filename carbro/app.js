/* ═══════════════════════════════════════════════════════════
   CarBro – App-Logik
   · Hash-Routing (SPA)   · Checklisten mit localStorage
   · Theme-Umschaltung    · Fortschritts-Balken   · Service-Worker
   ═══════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  var STORE = "carbro:";
  var ROUTES = ["home", "kauf", "service", "guide-oel", "guide-reifen", "guide-winter", "unfall", "wissen"];
  var NAV_FOR = { home: "home", kauf: "kauf", service: "service", "guide-oel": "service", "guide-reifen": "service", "guide-winter": "service", unfall: "service", wissen: "wissen" };

  /* ── kleine Helfer ── */
  function $(s, c) { return (c || document).querySelector(s); }
  function $all(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function load(key, def) { try { var v = localStorage.getItem(STORE + key); return v == null ? def : JSON.parse(v); } catch (e) { return def; } }
  function save(key, val) { try { localStorage.setItem(STORE + key, JSON.stringify(val)); } catch (e) {} }
  function vibrate(ms) { if (navigator.vibrate) { try { navigator.vibrate(ms); } catch (e) {} } }

  var toastEl = $("#toast"), toastTimer;
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg;
    toastEl.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove("show"); }, 2200);
  }

  /* ─────────── Routing ─────────── */
  function currentRoute() {
    var h = (location.hash || "#home").replace(/^#/, "");
    return ROUTES.indexOf(h) !== -1 ? h : "home";
  }
  function go(route) {
    if (location.hash.replace(/^#/, "") === route) { render(route); }
    else { location.hash = route; }
  }
  function render(route) {
    $all(".view").forEach(function (v) { v.classList.remove("active"); });
    var view = $("#view-" + route);
    if (view) view.classList.add("active");
    var navKey = NAV_FOR[route] || "home";
    $all(".nav-btn").forEach(function (b) { b.classList.toggle("active", b.getAttribute("data-go") === navKey); });
    closeDrawer();
    window.scrollTo({ top: 0, behavior: "instant" in window ? "instant" : "auto" });
  }
  window.addEventListener("hashchange", function () { render(currentRoute()); });

  /* ─────────── Checklisten ─────────── */
  function clKey(id) { return "cl:" + id; }

  function initChecklists() {
    $all("[data-checklist]").forEach(function (cont) {
      var id = cont.getAttribute("data-checklist");
      var inputs = $all('input[type="checkbox"]', cont);
      var stateArr = load(clKey(id), []);
      inputs.forEach(function (inp, i) {
        inp.checked = !!stateArr[i];
        inp.addEventListener("change", function () {
          var arr = load(clKey(id), []);
          arr[i] = inp.checked;
          save(clKey(id), arr);
          if (inp.checked) vibrate(40);
          updateProgress(id);
        });
      });
      updateProgress(id);
    });
  }

  /* speichert das ursprüngliche Label-Format je Element */
  var labelFmt = new WeakMap();
  function progressLabels(id) { return $all('[data-progress-label="' + id + '"]'); }

  function countChecklist(id) {
    var cont = $('[data-checklist="' + id + '"]');
    if (!cont) {
      // Fortschritt kann auch ohne sichtbare Liste benötigt werden (z.B. Home-Kachel)
      var arr = load(clKey(id), []);
      var checked = arr.filter(Boolean).length;
      // Gesamtzahl ist unbekannt -> aus gespeichertem Array ableiten, sonst aus DOM später
      return { checked: checked, total: arr.length };
    }
    var inputs = $all('input[type="checkbox"]', cont);
    var checked = inputs.filter(function (i) { return i.checked; }).length;
    return { checked: checked, total: inputs.length };
  }

  function updateProgress(id) {
    var c = countChecklist(id);
    var pct = c.total ? Math.round((c.checked / c.total) * 100) : 0;

    $all('[data-progress="' + id + '"]').forEach(function (bar) {
      bar.style.width = pct + "%";
    });
    progressLabels(id).forEach(function (lbl) {
      if (!labelFmt.has(lbl)) {
        labelFmt.set(lbl, /Schritte/i.test(lbl.textContent) ? "steps" : "pct");
      }
      var fmt = labelFmt.get(lbl);
      lbl.textContent = fmt === "steps"
        ? c.checked + "/" + c.total + " Schritte erledigt"
        : pct + "% erledigt";
    });
  }

  /* Home-Kachel braucht Gesamtzahl der Öl-Liste, auch wenn Liste nicht im DOM sichtbar.
     -> wir kennen die feste Länge (3). Fallback-Map: */
  var KNOWN_TOTALS = { "cl-oel": 3 };
  // countChecklist überschreiben, falls Liste nicht im DOM, aber Total bekannt
  var _origCount = countChecklist;
  countChecklist = function (id) {
    var r = _origCount(id);
    if ((!r.total || r.total === 0) && KNOWN_TOTALS[id]) {
      var arr = load(clKey(id), []);
      return { checked: arr.filter(Boolean).length, total: KNOWN_TOTALS[id] };
    }
    return r;
  };

  function resetChecklist(id) {
    save(clKey(id), []);
    var cont = $('[data-checklist="' + id + '"]');
    if (cont) $all('input[type="checkbox"]', cont).forEach(function (i) { i.checked = false; });
    updateProgress(id);
    toast("Checkliste zurückgesetzt");
    vibrate(30);
  }

  /* ─────────── Theme ─────────── */
  var META_THEME = { marine: "#08132a", drive: "#111316" };
  function applyTheme(t) {
    if (t !== "marine" && t !== "drive") t = "marine";
    document.documentElement.setAttribute("data-theme", t);
    var meta = $('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", META_THEME[t]);
    save("theme", t);
    $all(".theme-opt").forEach(function (o) { o.classList.toggle("sel", o.getAttribute("data-set-theme") === t); });
  }
  function toggleTheme() {
    var cur = document.documentElement.getAttribute("data-theme");
    applyTheme(cur === "marine" ? "drive" : "marine");
    toast(cur === "marine" ? "Drive-Ready Theme" : "Marine Cybernetic Theme");
  }

  /* ─────────── Drawer ─────────── */
  var drawer = $("#drawer"), scrim = $("#scrim");
  function openDrawer() { drawer.classList.add("open"); scrim.classList.add("open"); drawer.setAttribute("aria-hidden", "false"); }
  function closeDrawer() { drawer.classList.remove("open"); scrim.classList.remove("open"); drawer.setAttribute("aria-hidden", "true"); }

  /* ─────────── Wissens-Filter ─────────── */
  var activeCat = null;
  function filterKnowledge(cat) {
    if (activeCat === cat) cat = null;      // erneuter Klick = alle anzeigen
    activeCat = cat;
    var any = false;
    $all("#view-wissen .know").forEach(function (card) {
      var match = !cat || card.getAttribute("data-cat") === cat;
      card.style.display = match ? "" : "none";
      if (match) any = true;
    });
    $all("#view-wissen .cat").forEach(function (b) {
      b.style.borderColor = b.getAttribute("data-filter") === cat ? "var(--accent)" : "";
    });
    if (!any) { toast("Mehr Artikel kommen bald 🔧"); filterKnowledge(null); }
  }

  /* ─────────── Globale Klick-Delegation ─────────── */
  document.addEventListener("click", function (e) {
    var goEl = e.target.closest("[data-go]");
    if (goEl) { e.preventDefault(); go(goEl.getAttribute("data-go")); return; }

    var navEl = e.target.closest("[data-nav]");
    if (navEl) { closeDrawer(); /* href-Hash erledigt Routing */ return; }

    var resetEl = e.target.closest("[data-reset]");
    if (resetEl) { e.preventDefault(); resetChecklist(resetEl.getAttribute("data-reset")); return; }

    var themeSet = e.target.closest("[data-set-theme]");
    if (themeSet) { applyTheme(themeSet.getAttribute("data-set-theme")); return; }

    var catEl = e.target.closest("[data-filter]");
    if (catEl) { filterKnowledge(catEl.getAttribute("data-filter")); return; }
  });

  $("#menuBtn").addEventListener("click", openDrawer);
  $("#themeBtn").addEventListener("click", toggleTheme);
  scrim.addEventListener("click", closeDrawer);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeDrawer(); });

  /* ─────────── Init ─────────── */
  applyTheme(load("theme", "marine"));
  initChecklists();
  render(currentRoute());

  /* ─────────── Service-Worker ─────────── */
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
      navigator.serviceWorker.register("sw.js").catch(function () {});
    });
  }
})();
