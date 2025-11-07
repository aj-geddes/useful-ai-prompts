---
name: app-store-deployment
description: Deploy iOS and Android apps to App Store and Google Play. Covers signing, versioning, build configuration, submission process, and release management.
---

# App Store Deployment

## Overview

Publish mobile applications to official app stores with proper code signing, versioning, testing, and submission procedures.

## When to Use

- Publishing apps to App Store and Google Play
- Managing app versions and releases
- Configuring signing certificates and provisioning profiles
- Automating build and deployment processes
- Managing app updates and rollouts

## Instructions

### 1. **iOS Deployment Setup**

```bash
# Create development and distribution signing certificates
# Step 1: Generate Certificate Signing Request (CSR) in Keychain Access
# Step 2: Create App ID in Apple Developer Portal
# Step 3: Create provisioning profiles (Development, Distribution)

# Xcode configuration for signing
# Set Team ID, Bundle Identifier, and select provisioning profiles
# Build Settings:
# - Code Sign Identity: "iPhone Distribution"
# - Provisioning Profile: Select appropriate profile
# - Code Sign Style: Automatic (recommended)

# Info.plist settings
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleShortVersionString</key>
  <string>1.0.0</string>
  <key>CFBundleVersion</key>
  <string>1</string>
  <key>NSAppTransportSecurity</key>
  <dict>
    <key>NSAllowsArbitraryLoads</key>
    <false/>
  </dict>
  <key>NSUserTrackingUsageDescription</key>
  <string>We use tracking for analytics</string>
</dict>
</plist>

# Build for App Store submission
xcodebuild -workspace MyApp.xcworkspace \
  -scheme MyApp \
  -configuration Release \
  -archivePath ~/Desktop/MyApp.xcarchive \
  archive

# Export for distribution
xcodebuild -exportArchive \
  -archivePath ~/Desktop/MyApp.xcarchive \
  -exportOptionsPlist ExportOptions.plist \
  -exportPath ~/Desktop/MyApp

# ExportOptions.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>teamID</key>
  <string>YOUR_TEAM_ID</string>
  <key>signingStyle</key>
  <string>automatic</string>
  <key>method</key>
  <string>app-store</string>
</dict>
</plist>

# Upload to App Store
xcrun altool --upload-app --file MyApp.ipa \
  --type ios \
  -u your-apple-id@example.com \
  -p your-app-specific-password
```

### 2. **Android Deployment Setup**

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

### 3. **Version Management**

```bash
# Version tracking
# package.json
{
  "name": "myapp",
  "version": "1.0.0",
  "build": {
    "ios": { "buildNumber": "1" },
    "android": { "versionCode": 1 }
  }
}

# Increment version script
#!/bin/bash
CURRENT=$(jq -r '.version' package.json)
IFS='.' read -ra VER <<< "$CURRENT"

MAJOR=${VER[0]}
MINOR=${VER[1]}
PATCH=${VER[2]}

PATCH=$((PATCH + 1))
NEW_VERSION="$MAJOR.$MINOR.$PATCH"

jq ".version = \"$NEW_VERSION\"" package.json > package.json.tmp
mv package.json.tmp package.json

echo "Version updated to $NEW_VERSION"
```

### 4. **Automated CI/CD with GitHub Actions**

```yaml
name: Deploy to App Stores

on:
  push:
    tags:
      - 'v*'

jobs:
  build-ios:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm install

      - name: Build iOS App
        run: |
          cd ios
          pod install
          xcodebuild -workspace MyApp.xcworkspace \
            -scheme MyApp \
            -configuration Release \
            -archivePath ~/Desktop/MyApp.xcarchive \
            archive

      - name: Upload to App Store
        env:
          APPLE_ID: ${{ secrets.APPLE_ID }}
          APPLE_PASSWORD: ${{ secrets.APPLE_PASSWORD }}
        run: |
          xcrun altool --upload-app \
            --file MyApp.ipa \
            --type ios \
            -u $APPLE_ID \
            -p $APPLE_PASSWORD

  build-android:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Java
        uses: actions/setup-java@v3
        with:
          java-version: '11'

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm install

      - name: Build Android App
        env:
          KEYSTORE_PASSWORD: ${{ secrets.KEYSTORE_PASSWORD }}
          KEY_ALIAS: ${{ secrets.KEY_ALIAS }}
          KEY_PASSWORD: ${{ secrets.KEY_PASSWORD }}
        run: |
          cd android
          ./gradlew bundleRelease

      - name: Upload to Google Play
        uses: r0adkll/upload-google-play@v1
        with:
          serviceAccountJsonPlainText: ${{ secrets.PLAY_STORE_SERVICE_ACCOUNT }}
          packageName: com.example.myapp
          releaseFiles: android/app/build/outputs/bundle/release/app.aab
          track: internal
          status: completed

  create-release:
    runs-on: ubuntu-latest
    needs: [build-ios, build-android]
    steps:
      - uses: actions/checkout@v3

      - name: Create GitHub Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          body: Release notes here
          draft: false
          prerelease: false
```

### 5. **Pre-Deployment Checklist**

```markdown
# iOS Checklist
- [ ] Increment version (CFBundleShortVersionString)
- [ ] Update build number (CFBundleVersion)
- [ ] Run all tests (>80% coverage)
- [ ] Test on minimum iOS version
- [ ] Review crash logs
- [ ] Check for deprecated APIs
- [ ] Verify all permissions documented
- [ ] Test offline functionality
- [ ] Verify app icon (1024x1024)
- [ ] Set privacy policy URL
- [ ] Archive and verify build
- [ ] Test on real devices

# Android Checklist
- [ ] Increment versionCode and versionName
- [ ] Run all tests (>80% coverage)
- [ ] Test on API 21+ devices
- [ ] Verify navigation
- [ ] Check battery optimization
- [ ] Enable app signing
- [ ] Build release AAB
- [ ] Verify ProGuard obfuscation
- [ ] Test landscape/portrait
- [ ] Upload screenshots
- [ ] Add release notes
- [ ] Test on multiple devices
```

## Best Practices

### ✅ DO
- Use signed certificates and provisioning profiles
- Automate builds with CI/CD
- Test on real devices before submission
- Keep version numbers consistent
- Document deployment procedures
- Use environment-specific configurations
- Implement proper error tracking
- Monitor app performance post-launch
- Plan rollout strategy
- Keep backup of signing materials
- Test offline functionality
- Maintain release notes

### ❌ DON'T
- Commit signing materials to git
- Skip device testing
- Release untested code
- Ignore store policies
- Use hardcoded API keys
- Skip security reviews
- Deploy without monitoring
- Ignore crash reports
- Make large version jumps
- Use invalid certificates
- Deploy without backups
- Release during holidays
