---
name: frontend-routing
description: >
  Implement client-side routing using React Router, Vue Router, and Angular
  Router. Use when building multi-page applications with navigation and route
  protection.
---

# Frontend Routing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement client-side routing with navigation, lazy loading, protected routes, and state management for multi-page single-page applications.

## When to Use

- Multi-page navigation
- URL-based state management
- Protected/guarded routes
- Lazy loading of components
- Query parameter handling

## Quick Start

Minimal working example:

```typescript
// App.tsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Layout } from './components/Layout';
import { Home } from './pages/Home';
import { NotFound } from './pages/NotFound';
import { useAuth } from './hooks/useAuth';
import React from 'react';

// Lazy loaded components
const Dashboard = React.lazy(() => import('./pages/Dashboard'));
const UserProfile = React.lazy(() => import('./pages/UserProfile'));
const Settings = React.lazy(() => import('./pages/Settings'));

// Protected route wrapper
const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
};

export const App: React.FC = () => {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [React Router v6](references/react-router-v6.md) | React Router v6 |
| [Vue Router 4](references/vue-router-4.md) | Vue Router 4 |
| [Angular Routing](references/angular-routing.md) | Angular Routing |
| [Query Parameter Handling](references/query-parameter-handling.md) | Query Parameter Handling |
| [Route Transition Effects](references/route-transition-effects.md) | Route Transition Effects |

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
