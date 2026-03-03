# Firebase Cloud Messaging Setup

## Firebase Cloud Messaging Setup

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

    messaging().setBackgroundMessageHandler(async (remoteMessage) => {
      if (remoteMessage.data?.type === "sync") {
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
    console.error("Firebase initialization failed:", error);
  }
}

export async function saveTokenToBackend(token) {
  try {
    const response = await fetch("https://api.example.com/device-tokens", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        token,
        platform: Platform.OS,
        timestamp: new Date().toISOString(),
      }),
    });
    if (!response.ok) {
      console.error("Failed to save token");
    }
  } catch (error) {
    console.error("Error saving token:", error);
  }
}

function handleNotificationOpen(remoteMessage) {
  const { data } = remoteMessage;
  if (data?.deepLink) {
    navigationRef.navigate(data.deepLink, JSON.parse(data.params || "{}"));
  }
}
```
