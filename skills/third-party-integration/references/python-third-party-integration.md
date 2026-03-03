# Python Third-Party Integration

## Python Third-Party Integration

```python
import requests
import time
from typing import Optional, Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, api_key: str, base_url: str, timeout: int = 30):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })

    def request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        max_retries: int = 3
    ) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        attempt = 0

        while attempt < max_retries:
            try:
                response = self.session.request(
                    method,
                    url,
                    json=data,
                    timeout=self.timeout
                )

                if response.status_code >= 200 and response.status_code < 300:
                    return {
                        'success': True,
                        'data': response.json(),
                        'status': response.status_code
                    }

                if response.status_code >= 500 or response.status_code == 429:
                    raise requests.RequestException(f"HTTP {response.status_code}")

                return {
                    'success': False,
                    'error': response.json().get('message', 'Error'),
                    'status': response.status_code
                }

            except requests.RequestException as e:
                attempt += 1
                if attempt >= max_retries:
                    logger.error(f"API request failed: {e}")
                    return {
                        'success': False,
                        'error': str(e),
                        'status': None
                    }

                wait_time = 2 ** attempt
                time.sleep(wait_time)

        return {'success': False, 'error': 'Max retries exceeded'}

    def get(self, endpoint: str) -> Dict[str, Any]:
        return self.request('GET', endpoint)

    def post(self, endpoint: str, data: Dict) -> Dict[str, Any]:
        return self.request('POST', endpoint, data)

    def put(self, endpoint: str, data: Dict) -> Dict[str, Any]:
        return self.request('PUT', endpoint, data)

    def delete(self, endpoint: str) -> Dict[str, Any]:
        return self.request('DELETE', endpoint)

# Payment processor example
class PaymentGateway(APIClient):
    def create_payment(self, amount: float, currency: str, customer_id: str):
        return self.post('charges', {
            'amount': int(amount * 100),
            'currency': currency,
            'customer': customer_id
        })

    def refund(self, charge_id: str, amount: Optional[float] = None):
        return self.post(f'charges/{charge_id}/refund', {
            'amount': int(amount * 100) if amount else None
        })
```
