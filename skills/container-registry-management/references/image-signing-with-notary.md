# Image Signing with Notary

## Image Signing with Notary

```bash
#!/bin/bash
# sign-image.sh - Sign container images with Notary

set -euo pipefail

IMAGE="${1}"
NOTATION_KEY="${2:-mykey}"

echo "Signing image: $IMAGE"

# Initialize Notary
notary key list

# Sign image
notation sign \
  --key "$NOTATION_KEY" \
  --allow-missing \
  "$IMAGE"

echo "Image signed successfully"

# Verify signature
notation verify "$IMAGE"
```
