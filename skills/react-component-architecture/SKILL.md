---
name: react-component-architecture
description: >
  Design scalable React components using functional components, hooks,
  composition patterns, and TypeScript. Use when building reusable component
  libraries and maintainable UI systems.
---

# React Component Architecture

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build scalable, maintainable React components using modern patterns including functional components, hooks, composition, and TypeScript for type safety.

## When to Use

- Component library design
- Large-scale React applications
- Reusable UI patterns
- Custom hooks development
- Performance optimization

## Quick Start

Minimal working example:

```typescript
// Button.tsx
import React, { useState, useCallback } from 'react';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  disabled = false,
  onClick,
  children
}) => {
  const variantStyles = {
    primary: 'bg-blue-500 hover:bg-blue-600',
    secondary: 'bg-gray-500 hover:bg-gray-600',
    danger: 'bg-red-500 hover:bg-red-600'
  };

  const sizeStyles = {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Functional Component with Hooks](references/functional-component-with-hooks.md) | Functional Component with Hooks |
| [Custom Hooks Pattern](references/custom-hooks-pattern.md) | Custom Hooks Pattern |
| [Composition Pattern](references/composition-pattern.md) | Composition Pattern |
| [Higher-Order Component (HOC)](references/higher-order-component-hoc.md) | Higher-Order Component (HOC) |
| [Render Props Pattern](references/render-props-pattern.md) | Render Props Pattern |

## Best Practices

### ✅ DO

- Keep components small and single-purpose — split when a component handles more than one concern
- Define explicit TypeScript interfaces for all props, including `children` typing
- Extract reusable logic into custom hooks rather than duplicating state management across components
- Use composition (children, render props, slots) over deep prop drilling or inheritance
- Memoize expensive computations with `useMemo` and stable callback references with `useCallback`
- Co-locate component styles, tests, and types in the same directory for discoverability

### ❌ DON'T

- Mutate state directly or derive state from props without `useMemo` (causes stale renders)
- Use `useEffect` for derived state that can be computed during render
- Create deeply nested component hierarchies — flatten with context or composition instead
- Export internal implementation components that consumers should not use directly
