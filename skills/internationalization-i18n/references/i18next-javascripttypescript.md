# i18next (JavaScript/TypeScript)

## i18next (JavaScript/TypeScript)

### Basic Setup

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

export default i18next;
```

### Translation Files

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

### React Integration

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

### Node.js/Express Backend

```typescript
// i18n-middleware.ts
import i18next from "i18next";
import Backend from "i18next-fs-backend";
import middleware from "i18next-http-middleware";

i18next
  .use(Backend)
  .use(middleware.LanguageDetector)
  .init({
    fallbackLng: "en",
    preload: ["en", "es", "fr"],
    backend: {
      loadPath: "./locales/{{lng}}/{{ns}}.json",
    },
  });

export const i18nMiddleware = middleware.handle(i18next);

// app.ts
import express from "express";
import { i18nMiddleware } from "./i18n-middleware";

const app = express();
app.use(i18nMiddleware);

app.get("/api/welcome", (req, res) => {
  res.json({
    message: req.t("welcome"),
    greeting: req.t("greeting", { name: "User" }),
  });
});
```
