# Python/Flask File Upload

## Python/Flask File Upload

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
