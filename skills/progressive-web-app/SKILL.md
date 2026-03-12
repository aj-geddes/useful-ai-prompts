---
name: progressive-web-app
description: >
  Build progressive web apps using service workers, web manifest, offline
  support, and installability. Use when creating app-like web experiences.
---

# Progressive Web App

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build progressive web applications with offline support, installability, service workers, and web app manifests to deliver app-like experiences in the browser.

## When to Use

- App-like web experiences
- Offline functionality needed
- Mobile installation required
- Push notifications
- Fast loading experiences

## Quick Start

Minimal working example:

```json
// public/manifest.json
{
  "name": "My Awesome App",
  "short_name": "AwesomeApp",
  "description": "A progressive web application",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "orientation": "portrait-primary",
  "background_color": "#ffffff",
  "theme_color": "#007bff",
  "icons": [
    {
      "src": "/images/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/images/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any"
    },
    {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Web App Manifest](references/web-app-manifest.md) | Web App Manifest |
| [Service Worker Implementation](references/service-worker-implementation.md) | Service Worker Implementation |
| [Install Prompt and App Installation](references/install-prompt-and-app-installation.md) | Install Prompt and App Installation |
| [Offline Support with IndexedDB](references/offline-support-with-indexeddb.md) | Offline Support with IndexedDB |
| [Push Notifications](references/push-notifications.md) | Push Notifications |

## Best Practices

### ✅ DO

- Implement a cache-first strategy for static assets and network-first for API calls in your service worker
- Provide a meaningful offline fallback page with cached content and clear messaging
- Use `manifest.json` with all required fields (`name`, `short_name`, `start_url`, `display`, `icons`) to pass installability checks
- Version your service worker cache names and clean up old caches in the `activate` event
- Test the full install flow on real devices, including Add to Home Screen and offline behavior
- Precache critical app shell resources during the service worker `install` event

### ❌ DON'T

- Cache API responses indefinitely without a TTL or invalidation strategy
- Register a service worker that intercepts all requests without a proper routing strategy
- Forget to handle service worker update conflicts (stale tabs vs. new worker)
- Serve push notifications without user opt-in or a clear value proposition
