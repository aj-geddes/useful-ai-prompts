# API Key Authentication

## API Key Authentication

```javascript
// API Key middleware
const verifyApiKey = (req, res, next) => {
  const apiKey = req.headers['x-api-key'];

  if (!apiKey) {
    return res.status(401).json({ error: 'API key required' });
  }

  try {
    // Verify API key format and existence
    const keyHash = crypto.createHash('sha256').update(apiKey).digest('hex');
    const apiKeyRecord = await ApiKey.findOne({ key_hash: keyHash, active: true });

    if (!apiKeyRecord) {
      return res.status(401).json({ error: 'Invalid API key' });
    }

    req.apiKey = apiKeyRecord;
    next();
  } catch (error) {
    res.status(500).json({ error: 'Authentication failed' });
  }
};

// Generate API key endpoint
app.post('/api/apikeys/generate', verifyToken, async (req, res) => {
  try {
    const apiKey = crypto.randomBytes(32).toString('hex');
    const keyHash = crypto.createHash('sha256').update(apiKey).digest('hex');

    const record = await ApiKey.create({
      userId: req.user.userId,
      key_hash: keyHash,
      name: req.body.name,
      active: true
    });

    res.json({ apiKey, message: 'Save this key securely' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to generate API key' });
  }
});

// Protected endpoint with API key
app.get('/api/data', verifyApiKey, (req, res) => {
  res.json({ data: 'sensitive data for API key holder' });
});
```
