---
name: accessibility-compliance
description: Implement WCAG 2.1/2.2 accessibility standards, screen reader compatibility, keyboard navigation, and a11y testing. Use when building inclusive web applications, ensuring regulatory compliance, or improving user experience for people with disabilities.
---

# Accessibility Compliance

## Overview

Implement comprehensive accessibility features following WCAG guidelines to ensure your application is usable by everyone, including people with disabilities.

## When to Use

- Building public-facing web applications
- Ensuring WCAG 2.1/2.2 AA or AAA compliance
- Supporting screen readers (NVDA, JAWS, VoiceOver)
- Implementing keyboard-only navigation
- Meeting ADA, Section 508, or similar regulations
- Improving SEO and overall user experience
- Conducting accessibility audits

## Key Principles (POUR)

1. **Perceivable** - Information must be presentable to users in ways they can perceive
2. **Operable** - Interface components must be operable
3. **Understandable** - Information and operation must be understandable
4. **Robust** - Content must be robust enough to be interpreted by assistive technologies

## Implementation Examples

### 1. **Semantic HTML with ARIA**

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

### 2. **React Component with Accessibility**

```typescript
import React, { useRef, useEffect, useState } from 'react';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
}

const AccessibleModal: React.FC<ModalProps> = ({
  isOpen,
  onClose,
  title,
  children
}) => {
  const modalRef = useRef<HTMLDivElement>(null);
  const previousFocusRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (isOpen) {
      // Save previous focus
      previousFocusRef.current = document.activeElement as HTMLElement;

      // Focus modal
      modalRef.current?.focus();

      // Trap focus within modal
      const trapFocus = (e: KeyboardEvent) => {
        if (e.key === 'Escape') {
          onClose();
        }
      };

      document.addEventListener('keydown', trapFocus);

      return () => {
        document.removeEventListener('keydown', trapFocus);
        // Restore previous focus
        previousFocusRef.current?.focus();
      };
    }
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
      ref={modalRef}
      tabIndex={-1}
      className="modal-overlay"
      onClick={onClose}
    >
      <div
        className="modal-content"
        onClick={(e) => e.stopPropagation()}
      >
        <h2 id="modal-title">{title}</h2>
        <button
          onClick={onClose}
          aria-label="Close modal"
          className="close-button"
        >
          &times;
        </button>
        <div className="modal-body">
          {children}
        </div>
      </div>
    </div>
  );
};

export default AccessibleModal;
```

### 3. **Keyboard Navigation Handler**

```typescript
// Keyboard navigation utilities
export const KeyboardNavigation = {
  // Handle arrow key navigation in lists
  handleListNavigation: (event: KeyboardEvent, items: HTMLElement[]) => {
    const currentIndex = items.findIndex(item =>
      item === document.activeElement
    );

    let nextIndex: number;

    switch (event.key) {
      case 'ArrowDown':
        event.preventDefault();
        nextIndex = Math.min(currentIndex + 1, items.length - 1);
        items[nextIndex]?.focus();
        break;

      case 'ArrowUp':
        event.preventDefault();
        nextIndex = Math.max(currentIndex - 1, 0);
        items[nextIndex]?.focus();
        break;

      case 'Home':
        event.preventDefault();
        items[0]?.focus();
        break;

      case 'End':
        event.preventDefault();
        items[items.length - 1]?.focus();
        break;
    }
  },

  // Make element keyboard accessible
  makeAccessible: (
    element: HTMLElement,
    onClick: () => void
  ): void => {
    element.setAttribute('tabindex', '0');
    element.setAttribute('role', 'button');

    element.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        onClick();
      }
    });
  }
};
```

### 4. **Color Contrast Validator**

```python
from typing import Tuple
import math

def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def calculate_luminance(rgb: Tuple[int, int, int]) -> float:
    """Calculate relative luminance."""
    def adjust(color: int) -> float:
        c = color / 255.0
        if c <= 0.03928:
            return c / 12.92
        return math.pow((c + 0.055) / 1.055, 2.4)

    r, g, b = rgb
    return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)

def calculate_contrast_ratio(color1: str, color2: str) -> float:
    """Calculate WCAG contrast ratio between two colors."""
    lum1 = calculate_luminance(hex_to_rgb(color1))
    lum2 = calculate_luminance(hex_to_rgb(color2))

    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)

    return (lighter + 0.05) / (darker + 0.05)

def check_wcag_compliance(
    foreground: str,
    background: str,
    level: str = 'AA',
    large_text: bool = False
) -> dict:
    """Check if color combination meets WCAG standards."""
    ratio = calculate_contrast_ratio(foreground, background)

    # WCAG 2.1 requirements
    requirements = {
        'AA': {'normal': 4.5, 'large': 3.0},
        'AAA': {'normal': 7.0, 'large': 4.5}
    }

    required_ratio = requirements[level]['large' if large_text else 'normal']
    passes = ratio >= required_ratio

    return {
        'ratio': round(ratio, 2),
        'required': required_ratio,
        'passes': passes,
        'level': level,
        'grade': 'Pass' if passes else 'Fail'
    }

# Usage
result = check_wcag_compliance('#000000', '#FFFFFF', 'AA', False)
print(f"Contrast ratio: {result['ratio']}:1")  # 21:1
print(f"WCAG {result['level']}: {result['grade']}")  # Pass
```

