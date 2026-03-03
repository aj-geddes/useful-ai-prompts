# Node.js Encryption Library

## Node.js Encryption Library

```javascript
// encryption-service.js
const crypto = require("crypto");
const fs = require("fs").promises;

class EncryptionService {
  constructor() {
    // AES-256-GCM for symmetric encryption
    this.algorithm = "aes-256-gcm";
    this.keyLength = 32; // 256 bits
    this.ivLength = 16; // 128 bits
    this.saltLength = 64;
    this.tagLength = 16;
  }

  /**
   * Generate a cryptographically secure random key
   */
  generateKey() {
    return crypto.randomBytes(this.keyLength);
  }

  /**
   * Derive a key from a password using PBKDF2
   */
  async deriveKey(password, salt = null) {
    if (!salt) {
      salt = crypto.randomBytes(this.saltLength);
    }

    return new Promise((resolve, reject) => {
      crypto.pbkdf2(
        password,
        salt,
        100000, // iterations
        this.keyLength,
        "sha512",
        (err, derivedKey) => {
          if (err) reject(err);
          else resolve({ key: derivedKey, salt });
        },
      );
    });
  }

  /**
   * Encrypt data using AES-256-GCM
   */
  encrypt(data, key) {
    const iv = crypto.randomBytes(this.ivLength);
    const cipher = crypto.createCipheriv(this.algorithm, key, iv);

    let encrypted = cipher.update(data, "utf8", "hex");
    encrypted += cipher.final("hex");

    const tag = cipher.getAuthTag();

    // Return IV + encrypted data + auth tag
    return {
      encrypted: encrypted,
      iv: iv.toString("hex"),
      tag: tag.toString("hex"),
    };
  }

  /**
   * Decrypt data using AES-256-GCM
   */
  decrypt(encryptedData, key, iv, tag) {
    const decipher = crypto.createDecipheriv(
      this.algorithm,
      key,
      Buffer.from(iv, "hex"),
    );

    decipher.setAuthTag(Buffer.from(tag, "hex"));

    let decrypted = decipher.update(encryptedData, "hex", "utf8");
    decrypted += decipher.final("utf8");

    return decrypted;
  }

  /**
   * Encrypt file
   */
  async encryptFile(inputPath, outputPath, key) {
    const iv = crypto.randomBytes(this.ivLength);
    const cipher = crypto.createCipheriv(this.algorithm, key, iv);

    const input = await fs.readFile(inputPath);
    const encrypted = Buffer.concat([cipher.update(input), cipher.final()]);

    const tag = cipher.getAuthTag();

    // Write IV + encrypted data + auth tag
    const output = Buffer.concat([iv, encrypted, tag]);
    await fs.writeFile(outputPath, output);

    return { iv: iv.toString("hex"), tag: tag.toString("hex") };
  }

  /**
   * Decrypt file
   */
  async decryptFile(inputPath, outputPath, key) {
    const data = await fs.readFile(inputPath);

    const iv = data.subarray(0, this.ivLength);
    const tag = data.subarray(data.length - this.tagLength);
    const encrypted = data.subarray(
      this.ivLength,
      data.length - this.tagLength,
    );

    const decipher = crypto.createDecipheriv(this.algorithm, key, iv);
    decipher.setAuthTag(tag);

    const decrypted = Buffer.concat([
      decipher.update(encrypted),
      decipher.final(),
    ]);

    await fs.writeFile(outputPath, decrypted);
  }

  /**
   * Hash password using bcrypt-style approach
   */
  async hashPassword(password) {
    const salt = crypto.randomBytes(16);

    return new Promise((resolve, reject) => {
      crypto.pbkdf2(password, salt, 100000, 64, "sha512", (err, hash) => {
        if (err) reject(err);
        else {
          const combined = Buffer.concat([salt, hash]);
          resolve(combined.toString("hex"));
        }
      });
    });
  }

  /**
   * Verify password hash
   */
  async verifyPassword(password, hashedPassword) {
    const combined = Buffer.from(hashedPassword, "hex");
    const salt = combined.subarray(0, 16);
    const hash = combined.subarray(16);

    return new Promise((resolve, reject) => {
      crypto.pbkdf2(
        password,
        salt,
        100000,
        64,
        "sha512",
        (err, derivedHash) => {
          if (err) reject(err);
          else resolve(crypto.timingSafeEqual(hash, derivedHash));
        },
      );
    });
  }

  /**
   * Generate RSA key pair
   */
  generateKeyPair() {
    return crypto.generateKeyPairSync("rsa", {
      modulusLength: 4096,
      publicKeyEncoding: {
        type: "spki",
        format: "pem",
      },
      privateKeyEncoding: {
        type: "pkcs8",
        format: "pem",
        cipher: "aes-256-cbc",
        passphrase: process.env.KEY_PASSPHRASE || "top-secret",
      },
    });
  }

  /**
   * Encrypt with public key (RSA)
   */
  encryptWithPublicKey(data, publicKey) {
    return crypto.publicEncrypt(
      {
        key: publicKey,
        padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
        oaepHash: "sha256",
      },
      Buffer.from(data),
    );
  }

  /**
   * Decrypt with private key (RSA)
   */
  decryptWithPrivateKey(encrypted, privateKey) {
    return crypto.privateDecrypt(
      {
        key: privateKey,
        padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
        oaepHash: "sha256",
      },
      encrypted,
    );
  }
}

// Usage examples
async function main() {
  const encryptionService = new EncryptionService();

  // 1. Symmetric encryption
  const key = encryptionService.generateKey();
  const encrypted = encryptionService.encrypt("Secret message", key);
  console.log("Encrypted:", encrypted);

  const decrypted = encryptionService.decrypt(
    encrypted.encrypted,
    key,
    encrypted.iv,
    encrypted.tag,
  );
  console.log("Decrypted:", decrypted);

  // 2. Password-based encryption
  const { key: derivedKey, salt } =
    await encryptionService.deriveKey("myPassword");
  const passwordEncrypted = encryptionService.encrypt("Data", derivedKey);
  console.log("Password encrypted:", passwordEncrypted);

  // 3. Password hashing
  const hashedPassword =
    await encryptionService.hashPassword("userPassword123");
  const isValid = await encryptionService.verifyPassword(
    "userPassword123",
    hashedPassword,
  );
  console.log("Password valid:", isValid);

  // 4. RSA encryption
  const { publicKey, privateKey } = encryptionService.generateKeyPair();
  const rsaEncrypted = encryptionService.encryptWithPublicKey(
    "Secret",
    publicKey,
  );
  const rsaDecrypted = encryptionService.decryptWithPrivateKey(
    rsaEncrypted,
    privateKey,
  );
  console.log("RSA decrypted:", rsaDecrypted.toString());
}

main().catch(console.error);

module.exports = EncryptionService;
```
