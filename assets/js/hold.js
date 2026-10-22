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
