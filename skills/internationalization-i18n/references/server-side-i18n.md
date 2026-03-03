# Server-Side i18n

## Server-Side i18n

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
