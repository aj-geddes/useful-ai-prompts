---
name: internationalization-i18n
description: Implement internationalization (i18n) and localization including message extraction, translation catalogs, pluralization rules, date/time/number formatting, RTL language support, and i18n libraries like i18next and gettext. Use for multi-language, translation, or localization needs.
---

# Internationalization (i18n) & Localization

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

## Instructions

### 1. **i18next (JavaScript/TypeScript)**

#### Basic Setup
```typescript
// i18n.ts
import i18next from 'i18next';
import Backend from 'i18next-http-backend';
import LanguageDetector from 'i18next-browser-languagedetector';

await i18next
  .use(Backend)
  .use(LanguageDetector)
  .init({
    fallbackLng: 'en',
    debug: process.env.NODE_ENV === 'development',

    interpolation: {
      escapeValue: false // React already escapes
    },

    backend: {
      loadPath: '/locales/{{lng}}/{{ns}}.json'
    },

    detection: {
      order: ['querystring', 'cookie', 'localStorage', 'navigator'],
      caches: ['localStorage', 'cookie']
    }
  });

export default i18next;
```

#### Translation Files
```json
// locales/en/translation.json
{
  "welcome": "Welcome to our app",
  "greeting": "Hello, {{name}}!",
  "itemCount": "You have {{count}} item",
  "itemCount_plural": "You have {{count}} items",
  "user": {
    "profile": "User Profile",
    "settings": "Settings",
    "logout": "Log out"
  },
  "validation": {
    "required": "This field is required",
    "email": "Please enter a valid email",
    "minLength": "Must be at least {{min}} characters"
  }
}

// locales/es/translation.json
{
  "welcome": "Bienvenido a nuestra aplicación",
  "greeting": "¡Hola, {{name}}!",
  "itemCount": "Tienes {{count}} artículo",
  "itemCount_plural": "Tienes {{count}} artículos",
  "user": {
    "profile": "Perfil de Usuario",
    "settings": "Configuración",
    "logout": "Cerrar sesión"
  },
  "validation": {
    "required": "Este campo es obligatorio",
    "email": "Por favor ingrese un correo válido",
    "minLength": "Debe tener al menos {{min}} caracteres"
  }
}

// locales/fr/translation.json
{
  "welcome": "Bienvenue dans notre application",
  "greeting": "Bonjour, {{name}} !",
  "itemCount": "Vous avez {{count}} article",
  "itemCount_plural": "Vous avez {{count}} articles",
  "user": {
    "profile": "Profil utilisateur",
    "settings": "Paramètres",
    "logout": "Se déconnecter"
  }
}
```

#### React Integration
```typescript
// App.tsx
import { useTranslation } from 'react-i18next';
import './i18n';

export function App() {
  const { t, i18n } = useTranslation();

  const changeLanguage = (lng: string) => {
    i18n.changeLanguage(lng);
  };

  return (
    <div>
      <h1>{t('welcome')}</h1>
      <p>{t('greeting', { name: 'John' })}</p>
      <p>{t('itemCount', { count: 5 })}</p>

      {/* Language switcher */}
      <select
        value={i18n.language}
        onChange={(e) => changeLanguage(e.target.value)}
      >
        <option value="en">English</option>
        <option value="es">Español</option>
        <option value="fr">Français</option>
      </select>
    </div>
  );
}

// Component with namespace
export function UserProfile() {
  const { t } = useTranslation('user');

  return (
    <div>
      <h2>{t('profile')}</h2>
      <button>{t('logout')}</button>
    </div>
  );
}
```

