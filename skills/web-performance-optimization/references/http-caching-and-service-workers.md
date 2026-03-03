# HTTP Caching and Service Workers

## HTTP Caching and Service Workers

```typescript
// service-worker.ts
const CACHE_NAME = "v1";
const ASSETS_TO_CACHE = ["/", "/index.html", "/css/style.css", "/js/app.js"];

self.addEventListener("install", (event: ExtendableEvent) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    }),
  );
});

self.addEventListener("fetch", (event: FetchEvent) => {
  // Cache first, fall back to network
  event.respondWith(
    caches.match(event.request).then((response) => {
      if (response) return response;

      return fetch(event.request)
        .then((response) => {
          // Clone the response
          const cloned = response.clone();

          // Cache successful responses
          if (response.status === 200) {
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, cloned);
            });
          }

          return response;
        })
        .catch(() => {
          // Return offline page if available
          return caches.match("/offline.html");
        });
    }),
  );
});

// Register service worker
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/service-worker.js")
      .catch((err) => console.error("SW registration failed:", err));
  });
}
```
