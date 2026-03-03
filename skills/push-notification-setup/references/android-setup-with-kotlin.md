# Android Setup with Kotlin

## Android Setup with Kotlin

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
