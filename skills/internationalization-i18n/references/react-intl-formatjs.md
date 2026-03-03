# React-Intl (Format.js)

## React-Intl (Format.js)

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
