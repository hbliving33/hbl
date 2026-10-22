// Phone menu
(() => {
  const btn = document.querySelector(".menu-btn"), nav = document.getElementById("nav");
  if (!btn || !nav) return;
  btn.addEventListener("click", () => btn.setAttribute("aria-expanded", nav.classList.toggle("open")));
  nav.addEventListener("click", (e) => { if (e.target.closest("a")) { nav.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); } });
})();

// Plan buttons pre-select the plan in the advertiser form
document.querySelectorAll("[data-plan]").forEach((a) => a.addEventListener("click", () => {
  const sel = document.getElementById("planSel");
  const v = { Monthly: "Monthly, $10 a month", Yearly: "Yearly, $100 (two months free)", Neighborhood: "Bring HBLiving to my neighborhood" }[a.dataset.plan];
  if (sel && v) sel.value = v;
}));

// App: offline support and automatic updates
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("sw.js", { updateViaCache: "none" }).then((reg) => {
    document.addEventListener("visibilitychange", () => { if (!document.hidden) reg.update(); });
  }).catch(() => {});
  let reloaded = false; const hadController = !!navigator.serviceWorker.controller;
  navigator.serviceWorker.addEventListener("controllerchange", () => { if (hadController && !reloaded) { reloaded = true; location.reload(); } });
}

// A link like index.html?community=Suburbia%20Park#advertise pre-selects the community in the form
(() => {
  const c = new URLSearchParams(location.search).get("community"), sel = document.querySelector('select[name="community"]');
  if (c && sel) [...sel.options].forEach((o) => { if (o.text.toLowerCase().startsWith(c.toLowerCase())) sel.value = o.text; });
})();
