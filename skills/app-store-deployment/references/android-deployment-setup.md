# Android Deployment Setup

## Android Deployment Setup

```gradle
// build.gradle configuration
android {
  compileSdkVersion 33

  defaultConfig {
    applicationId "com.example.myapp"
    minSdkVersion 21
    targetSdkVersion 33
    versionCode 1
    versionName "1.0.0"
  }

  signingConfigs {
    release {
      storeFile file("keystore.jks")
      storePassword System.getenv("KEYSTORE_PASSWORD")
      keyAlias System.getenv("KEY_ALIAS")
      keyPassword System.getenv("KEY_PASSWORD")
    }
  }

  buildTypes {
    release {
      signingConfig signingConfigs.release
      minifyEnabled true
      shrinkResources true
      proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
    }
  }
}

dependencies {
  implementation 'com.google.android.play:core:1.10.3'
}
```

```bash
# Create keystore for app signing
keytool -genkey -v \
  -keystore ~/my-release-key.jks \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10950 \
  -alias my-key-alias

# Build App Bundle
./gradlew bundleRelease

# Build APK for testing
./gradlew assembleRelease

# Verify APK signature
jarsigner -verify -verbose -certs app/build/outputs/apk/release/app-release.apk
```
