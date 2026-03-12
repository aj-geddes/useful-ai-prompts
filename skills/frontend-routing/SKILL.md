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

- Lazy-load route components with React.lazy or dynamic imports to reduce initial bundle size
- Implement route-level error boundaries so a crash in one route doesn't break the whole app
- Use a centralized route config (array or object) rather than scattering Route declarations
- Protect authenticated routes with a guard component that redirects before rendering
- Preserve scroll position on back navigation and reset it on forward navigation
- Reflect meaningful application state in the URL so users can bookmark and share deep links

### ❌ DON'T

- Store transient UI state (modals, toasts) in the URL — route params are for navigable state only
- Use nested wildcard routes without a catch-all 404 page at the end
- Fetch data inside the route component without a loading state — use loader functions or Suspense
- Hard-code route paths as strings throughout the app — define them as constants in one place
