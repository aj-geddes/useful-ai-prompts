# Semantic HTML and ARIA

## Semantic HTML and ARIA

```html
<!-- Good semantic structure -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

<main>
  <article>
    <header>
      <h1>Article Title</h1>
      <time datetime="2024-01-15">January 15, 2024</time>
    </header>
    <p>Article content...</p>
  </article>

  <aside aria-label="Related articles">
    <h2>Related Articles</h2>
    <ul>
      <li><a href="/article1">Article 1</a></li>
      <li><a href="/article2">Article 2</a></li>
    </ul>
  </aside>
</main>

<footer>
  <p>&copy; 2024 Company Name</p>
</footer>

<!-- Form with proper labels -->
<form>
  <div class="form-group">
    <label for="email">Email Address</label>
    <input
      id="email"
      type="email"
      name="email"
      required
      aria-required="true"
      aria-describedby="email-help"
    />
    <small id="email-help">We'll never share your email</small>
  </div>

  <div class="form-group">
    <label for="password">Password</label>
    <input
      id="password"
      type="password"
      name="password"
      required
      aria-required="true"
      aria-describedby="password-requirements"
    />
    <div id="password-requirements">
      <ul>
        <li>At least 8 characters</li>
        <li>One uppercase letter</li>
        <li>One number</li>
      </ul>
    </div>
  </div>

  <button type="submit">Sign Up</button>
</form>

<!-- Modal with proper ARIA -->
<div
  id="modal"
  role="dialog"
  aria-labelledby="modal-title"
  aria-describedby="modal-description"
  aria-modal="true"
>
  <button aria-label="Close modal">×</button>
  <h2 id="modal-title">Confirm Action</h2>
  <p id="modal-description">Are you sure?</p>
  <button>Cancel</button>
  <button>Confirm</button>
</div>

<!-- Alert with role -->
<div role="alert" aria-live="polite">
  <strong>Error:</strong> Please correct the highlighted fields
</div>
```
