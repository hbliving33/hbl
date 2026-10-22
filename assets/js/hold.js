// HBLiving one-pager: an original one-drop reggae groove, made live in the browser (no recordings).
// Browsers only allow sound after the visitor taps or clicks, so it starts on the first tap anywhere,
// or plays right away when the browser already allows it.
(() => {
  const btn = document.getElementById("play"), hint = document.getElementById("hint"), txt = btn && btn.querySelector(".pl-txt");
  const AC = window.AudioContext || window.webkitAudioContext;
  if (!btn || !AC) { if (btn) btn.hidden = true; if (hint) hint.hidden = true; return; }

  const BPM = 74, STEP = 60 / BPM / 4;          // sixteenth notes
  const BARS = [                                  // A minor, G, F, G
    { root: 110.00, chord: [220.00, 261.63, 329.63] },
    { root: 98.00, chord: [196.00, 246.94, 293.66] },
    { root: 87.31, chord: [174.61, 220.00, 261.63] },
    { root: 98.00, chord: [196.00, 246.94, 293.66] }
  ];
  const BASS = [[0, 1, 2], [3, 1, 1], [6, 1.5, 2], [10, 1, 1], [11, 1, 1], [14, 1.5, 2]];  // step, ratio to root, length in steps

  let ctx = null, out, echo, noise, timer = null, step = 0, nextT = 0, playing = false, stoppedByUser = false;

  function setup() {
    ctx = new AC();
    const comp = ctx.createDynamicsCompressor();
    out = ctx.createGain(); out.gain.value = 0.55;
    out.connect(comp); comp.connect(ctx.destination);
    // dub echo for the skank
    echo = ctx.createDelay(1); echo.delayTime.value = STEP * 3;
    const fb = ctx.createGain(); fb.gain.value = 0.32;
    const eg = ctx.createGain(); eg.gain.value = 0.35;
    echo.connect(fb); fb.connect(echo); echo.connect(eg); eg.connect(out);
    noise = ctx.createBuffer(1, ctx.sampleRate, ctx.sampleRate);
    const d = noise.getChannelData(0); for (let i = 0; i < d.length; i++) d[i] = Math.random() * 2 - 1;
  }

  function env(g, t, peak, len) { g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(peak, t + 0.005); g.gain.exponentialRampToValueAtTime(0.0001, t + len); }

  function kick(t) {
    const o = ctx.createOscillator(), g = ctx.createGain();
    o.frequency.setValueAtTime(120, t); o.frequency.exponentialRampToValueAtTime(42, t + 0.18);
    env(g, t, 1, 0.35); o.connect(g); g.connect(out); o.start(t); o.stop(t + 0.4);
  }
  function hiss(t, freq, q, peak, len, type) {
    const s = ctx.createBufferSource(), f = ctx.createBiquadFilter(), g = ctx.createGain();
    s.buffer = noise; f.type = type; f.frequency.value = freq; f.Q.value = q;
    env(g, t, peak, len); s.connect(f); f.connect(g); g.connect(out); s.start(t); s.stop(t + len + 0.02);
  }
  function rim(t) {
    hiss(t, 1900, 2, 0.5, 0.09, "bandpass");
    const o = ctx.createOscillator(), g = ctx.createGain(); o.type = "triangle"; o.frequency.value = 820;
    env(g, t, 0.25, 0.05); o.connect(g); g.connect(out); o.start(t); o.stop(t + 0.08);
  }
  function skank(t, chord) {
    const f = ctx.createBiquadFilter(), g = ctx.createGain();
    f.type = "bandpass"; f.frequency.value = 1400; f.Q.value = 0.9;
    env(g, t, 0.22, 0.11); f.connect(g); g.connect(out); g.connect(echo);
    chord.forEach((hz) => { [1, 2].forEach((m) => { const o = ctx.createOscillator(); o.type = "sawtooth"; o.frequency.value = hz * m; o.detune.value = (Math.random() - 0.5) * 8; o.connect(f); o.start(t); o.stop(t + 0.14); }); });
  }
  function bubble(t, chord) {
    const g = ctx.createGain(); env(g, t, 0.06, 0.16); g.connect(out);
    chord.forEach((hz) => { const o = ctx.createOscillator(); o.type = "sine"; o.frequency.value = hz * 2; o.connect(g); o.start(t); o.stop(t + 0.2); });
  }
  function bass(t, hz, len) {
    const o = ctx.createOscillator(), f = ctx.createBiquadFilter(), g = ctx.createGain();
    o.type = "triangle"; o.frequency.value = hz / 2 * 2; f.type = "lowpass"; f.frequency.value = 420;
    g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.85, t + 0.02); g.gain.setValueAtTime(0.85, t + len * 0.7); g.gain.exponentialRampToValueAtTime(0.0001, t + len);
    o.connect(f); f.connect(g); g.connect(out); o.start(t); o.stop(t + len + 0.05);
  }

  function play16(s, t) {
    const bar = BARS[Math.floor(s / 16) % BARS.length], k = s % 16;
    const swing = k % 2 ? STEP * 0.12 : 0, tt = t + swing;
    if (k === 8) { kick(tt); rim(tt); }                                  // the one drop, on beat three
    if (k % 2 === 0) hiss(tt, 8000, 0.7, k % 4 === 2 ? 0.16 : 0.08, 0.04, "highpass");
    if (k === 4 || k === 12) skank(tt, bar.chord);                       // offbeat guitar chop
    if (k === 6 || k === 14) bubble(tt, bar.chord);                      // organ bubble
    BASS.forEach(([at, ratio, len]) => { if (at === k) bass(tt, bar.root * ratio, len * STEP); });
  }

  function tick() {
    while (nextT < ctx.currentTime + 0.12) { play16(step, nextT); nextT += STEP; step = (step + 1) % (16 * BARS.length); }
  }

  async function start() {
    if (!ctx) setup();
    await ctx.resume();
    if (ctx.state !== "running" || playing) return;
    playing = true; stoppedByUser = false; step = 0; nextT = ctx.currentTime + 0.05;
    timer = setInterval(tick, 25); tick();
    out.gain.cancelScheduledValues(ctx.currentTime); out.gain.setValueAtTime(0.0001, ctx.currentTime); out.gain.exponentialRampToValueAtTime(0.55, ctx.currentTime + 1.2);
    document.body.classList.add("playing"); btn.setAttribute("aria-pressed", "true"); txt.textContent = "Pause the vibes"; hint.hidden = true;
  }
  function stop() {
    playing = false; stoppedByUser = true; clearInterval(timer);
    if (ctx) ctx.suspend();
    document.body.classList.remove("playing"); btn.setAttribute("aria-pressed", "false"); txt.textContent = "Play the vibes";
  }

  btn.addEventListener("click", (e) => { e.stopPropagation(); playing ? stop() : start(); });
  addEventListener("pointerdown", () => { if (!playing && !stoppedByUser) start(); }, { once: false });
  addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") return; if (!playing && !stoppedByUser) start(); }, { once: true });
  document.addEventListener("visibilitychange", () => { if (document.hidden && playing) { clearInterval(timer); ctx.suspend(); } else if (!document.hidden && playing) { ctx.resume().then(() => { nextT = ctx.currentTime + 0.05; timer = setInterval(tick, 25); }); } });

  // Plays straight away when the browser already allows sound for this site
  try { const probe = new AC(); if (probe.state === "running") { probe.close(); start(); } else probe.close(); } catch (e) {}
})();
