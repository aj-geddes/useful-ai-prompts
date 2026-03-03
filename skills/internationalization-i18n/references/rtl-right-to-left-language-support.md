# RTL (Right-to-Left) Language Support

## RTL (Right-to-Left) Language Support

```typescript
// rtl-utils.ts
const RTL_LANGUAGES = ["ar", "he", "fa", "ur"];

export function isRTL(locale: string): boolean {
  const lang = locale.split("-")[0];
  return RTL_LANGUAGES.includes(lang);
}

export function getDirection(locale: string): "ltr" | "rtl" {
  return isRTL(locale) ? "rtl" : "ltr";
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
