# Python Secrets Rotation with Vault

## Python Secrets Rotation with Vault

```python
# secrets_rotation.py
import hvac
import secrets
import string
from datetime import datetime, timedelta
from typing import Dict, Any
import psycopg2
import boto3

class SecretsRotation:
    def __init__(self, vault_url: str, vault_token: str):
        self.vault_client = hvac.Client(url=vault_url, token=vault_token)
        self.ssm = boto3.client('ssm')

    def generate_secret(self, secret_type: str = 'api_key', length: int = 32) -> str:
        """Generate new secret value"""
        if secret_type == 'api_key':
            return secrets.token_urlsafe(length)

        elif secret_type == 'password':
            # Strong password with all character types
            chars = string.ascii_letters + string.digits + string.punctuation
            return ''.join(secrets.choice(chars) for _ in range(length))

        elif secret_type == 'jwt_secret':
            return secrets.token_urlsafe(64)

        else:
            return secrets.token_bytes(length).hex()

    def rotate_secret(self, path: str, secret_type: str = 'api_key') -> Dict[str, Any]:
        """Rotate secret with zero downtime"""
        print(f"Starting rotation for: {path}")

        try:
            # Read current secret
            current_secret = self.vault_client.secrets.kv.v2.read_secret(path=path)
            current_data = current_secret['data']['data']

            # Generate new value
            new_value = self.generate_secret(secret_type)

            # Store with both old and new values
            rotation_data = {
                'current': new_value,
                'previous': current_data.get('current', current_data.get('value')),
                'rotated_at': datetime.utcnow().isoformat()
            }

            self.vault_client.secrets.kv.v2.create_or_update_secret(
                path=path,
                secret=rotation_data
            )

            print(f"Secret rotated successfully: {path}")

            return {
                'success': True,
                'path': path,
                'rotated_at': rotation_data['rotated_at']
            }

        except Exception as e:
            print(f"Rotation failed for {path}: {e}")
            raise

    def rotate_database_password(self, secret_path: str) -> Dict[str, Any]:
        """Rotate database credentials"""
        # Get current credentials
        secret = self.vault_client.secrets.kv.v2.read_secret(path=secret_path)
        creds = secret['data']['data']

        # Generate new password
        new_password = self.generate_secret('password', 20)

        # Connect to database
        conn = psycopg2.connect(
            host=creds['host'],
            database=creds['database'],
            user=creds['username'],
            password=creds['password']
        )

        cursor = conn.cursor()

        try:
            # Update password in database
            cursor.execute(
                f"ALTER USER {creds['username']} WITH PASSWORD %s",
                (new_password,)
            )
            conn.commit()

            # Update secret in Vault
            updated_creds = {
                **creds,
                'password': new_password,
                'rotated_at': datetime.utcnow().isoformat()
            }

            self.vault_client.secrets.kv.v2.create_or_update_secret(
                path=secret_path,
                secret=updated_creds
            )

            print(f"Database credentials rotated: {secret_path}")

            return {'success': True}

        finally:
            cursor.close()
            conn.close()

    def schedule_rotation(self, path: str, interval_days: int = 90):
        """Schedule automatic rotation using AWS Lambda"""
        # Create rotation schedule in AWS Secrets Manager
        # or use cron job

        schedule_expression = f"rate({interval_days} days)"

        # This would trigger a Lambda function
        print(f"Rotation scheduled for {path}: every {interval_days} days")

    def rotate_encryption_keys(self, key_id: str):
        """Rotate encryption keys"""
        kms = boto3.client('kms')

        # Enable automatic key rotation
        kms.enable_key_rotation(KeyId=key_id)

        print(f"Automatic rotation enabled for KMS key: {key_id}")

    def audit_rotation_history(self, path: str) -> list:
        """Get rotation history"""
        versions = self.vault_client.secrets.kv.v2.read_secret_metadata(path=path)

        history = []
        for version, metadata in versions['data']['versions'].items():
            history.append({
                'version': version,
                'created_time': metadata['created_time'],
                'deleted': metadata.get('deletion_time') is not None
            })

        return sorted(history, key=lambda x: x['created_time'], reverse=True)

# Usage
if __name__ == '__main__':
    rotation = SecretsRotation(
        vault_url='http://localhost:8200',
        vault_token='your-token'
    )

    # Rotate API key
    rotation.rotate_secret('api-keys/external-service', 'api_key')

    # Rotate database credentials
    rotation.rotate_database_password('database/production')

    # Schedule rotations
    rotation.schedule_rotation('api-keys/external-service', 30)
    rotation.schedule_rotation('database/production', 90)

    # View history
    history = rotation.audit_rotation_history('api-keys/external-service')
    print(f"Rotation history: {history}")
```
