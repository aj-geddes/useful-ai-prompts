---
name: push-notification-setup
description: Implement push notifications for iOS and Android. Covers Firebase Cloud Messaging, Apple Push Notification service, handling notifications, and backend integration.
---

# Push Notification Setup

## Overview

Implement comprehensive push notification systems for iOS and Android applications using Firebase Cloud Messaging and native platform services.

## When to Use

- Sending real-time notifications to users
- Implementing user engagement features
- Deep linking from notifications to specific screens
- Handling silent/background notifications
- Tracking notification analytics

## Instructions

### 1. **Firebase Cloud Messaging Setup**

```javascript
import messaging from '@react-native-firebase/messaging';
import { Platform } from 'react-native';

export async function initializeFirebase() {
  try {
    if (Platform.OS === 'ios') {
      const permission = await messaging().requestPermission();
      if (permission === messaging.AuthorizationStatus.AUTHORIZED) {
        console.log('iOS notification permission granted');
      }
    }

    const token = await messaging().getToken();
    console.log('FCM Token:', token);
    await saveTokenToBackend(token);

    messaging().onTokenRefresh(async (newToken) => {
      await saveTokenToBackend(newToken);
    });

    messaging().onMessage(async (remoteMessage) => {
      console.log('Notification received:', remoteMessage);
      showLocalNotification(remoteMessage);
    });

    messaging().setBackgroundMessageHandler(async (remoteMessage) => {
      if (remoteMessage.data?.type === 'sync') {
        syncData();
      }
    });

    messaging()
      .getInitialNotification()
      .then((remoteMessage) => {
        if (remoteMessage) {
          handleNotificationOpen(remoteMessage);
        }
      });

    messaging().onNotificationOpenedApp((remoteMessage) => {
      handleNotificationOpen(remoteMessage);
    });
  } catch (error) {
    console.error('Firebase initialization failed:', error);
  }
}

export async function saveTokenToBackend(token) {
  try {
    const response = await fetch('https://api.example.com/device-tokens', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        token,
        platform: Platform.OS,
        timestamp: new Date().toISOString()
      })
    });
    if (!response.ok) {
      console.error('Failed to save token');
    }
  } catch (error) {
    console.error('Error saving token:', error);
  }
}

function handleNotificationOpen(remoteMessage) {
  const { data } = remoteMessage;
  if (data?.deepLink) {
    navigationRef.navigate(data.deepLink, JSON.parse(data.params || '{}'));
  }
}
```

### 2. **iOS Native Setup with Swift**

```swift
import UIKit
import UserNotifications

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    requestNotificationPermission()

    if let remoteNotification = launchOptions?[.remoteNotification] as? [AnyHashable: Any] {
      handlePushNotification(remoteNotification)
    }

    return true
  }

  func requestNotificationPermission() {
    UNUserNotificationCenter.current().requestAuthorization(
      options: [.alert, .sound, .badge]
    ) { granted, error in
      if granted {
        DispatchQueue.main.async {
          UIApplication.shared.registerForRemoteNotifications()
        }
      }
    }
  }

  func application(
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
  ) {
    let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()
    print("Device Token: \(token)")
    saveTokenToBackend(token: token)
  }

  func application(
    _ application: UIApplication,
    didFailToRegisterForRemoteNotificationsWithError error: Error
  ) {
    print("Failed to register: \(error)")
  }

  func userNotificationCenter(
    _ center: UNUserNotificationCenter,
    willPresent notification: UNNotification,
    withCompletionHandler completionHandler:
      @escaping (UNNotificationPresentationOptions) -> Void
  ) {
    let userInfo = notification.request.content.userInfo
    if #available(iOS 14.0, *) {
      completionHandler([.banner, .sound, .badge])
    } else {
      completionHandler([.sound, .badge])
    }
    handlePushNotification(userInfo)
  }

  func userNotificationCenter(
    _ center: UNUserNotificationCenter,
    didReceive response: UNNotificationResponse,
    withCompletionHandler completionHandler: @escaping () -> Void
  ) {
    let userInfo = response.notification.request.content.userInfo
    handlePushNotification(userInfo)
    completionHandler()
  }

  private func handlePushNotification(_ userInfo: [AnyHashable: Any]) {
    if let deepLink = userInfo["deepLink"] as? String {
      NotificationCenter.default.post(
        name: NSNotification.Name("openDeepLink"),
        object: deepLink
      )
    }
  }

  private func saveTokenToBackend(token: String) {
    let urlString = "https://api.example.com/device-tokens"
    guard let url = URL(string: urlString) else { return }

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    let body: [String: Any] = ["token": token, "platform": "ios"]
    request.httpBody = try? JSONSerialization.data(withJSONObject: body)

    URLSession.shared.dataTask(with: request).resume()
  }
}
```