#### Node.js/Express Backend
```typescript
// i18n-middleware.ts
import i18next from 'i18next';
import Backend from 'i18next-fs-backend';
import middleware from 'i18next-http-middleware';

i18next
  .use(Backend)
  .use(middleware.LanguageDetector)
  .init({
    fallbackLng: 'en',
    preload: ['en', 'es', 'fr'],
    backend: {
      loadPath: './locales/{{lng}}/{{ns}}.json'
    }
  });

export const i18nMiddleware = middleware.handle(i18next);

// app.ts
import express from 'express';
import { i18nMiddleware } from './i18n-middleware';

const app = express();
app.use(i18nMiddleware);

app.get('/api/welcome', (req, res) => {
  res.json({
    message: req.t('welcome'),
    greeting: req.t('greeting', { name: 'User' })
  });
});
```

### 2. **React-Intl (Format.js)**

```typescript
// IntlProvider setup
import { IntlProvider } from 'react-intl';
import messages_en from './translations/en.json';
import messages_es from './translations/es.json';

const messages = {
  en: messages_en,
  es: messages_es
};

export function App() {
  const [locale, setLocale] = useState('en');

  return (
    <IntlProvider locale={locale} messages={messages[locale]}>
      <YourApp />
    </IntlProvider>
  );
}

// Using translations
import { FormattedMessage, useIntl } from 'react-intl';

export function Welcome() {
  const intl = useIntl();

  return (
    <div>
      {/* Basic translation */}
      <h1>
        <FormattedMessage id="welcome" defaultMessage="Welcome" />
      </h1>

      {/* With variables */}
      <p>
        <FormattedMessage
          id="greeting"
          defaultMessage="Hello, {name}!"
          values={{ name: 'John' }}
        />
      </p>

      {/* Pluralization */}
      <p>
        <FormattedMessage
          id="itemCount"
          defaultMessage="{count, plural, =0 {No items} one {# item} other {# items}}"
          values={{ count: 5 }}
        />
      </p>

      {/* In code */}
      <button title={intl.formatMessage({ id: 'submit' })}>
        {intl.formatMessage({ id: 'submit' })}
      </button>
    </div>
  );
}
```

### 3. **Python i18n (gettext)**

```python
# i18n.py
import gettext
import os

class I18n:
    def __init__(self, locale='en', domain='messages'):
        self.locale = locale
        self.domain = domain
        self._translator = None
        self._load_translations()

    def _load_translations(self):
        locale_dir = os.path.join(os.path.dirname(__file__), 'locales')
        try:
            self._translator = gettext.translation(
                self.domain,
                localedir=locale_dir,
                languages=[self.locale]
            )
        except FileNotFoundError:
            # Fall back to NullTranslations (no translation)
            self._translator = gettext.NullTranslations()

    def t(self, message, **kwargs):
        """Translate message with optional variable substitution"""
        translated = self._translator.gettext(message)
        if kwargs:
            return translated.format(**kwargs)
        return translated

    def tn(self, singular, plural, n, **kwargs):
        """Translate with pluralization"""
        translated = self._translator.ngettext(singular, plural, n)
        if kwargs:
            return translated.format(n=n, **kwargs)
        return translated

# Usage
i18n = I18n(locale='es')

print(i18n.t("Welcome to our app"))
print(i18n.t("Hello, {name}!", name="Juan"))
print(i18n.tn("You have {n} item", "You have {n} items", 5))
```

```python
# Extracting messages for translation
# Install: pip install Babel

# babel.cfg
[python: **.py]

# Extract messages
# pybabel extract -F babel.cfg -o locales/messages.pot .

# Initialize new language
# pybabel init -i locales/messages.pot -d locales -l es

# Compile translations
# pybabel compile -d locales
```

### 4. **Date and Time Formatting**

