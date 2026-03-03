# Python i18n (gettext)

## Python i18n (gettext)

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