### 5. **Screen Reader Announcements**

```typescript
class ScreenReaderAnnouncer {
  private liveRegion: HTMLElement;

  constructor() {
    this.liveRegion = this.createLiveRegion();
  }

  private createLiveRegion(): HTMLElement {
    const region = document.createElement('div');
    region.setAttribute('role', 'status');
    region.setAttribute('aria-live', 'polite');
    region.setAttribute('aria-atomic', 'true');
    region.className = 'sr-only';
    region.style.cssText = `
      position: absolute;
      left: -10000px;
      width: 1px;
      height: 1px;
      overflow: hidden;
    `;
    document.body.appendChild(region);
    return region;
  }

  announce(message: string, priority: 'polite' | 'assertive' = 'polite'): void {
    this.liveRegion.setAttribute('aria-live', priority);

    // Clear then set message to ensure announcement
    this.liveRegion.textContent = '';
    setTimeout(() => {
      this.liveRegion.textContent = message;
    }, 100);
  }

  cleanup(): void {
    this.liveRegion.remove();
  }
}

// Usage
const announcer = new ScreenReaderAnnouncer();

// Announce form validation error
announcer.announce('Email field is required', 'assertive');

// Announce successful action
announcer.announce('Item added to cart', 'polite');
```

### 6. **Focus Management**

```typescript
class FocusManager {
  private focusableSelectors = [
    'a[href]',
    'button:not([disabled])',
    'textarea:not([disabled])',
    'input:not([disabled])',
    'select:not([disabled])',
    '[tabindex]:not([tabindex="-1"])'
  ].join(', ');

  getFocusableElements(container: HTMLElement): HTMLElement[] {
    return Array.from(
      container.querySelectorAll(this.focusableSelectors)
    ) as HTMLElement[];
  }

  trapFocus(container: HTMLElement): () => void {
    const focusable = this.getFocusableElements(container);
    const firstFocusable = focusable[0];
    const lastFocusable = focusable[focusable.length - 1];

    const handleTabKey = (e: KeyboardEvent) => {
      if (e.key !== 'Tab') return;

      if (e.shiftKey) {
        if (document.activeElement === firstFocusable) {
          lastFocusable.focus();
          e.preventDefault();
        }
      } else {
        if (document.activeElement === lastFocusable) {
          firstFocusable.focus();
          e.preventDefault();
        }
      }
    };

    container.addEventListener('keydown', handleTabKey);

    return () => container.removeEventListener('keydown', handleTabKey);
  }
}
```

## Testing Tools and Techniques

### Automated Testing

```typescript
// Jest + Testing Library accessibility tests
import { render, screen } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

describe('Accessibility', () => {
  it('should not have accessibility violations', async () => {
    const { container } = render(<MyComponent />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('should have proper ARIA labels', () => {
    render(<Button onClick={() => {}}>Click me</Button>);
    const button = screen.getByRole('button', { name: /click me/i });
    expect(button).toBeInTheDocument();
  });

  it('should be keyboard navigable', () => {
    const { container } = render(<Navigation />);
    const links = screen.getAllByRole('link');
    links.forEach(link => {
      expect(link).toHaveAttribute('href');
    });
  });
});
```

## Best Practices

### ✅ DO
- Use semantic HTML elements
- Provide text alternatives for images
- Ensure sufficient color contrast (4.5:1 minimum)
- Support keyboard navigation
- Implement focus management
- Test with screen readers
- Use ARIA attributes correctly
- Provide skip links
- Make forms accessible with labels
- Support text resizing up to 200%

### ❌ DON'T
- Rely solely on color to convey information
- Remove focus indicators
- Use only mouse/touch interactions
- Auto-play media without controls
- Create keyboard traps
- Use positive tabindex values
- Override user preferences
- Hide content only visually that should be hidden from screen readers

## Checklist

- [ ] All images have alt text
- [ ] Color contrast meets WCAG AA standards
- [ ] All interactive elements are keyboard accessible
- [ ] Focus indicators are visible
- [ ] Form inputs have associated labels
- [ ] Error messages are announced to screen readers
- [ ] Skip links are provided
- [ ] Headings follow hierarchical order
- [ ] ARIA attributes are used correctly
- [ ] Content is readable at 200% zoom
- [ ] Tested with keyboard only
- [ ] Tested with screen reader (NVDA, JAWS, VoiceOver)

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [Lighthouse Accessibility Audit](https://developers.google.com/web/tools/lighthouse)