#### JavaScript (Intl API)
```typescript
// date-formatter.ts
export class DateFormatter {
  constructor(private locale: string) {}

  // Format date
  formatDate(date: Date, options?: Intl.DateTimeFormatOptions): string {
    return new Intl.DateTimeFormat(this.locale, options).format(date);
  }

  // Predefined formats
  short(date: Date): string {
    return this.formatDate(date, {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  }

  long(date: Date): string {
    return this.formatDate(date, {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      weekday: 'long'
    });
  }

  time(date: Date): string {
    return this.formatDate(date, {
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    });
  }

  relative(date: Date): string {
    const rtf = new Intl.RelativeTimeFormat(this.locale, { numeric: 'auto' });
    const diff = date.getTime() - Date.now();
    const days = Math.round(diff / (1000 * 60 * 60 * 24));

    if (Math.abs(days) < 1) {
      const hours = Math.round(diff / (1000 * 60 * 60));
      return rtf.format(hours, 'hour');
    }

    return rtf.format(days, 'day');
  }
}

// Usage
const enFormatter = new DateFormatter('en-US');
const esFormatter = new DateFormatter('es-ES');
const jaFormatter = new DateFormatter('ja-JP');

const date = new Date('2024-01-15');

console.log(enFormatter.short(date));  // Jan 15, 2024
console.log(esFormatter.short(date));  // 15 ene 2024
console.log(jaFormatter.short(date));  // 2024年1月15日

console.log(enFormatter.relative(new Date(Date.now() - 86400000)));  // yesterday
```

#### React-Intl Date Formatting
```typescript
import { FormattedDate, FormattedTime, FormattedRelativeTime } from 'react-intl';

export function DateDisplay() {
  const date = new Date();

  return (
    <div>
      {/* Date */}
      <FormattedDate
        value={date}
        year="numeric"
        month="long"
        day="numeric"
      />

      {/* Time */}
      <FormattedTime value={date} />

      {/* Relative time */}
      <FormattedRelativeTime
        value={-1}
        unit="day"
        updateIntervalInSeconds={60}
      />
    </div>
  );
}
```

### 5. **Number and Currency Formatting**

```typescript
// number-formatter.ts
export class NumberFormatter {
  constructor(private locale: string) {}

  // Format number
  formatNumber(value: number, options?: Intl.NumberFormatOptions): string {
    return new Intl.NumberFormat(this.locale, options).format(value);
  }

  // Currency
  currency(value: number, currency: string): string {
    return this.formatNumber(value, {
      style: 'currency',
      currency
    });
  }

  // Percentage
  percent(value: number): string {
    return this.formatNumber(value, {
      style: 'percent',
      minimumFractionDigits: 0,
      maximumFractionDigits: 2
    });
  }

  // Decimal
  decimal(value: number, decimals: number = 2): string {
    return this.formatNumber(value, {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals
    });
  }

  // Compact notation (1.2K, 1.5M)
  compact(value: number): string {
    return this.formatNumber(value, {
      notation: 'compact',
      compactDisplay: 'short'
    });
  }
}

// Usage
const enFormatter = new NumberFormatter('en-US');
const deFormatter = new NumberFormatter('de-DE');
const jaFormatter = new NumberFormatter('ja-JP');

console.log(enFormatter.currency(1234.56, 'USD'));  // $1,234.56
console.log(deFormatter.currency(1234.56, 'EUR'));  // 1.234,56 €
console.log(jaFormatter.currency(1234.56, 'JPY'));  // ¥1,235

console.log(enFormatter.percent(0.1234));  // 12.34%
console.log(enFormatter.compact(1234567));  // 1.2M
```

### 6. **Pluralization Rules**

```typescript
// pluralization.ts
export class PluralRules {
  constructor(private locale: string) {}

  // Get plural category
  select(count: number): Intl.LDMLPluralRule {
    const pr = new Intl.PluralRules(this.locale);
    return pr.select(count);
  }

  // Format with pluralization
  format(count: number, forms: Record<Intl.LDMLPluralRule, string>): string {
    const rule = this.select(count);
    return forms[rule] || forms.other;
  }
}

// Usage
const enRules = new PluralRules('en');

console.log(enRules.format(0, {
  zero: 'No items',
  one: 'One item',
  other: '{{count}} items'
}));

console.log(enRules.format(1, {
  one: 'One item',
  other: '{{count}} items'
}));

// Different languages have different plural rules
const arRules = new PluralRules('ar'); // Arabic has 6 plural forms
const plRules = new PluralRules('pl'); // Polish has complex plural rules
```

