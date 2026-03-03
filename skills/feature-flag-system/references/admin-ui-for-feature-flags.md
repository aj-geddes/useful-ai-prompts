# Admin UI for Feature Flags

## Admin UI for Feature Flags

```typescript
interface FlagFormData {
  key: string;
  description: string;
  enabled: boolean;
  rolloutPercentage?: number;
  targetUsers?: string[];
  targetAttributes?: Record<string, any>;
}

function FeatureFlagDashboard() {
  const [flags, setFlags] = useState<FlagConfig[]>([]);
  const flagService = new FeatureFlagService();

  useEffect(() => {
    loadFlags();
  }, []);

  const loadFlags = async () => {
    const allFlags = flagService.getAllFlags();
    setFlags(allFlags);
  };

  const toggleFlag = async (key: string) => {
    const flag = flags.find(f => f.key === key);
    if (flag) {
      await flagService.updateFlag(key, { enabled: !flag.enabled });
      await loadFlags();
    }
  };

  return (
    <div className="dashboard">
      <h1>Feature Flags</h1>

      <table>
        <thead>
          <tr>
            <th>Flag</th>
            <th>Description</th>
            <th>Status</th>
            <th>Rollout</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {flags.map(flag => (
            <tr key={flag.key}>
              <td>{flag.key}</td>
              <td>{flag.description}</td>
              <td>
                <Switch
                  checked={flag.enabled}
                  onChange={() => toggleFlag(flag.key)}
                />
              </td>
              <td>{getRolloutPercentage(flag)}%</td>
              <td>
                <button onClick={() => editFlag(flag)}>Edit</button>
                <button onClick={() => deleteFlag(flag.key)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```
