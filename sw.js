const CACHE = "yuwen-root-v3";
const ASSETS = [
  "./",
  "./index.html",
  "./manifest.webmanifest",
  "./css/app.css",
  "./js/app.js",
  "./js/store.js",
  "./js/quiz.js",
  "./js/render.js",
  "./js/poems.js",
  "./js/util.js",
  "./data/poems.json",
  "./data/POEMS_SOURCES.md",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./icons/apple-touch-icon.png",
];

function relPath(url) {
  const base = new URL(self.registration.scope);
  if (url.origin !== base.origin) return null;
  if (!url.pathname.startsWith(base.pathname)) return null;
  let rel = decodeURIComponent(url.pathname.slice(base.pathname.length));
  if (rel.endsWith("/")) rel = rel.slice(0, -1);
  return rel;
}

function isAppShell(url) {
  const rel = relPath(url);
  if (rel == null) return false;
  if (rel === "review" || rel.startsWith("review/") || rel === "app" || rel.startsWith("app/")) return false;
  if (rel === "" || rel === "index.html") return true;
  return /^(css|js|data|icons)\//.test(rel) || rel === "manifest.webmanifest";
}

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((key) => key !== CACHE).map((key) => caches.delete(key)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (!isAppShell(url)) return;
  event.respondWith(
    caches.match(req).then((cached) => {
      const fetched = fetch(req)
        .then((res) => {
          if (res && res.ok && (res.type === "basic" || res.type === "default")) {
            const copy = res.clone();
            caches.open(CACHE).then((cache) => cache.put(req, copy));
          }
          return res;
        })
        .catch(() => cached);
      return cached || fetched;
    })
  );
});
