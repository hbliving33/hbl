// HBLiving monthly report: sign in with an admin email, pick a month, see views and taps per ad.
(() => {
  const C = window.HBL_TRACK || {}, box = document.getElementById("rep"), msg = document.getElementById("repMsg");
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  if (!C.url || !C.key || !window.supabase) { msg.textContent = "Counting is not turned on yet.  Add the Supabase address and key in assets/js/track.js."; return; }
  const sb = window.supabase.createClient(C.url, C.key);
  const names = Object.fromEntries((window.HB_ADS || []).map((a) => [a.id, a.name]));
  const siteName = (s) => s === "hbliving" ? "HBLiving" : ((window.HB_COMMUNITIES || []).find((c) => c.id === s) || { name: s }).name;
  const signin = document.getElementById("repSignin"), main = document.getElementById("repMain"), month = document.getElementById("repMonth");
  const now = new Date(); month.value = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}`;

  async function run() {
    msg.textContent = "Loading...";
    const { data, error } = await sb.rpc("ad_report", { p_month: month.value + "-01" });
    if (error) { msg.textContent = "Could not load the report: " + error.message; return; }
    if (!data.length) { box.innerHTML = ""; msg.textContent = "No activity for this month, or this email is not on the admin list."; return; }
    msg.textContent = "";
    const byAd = {};
    data.forEach((r) => (byAd[r.ad] = byAd[r.ad] || []).push(r));
    const label = new Date(month.value + "-01T12:00").toLocaleDateString("en-US", { month: "long", year: "numeric" });
    box.innerHTML = Object.entries(byAd).map(([ad, rows]) => {
      const t = rows.reduce((a, r) => ({ v: a.v + +r.views, c: a.c + +r.calls, w: a.w + +r.webs, d: a.d + +r.dirs }), { v: 0, c: 0, w: 0, d: 0 });
      const text = `${names[ad] || ad}, ${label}:  ${t.v} views, ${t.c} taps to call, ${t.w} website visits and ${t.d} directions requests.`;
      return `<section class="rep-ad"><h2>${esc(names[ad] || ad)}</h2>
        <table><thead><tr><th>Where</th><th>Views</th><th>Call taps</th><th>Website</th><th>Directions</th></tr></thead><tbody>
        ${rows.map((r) => `<tr><td>${esc(siteName(r.site))}</td><td>${r.views}</td><td>${r.calls}</td><td>${r.webs}</td><td>${r.dirs}</td></tr>`).join("")}
        <tr class="tot"><td>Total</td><td>${t.v}</td><td>${t.c}</td><td>${t.w}</td><td>${t.d}</td></tr></tbody></table>
        <button type="button" class="btn btn-ghost" data-copy="${esc(text)}">Copy summary for the advertiser</button></section>`;
    }).join("");
  }
  box.addEventListener("click", async (e) => { const b = e.target.closest("[data-copy]"); if (!b) return; try { await navigator.clipboard.writeText(b.dataset.copy); b.textContent = "Copied"; } catch (err) { b.textContent = b.dataset.copy; } });
  month.addEventListener("change", run);
  document.getElementById("repOut").addEventListener("click", async () => { await sb.auth.signOut(); location.reload(); });
  document.getElementById("repSignin").addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = new FormData(e.target).get("email");
    const { error } = await sb.auth.signInWithOtp({ email, options: { emailRedirectTo: location.href.split("#")[0] } });
    msg.textContent = error ? "Could not send the sign-in link: " + error.message : "Check your email for a sign-in link.";
  });
  sb.auth.getSession().then(({ data }) => { if (data.session) { signin.hidden = true; main.hidden = false; run(); } else { signin.hidden = false; main.hidden = true; msg.textContent = ""; } });
})();
