# Semantic HTML with ARIA

## Semantic HTML with ARIA

```html
<!-- Bad: Non-semantic markup -->
<div class="button" onclick="submit()">Submit</div>

<!-- Good: Semantic HTML -->
<button type="submit" aria-label="Submit form">Submit</button>

<!-- Custom components with proper ARIA -->
<div
  role="button"
  tabindex="0"
  aria-pressed="false"
  onclick="toggle()"
  onkeydown="handleKeyPress(event)"
>
  Toggle Feature
</div>

<!-- Form with proper labels and error handling -->
<form>
  <label for="email">Email Address</label>
  <input
    id="email"
    type="email"
    name="email"
    aria-required="true"
    aria-invalid="false"
    aria-describedby="email-error"
  />
  <span id="email-error" role="alert" aria-live="polite"></span>
</form>
```
