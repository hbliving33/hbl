// HBLiving one-pager: plays a recorded track from assets/audio/vibes.mp3.
// Browsers only allow sound after the visitor taps or clicks, so it starts on the first tap anywhere.
// If the track file is missing, the play button and hint stay hidden.
(() => {
  const btn = document.getElementById("play"), hint = document.getElementById("hint"), txt = btn && btn.querySelector(".pl-txt");
  if (!btn) return;
  btn.hidden = true; hint.hidden = true;
  const audio = new Audio("assets/audio/vibes.mp3");
  audio.loop = true; audio.preload = "auto"; audio.volume = 0.7;
  let stoppedByUser = false;
  const ui = (on) => { document.body.classList.toggle("playing", on); btn.setAttribute("aria-pressed", String(on)); txt.textContent = on ? "Pause the vibes" : "Play the vibes"; if (on) hint.hidden = true; };
  const start = () => audio.play().then(() => ui(true)).catch(() => {});
  audio.addEventListener("canplay", () => {
    btn.hidden = false;
    start().then(() => { if (audio.paused) hint.hidden = false; });
  }, { once: true });
  audio.addEventListener("pause", () => ui(false));
  btn.addEventListener("click", (e) => { e.stopPropagation(); if (audio.paused) { stoppedByUser = false; start(); } else { stoppedByUser = true; audio.pause(); } });
  addEventListener("pointerdown", (e) => { if (e.target.closest("#play")) return; if (audio.paused && !stoppedByUser && !btn.hidden) start(); });
})();

// Surf City right now: local time and weather (Open-Meteo, free, no key)
(() => {
  const el = document.getElementById("nowTxt");
  if (!el) return;
  const WX = [[0, "Clear"], [1, "Mostly clear"], [2, "Partly cloudy"], [3, "Cloudy"], [48, "Foggy"], [57, "Drizzle"], [67, "Rain"], [77, "Snow"], [82, "Showers"], [86, "Snow showers"], [99, "Thunderstorms"]];
  const look = (c) => (WX.find(([max]) => c <= max) || [0, ""])[1];
  let wx = "";
  const tz = { timeZone: "America/Los_Angeles" };
  const date = () => new Date().toLocaleDateString("en-US", { ...tz, weekday: "short", month: "short", day: "numeric" });
  const time = () => new Date().toLocaleTimeString("en-US", { ...tz, hour: "numeric", minute: "2-digit" });
  const paint = () => { el.textContent = `${date()}  ·  ${time()}${wx ? "  ·  " + wx : ""}`; };
  async function load() {
    try {
      const r = await fetch("https://api.open-meteo.com/v1/forecast?latitude=33.6595&longitude=-117.9988&current=temperature_2m,weather_code&temperature_unit=fahrenheit&timezone=America%2FLos_Angeles");
      if (!r.ok) return;
      const w = await r.json();
      wx = `${Math.round(w.current.temperature_2m)}°`; paint();
    } catch (e) {}
  }
  paint(); load(); setInterval(paint, 15000); setInterval(load, 15 * 60 * 1000);
})();

// Visit counter: counts this visit in the HBLiving database.  No cookies, no personal data.
(() => {
  if (/^(localhost|127\.)/.test(location.hostname)) return;
  const path = location.pathname.replace(/index\.html$/, "") || "/";
  try { const k = "hbl-hit:" + path; if (sessionStorage.getItem(k)) return; sessionStorage.setItem(k, "1"); } catch (e) {}
  fetch("https://raooyhmkovzshmhgarwm.supabase.co/rest/v1/rpc/count_hit", { method: "POST", keepalive: true,
    headers: { apikey: "sb_publishable_apjQYn1UxVPG_Ecwxs3rdQ_ovJix8Fo", "Content-Type": "application/json" },
    body: JSON.stringify({ p_site: "hbliving", p_path: path }) }).catch(() => {});
})();
