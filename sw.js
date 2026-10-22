// HBLiving offline support.  Pages always try the network first, so updates show right away.
const CACHE = "hbl-b4d9d382af";
const CORE = ["./", "index.html", "manifest.webmanifest", "assets/img/mark.svg", "assets/img/icon-192.png"];
const OFFLINE_HTML = '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Offline</title><body style="font-family:system-ui;padding:40px;text-align:center"><h1>You are offline</h1><p>Check your connection, then try again.</p><p><a href="./">Try again</a></p></body>';
const offline = () => new Response(OFFLINE_HTML, { headers: { "Content-Type": "text/html; charset=utf-8" } });
self.addEventListener("install", (e) => { e.waitUntil(caches.open(CACHE).then((c) => Promise.all(CORE.map((u) => c.add(u).catch(() => {})))).then(() => self.skipWaiting())); });
self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;
  if (req.mode === "navigate") {
    e.respondWith(fetch(req).then((res) => { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); return res; })
      .catch(() => caches.match(req).then((r) => r || caches.match("index.html")).then((r) => r || offline())));
    return;
  }
  e.respondWith(caches.match(req).then((hit) => {
    const net = fetch(req).then((res) => { if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); } return res; }).catch(() => hit || Response.error());
    return hit || net;
  }));
});
