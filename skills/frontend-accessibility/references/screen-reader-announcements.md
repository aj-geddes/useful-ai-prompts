# Screen Reader Announcements

## Screen Reader Announcements

```typescript
// LiveRegion component for announcements
interface LiveRegionProps {
  message: string;
  politeness?: 'polite' | 'assertive' | 'off';
  role?: 'status' | 'alert';
}

const LiveRegion: React.FC<LiveRegionProps> = ({
  message,
  politeness = 'polite',
  role = 'status'
}) => {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (message && ref.current) {
      ref.current.textContent = message;
    }
  }, [message]);

  return (
    <div
      ref={ref}
      role={role}
      aria-live={politeness}
      aria-atomic="true"
      className="sr-only"
    />
  );
};

// Usage in component
const SearchResults: React.FC = () => {
  const [results, setResults] = useState([]);
  const [message, setMessage] = useState('');

  const handleSearch = async (query: string) => {
    const response = await fetch(`/api/search?q=${query}`);
    const data = await response.json();
    setResults(data);
    setMessage(`Found ${data.length} results`);
  };

  return (
    <>
      <LiveRegion message={message} />
      <input
        type="text"
        placeholder="Search..."
        onChange={(e) => handleSearch(e.target.value)}
        aria-label="Search results"
      />
      <ul>
        {results.map(item => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
    </>
  );
};

// Skip to main content link (hidden by default)
const skipLink = document.createElement('a');
skipLink.href = '#main-content';
skipLink.textContent = 'Skip to main content';
skipLink.style.position = 'absolute';
skipLink.style.top = '-40px';
skipLink.style.left = '0';
skipLink.style.background = '#000';
skipLink.style.color = '#fff';
skipLink.style.padding = '8px';
skipLink.style.zIndex = '100';
skipLink.addEventListener('focus', () => {
  skipLink.style.top = '0';
});
skipLink.addEventListener('blur', () => {
  skipLink.style.top = '-40px';
});
document.body.insertBefore(skipLink, document.body.firstChild);
```
