# FastAPI File Upload

## FastAPI File Upload

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
