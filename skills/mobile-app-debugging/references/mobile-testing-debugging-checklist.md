# Mobile Testing & Debugging Checklist

## Mobile Testing & Debugging Checklist

```yaml
Device Testing:

[ ] Test on both iOS and Android
[ ] Test on old and new devices
[ ] Test with poor network (3G throttle)
[ ] Test in airplane mode
[ ] Test with low battery
[ ] Test with low memory
[ ] Test with location disabled
[ ] Test with notifications disabled
[ ] Test rotation changes
[ ] Test while backgrounded

Performance:

[ ] <16ms per frame (60 FPS)
[ ] Memory usage <100MB
[ ] Battery drain acceptable
[ ] Network requests efficient
[ ] Background tasks minimal

Networking:

[ ] Works on WiFi
[ ] Works on cellular
[ ] Handles network timeouts
[ ] Handles offline mode
[ ] Retries failed requests
[ ] Shows loading indicators
[ ] Shows error messages

UI/UX:

[ ] Responsive touch targets (44x44 min)
[ ] Readable text (16pt minimum)
[ ] Colors accessible
[ ] Orientation changes handled
[ ] Keyboard shows/hides correctly
[ ] Safe areas respected (notches)

---

Tools:

Testing Devices:
  - iOS: iPhone SE (small), iPhone 12/13 (modern)
  - Android: Pixel 4 (standard), Pixel 6 (new)
  - Virtual: Simulators for iteration

Device Management:
  - TestFlight (iOS)
  - Google Play Beta (Android)
  - Firebase Test Lab
  - BrowserStack

Monitoring:
  - Crashlytics
  - Firebase Analytics
  - App Performance Monitoring
  - Custom event tracking
```