### 3. **Android Setup with Kotlin**

```kotlin
// AndroidManifest.xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
  <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
  <application>
    <service
      android:name=".services.MyFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>

import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Intent
import android.os.Build
import androidx.core.app.NotificationCompat
import com.google.firebase.messaging.FirebaseMessagingService
import com.google.firebase.messaging.RemoteMessage

class MyFirebaseMessagingService : FirebaseMessagingService() {
  override fun onNewToken(token: String) {
    super.onNewToken(token)
    println("FCM Token: $token")
    saveTokenToBackend(token)
  }

  override fun onMessageReceived(remoteMessage: RemoteMessage) {
    super.onMessageReceived(remoteMessage)

    val title = remoteMessage.notification?.title ?: "Notification"
    val body = remoteMessage.notification?.body ?: ""
    val deepLink = remoteMessage.data["deepLink"] ?: ""

    if (remoteMessage.notification != null) {
      showNotification(title, body, deepLink)
    }
  }

  private fun showNotification(title: String, message: String, deepLink: String = "") {
    val channelId = "default_channel"
    createNotificationChannel(channelId)

    val intent = Intent(this, MainActivity::class.java).apply {
      if (deepLink.isNotEmpty()) {
        data = android.net.Uri.parse(deepLink)
      }
      addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP)
    }

    val pendingIntent = PendingIntent.getActivity(
      this, 0, intent,
      PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
    )

    val notification = NotificationCompat.Builder(this, channelId)
      .setSmallIcon(R.drawable.ic_notification)
      .setContentTitle(title)
      .setContentText(message)
      .setAutoCancel(true)
      .setContentIntent(pendingIntent)
      .setPriority(NotificationCompat.PRIORITY_DEFAULT)
      .build()

    val notificationManager = getSystemService(NOTIFICATION_SERVICE) as NotificationManager
    notificationManager.notify(System.currentTimeMillis().toInt(), notification)
  }

  private fun createNotificationChannel(channelId: String) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
      val channel = NotificationChannel(
        channelId,
        "Default Channel",
        NotificationManager.IMPORTANCE_DEFAULT
      )
      val notificationManager = getSystemService(NOTIFICATION_SERVICE) as NotificationManager
      notificationManager.createNotificationChannel(channel)
    }
  }

  private fun saveTokenToBackend(token: String) {
    println("Saving token to backend: $token")
  }
}
```

### 4. **Flutter Implementation**

```dart
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/material.dart';

class NotificationHandler {
  static Future<void> initialize(NavigatorState navigator) async {
    final settings = await FirebaseMessaging.instance.requestPermission(
      alert: true,
      sound: true,
      badge: true,
    );

    if (settings.authorizationStatus == AuthorizationStatus.authorized) {
      print('Notification permission granted');
    }

    final token = await FirebaseMessaging.instance.getToken();
    print('FCM Token: $token');

    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      print('Received: ${message.notification?.title}');
    });

    FirebaseMessaging.onMessageOpenedApp.listen((RemoteMessage message) {
      _handleDeepLink(navigator, message.data);
    });

    final initialMessage = await FirebaseMessaging.instance.getInitialMessage();
    if (initialMessage != null) {
      _handleDeepLink(navigator, initialMessage.data);
    }
  }

  static void _handleDeepLink(NavigatorState navigator, Map<String, dynamic> data) {
    final deepLink = data['deepLink'] as String?;
    if (deepLink != null) {
      navigator.pushNamed(deepLink);
    }
  }
}
```

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