#### ICU Message Format
```typescript
// Using intl-messageformat
import IntlMessageFormat from 'intl-messageformat';

const message = new IntlMessageFormat(
  '{count, plural, =0 {No items} one {# item} other {# items}}',
  'en'
);

console.log(message.format({ count: 0 }));  // No items
console.log(message.format({ count: 1 }));  // 1 item
console.log(message.format({ count: 5 }));  // 5 items

// With gender
const genderMessage = new IntlMessageFormat(
  '{gender, select, male {He} female {She} other {They}} bought {count, plural, one {# item} other {# items}}',
  'en'
);

console.log(genderMessage.format({ gender: 'female', count: 2 }));
// She bought 2 items
```

### 7. **RTL (Right-to-Left) Language Support**

```typescript
// rtl-utils.ts
const RTL_LANGUAGES = ['ar', 'he', 'fa', 'ur'];

export function isRTL(locale: string): boolean {
  const lang = locale.split('-')[0];
  return RTL_LANGUAGES.includes(lang);
}

export function getDirection(locale: string): 'ltr' | 'rtl' {
  return isRTL(locale) ? 'rtl' : 'ltr';
}
```

```css
/* styles/rtl.css */
:root {
  --text-align-start: left;
  --text-align-end: right;
  --margin-start: margin-left;
  --margin-end: margin-right;
  --padding-start: padding-left;
  --padding-end: padding-right;
}

[dir="rtl"] {
  --text-align-start: right;
  --text-align-end: left;
  --margin-start: margin-right;
  --margin-end: margin-left;
  --padding-start: padding-right;
  --padding-end: padding-left;
}

.container {
  text-align: var(--text-align-start);
  margin-left: var(--margin-start);
  padding-right: var(--padding-end);
}

/* Or use logical properties (modern approach) */
.modern-container {
  text-align: start;
  margin-inline-start: 1rem;
  padding-inline-end: 2rem;
}
```

```typescript
// RTL React component
import { useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { isRTL, getDirection } from './rtl-utils';

export function App() {
  const { i18n } = useTranslation();

  useEffect(() => {
    const direction = getDirection(i18n.language);
    document.documentElement.setAttribute('dir', direction);
    document.documentElement.setAttribute('lang', i18n.language);
  }, [i18n.language]);

  return (
    <div className="app">
      {/* Your app content */}
    </div>
  );
}
```

### 8. **Translation Management**

#### Message Extraction
```typescript
// extract-messages.ts
import { sync as globSync } from 'glob';
import fs from 'fs';

const TRANSLATION_PATTERN = /t\(['"]([^'"]+)['"]\)/g;

export function extractMessages(pattern: string): Set<string> {
  const messages = new Set<string>();
  const files = globSync(pattern);

  for (const file of files) {
    const content = fs.readFileSync(file, 'utf8');
    let match;

    while ((match = TRANSLATION_PATTERN.exec(content)) !== null) {
      messages.add(match[1]);
    }
  }

  return messages;
}

// Generate translation template
export function generateTemplate(messages: Set<string>): object {
  const template: Record<string, string> = {};

  for (const message of messages) {
    template[message] = message; // Default to English
  }

  return template;
}

// Usage
const messages = extractMessages('src/**/*.{ts,tsx}');
const template = generateTemplate(messages);

fs.writeFileSync(
  'locales/en/translation.json',
  JSON.stringify(template, null, 2)
);
```

