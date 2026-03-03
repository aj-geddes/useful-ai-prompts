---
name: code-documentation
description: >
  Write comprehensive code documentation including JSDoc, Python docstrings,
  inline comments, function documentation, and API comments. Use when
  documenting code, writing docstrings, or creating inline documentation.
---

# Code Documentation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create clear, comprehensive code documentation using language-specific standards like JSDoc, Python docstrings, JavaDoc, and inline comments.

## When to Use

- Function and class documentation
- JSDoc for JavaScript/TypeScript
- Python docstrings
- JavaDoc for Java
- Inline code comments
- API documentation from code
- Type definitions
- Usage examples in code

## Quick Start

Minimal working example:

```javascript
/**
 * Calculates the total price including tax and discount.
 *
 * @param {number} basePrice - The base price before tax and discount
 * @param {number} taxRate - Tax rate as a decimal (e.g., 0.08 for 8%)
 * @param {number} [discount=0] - Optional discount amount
 * @returns {number} The final price after tax and discount
 * @throws {Error} If basePrice or taxRate is negative
 *
 * @example
 * const price = calculateTotalPrice(100, 0.08, 10);
 * console.log(price); // 98
 *
 * @example
 * // Without discount
 * const price = calculateTotalPrice(100, 0.08);
 * console.log(price); // 108
 */
function calculateTotalPrice(basePrice, taxRate, discount = 0) {
  if (basePrice < 0 || taxRate < 0) {
    throw new Error("Price and tax rate must be non-negative");
  }
  return basePrice * (1 + taxRate) - discount;
}

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Function Documentation](references/function-documentation.md) | Function Documentation |
| [Class Documentation](references/class-documentation.md) | Class Documentation |
| [Type Definitions](references/type-definitions.md) | Type Definitions |
| [Function Documentation](references/function-documentation-2.md) | Function Documentation |
| [Class Documentation](references/class-documentation-2.md) | Class Documentation |
| [Module Documentation](references/module-documentation.md) | Module Documentation |

## Best Practices

### ✅ DO

- Document public APIs thoroughly
- Include usage examples
- Document parameters and return values
- Specify thrown exceptions/errors
- Use language-specific standards (JSDoc, docstrings, etc.)
- Keep comments up-to-date
- Document "why" not "what"
- Include edge cases and gotchas
- Add links to related functions
- Document type definitions
- Use consistent formatting

### ❌ DON'T

- State the obvious in comments
- Leave commented-out code
- Write misleading comments
- Skip examples for complex functions
- Use vague parameter descriptions
- Forget to update docs when code changes
- Over-comment simple code
