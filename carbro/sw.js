/* ═══════════════════════════════════════════════
   CarBro – Service Worker
   Cache-first für App-Shell, Network-first für HTML,
   Stale-while-revalidate für Fonts.
   ═══════════════════════════════════════════════ */
const VERSION = "carbro-v1.0.0";
const CORE = "core-" + VERSION;
const RUNTIME = "runtime-" + VERSION;
const OFFLINE_URL = "offline.html";

const PRECACHE = [
  "./",
  "index.html",
  "app.css",
  "app.js",
  "manifest.webmanifest",
  "offline.html",
  "icons/icon-192.png",
  "icons/icon-512.png",
  "icons/maskable-192.png",
  "icons/maskable-512.png",
  "icons/apple-touch-icon.png",
  "icons/favicon-32.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CORE).then((c) => c.addAll(PRECACHE)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CORE && k !== RUNTIME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const { request } = event;
  if (request.method !== "GET") return;

  const url = new URL(request.url);
  const isFont =
    url.hostname === "fonts.googleapis.com" ||
    url.hostname === "fonts.gstatic.com";

  /* HTML-Navigation: Network-first, Fallback Cache -> Offline-Seite */
  if (request.mode === "navigate") {
    event.respondWith(
      fetch(request)
        .then((res) => {
          const clone = res.clone();
          caches.open(CORE).then((c) => c.put("index.html", clone));
          return res;
        })
        .catch(() =>
          caches.match(request).then((r) => r || caches.match("index.html") || caches.match(OFFLINE_URL))
        )
    );
    return;
  }

  /* Google Fonts: stale-while-revalidate */
  if (isFont) {
    event.respondWith(
      caches.open(RUNTIME).then((cache) =>
        cache.match(request).then((cached) => {
          const network = fetch(request)
            .then((res) => { if (res && res.status === 200) cache.put(request, res.clone()); return res; })
            .catch(() => cached);
          return cached || network;
        })
      )
    );
    return;
  }

  /* eigene Assets: Cache-first mit Hintergrund-Update */
  if (url.origin === location.origin) {
    event.respondWith(
      caches.match(request).then((cached) => {
        const network = fetch(request)
          .then((res) => {
            if (res && res.status === 200 && res.type === "basic") {
              const clone = res.clone();
              caches.open(CORE).then((c) => c.put(request, clone));
            }
            return res;
          })
          .catch(() => cached);
        return cached || network;
      })
    );
  }
});
