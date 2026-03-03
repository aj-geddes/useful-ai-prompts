---
name: vue-application-structure
description: >
  Structure Vue 3 applications using Composition API, component organization,
  and TypeScript. Use when building scalable Vue applications with proper
  separation of concerns.
---

# Vue Application Structure

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build well-organized Vue 3 applications using Composition API, proper file organization, and TypeScript for type safety and maintainability.

## When to Use

- Large-scale Vue applications
- Component library development
- Reusable composable hooks
- Complex state management
- Performance optimization

## Quick Start

Minimal working example:

```typescript
// useCounter.ts (Composable)
import { ref, computed } from 'vue';

export function useCounter(initialValue = 0) {
  const count = ref(initialValue);

  const doubled = computed(() => count.value * 2);
  const increment = () => count.value++;
  const decrement = () => count.value--;
  const reset = () => count.value = initialValue;

  return {
    count,
    doubled,
    increment,
    decrement,
    reset
  };
}

// Counter.vue
<template>
  <div class="counter">
    <p>Count: {{ count }}</p>
    <p>Doubled: {{ doubled }}</p>
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Vue 3 Composition API Component](references/vue-3-composition-api-component.md) | Vue 3 Composition API Component |
| [Async Data Fetching Composable](references/async-data-fetching-composable.md) | Async Data Fetching Composable |
| [Component Organization Structure](references/component-organization-structure.md) | Component Organization Structure |
| [Form Handling Composable](references/form-handling-composable.md) | Form Handling Composable |
| [Pinia Store (State Management)](references/pinia-store-state-management.md) | Pinia Store (State Management) |

## Best Practices

### ✅ DO

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
