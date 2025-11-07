---
name: file-upload-handling
description: Implement secure file upload handling with validation, virus scanning, storage management, and serving files efficiently. Use when building file upload features, managing file storage, and implementing file download systems.
---

# File Upload Handling

## Overview

Build secure and robust file upload systems with validation, sanitization, virus scanning, efficient storage management, CDN integration, and proper file serving mechanisms across different backend frameworks.

## When to Use

- Implementing file upload features
- Managing user-uploaded documents
- Storing and serving media files
- Implementing profile picture uploads
- Building document management systems
- Handling bulk file imports

## Instructions

### 1. **Python/Flask File Upload**

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

    def validate_file(self, file):
        """Validate uploaded file"""
        errors = []

        # Check filename
        if not file.filename:
            errors.append('No filename provided')

        # Check file extension
        filename = secure_filename(file.filename)
        ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
        if ext not in self.allowed_extensions:
            errors.append(f'File type not allowed. Allowed: {", ".join(self.allowed_extensions)}')

        # Check file size
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0)
        if file_size > self.max_size:
            errors.append(f'File too large. Max size: {self.max_size / 1024 / 1024}MB')

        # Check MIME type
        file_content = file.read(8192)
        file.seek(0)
        detected_mime = self.mime.from_buffer(file_content)
        if not self._is_valid_mime(detected_mime, ext):
            errors.append('File MIME type does not match extension')

        return errors

    def _is_valid_mime(self, mime_type, ext):
        """Verify MIME type matches extension"""
        allowed_mimes = {
            'txt': ['text/plain'],
            'pdf': ['application/pdf'],
            'png': ['image/png'],
            'jpg': ['image/jpeg'],
            'jpeg': ['image/jpeg'],
            'gif': ['image/gif'],
            'doc': ['application/msword'],
            'docx': ['application/vnd.openxmlformats-officedocument.wordprocessingml.document']
        }
        return mime_type in allowed_mimes.get(ext, [])

    def save_file(self, file, user_id):
        """Save uploaded file with sanitization"""
        errors = self.validate_file(file)
        if errors:
            return {'success': False, 'errors': errors}

        # Generate secure filename
        file_hash = hashlib.sha256(secrets.token_bytes(32)).hexdigest()
        filename = secure_filename(file.filename)
        ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
        safe_filename = f"{file_hash}.{ext}"

        # Create user-specific directory
        user_upload_dir = os.path.join(self.upload_dir, user_id)
        os.makedirs(user_upload_dir, exist_ok=True)

        filepath = os.path.join(user_upload_dir, safe_filename)

        try:
            file.save(filepath)

            file_info = {
                'id': file_hash,
                'original_name': filename,
                'safe_name': safe_filename,
                'size': os.path.getsize(filepath),
                'user_id': user_id,
                'uploaded_at': datetime.utcnow().isoformat(),
                'mime_type': self.mime.from_file(filepath)
            }

            return {'success': True, 'file': file_info}

        except Exception as e:
            return {'success': False, 'error': str(e)}

    def delete_file(self, user_id, file_id):
        """Delete file safely"""
        filepath = os.path.join(self.upload_dir, user_id, f"{file_id}.*")
        import glob
        files = glob.glob(filepath)

        for f in files:
            try:
                os.remove(f)
                return {'success': True}
            except Exception as e:
                return {'success': False, 'error': str(e)}

        return {'success': False, 'error': 'File not found'}

# routes.py
from flask import request, jsonify, send_file, safe_join
from functools import wraps
import os

file_service = FileUploadService(
    app.config['UPLOAD_DIRECTORY'],
    app.config['ALLOWED_EXTENSIONS']
)

@app.route('/api/upload', methods=['POST'])
@token_required
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    result = file_service.save_file(file, current_user.id)

    if result['success']:
        # Save metadata to database
        file_record = FileRecord(
            file_id=result['file']['id'],
            original_name=result['file']['original_name'],
            user_id=current_user.id,
            size=result['file']['size'],
            mime_type=result['file']['mime_type']
        )
        db.session.add(file_record)
        db.session.commit()

        return jsonify(result['file']), 201
    else:
        return jsonify({'errors': result.get('errors') or [result['error']]}), 400

@app.route('/api/files/<file_id>', methods=['GET'])
@token_required
def download_file(file_id):
    file_record = FileRecord.query.filter_by(
        file_id=file_id,
        user_id=current_user.id
    ).first()

    if not file_record:
        return jsonify({'error': 'File not found'}), 404

    # Construct safe file path
    filepath = safe_join(
        app.config['UPLOAD_DIRECTORY'],
        current_user.id,
        file_record.file_id + '.' + file_record.original_name.rsplit('.', 1)[1]
    )

    if filepath and os.path.exists(filepath):
        return send_file(
            filepath,
            mimetype=file_record.mime_type,
            as_attachment=True,
            download_name=file_record.original_name
        )

    return jsonify({'error': 'File not found'}), 404

