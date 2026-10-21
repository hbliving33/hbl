// HB Living map: territories, ad pins and the ad list, all linked together.
(() => {
  const el = document.getElementById("hbMap");
  if (!el || !window.L) return;
  const T = window.HB_TERRITORIES, ADS = window.HB_ADS, Z = window.HB_ZIPS;
  const byId = Object.fromEntries(T.map((t) => [t.id, t]));
  const zipT = {}; T.forEach((t) => t.zips.forEach((z) => (zipT[z] = t)));
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  const map = L.map(el, { scrollWheelZoom: false, zoomSnap: 0.25 });
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", { maxZoom: 18, attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' }).addTo(map);

  const layers = {};
  const shapes = L.geoJSON(Z, {
    style: (f) => { const t = zipT[f.properties.zip]; return { color: t.color, weight: 2, fillColor: t.color, fillOpacity: 0.16 }; },
    onEachFeature: (f, layer) => {
      const t = zipT[f.properties.zip];
      (layers[t.id] = layers[t.id] || []).push(layer);
      layer.on("click", () => pick(t.id));
      layer.bindTooltip(t.name, { sticky: true, className: "terr-tip" });
    }
  }).addTo(map);
  const all = shapes.getBounds();
  map.fitBounds(all, { padding: [10, 10] });

  const pinIcon = (a) => L.divIcon({ className: "", html: `<span class="pin${a.featured ? " pin-feat" : ""}" style="--c:${byId[a.territory].color}"></span>`, iconSize: [26, 26], iconAnchor: [13, 24], popupAnchor: [0, -22] });
  const pins = ADS.map((a, i) => {
    const m = L.marker([a.lat, a.lng], { icon: pinIcon(a), title: a.name }).addTo(map);
    m.bindPopup(`<b>${esc(a.name)}</b><br>${esc(a.cat)}${a.sample ? "<br><i>Sample ad</i>" : ""}`);
    m.on("click", () => highlight(i, false));
    return m;
  });

  const list = document.getElementById("adList"), chips = document.getElementById("terrChips"), info = document.getElementById("terrInfo");
  chips.innerHTML = `<button type="button" data-t="all" aria-pressed="true">All of HB</button>` + T.map((t) => `<button type="button" data-t="${t.id}" aria-pressed="false" style="--c:${t.color}"><i></i>${esc(t.name)}</button>`).join("");
  let current = "all";

  function card(a, i) {
    const t = byId[a.territory];
    return `<li class="mad${a.featured ? " mad-feat" : ""}" data-i="${i}" style="--c:${t.color}">
      <div class="mad-top"><span class="mad-cat">${esc(a.cat)}</span>${a.featured ? '<span class="ad-badge">Featured</span>' : ""}</div>
      <b>${esc(a.name)}</b><span class="mad-line">${esc(a.line)}</span>
      <span class="mad-terr"><i></i>${esc(t.name)}</span>${a.sample ? '<span class="mad-sample">Sample ad</span>' : ""}</li>`;
  }
  function paint() {
    const show = ADS.map((a, i) => [a, i]).filter(([a]) => current === "all" || a.territory === current)
      .sort((x, y) => (y[0].featured ? 1 : 0) - (x[0].featured ? 1 : 0));
    list.innerHTML = show.length ? show.map(([a, i]) => card(a, i)).join("") : '<li class="empty">No ads in this area yet.  Yours could be the first.</li>';
    const t = byId[current];
    info.innerHTML = t ? `<b style="color:${t.color}">${esc(t.name)}</b><span>${esc(t.blurb)}  ZIP ${t.zips.join(" and ")}.</span>` : `<b>All of Huntington Beach</b><span>Four areas, one map.  Tap an area to zoom in.</span>`;
    chips.querySelectorAll("button").forEach((b) => b.setAttribute("aria-pressed", b.dataset.t === current));
    Object.entries(layers).forEach(([id, ls]) => ls.forEach((l) => l.setStyle({ fillOpacity: current === "all" || id === current ? 0.16 : 0.04, weight: id === current ? 3 : 2 })));
    pins.forEach((m, i) => m.setOpacity(current === "all" || ADS[i].territory === current ? 1 : 0.25));
  }
  function pick(id) {
    current = id;
    if (id === "all") map.flyToBounds(all, { padding: [10, 10], duration: 0.6 });
    else map.flyToBounds(L.featureGroup(layers[id]).getBounds(), { padding: [16, 16], duration: 0.6 });
    paint();
  }
  function highlight(i, fly) {
    list.querySelectorAll(".mad").forEach((c) => c.classList.toggle("on", +c.dataset.i === i));
    if (fly) { map.flyTo([ADS[i].lat, ADS[i].lng], 15, { duration: 0.6 }); pins[i].openPopup(); }
    const c = list.querySelector(`.mad[data-i="${i}"]`); if (c && !fly) c.scrollIntoView({ block: "nearest", behavior: "smooth" });
  }
  chips.addEventListener("click", (e) => { const b = e.target.closest("button"); if (b) pick(b.dataset.t); });
  list.addEventListener("click", (e) => { const c = e.target.closest(".mad"); if (c) highlight(+c.dataset.i, true); });
  paint();
})();
