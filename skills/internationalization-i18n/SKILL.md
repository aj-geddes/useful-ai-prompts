---
name: internationalization-i18n
description: >
  Implement internationalization (i18n) and localization including message
  extraction, translation catalogs, pluralization rules, date/time/number
  formatting, RTL language support, and i18n libraries like i18next and gettext.
  Use for multi-language, translation, or localization needs.
---

# Internationalization (i18n) & Localization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Comprehensive guide to implementing internationalization and localization in applications. Covers message translation, pluralization, date/time/number formatting, RTL languages, and integration with popular i18n libraries.

## When to Use

- Building multi-language applications
- Supporting international users
- Implementing language switching
- Formatting dates, times, and numbers for different locales
- Supporting RTL (right-to-left) languages
- Extracting and managing translation strings
- Implementing pluralization rules
- Setting up translation workflows

## Quick Start

Minimal working example:

```typescript
// i18n.ts
import i18next from "i18next";
import Backend from "i18next-http-backend";
import LanguageDetector from "i18next-browser-languagedetector";

await i18next
  .use(Backend)
  .use(LanguageDetector)
  .init({
    fallbackLng: "en",
    debug: process.env.NODE_ENV === "development",

    interpolation: {
      escapeValue: false, // React already escapes
    },

    backend: {
      loadPath: "/locales/{{lng}}/{{ns}}.json",
    },

    detection: {
      order: ["querystring", "cookie", "localStorage", "navigator"],
      caches: ["localStorage", "cookie"],
    },
  });
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [i18next (JavaScript/TypeScript)](references/i18next-javascripttypescript.md) | i18next (JavaScript/TypeScript) |
| [React-Intl (Format.js)](references/react-intl-formatjs.md) | React-Intl (Format.js) |
| [Python i18n (gettext)](references/python-i18n-gettext.md) | Python i18n (gettext) |
| [Date and Time Formatting](references/date-and-time-formatting.md) | Date and Time Formatting |
| [Number and Currency Formatting](references/number-and-currency-formatting.md) | Number and Currency Formatting |
| [Pluralization Rules](references/pluralization-rules.md) | Pluralization Rules |
| [RTL (Right-to-Left) Language Support](references/rtl-right-to-left-language-support.md) | RTL (Right-to-Left) Language Support |
| [Translation Management](references/translation-management.md) | Translation Management |
| [Locale Detection](references/locale-detection.md) | Locale Detection |
| [Server-Side i18n](references/server-side-i18n.md) | Server-Side i18n |

## Best Practices

### ✅ DO

- Extract all user-facing strings to translation files
- Use ICU message format for complex messages
- Support pluralization correctly for each language
- Use locale-aware date/time/number formatting
- Implement RTL support for Arabic, Hebrew, etc.
- Provide fallback language (usually English)
- Use namespaces to organize translations
- Test with pseudo-localization (ääçćëńţś)
- Store locale preference (cookie, localStorage)
- Use professional translators for production
- Implement translation management workflow
- Support dynamic locale switching
- Use translation memory tools

### ❌ DON'T

- Hardcode user-facing strings in code
- Concatenate translated strings
- Assume English grammar rules apply to all languages
- Use generic plural forms (one/many) for all languages
- Forget about text expansion (German is ~30% longer)
- Store dates/times in locale-specific formats
- Use flags to represent languages (flag ≠ language)
- Translate technical terms without context
- Mix translation keys with UI strings
- Forget to translate alt text, titles, placeholders
- Assume left-to-right layout
