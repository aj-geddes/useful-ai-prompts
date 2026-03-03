# Secrets Detection

## Secrets Detection

```bash
# Install detect-secrets
pip install detect-secrets

# Scan repository
detect-secrets scan --all-files --force-use-all-plugins

# Check for hardcoded secrets
git secrets --scan

# TruffleHog for git history
trufflehog git https://github.com/user/repo --only-verified
```
