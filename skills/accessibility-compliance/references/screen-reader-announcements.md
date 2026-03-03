# Screen Reader Announcements

## Screen Reader Announcements

```typescript
class ScreenReaderAnnouncer {
  private liveRegion: HTMLElement;

  constructor() {
    this.liveRegion = this.createLiveRegion();
  }

  private createLiveRegion(): HTMLElement {
    const region = document.createElement("div");
    region.setAttribute("role", "status");
    region.setAttribute("aria-live", "polite");
    region.setAttribute("aria-atomic", "true");
    region.className = "sr-only";
    region.style.cssText = `
      position: absolute;
      left: -10000px;
      width: 1px;
      height: 1px;
      overflow: hidden;
    `;
    document.body.appendChild(region);
    return region;
  }

  announce(message: string, priority: "polite" | "assertive" = "polite"): void {
    this.liveRegion.setAttribute("aria-live", priority);

    // Clear then set message to ensure announcement
    this.liveRegion.textContent = "";
    setTimeout(() => {
      this.liveRegion.textContent = message;
    }, 100);
  }

  cleanup(): void {
    this.liveRegion.remove();
  }
}

// Usage
const announcer = new ScreenReaderAnnouncer();

// Announce form validation error
announcer.announce("Email field is required", "assertive");

// Announce successful action
announcer.announce("Item added to cart", "polite");
```
