# Query Parameter Handling

## Query Parameter Handling

```typescript
// React Hook for Query Params
import { useSearchParams } from 'react-router-dom';

const SearchUsers: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();

  const handleSearch = (query: string) => {
    setSearchParams({ q: query, page: '1' });
  };

  const query = searchParams.get('q') || '';
  const page = searchParams.get('page') || '1';

  return (
    <div>
      <input
        value={query}
        onChange={(e) => handleSearch(e.target.value)}
        placeholder="Search..."
      />
      <p>Results for: {query} (Page {page})</p>
    </div>
  );
};

// Vue Query Param Hook
import { useRoute, useRouter } from 'vue-router';
import { computed } from 'vue';

export function useQueryParams() {
  const route = useRoute();
  const router = useRouter();

  const query = computed(() => route.query.q as string || '');
  const page = computed(() => parseInt(route.query.page as string) || 1);

  const setQuery = (q: string) => {
    router.push({ query: { q, page: '1' } });
  };

  return { query, page, setQuery };
}
```
