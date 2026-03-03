# BEM (Block Element Modifier) Pattern

## BEM (Block Element Modifier) Pattern

```css
/* Block - standalone component */
.button {
  display: inline-block;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
}

/* Element - component part */
.button__icon {
  margin-right: 8px;
  vertical-align: middle;
}

/* Modifier - variant */
.button--primary {
  background-color: #007bff;
  color: white;
}

.button--primary:hover {
  background-color: #0056b3;
}

.button--secondary {
  background-color: #6c757d;
  color: white;
}

.button--disabled {
  opacity: 0.6;
  cursor: not-allowed;
  pointer-events: none;
}

.button--large {
  padding: 15px 30px;
  font-size: 18px;
}

.button--small {
  padding: 5px 10px;
  font-size: 12px;
}

/* Card Block with Elements */
.card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card__header {
  padding: 16px;
  border-bottom: 1px solid #e0e0e0;
  background-color: #f8f9fa;
}

.card__body {
  padding: 16px;
}

.card__footer {
  padding: 16px;
  border-top: 1px solid #e0e0e0;
  background-color: #f8f9fa;
}

.card--elevated {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}
```
