---
name: frontend-accessibility
description: Implement WCAG compliance using semantic HTML, ARIA, keyboard navigation, and screen reader support. Use when building inclusive applications for all users.
---

# Frontend Accessibility

## Overview

Build accessible web applications following WCAG guidelines with semantic HTML, ARIA attributes, keyboard navigation, and screen reader support for inclusive user experiences.

## When to Use

- Compliance with accessibility standards
- Inclusive design requirements
- Screen reader support
- Keyboard navigation
- Color contrast issues

## Implementation Examples

### 1. **Semantic HTML and ARIA**

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

### 2. **Keyboard Navigation**

```typescript
// React Component with keyboard support
import React, { useEffect, useRef, useState } from 'react';

interface MenuItem {
  id: string;
  label: string;
  href: string;
}

const KeyboardNavigationMenu: React.FC<{ items: MenuItem[] }> = ({ items }) => {
  const [activeIndex, setActiveIndex] = useState(0);
  const menuRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      switch (e.key) {
        case 'ArrowLeft':
        case 'ArrowUp':
          e.preventDefault();
          setActiveIndex(prev =>
            prev === 0 ? items.length - 1 : prev - 1
          );
          break;

        case 'ArrowRight':
        case 'ArrowDown':
          e.preventDefault();
          setActiveIndex(prev =>
            prev === items.length - 1 ? 0 : prev + 1
          );
          break;

        case 'Home':
          e.preventDefault();
          setActiveIndex(0);
          break;

        case 'End':
          e.preventDefault();
          setActiveIndex(items.length - 1);
          break;

        case 'Enter':
        case ' ':
          e.preventDefault();
          const link = menuRef.current?.querySelectorAll('a')[activeIndex];
          link?.click();
          break;

        case 'Escape':
          menuRef.current?.querySelector('a')?.blur();
          break;

        default:
          break;
      }
    };

    menuRef.current?.addEventListener('keydown', handleKeyDown);
    return () => menuRef.current?.removeEventListener('keydown', handleKeyDown);
  }, [items.length, activeIndex]);

  return (
    <div role="menubar" ref={menuRef}>
      {items.map((item, index) => (
        <a
          key={item.id}
          href={item.href}
          role="menuitem"
          tabIndex={index === activeIndex ? 0 : -1}
          onFocus={() => setActiveIndex(index)}
          aria-current={index === activeIndex ? 'page' : undefined}
        >
          {item.label}
        </a>
      ))}
    </div>
  );
};
```

### 3. **Color Contrast and Visual Accessibility**

```css
/* Proper color contrast (WCAG AA: 4.5:1 for text, 3:1 for large text) */
:root {
  --color-text: #1a1a1a; /* Black - high contrast */
  --color-background: #ffffff;
  --color-primary: #0066cc; /* Blue with good contrast */
  --color-success: #008000; /* Not pure green */
  --color-error: #d32f2f; /* Not pure red */
  --color-warning: #ff8c00; /* Not yellow */
}

body {
  color: var(--color-text);
  background-color: var(--color-background);
  font-size: 16px;
  line-height: 1.5;
}

a {
  color: var(--color-primary);
  text-decoration: underline; /* Don't rely on color alone */
}

button {
  min-height: 44px; /* Touch target size */
  min-width: 44px;
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

/* Focus visible for keyboard navigation */
button:focus-visible,
a:focus-visible,
input:focus-visible {
  outline: 3px solid var(--color-primary);
  outline-offset: 2px;
}

/* High contrast mode support */
@media (prefers-contrast: more) {
  body {
    font-weight: 500;
  }

  button {
    border: 2px solid currentColor;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #e0e0e0;
    --color-background: #1a1a1a;
    --color-primary: #6495ed;
  }
}
```

### 4. **Screen Reader Announcements**

```typescript
// LiveRegion component for announcements
interface LiveRegionProps {
  message: string;
  politeness?: 'polite' | 'assertive' | 'off';
  role?: 'status' | 'alert';
}

const LiveRegion: React.FC<LiveRegionProps> = ({
  message,
  politeness = 'polite',
  role = 'status'
}) => {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (message && ref.current) {
      ref.current.textContent = message;
    }
  }, [message]);

  return (
    <div
      ref={ref}
      role={role}
      aria-live={politeness}
      aria-atomic="true"
      className="sr-only"
    />
  );
};

// Usage in component
const SearchResults: React.FC = () => {
  const [results, setResults] = useState([]);
  const [message, setMessage] = useState('');

  const handleSearch = async (query: string) => {
    const response = await fetch(`/api/search?q=${query}`);
    const data = await response.json();
    setResults(data);
    setMessage(`Found ${data.length} results`);
  };

  return (
    <>
      <LiveRegion message={message} />
      <input
        type="text"
        placeholder="Search..."
        onChange={(e) => handleSearch(e.target.value)}
        aria-label="Search results"
      />
      <ul>
        {results.map(item => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
    </>
  );
};

// Skip to main content link (hidden by default)
const skipLink = document.createElement('a');
skipLink.href = '#main-content';
skipLink.textContent = 'Skip to main content';
skipLink.style.position = 'absolute';
skipLink.style.top = '-40px';
skipLink.style.left = '0';
skipLink.style.background = '#000';
skipLink.style.color = '#fff';
skipLink.style.padding = '8px';
skipLink.style.zIndex = '100';
skipLink.addEventListener('focus', () => {
  skipLink.style.top = '0';
});
skipLink.addEventListener('blur', () => {
  skipLink.style.top = '-40px';
});
document.body.insertBefore(skipLink, document.body.firstChild);
```

### 5. **Accessibility Testing**

```typescript
// jest-axe integration test
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { Button } from './Button';

expect.extend(toHaveNoViolations);

describe('Button Accessibility', () => {
  it('should not have accessibility violations', async () => {
    const { container } = render(
      <Button>Click me</Button>
    );

    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('should have proper ARIA labels', async () => {
    const { container } = render(
      <Button aria-label="Close dialog">×</Button>
    );

    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});

// Accessibility Checker Hook
const useAccessibilityChecker = () => {
  useEffect(() => {
    // Run accessibility checks in development
    if (process.env.NODE_ENV === 'development') {
      import('axe-core').then(axe => {
        axe.run((error, results) => {
          if (results.violations.length > 0) {
            console.warn('Accessibility violations found:', results.violations);
          }
        });
      });
    }
  }, []);
};
```

## Best Practices

- Use semantic HTML elements
- Provide meaningful alt text for images
- Ensure 4.5:1 color contrast ratio for text
- Support keyboard navigation entirely
- Use ARIA only when necessary
- Test with screen readers (NVDA, JAWS)
- Implement skip links
- Support zoom up to 200%
- Use descriptive link text
- Test with actual assistive technologies

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [Axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [WebAIM Resources](https://webaim.org/)