#### Translation Status
```typescript
// check-translations.ts
export function checkTranslationStatus(
  baseLocale: object,
  targetLocale: object
): {
  missing: string[];
  extra: string[];
  coverage: number;
} {
  const baseKeys = new Set(Object.keys(baseLocale));
  const targetKeys = new Set(Object.keys(targetLocale));

  const missing = [...baseKeys].filter(key => !targetKeys.has(key));
  const extra = [...targetKeys].filter(key => !baseKeys.has(key));

  const coverage = (targetKeys.size / baseKeys.size) * 100;

  return { missing, extra, coverage };
}

// Usage
const enMessages = require('./locales/en/translation.json');
const esMessages = require('./locales/es/translation.json');

const status = checkTranslationStatus(enMessages, esMessages);
console.log(`Spanish translation coverage: ${status.coverage.toFixed(2)}%`);
console.log(`Missing keys: ${status.missing.join(', ')}`);
```

### 9. **Locale Detection**

```typescript
// locale-detector.ts
export class LocaleDetector {
  // Detect from browser
  static fromBrowser(): string {
    return navigator.language || navigator.languages[0] || 'en';
  }

  // Detect from URL
  static fromURL(): string | null {
    const params = new URLSearchParams(window.location.search);
    return params.get('lang') || params.get('locale');
  }

  // Detect from cookie
  static fromCookie(name: string = 'locale'): string | null {
    const match = document.cookie.match(new RegExp(`${name}=([^;]+)`));
    return match ? match[1] : null;
  }

  // Detect from localStorage
  static fromStorage(key: string = 'locale'): string | null {
    return localStorage.getItem(key);
  }

  // Detect with priority
  static detect(defaultLocale: string = 'en'): string {
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
    localStorage.setItem('locale', locale);
    document.cookie = `locale=${locale}; path=/; max-age=31536000`;
  }
}
```

### 10. **Server-Side i18n**

```typescript
// Next.js i18n configuration
// next.config.js
module.exports = {
  i18n: {
    locales: ['en', 'es', 'fr', 'de', 'ja'],
    defaultLocale: 'en',
    localeDetection: true
  }
};

// pages/index.tsx
import { GetStaticProps } from 'next';
import { useTranslation } from 'next-i18next';
import { serverSideTranslations } from 'next-i18next/serverSideTranslations';

export default function Home() {
  const { t } = useTranslation('common');

  return (
    <div>
      <h1>{t('welcome')}</h1>
    </div>
  );
}

export const getStaticProps: GetStaticProps = async ({ locale }) => {
  return {
    props: {
      ...(await serverSideTranslations(locale ?? 'en', ['common']))
    }
  };
};
```

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

## Common Patterns

### Pattern 1: Translation Hook
```typescript
export function useLocale() {
  const { i18n } = useTranslation();

  return {
    locale: i18n.language,
    changeLocale: (lng: string) => i18n.changeLanguage(lng),
    t: i18n.t,
    formatDate: (date: Date) => new DateFormatter(i18n.language).short(date),
    formatNumber: (num: number) => new NumberFormatter(i18n.language).formatNumber(num),
    formatCurrency: (amount: number, currency: string) =>
      new NumberFormatter(i18n.language).currency(amount, currency)
  };
}
```

### Pattern 2: Language Switcher Component
```typescript
export function LanguageSwitcher() {
  const { locale, changeLocale } = useLocale();

  const languages = [
    { code: 'en', name: 'English', nativeName: 'English' },
    { code: 'es', name: 'Spanish', nativeName: 'Español' },
    { code: 'fr', name: 'French', nativeName: 'Français' },
    { code: 'de', name: 'German', nativeName: 'Deutsch' }
  ];

  return (
    <select value={locale} onChange={(e) => changeLocale(e.target.value)}>
      {languages.map((lang) => (
        <option key={lang.code} value={lang.code}>
          {lang.nativeName}
        </option>
      ))}
    </select>
  );
}
```

## Tools & Resources

- **i18next**: Comprehensive i18n framework
- **react-intl (Format.js)**: React i18n library
- **LinguiJS**: Developer-friendly i18n
- **vue-i18n**: Vue.js i18n plugin
- **Crowdin**: Translation management platform
- **Lokalise**: Localization management
- **Phrase**: Localization platform
- **POEditor**: Translation management
- **BabelEdit**: Translation editor
- **Pseudolocalization**: Testing tool
