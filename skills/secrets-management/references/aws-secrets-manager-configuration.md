# AWS Secrets Manager Configuration

## AWS Secrets Manager Configuration

```python
# aws-secrets-manager.py
import boto3
import json
from datetime import datetime

class SecretsManager:
    def __init__(self, region='us-east-1'):
        self.client = boto3.client('secretsmanager', region_name=region)

    def create_secret(self, name, secret_value, tags=None):
        """Create a new secret"""
        try:
            response = self.client.create_secret(
                Name=name,
                SecretString=json.dumps(secret_value),
                Tags=tags or []
            )
            return response['ARN']
        except Exception as e:
            print(f"Error creating secret: {e}")
            raise

    def get_secret(self, name):
        """Retrieve a secret"""
        try:
            response = self.client.get_secret_value(SecretId=name)
            return json.loads(response['SecretString'])
        except Exception as e:
            print(f"Error retrieving secret: {e}")
            raise

    def update_secret(self, name, secret_value):
        """Update a secret"""
        try:
            response = self.client.update_secret(
                SecretId=name,
                SecretString=json.dumps(secret_value)
            )
            return response['ARN']
        except Exception as e:
            print(f"Error updating secret: {e}")
            raise

    def rotate_secret(self, name, rotation_rules):
        """Enable automatic rotation"""
        try:
            self.client.rotate_secret(
                SecretId=name,
                RotationRules=rotation_rules
            )
        except Exception as e:
            print(f"Error rotating secret: {e}")
            raise

    def list_secrets(self):
        """List all secrets"""
        try:
            response = self.client.list_secrets()
            return response['SecretList']
        except Exception as e:
            print(f"Error listing secrets: {e}")
            raise

    def delete_secret(self, name, recovery_days=30):
        """Delete a secret with recovery window"""
        try:
            response = self.client.delete_secret(
                SecretId=name,
                RecoveryWindowInDays=recovery_days
            )
            return response
        except Exception as e:
            print(f"Error deleting secret: {e}")
            raise

# Usage
if __name__ == '__main__':
    manager = SecretsManager()

    # Create database credentials secret
    db_creds = {
        'username': 'admin',
        'password': 'SecurePassword123!',
        'host': 'postgres.example.com',
        'port': 5432,
        'dbname': 'myapp'
    }

    secret_arn = manager.create_secret(
        'prod/database/credentials',
        db_creds,
        tags=[
            {'Key': 'Environment', 'Value': 'production'},
            {'Key': 'Service', 'Value': 'myapp'}
        ]
    )

    print(f"Secret created: {secret_arn}")

    # Setup rotation
    manager.rotate_secret(
        'prod/database/credentials',
        {'AutomaticallyAfterDays': 30}
    )

    # Retrieve secret
    retrieved = manager.get_secret('prod/database/credentials')
    print(f"Retrieved secret: {retrieved}")
```