@app.route('/api/files/<file_id>', methods=['DELETE'])
@token_required
def delete_file(file_id):
    file_record = FileRecord.query.filter_by(
        file_id=file_id,
        user_id=current_user.id
    ).first()

    if not file_record:
        return jsonify({'error': 'File not found'}), 404

    result = file_service.delete_file(current_user.id, file_id)

    if result['success']:
        db.session.delete(file_record)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': result['error']}), 500
```

### 2. **Node.js Express File Upload with Multer**

```javascript
// config.js
const multer = require('multer');
const path = require('path');
const crypto = require('crypto');
const fs = require('fs');

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        const uploadDir = path.join(__dirname, 'uploads', req.user.id);
        fs.mkdirSync(uploadDir, { recursive: true });
        cb(null, uploadDir);
    },
    filename: (req, file, cb) => {
        const hash = crypto.randomBytes(16).toString('hex');
        const ext = path.extname(file.originalname);
        cb(null, hash + ext);
    }
});

const fileFilter = (req, file, cb) => {
    const allowedMimes = [
        'image/jpeg',
        'image/png',
        'image/gif',
        'application/pdf',
        'text/plain'
    ];

    const allowedExts = ['.pdf', '.txt', '.png', '.jpg', '.jpeg', '.gif', '.docx', '.doc'];
    const ext = path.extname(file.originalname).toLowerCase();

    if (!allowedMimes.includes(file.mimetype) || !allowedExts.includes(ext)) {
        return cb(new Error('Invalid file type'));
    }

    cb(null, true);
};

const upload = multer({
    storage: storage,
    fileFilter: fileFilter,
    limits: {
        fileSize: 50 * 1024 * 1024 // 50 MB
    }
});

module.exports = upload;

// file-service.js
const fs = require('fs').promises;
const path = require('path');
const FileRecord = require('../models/FileRecord');

class FileService {
    async uploadFile(req) {
        if (!req.file) {
            throw new Error('No file provided');
        }

        const fileInfo = {
            id: path.basename(req.file.filename, path.extname(req.file.filename)),
            originalName: req.file.originalname,
            safeName: req.file.filename,
            size: req.file.size,
            mimeType: req.file.mimetype,
            userId: req.user.id,
            uploadedAt: new Date()
        };

        // Save to database
        const record = await FileRecord.create(fileInfo);
        return record;
    }

    async downloadFile(fileId, userId) {
        const record = await FileRecord.findOne({
            where: { id: fileId, userId }
        });

        if (!record) {
            throw new Error('File not found');
        }

        const filepath = path.join(__dirname, 'uploads', userId, record.safeName);
        return { record, filepath };
    }

    async deleteFile(fileId, userId) {
        const record = await FileRecord.findOne({
            where: { id: fileId, userId }
        });

        if (!record) {
            throw new Error('File not found');
        }

        const filepath = path.join(__dirname, 'uploads', userId, record.safeName);
        await fs.unlink(filepath);
        await record.destroy();

        return { success: true };
    }

    async listUserFiles(userId, limit = 20, offset = 0) {
        const { rows, count } = await FileRecord.findAndCountAll({
            where: { userId },
            limit,
            offset,
            order: [['uploadedAt', 'DESC']]
        });

        return { files: rows, total: count };
    }
}

module.exports = new FileService();

// routes.js
const express = require('express');
const upload = require('../config/multer');
const fileService = require('../services/file-service');
const { authenticate } = require('../middleware/auth');

const router = express.Router();

