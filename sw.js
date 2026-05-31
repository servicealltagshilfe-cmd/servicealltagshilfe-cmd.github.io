/* ═══════════════════════════════════════════════
   Service Worker – Alltagshelfer PWA
   Strategy: Cache-first für Assets, Network-first für HTML
   ═══════════════════════════════════════════════ */

const CACHE = 'alltagshelfer-v1';
const OFFLINE_URL = '/offline.html';

const PRECACHE = [
  '/',
  '/index.html',
  '/manifest.json',
  '/icons/icon-192.svg',
  '/icons/icon-512.svg',
  OFFLINE_URL
];

/* ── Install: Precache alle wichtigen Assets ── */
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE).then(cache => cache.addAll(PRECACHE))
  );
  self.skipWaiting();
});

/* ── Activate: Alte Caches entfernen ── */
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.filter(k => k !== CACHE).map(k => caches.delete(k))
      )
    )
  );
  self.clients.claim();
});

/* ── Fetch: Strategie nach Request-Typ ── */
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  /* Nur eigene Origin behandeln */
  if (url.origin !== location.origin) return;

  /* HTML: Network-first, Fallback auf Cache, dann Offline-Seite */
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then(response => {
          const clone = response.clone();
          caches.open(CACHE).then(c => c.put(request, clone));
          return response;
        })
        .catch(() =>
          caches.match(request).then(cached =>
            cached || caches.match(OFFLINE_URL)
          )
        )
    );
    return;
  }

  /* Assets: Cache-first, dann Network */
  event.respondWith(
    caches.match(request).then(cached => {
      if (cached) {
        /* Hintergrund-Update */
        fetch(request).then(response => {
          if (response && response.status === 200) {
            caches.open(CACHE).then(c => c.put(request, response));
          }
        }).catch(() => {});
        return cached;
      }
      return fetch(request).then(response => {
        if (!response || response.status !== 200 || response.type === 'opaque') {
          return response;
        }
        const clone = response.clone();
        caches.open(CACHE).then(c => c.put(request, clone));
        return response;
      });
    })
  );
});
