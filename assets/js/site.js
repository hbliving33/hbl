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
  if (sel) sel.value = a.dataset.plan === "Featured" ? "Featured, $10 a month" : "Local Listing, $5 a month";
}));

// App: offline support and automatic updates
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("sw.js", { updateViaCache: "none" }).then((reg) => {
    document.addEventListener("visibilitychange", () => { if (!document.hidden) reg.update(); });
  }).catch(() => {});
  let reloaded = false;
  navigator.serviceWorker.addEventListener("controllerchange", () => { if (!reloaded) { reloaded = true; location.reload(); } });
}
