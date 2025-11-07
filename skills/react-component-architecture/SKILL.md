---
name: react-component-architecture
description: Design scalable React components using functional components, hooks, composition patterns, and TypeScript. Use when building reusable component libraries and maintainable UI systems.
---

# React Component Architecture

## Overview

Build scalable, maintainable React components using modern patterns including functional components, hooks, composition, and TypeScript for type safety.

## When to Use

- Component library design
- Large-scale React applications
- Reusable UI patterns
- Custom hooks development
- Performance optimization

## Implementation Examples

### 1. **Functional Component with Hooks**

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
    sm: 'px-2 py-1 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg'
  };

  return (
    <button
      className={`${variantStyles[variant]} ${sizeStyles[size]} text-white rounded disabled:opacity-50`}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
};
```

### 2. **Custom Hooks Pattern**

```typescript
// useFormInput.ts
import { useState, useCallback } from 'react';

interface UseFormInputOptions {
  initialValue?: string;
  validator?: (value: string) => string | null;
}

export const useFormInput = (options: UseFormInputOptions = {}) => {
  const [value, setValue] = useState(options.initialValue || '');
  const [error, setError] = useState<string | null>(null);

  const validate = useCallback(() => {
    if (options.validator) {
      const validationError = options.validator(value);
      setError(validationError);
      return !validationError;
    }
    return true;
  }, [value, options.validator]);

  const reset = useCallback(() => {
    setValue(options.initialValue || '');
    setError(null);
  }, [options.initialValue]);

  return {
    value,
    setValue,
    error,
    validate,
    reset,
    bind: {
      value,
      onChange: (e: React.ChangeEvent<HTMLInputElement>) => setValue(e.target.value)
    }
  };
};

// Usage
const MyForm: React.FC = () => {
  const email = useFormInput({
    validator: (v) => !v.includes('@') ? 'Invalid email' : null
  });

  return (
    <div>
      <input {...email.bind} />
      {email.error && <span className="text-red-500">{email.error}</span>}
    </div>
  );
};
```

### 3. **Composition Pattern**

```typescript
// Card.tsx
interface CardProps {
  children: React.ReactNode;
  className?: string;
}

const Card: React.FC<CardProps> = ({ children, className = '' }) => (
  <div className={`border rounded p-4 ${className}`}>{children}</div>
);

const CardHeader: React.FC<CardProps> = ({ children }) => (
  <div className="border-b pb-2 mb-3 font-bold">{children}</div>
);

const CardBody: React.FC<CardProps> = ({ children }) => (
  <div className="py-2">{children}</div>
);

const CardFooter: React.FC<CardProps> = ({ children }) => (
  <div className="border-t pt-2 mt-3">{children}</div>
);

// Compound component
export { Card };
Card.Header = CardHeader;
Card.Body = CardBody;
Card.Footer = CardFooter;

// Usage
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Body>Content</Card.Body>
  <Card.Footer>Actions</Card.Footer>
</Card>
```

### 4. **Higher-Order Component (HOC)**

```typescript
// withLoader.tsx
interface WithLoaderProps {
  isLoading: boolean;
  error?: Error | null;
}

function withLoader<P extends object>(
  Component: React.ComponentType<P>
): React.FC<P & WithLoaderProps> {
  return ({ isLoading, error, ...props }: P & WithLoaderProps) => {
    if (isLoading) return <div>Loading...</div>;
    if (error) return <div className="text-red-500">{error.message}</div>;
    return <Component {...(props as P)} />;
  };
}

// Usage
const UserList: React.FC<{ users: User[] }> = ({ users }) => (
  <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>
);

export const LoadingUserList = withLoader(UserList);
```

### 5. **Render Props Pattern**

```typescript
// DataFetcher.tsx
interface DataFetcherProps<T> {
  url: string;
  children: (data: T | null, loading: boolean, error: Error | null) => React.ReactNode;
}

export const DataFetcher = <T,>({ url, children }: DataFetcherProps<T>) => {
  const [data, setData] = React.useState<T | null>(null);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState<Error | null>(null);

  React.useEffect(() => {
    fetch(url)
      .then(r => r.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [url]);

  return <>{children(data, loading, error)}</>;
};

// Usage
<DataFetcher<User[]> url="/api/users">
  {(users, loading, error) => (
    <>{loading ? <p>Loading...</p> : users?.map(u => <p key={u.id}>{u.name}</p>)}</>
  )}
</DataFetcher>
```

## Best Practices

- Use TypeScript for type safety
- Implement proper prop validation
- Keep components focused and single-purpose
- Leverage hooks for state and side effects
- Use composition over inheritance
- Memoize expensive computations
- Extract custom hooks for reusable logic

## Resources

- [React Documentation](https://react.dev)
- [React Hooks API](https://react.dev/reference/react)
- [TypeScript with React](https://www.typescriptlang.org/docs/handbook/react.html)
