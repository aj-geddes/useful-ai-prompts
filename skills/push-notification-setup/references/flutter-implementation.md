# Flutter Implementation

## Flutter Implementation

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
