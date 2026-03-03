---
name: file-upload-handling
description: >
  Implement secure file upload handling with validation, virus scanning, storage
  management, and serving files efficiently. Use when building file upload
  features, managing file storage, and implementing file download systems.
---

# File Upload Handling

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build secure and robust file upload systems with validation, sanitization, virus scanning, efficient storage management, CDN integration, and proper file serving mechanisms across different backend frameworks.

## When to Use

- Implementing file upload features
- Managing user-uploaded documents
- Storing and serving media files
- Implementing profile picture uploads
- Building document management systems
- Handling bulk file imports

## Quick Start

Minimal working example:

```python
# config.py
import os

class Config:
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50 MB
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx', 'doc'}
    UPLOAD_DIRECTORY = os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER)

# file_service.py
import os
import mimetypes
import hashlib
import secrets
from werkzeug.utils import secure_filename
from datetime import datetime
import magic
import aiofiles

class FileUploadService:
    def __init__(self, upload_dir, allowed_extensions, max_size=50*1024*1024):
        self.upload_dir = upload_dir
        self.allowed_extensions = allowed_extensions
        self.max_size = max_size
        self.mime = magic.Magic(mime=True)
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Python/Flask File Upload](references/pythonflask-file-upload.md) | Python/Flask File Upload |
| [Node.js Express File Upload with Multer](references/nodejs-express-file-upload-with-multer.md) | Node.js Express File Upload with Multer |
| [FastAPI File Upload](references/fastapi-file-upload.md) | FastAPI File Upload |
| [S3/Cloud Storage Integration](references/s3cloud-storage-integration.md) | S3/Cloud Storage Integration |

## Best Practices

### ✅ DO

- Validate file extensions and MIME types
- Check file size before processing
- Use secure filenames to prevent directory traversal
- Store files outside web root
- Implement virus scanning
- Use CDN for file delivery
- Generate signed URLs for direct access
- Log file upload/download events
- Implement access control checks
- Clean up temporary files

### ❌ DON'T

- Trust user-provided filenames
- Store files in web-accessible directories
- Allow arbitrary file types
- Skip virus scanning for uploaded files
- Expose absolute file paths
- Allow unlimited file sizes
- Ignore access control
- Use predictable file paths
- Store sensitive metadata in filenames
- Forget to validate file content
