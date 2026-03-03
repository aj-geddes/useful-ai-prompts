# Locale Detection

## Locale Detection

```typescript
// locale-detector.ts
export class LocaleDetector {
  // Detect from browser
  static fromBrowser(): string {
    return navigator.language || navigator.languages[0] || "en";
  }

  // Detect from URL
  static fromURL(): string | null {
    const params = new URLSearchParams(window.location.search);
    return params.get("lang") || params.get("locale");
  }

  // Detect from cookie
  static fromCookie(name: string = "locale"): string | null {
    const match = document.cookie.match(new RegExp(`${name}=([^;]+)`));
    return match ? match[1] : null;
  }

  // Detect from localStorage
  static fromStorage(key: string = "locale"): string | null {
    return localStorage.getItem(key);
  }

  // Detect with priority
  static detect(defaultLocale: string = "en"): string {
    return (
      this.fromURL() ||
      this.fromStorage() ||
      this.fromCookie() ||
      this.fromBrowser() ||
      defaultLocale
    );
  }

  // Save locale
  static save(locale: string): void {
    localStorage.setItem("locale", locale);
    document.cookie = `locale=${locale}; path=/; max-age=31536000`;
  }
}
```
