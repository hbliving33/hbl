// HBLiving hit counter: counts ad views and taps (call, website, directions) for the monthly report.
// It stores counts in HBLiving's own Supabase database.  No Google Analytics, no cookies, nothing about the visitor.
// Leave url and key empty to turn counting off.  Fill them in from Supabase: Project Settings, API.
window.HBL_TRACK = { url: "", key: "" };
window.hblTrack = (() => {
  const C = window.HBL_TRACK, seen = new Set();
  const site = (window.SP_COMMUNITY || "hbliving");
  // New Supabase publishable keys go in the apikey header only.  An older anon key (it starts with eyJ) also goes in Authorization.
  function headers() {
    const h = { apikey: C.key, "Content-Type": "application/json", Prefer: "return=minimal" };
    if (C.key.startsWith("eyJ")) h.Authorization = "Bearer " + C.key;
    return h;
  }
  function send(ad, kind) {
    if (!C.url || !C.key || !ad) return;
    const body = JSON.stringify({ ad, kind, site });
    try {
      fetch(C.url.replace(/\/$/, "") + "/rest/v1/ad_events", { method: "POST", keepalive: true,
        headers: headers(), body }).catch(() => {});
    } catch (e) {}
  }
  // Count a view once per page visit, when at least half the ad is on screen
  const io = "IntersectionObserver" in window ? new IntersectionObserver((entries) => entries.forEach((en) => {
    if (en.isIntersecting && en.intersectionRatio >= 0.5) { const id = en.target.dataset.ad; if (!seen.has(id)) { seen.add(id); send(id, "view"); } io.unobserve(en.target); }
  }), { threshold: [0.5] }) : null;
  return {
    watch(el) { if (io && el && el.dataset.ad) io.observe(el); },
    tap(ad, kind) { send(ad, kind); }
  };
})();
// Any link with data-ad and data-kind counts as a tap
document.addEventListener("click", (e) => { const a = e.target.closest("[data-ad][data-kind]"); if (a) window.hblTrack.tap(a.dataset.ad, a.dataset.kind); });
