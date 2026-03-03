# Python Cryptography Implementation

## Python Cryptography Implementation

```python
# encryption_service.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import os
import base64
from typing import Tuple, Dict

class EncryptionService:
    def __init__(self):
        self.backend = default_backend()

    def generate_key(self) -> bytes:
        """Generate a random 256-bit key"""
        return os.urandom(32)

    def derive_key(self, password: str, salt: bytes = None) -> Tuple[bytes, bytes]:
        """Derive encryption key from password using PBKDF2"""
        if salt is None:
            salt = os.urandom(16)

        kdf = PBKDF2(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=self.backend
        )

        key = kdf.derive(password.encode())
        return key, salt

    def encrypt_aes_gcm(self, plaintext: bytes, key: bytes) -> Dict[str, str]:
        """Encrypt data using AES-256-GCM"""
        iv = os.urandom(12)  # 96-bit IV for GCM

        cipher = Cipher(
            algorithms.AES(key),
            modes.GCM(iv),
            backend=self.backend
        )

        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()

        return {
            'ciphertext': base64.b64encode(ciphertext).decode(),
            'iv': base64.b64encode(iv).decode(),
            'tag': base64.b64encode(encryptor.tag).decode()
        }

    def decrypt_aes_gcm(self, ciphertext: str, key: bytes, iv: str, tag: str) -> bytes:
        """Decrypt data using AES-256-GCM"""
        cipher = Cipher(
            algorithms.AES(key),
            modes.GCM(
                base64.b64decode(iv),
                base64.b64decode(tag)
            ),
            backend=self.backend
        )

        decryptor = cipher.decryptor()
        plaintext = decryptor.update(base64.b64decode(ciphertext)) + decryptor.finalize()

        return plaintext

    def encrypt_file(self, input_path: str, output_path: str, key: bytes) -> None:
        """Encrypt file using AES-256-GCM"""
        with open(input_path, 'rb') as f:
            plaintext = f.read()

        result = self.encrypt_aes_gcm(plaintext, key)

        # Write IV + ciphertext + tag
        with open(output_path, 'wb') as f:
            f.write(base64.b64decode(result['iv']))
            f.write(base64.b64decode(result['ciphertext']))
            f.write(base64.b64decode(result['tag']))

    def decrypt_file(self, input_path: str, output_path: str, key: bytes) -> None:
        """Decrypt file using AES-256-GCM"""
        with open(input_path, 'rb') as f:
            data = f.read()

        iv = data[:12]
        tag = data[-16:]
        ciphertext = data[12:-16]

        cipher = Cipher(
            algorithms.AES(key),
            modes.GCM(iv, tag),
            backend=self.backend
        )

        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        with open(output_path, 'wb') as f:
            f.write(plaintext)

    def generate_rsa_keypair(self) -> Tuple[bytes, bytes]:
        """Generate RSA key pair"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=self.backend
        )

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b'passphrase')
        )

        public_pem = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return private_pem, public_pem

    def encrypt_rsa(self, plaintext: bytes, public_key_pem: bytes) -> bytes:
        """Encrypt with RSA public key"""
        public_key = serialization.load_pem_public_key(
            public_key_pem,
            backend=self.backend
        )

        ciphertext = public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return ciphertext

    def decrypt_rsa(self, ciphertext: bytes, private_key_pem: bytes, passphrase: bytes) -> bytes:
        """Decrypt with RSA private key"""
        private_key = serialization.load_pem_private_key(
            private_key_pem,
            password=passphrase,
            backend=self.backend
        )

        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return plaintext

# Usage
if __name__ == '__main__':
    service = EncryptionService()

    # AES encryption
    key = service.generate_key()
    encrypted = service.encrypt_aes_gcm(b'Secret data', key)
    print(f"Encrypted: {encrypted['ciphertext']}")

    decrypted = service.decrypt_aes_gcm(
        encrypted['ciphertext'],
        key,
        encrypted['iv'],
        encrypted['tag']
    )
    print(f"Decrypted: {decrypted.decode()}")

    # Password-based encryption
    password = "mySecurePassword"
    key, salt = service.derive_key(password)
    print(f"Derived key: {base64.b64encode(key).decode()}")

    # RSA encryption
    private_key, public_key = service.generate_rsa_keypair()
    rsa_encrypted = service.encrypt_rsa(b'Secret message', public_key)
    rsa_decrypted = service.decrypt_rsa(rsa_encrypted, private_key, b'passphrase')
    print(f"RSA decrypted: {rsa_decrypted.decode()}")
```
