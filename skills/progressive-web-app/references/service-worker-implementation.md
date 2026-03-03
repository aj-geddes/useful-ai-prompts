# Service Worker Implementation

## Service Worker Implementation

```typescript
// public/service-worker.ts
const CACHE_NAME = "app-v1";
const STATIC_ASSETS = [
  "/",
  "/index.html",
  "/css/main.css",
  "/js/app.js",
  "/images/icon-192.png",
  "/offline.html",
];

// Install event
self.addEventListener("install", (event: ExtendableEvent) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    }),
  );
  self.skipWaiting();
});

// Activate event
self.addEventListener("activate", (event: ExtendableEvent) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name)),
      );
    }),
  );
  self.clients.claim();
});

// Fetch event with cache-first strategy for static assets
self.addEventListener("fetch", (event: FetchEvent) => {
  const { request } = event;

  // Skip non-GET requests
  if (request.method !== "GET") {
    return;
  }

  // Cache first for static assets
  if (request.destination === "image" || request.destination === "font") {
    event.respondWith(
      caches
        .match(request)
        .then((response) => {
          return (
            response ||
            fetch(request).then((res) => {
              if (res.ok) {
                const clone = res.clone();
                caches.open(CACHE_NAME).then((cache) => {
                  cache.put(request, clone);
                });
              }
              return res;
            })
          );
        })
        .catch(() => {
          return caches.match("/offline.html");
        }),
    );
  }

  // Network first for API calls
  if (request.url.includes("/api/")) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          if (response.ok) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(request, clone);
            });
          }
          return response;
        })
        .catch(() => {
          return caches.match(request);
        }),
    );
  }

  // Stale while revalidate for HTML
  if (request.destination === "document") {
    event.respondWith(
      caches.match(request).then((cachedResponse) => {
        const fetchPromise = fetch(request).then((response) => {
          if (response.ok) {
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(request, response.clone());
            });
          }
          return response;
        });

        return cachedResponse || fetchPromise;
      }),
    );
  }
});

// Background Sync
self.addEventListener("sync", (event: any) => {
  if (event.tag === "sync-notes") {
    event.waitUntil(syncNotes());
  }
});

async function syncNotes() {
  const db = await openDB("notes");
  const unsynced = await db.getAll(
    "keyval",
    IDBKeyRange.bound("pending_", "pending_\uffff"),
  );

  for (const item of unsynced) {
    try {
      await fetch("/api/notes", {
        method: "POST",
        body: JSON.stringify(item.value),
      });
      await db.delete("keyval", item.key);
    } catch (error) {
      console.error("Sync failed:", error);
    }
  }
}
```
