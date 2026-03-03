# iOS Deployment Setup

## iOS Deployment Setup

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
