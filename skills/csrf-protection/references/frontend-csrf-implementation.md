# Frontend CSRF Implementation

## Frontend CSRF Implementation

```javascript
// csrf-client.js
class CSRFClient {
  constructor() {
    this.token = null;
    this.tokenExpiry = null;
  }

  /**
   * Fetch CSRF token from server
   */
  async fetchToken() {
    const response = await fetch("/api/csrf-token", {
      credentials: "include",
    });

    const data = await response.json();
    this.token = data.csrfToken;
    this.tokenExpiry = Date.now() + 3600000; // 1 hour

    return this.token;
  }

  /**
   * Get valid token (fetch if needed)
   */
  async getToken() {
    if (!this.token || Date.now() > this.tokenExpiry) {
      await this.fetchToken();
    }

    return this.token;
  }

  /**
   * Make protected request
   */
  async request(url, options = {}) {
    const token = await this.getToken();

    const headers = {
      "Content-Type": "application/json",
      "X-CSRF-Token": token,
      ...options.headers,
    };

    return fetch(url, {
      ...options,
      headers,
      credentials: "include",
    });
  }

  /**
   * POST request with CSRF token
   */
  async post(url, data) {
    return this.request(url, {
      method: "POST",
      body: JSON.stringify(data),
    });
  }

  /**
   * PUT request with CSRF token
   */
  async put(url, data) {
    return this.request(url, {
      method: "PUT",
      body: JSON.stringify(data),
    });
  }

  /**
   * DELETE request with CSRF token
   */
  async delete(url) {
    return this.request(url, {
      method: "DELETE",
    });
  }
}

// Usage
const client = new CSRFClient();

async function transferFunds() {
  try {
    const response = await client.post("/api/transfer", {
      amount: 1000,
      toAccount: "123456",
    });

    const result = await response.json();
    console.log("Transfer successful:", result);
  } catch (error) {
    console.error("Transfer failed:", error);
  }
}

// React hook for CSRF
function useCSRF() {
  const [token, setToken] = React.useState(null);

  React.useEffect(() => {
    async function fetchToken() {
      const response = await fetch("/api/csrf-token");
      const data = await response.json();
      setToken(data.csrfToken);
    }

    fetchToken();
  }, []);

  return token;
}

// Usage in React form
function TransferForm() {
  const csrfToken = useCSRF();

  const handleSubmit = async (e) => {
    e.preventDefault();

    await fetch("/api/transfer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-Token": csrfToken,
      },
      body: JSON.stringify({
        amount: 1000,
        toAccount: "123456",
      }),
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="hidden" name="_csrf" value={csrfToken} />
      {/* form fields */}
      <button type="submit">Transfer</button>
    </form>
  );
}
```