router.post('/upload', authenticate, upload.single('file'), async (req, res, next) => {
    try {
        const file = await fileService.uploadFile(req);
        res.status(201).json(file);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

router.get('/files/:fileId', authenticate, async (req, res, next) => {
    try {
        const { record, filepath } = await fileService.downloadFile(
            req.params.fileId,
            req.user.id
        );
        res.download(filepath, record.originalName);
    } catch (error) {
        res.status(404).json({ error: error.message });
    }
});

router.delete('/files/:fileId', authenticate, async (req, res, next) => {
    try {
        await fileService.deleteFile(req.params.fileId, req.user.id);
        res.status(204).send();
    } catch (error) {
        res.status(404).json({ error: error.message });
    }
});

router.get('/files', authenticate, async (req, res, next) => {
    try {
        const page = parseInt(req.query.page) || 1;
        const limit = parseInt(req.query.limit) || 20;
        const offset = (page - 1) * limit;

        const { files, total } = await fileService.listUserFiles(
            req.user.id,
            limit,
            offset
        );

        res.json({
            data: files,
            pagination: { page, limit, total, pages: Math.ceil(total / limit) }
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

module.exports = router;
```

### 3. **FastAPI File Upload**

```python
# main.py
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.responses import FileResponse
import aiofiles
import os
import hashlib
import secrets
from pathlib import Path

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
MAX_FILE_SIZE = 50 * 1024 * 1024
ALLOWED_EXTENSIONS = {'.txt', '.pdf', '.png', '.jpg', '.jpeg', '.gif', '.docx', '.doc'}

class FileUploadService:
    async def validate_file(self, file: UploadFile) -> list:
        """Validate uploaded file"""
        errors = []

        # Check extension
        file_ext = Path(file.filename).suffix.lower()
        if file_ext not in ALLOWED_EXTENSIONS:
            errors.append(f'File type not allowed')

        # Check file size
        content = await file.read()
        await file.seek(0)

        if len(content) > MAX_FILE_SIZE:
            errors.append(f'File too large')

        return errors

    async def save_file(self, file: UploadFile, user_id: str):
        """Save uploaded file"""
        errors = await self.validate_file(file)
        if errors:
            return {'success': False, 'errors': errors}

        # Generate secure filename
        file_hash = hashlib.sha256(secrets.token_bytes(32)).hexdigest()
        file_ext = Path(file.filename).suffix
        safe_filename = f"{file_hash}{file_ext}"

        # Create user directory
        user_dir = UPLOAD_DIR / user_id
        user_dir.mkdir(exist_ok=True)

        filepath = user_dir / safe_filename

        try:
            content = await file.read()
            async with aiofiles.open(filepath, 'wb') as f:
                await f.write(content)

            return {
                'success': True,
                'file': {
                    'id': file_hash,
                    'original_name': file.filename,
                    'safe_name': safe_filename,
                    'size': len(content),
                    'mime_type': file.content_type
                }
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}

file_service = FileUploadService()

@app.post("/api/upload")
async def upload_file(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)
):
    """Upload file"""
    result = await file_service.save_file(file, current_user['id'])

    if result['success']:
        # Save to database
        file_record = FileRecord(
            file_id=result['file']['id'],
            original_name=result['file']['original_name'],
            user_id=current_user['id'],
            size=result['file']['size'],
            mime_type=result['file']['mime_type']
        )
        db.add(file_record)
        await db.commit()

        return result['file']
    else:
        raise HTTPException(status_code=400, detail=result.get('errors'))

@app.get("/api/files/{file_id}")
async def download_file(
    file_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Download file"""
    file_record = await db.query(FileRecord).filter(
        FileRecord.file_id == file_id,
        FileRecord.user_id == current_user['id']
    ).first()

    if not file_record:
        raise HTTPException(status_code=404, detail="File not found")

    filepath = UPLOAD_DIR / current_user['id'] / file_record.safe_name

    return FileResponse(
        path=filepath,
        media_type=file_record.mime_type,
        filename=file_record.original_name
    )

@app.delete("/api/files/{file_id}")
async def delete_file(
    file_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Delete file"""
    file_record = await db.query(FileRecord).filter(
        FileRecord.file_id == file_id,
        FileRecord.user_id == current_user['id']
    ).first()

    if not file_record:
        raise HTTPException(status_code=404, detail="File not found")

    filepath = UPLOAD_DIR / current_user['id'] / file_record.safe_name

    try:
        Path(filepath).unlink()
        await db.delete(file_record)
        await db.commit()
        return {'success': True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### 4. **S3/Cloud Storage Integration**

```python
# s3_service.py
import boto3
from datetime import timedelta
import os

class S3FileService:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )
        self.bucket_name = os.getenv('S3_BUCKET_NAME')

    def upload_file(self, file, user_id, file_key):
        """Upload file to S3"""
        try:
            self.s3_client.upload_fileobj(
                file,
                self.bucket_name,
                file_key,
                ExtraArgs={
                    'ContentType': file.content_type,
                    'Metadata': {'user_id': user_id}
                }
            )
            return {'success': True, 'key': file_key}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def get_signed_url(self, file_key, expires_in=3600):
        """Generate signed URL for download"""
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': file_key},
                ExpiresIn=expires_in
            )
            return {'success': True, 'url': url}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def delete_file(self, file_key):
        """Delete file from S3"""
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=file_key)
            return {'success': True}
        except Exception as e:
            return {'success': False, 'error': str(e)}
```

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

## Complete Example

```python
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if file.size > 10 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="File too large")

    allowed = ['.pdf', '.txt', '.jpg']
    ext = Path(file.filename).suffix
    if ext not in allowed:
        raise HTTPException(status_code=400, detail="Invalid file type")

    filename = f"{uuid4()}{ext}"
    async with aiofiles.open(f"uploads/{filename}", 'wb') as f:
        await f.write(await file.read())

    return {"filename": filename}
```
