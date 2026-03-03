# SMACSS (Scalable and Modular Architecture for CSS)

## SMACSS (Scalable and Modular Architecture for CSS)

```css
/* 1. Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
  font-family:
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #333;
  line-height: 1.6;
}

body {
  background-color: #fff;
}

a {
  color: #007bff;
  text-decoration: none;
}

/* 2. Layout Styles */
.layout-main {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20px;
  padding: 20px;
}

.layout-header {
  padding: 16px;
  background-color: #333;
  color: white;
}

.layout-sidebar {
  width: 250px;
  background-color: #f5f5f5;
  padding: 16px;
}

/* 3. Module Styles */
.module-card {
  padding: 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.module-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.module-form__input {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* 4. State Styles */
.is-hidden {
  display: none;
}

.is-active {
  background-color: #007bff;
  color: white;
}

.is-disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.is-error {
  border-color: #dc3545;
  color: #dc3545;
}

/* 5. Theme Styles */
.theme-dark {
  background-color: #222;
  color: #fff;
}

.theme-dark .module-card {
  border-color: #444;
}
```
