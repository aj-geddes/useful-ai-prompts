---
name: app-store-deployment
description: >
  Deploy iOS and Android apps to App Store and Google Play. Covers signing,
  versioning, build configuration, submission process, and release management.
---

# App Store Deployment

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Publish mobile applications to official app stores with proper code signing, versioning, testing, and submission procedures.

## When to Use

- Publishing apps to App Store and Google Play
- Managing app versions and releases
- Configuring signing certificates and provisioning profiles
- Automating build and deployment processes
- Managing app updates and rollouts

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [iOS Deployment Setup](references/ios-deployment-setup.md) | iOS Deployment Setup |
| [Android Deployment Setup](references/android-deployment-setup.md) | Android Deployment Setup |
| [Version Management](references/version-management.md) | Version Management |
| [Automated CI/CD with GitHub Actions](references/automated-cicd-with-github-actions.md) | Automated CI/CD with GitHub Actions |
| [Pre-Deployment Checklist](references/pre-deployment-checklist.md) | Pre-Deployment Checklist |

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
