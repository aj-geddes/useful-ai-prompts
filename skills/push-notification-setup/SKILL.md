---
name: push-notification-setup
description: >
  Implement push notifications for iOS and Android. Covers Firebase Cloud
  Messaging, Apple Push Notification service, handling notifications, and
  backend integration.
---

# Push Notification Setup

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive push notification systems for iOS and Android applications using Firebase Cloud Messaging and native platform services.

## When to Use

- Sending real-time notifications to users
- Implementing user engagement features
- Deep linking from notifications to specific screens
- Handling silent/background notifications
- Tracking notification analytics

## Quick Start

Minimal working example:

```javascript
import messaging from "@react-native-firebase/messaging";
import { Platform } from "react-native";

export async function initializeFirebase() {
  try {
    if (Platform.OS === "ios") {
      const permission = await messaging().requestPermission();
      if (permission === messaging.AuthorizationStatus.AUTHORIZED) {
        console.log("iOS notification permission granted");
      }
    }

    const token = await messaging().getToken();
    console.log("FCM Token:", token);
    await saveTokenToBackend(token);

    messaging().onTokenRefresh(async (newToken) => {
      await saveTokenToBackend(newToken);
    });

    messaging().onMessage(async (remoteMessage) => {
      console.log("Notification received:", remoteMessage);
      showLocalNotification(remoteMessage);
    });

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Firebase Cloud Messaging Setup](references/firebase-cloud-messaging-setup.md) | Firebase Cloud Messaging Setup |
| [iOS Native Setup with Swift](references/ios-native-setup-with-swift.md) | iOS Native Setup with Swift |
| [Android Setup with Kotlin](references/android-setup-with-kotlin.md) | Android Setup with Kotlin |
| [Flutter Implementation](references/flutter-implementation.md) | Flutter Implementation |

## Best Practices

### ✅ DO

- Request permission before sending notifications
- Implement token refresh handling
- Use different notification channels by priority
- Validate tokens regularly
- Track notification delivery
- Implement deep linking
- Handle notifications in all app states
- Use silent notifications for data sync
- Store tokens securely on backend
- Provide user notification preferences
- Test on real devices

### ❌ DON'T

- Send excessive notifications
- Send without permission
- Store tokens insecurely
- Ignore notification failures
- Send sensitive data in payload
- Use notifications for spam
- Forget to handle background notifications
- Make blocking calls in handlers
- Send duplicate notifications
- Ignore user preferences
