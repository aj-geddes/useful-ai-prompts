# Higher-Order Component (HOC)

## Higher-Order Component (HOC)

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
