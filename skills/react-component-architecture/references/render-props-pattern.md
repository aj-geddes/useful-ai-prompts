# Render Props Pattern

## Render Props Pattern

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
