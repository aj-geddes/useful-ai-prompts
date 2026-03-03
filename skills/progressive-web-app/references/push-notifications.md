# Push Notifications

## Push Notifications

```typescript
// services/pushNotification.ts
export async function subscribeToPushNotifications() {
  if (!("serviceWorker" in navigator) || !("PushManager" in window)) {
    console.log("Push notifications not supported");
    return;
  }

  try {
    const registration = await navigator.serviceWorker.ready;
    const subscription = await registration.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey: process.env.REACT_APP_VAPID_PUBLIC_KEY,
    });

    // Send subscription to server
    await fetch("/api/push-subscription", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(subscription),
    });

    return subscription;
  } catch (error) {
    console.error("Push subscription failed:", error);
  }
}

// service-worker.ts
self.addEventListener("push", (event: PushEvent) => {
  const data = event.data?.json() ?? {};
  const options: NotificationOptions = {
    title: data.title || "New Notification",
    body: data.message || "",
    icon: "/images/icon-192.png",
    badge: "/images/badge-72.png",
    tag: data.tag || "notification",
  };

  event.waitUntil(self.registration.showNotification(options.title, options));
});

self.addEventListener("notificationclick", (event: NotificationEvent) => {
  event.notification.close();
  event.waitUntil(
    self.clients.matchAll({ type: "window" }).then((clients) => {
      if (clients.length > 0) {
        return clients[0].focus();
      }
      return self.clients.openWindow("/");
    }),
  );
});
```
