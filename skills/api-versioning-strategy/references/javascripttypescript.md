# JavaScript/TypeScript

## JavaScript/TypeScript

```typescript
// v1 Client
class ApiClientV1 {
  async getUsers() {
    const response = await fetch("/api/v1/users");
    const data = await response.json();
    return data.users;
  }
}

// v2 Client
class ApiClientV2 {
  async getUsers() {
    const response = await fetch("/api/v2/users");
    const data = await response.json();
    return data.data; // Changed from .users to .data
  }
}
```


## Python

```python
# v1
response = requests.get(f"{base_url}/api/v1/users")
users = response.json()["users"]

# v2
response = requests.get(f"{base_url}/api/v2/users")
users = response.json()["data"]
```

````
