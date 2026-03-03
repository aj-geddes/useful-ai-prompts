# Node.js Express File Upload with Multer

## Node.js Express File Upload with Multer

```javascript
// config.js
const multer = require("multer");
const path = require("path");
const crypto = require("crypto");
const fs = require("fs");

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const uploadDir = path.join(__dirname, "uploads", req.user.id);
    fs.mkdirSync(uploadDir, { recursive: true });
    cb(null, uploadDir);
  },
  filename: (req, file, cb) => {
    const hash = crypto.randomBytes(16).toString("hex");
    const ext = path.extname(file.originalname);
    cb(null, hash + ext);
  },
});

const fileFilter = (req, file, cb) => {
  const allowedMimes = [
    "image/jpeg",
    "image/png",
    "image/gif",
    "application/pdf",
    "text/plain",
  ];

  const allowedExts = [
    ".pdf",
    ".txt",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".docx",
    ".doc",
  ];
  const ext = path.extname(file.originalname).toLowerCase();

  if (!allowedMimes.includes(file.mimetype) || !allowedExts.includes(ext)) {
    return cb(new Error("Invalid file type"));
  }

  cb(null, true);
};

const upload = multer({
  storage: storage,
  fileFilter: fileFilter,
  limits: {
    fileSize: 50 * 1024 * 1024, // 50 MB
  },
});

module.exports = upload;

// file-service.js
const fs = require("fs").promises;
const path = require("path");
const FileRecord = require("../models/FileRecord");

class FileService {
  async uploadFile(req) {
    if (!req.file) {
      throw new Error("No file provided");
    }

    const fileInfo = {
      id: path.basename(req.file.filename, path.extname(req.file.filename)),
      originalName: req.file.originalname,
      safeName: req.file.filename,
      size: req.file.size,
      mimeType: req.file.mimetype,
      userId: req.user.id,
      uploadedAt: new Date(),
    };

    // Save to database
    const record = await FileRecord.create(fileInfo);
    return record;
  }

  async downloadFile(fileId, userId) {
    const record = await FileRecord.findOne({
      where: { id: fileId, userId },
    });

    if (!record) {
      throw new Error("File not found");
    }

    const filepath = path.join(__dirname, "uploads", userId, record.safeName);
    return { record, filepath };
  }

  async deleteFile(fileId, userId) {
    const record = await FileRecord.findOne({
      where: { id: fileId, userId },
    });

    if (!record) {
      throw new Error("File not found");
    }

    const filepath = path.join(__dirname, "uploads", userId, record.safeName);
    await fs.unlink(filepath);
    await record.destroy();

    return { success: true };
  }

  async listUserFiles(userId, limit = 20, offset = 0) {
    const { rows, count } = await FileRecord.findAndCountAll({
      where: { userId },
      limit,
      offset,
      order: [["uploadedAt", "DESC"]],
    });

    return { files: rows, total: count };
  }
}

module.exports = new FileService();

// routes.js
const express = require("express");
const upload = require("../config/multer");
const fileService = require("../services/file-service");
const { authenticate } = require("../middleware/auth");

const router = express.Router();

router.post(
  "/upload",
  authenticate,
  upload.single("file"),
  async (req, res, next) => {
    try {
      const file = await fileService.uploadFile(req);
      res.status(201).json(file);
    } catch (error) {
      res.status(400).json({ error: error.message });
    }
  },
);

router.get("/files/:fileId", authenticate, async (req, res, next) => {
  try {
    const { record, filepath } = await fileService.downloadFile(
      req.params.fileId,
      req.user.id,
    );
    res.download(filepath, record.originalName);
  } catch (error) {
    res.status(404).json({ error: error.message });
  }
});

router.delete("/files/:fileId", authenticate, async (req, res, next) => {
  try {
    await fileService.deleteFile(req.params.fileId, req.user.id);
    res.status(204).send();
  } catch (error) {
    res.status(404).json({ error: error.message });
  }
});

router.get("/files", authenticate, async (req, res, next) => {
  try {
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 20;
    const offset = (page - 1) * limit;

    const { files, total } = await fileService.listUserFiles(
      req.user.id,
      limit,
      offset,
    );

    res.json({
      data: files,
      pagination: { page, limit, total, pages: Math.ceil(total / limit) },
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```
