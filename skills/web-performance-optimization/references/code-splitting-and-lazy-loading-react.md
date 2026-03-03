# Code Splitting and Lazy Loading (React)

## Code Splitting and Lazy Loading (React)

```typescript
// utils/lazyLoad.ts
import React from 'react';

export const lazyLoad = (importStatement: Promise<any>) => {
  return React.lazy(() =>
    importStatement.then(module => ({
      default: module.default
    }))
  );
};

// routes.tsx
import { lazyLoad } from './utils/lazyLoad';

export const routes = [
  {
    path: '/',
    component: () => import('./pages/Home'),
    lazy: lazyLoad(import('./pages/Home'))
  },
  {
    path: '/dashboard',
    lazy: lazyLoad(import('./pages/Dashboard'))
  },
  {
    path: '/users',
    lazy: lazyLoad(import('./pages/Users'))
  }
];

// App.tsx with Suspense
import { Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

export const App = () => {
  return (
    <BrowserRouter>
      <Suspense fallback={<LoadingSpinner />}>
        <Routes>
          {routes.map(route => (
            <Route key={route.path} path={route.path} element={<route.lazy />} />
          ))}
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
};

// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 10
        },
        common: {
          minChunks: 2,
          priority: 5,
          reuseExistingChunk: true
        }
      }
    }
  }
};
```
