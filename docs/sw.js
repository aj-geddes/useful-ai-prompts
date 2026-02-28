---
layout: null
---
// Service Worker for Performance Optimization
// Version 1.0.1

const CACHE_NAME = 'useful-ai-prompts-v1.0.1';
const urlsToCache = [
  '{{ site.baseurl }}/',
  '{{ site.baseurl }}/assets/css/main.css',
  '{{ site.baseurl }}/assets/js/main.js',
  '{{ site.baseurl }}/assets/js/enhanced-search.js',
  '{{ site.baseurl }}/search/',
  '{{ site.baseurl }}/categories/',
  // Add critical prompt pages
  '{{ site.baseurl }}/prompts/strategic-roadmap-generator/',
  '{{ site.baseurl }}/prompts/business-analyst-strategic-excellence/',
  '{{ site.baseurl }}/prompts/fullstack-developer-architect/'
];

// Install event - cache critical resources
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// Fetch event - serve from cache with network fallback
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Return cached version or fetch from network
        if (response) {
          return response;
        }
        
        // Clone the request because it's a stream
        const fetchRequest = event.request.clone();
        
        return fetch(fetchRequest).then(function(response) {
          // Check if valid response
          if (!response || response.status !== 200 || response.type !== 'basic') {
            return response;
          }
          
          // Clone the response because it's a stream
          const responseToCache = response.clone();
          
          // Cache dynamic content selectively
          if (shouldCache(event.request.url)) {
            caches.open(CACHE_NAME)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
              });
          }
          
          return response;
        });
      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheName !== CACHE_NAME) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Helper function to determine what should be cached
function shouldCache(url) {
  const cacheableExtensions = ['.css', '.js', '.json', '.html'];
  const cacheablePaths = ['/prompts/', '/categories/', '/search/'];
  
  // Cache static assets
  if (cacheableExtensions.some(ext => url.includes(ext))) {
    return true;
  }
  
  // Cache important pages
  if (cacheablePaths.some(path => url.includes(path))) {
    return true;
  }
  
  // Don't cache external resources or admin pages
  if (url.includes('cdnjs.cloudflare.com') || 
      url.includes('fonts.googleapis.com') ||
      url.includes('/admin/')) {
    return false;
  }
  
  return false;
}

// Background sync for offline functionality
self.addEventListener('sync', function(event) {
  if (event.tag === 'background-sync') {
    event.waitUntil(doBackgroundSync());
  }
});

function doBackgroundSync() {
  // Sync search index and critical data when connection restored
  return fetch('{{ site.baseurl }}/assets/data/search-index.json')
    .then(response => response.json())
    .then(data => {
      return caches.open(CACHE_NAME).then(cache => {
        cache.put('{{ site.baseurl }}/assets/data/search-index.json', 
                  new Response(JSON.stringify(data)));
      });
    });
}

// Offline fallback for HTML pages
self.addEventListener('fetch', function(event) {
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request).catch(function() {
        return caches.match('{{ site.baseurl }}/offline.html');
      })
    );
  }
});

// Advanced caching strategies
const RUNTIME_CACHE = 'runtime-cache-v1';
const STATIC_CACHE = 'static-cache-v1';

// Cache strategies for different resource types
self.addEventListener('fetch', function(event) {
  const url = new URL(event.request.url);
  
  // Handle different resource types with appropriate caching strategies
  if (event.request.destination === 'image') {
    event.respondWith(cacheFirst(event.request, STATIC_CACHE));
  } else if (event.request.destination === 'script' || event.request.destination === 'style') {
    event.respondWith(staleWhileRevalidate(event.request, STATIC_CACHE));
  } else if (url.pathname.startsWith('{{ site.baseurl }}/prompts/')) {
    event.respondWith(networkFirst(event.request, RUNTIME_CACHE));
  }
});

// Cache-first strategy for static assets
function cacheFirst(request, cacheName) {
  return caches.open(cacheName).then(cache => {
    return cache.match(request).then(response => {
      return response || fetch(request).then(fetchResponse => {
        cache.put(request, fetchResponse.clone());
        return fetchResponse;
      });
    });
  });
}

// Stale-while-revalidate for frequently updated resources
function staleWhileRevalidate(request, cacheName) {
  return caches.open(cacheName).then(cache => {
    return cache.match(request).then(response => {
      const fetchPromise = fetch(request).then(fetchResponse => {
        cache.put(request, fetchResponse.clone());
        return fetchResponse;
      });
      return response || fetchPromise;
    });
  });
}

// Network-first for dynamic content
function networkFirst(request, cacheName) {
  return fetch(request).then(response => {
    return caches.open(cacheName).then(cache => {
      cache.put(request, response.clone());
      return response;
    });
  }).catch(() => {
    return caches.match(request);
  });
}