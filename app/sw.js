self.addEventListener("install", (event) => {
  event.waitUntil(self.skipWaiting());
});

function rootOf(url) {
  const path = url.pathname.replace(/\/app(?:\/.*)?$/, "/");
  return url.origin + (path.endsWith("/") ? path : path + "/") + url.search + url.hash;
}

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter((key) => key.indexOf("yuwen-app-v1") === 0).map((key) => caches.delete(key)));
    const windows = await self.clients.matchAll({ type: "window", includeUncontrolled: true });
    await Promise.all(windows.map((client) => {
      const url = new URL(client.url);
      const next = rootOf(url);
      if (next !== client.url) return client.navigate(next);
      return null;
    }));
    await self.clients.claim();
  })());
});

self.addEventListener("fetch", (event) => {
  if (event.request.mode !== "navigate") return;
  const url = new URL(event.request.url);
  if (!/\/app(?:\/|$)/.test(url.pathname)) return;
  event.respondWith(Response.redirect(rootOf(url), 302));
});
