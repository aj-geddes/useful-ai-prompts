# OWASP ZAP (DAST)

## OWASP ZAP (DAST)

```python
# security_scan.py
from zapv2 import ZAPv2
import time

class SecurityScanner:
    def __init__(self, target_url, api_key=None):
        self.zap = ZAPv2(apikey=api_key, proxies={
            'http': 'http://localhost:8080',
            'https': 'http://localhost:8080'
        })
        self.target = target_url

    def scan(self):
        """Run full security scan."""
        print(f"Scanning {self.target}...")

        # Spider the application
        print("Spidering...")
        scan_id = self.zap.spider.scan(self.target)
        while int(self.zap.spider.status(scan_id)) < 100:
            time.sleep(2)
            print(f"Spider progress: {self.zap.spider.status(scan_id)}%")

        # Active scan
        print("Running active scan...")
        scan_id = self.zap.ascan.scan(self.target)
        while int(self.zap.ascan.status(scan_id)) < 100:
            time.sleep(5)
            print(f"Scan progress: {self.zap.ascan.status(scan_id)}%")

        return self.get_results()

    def get_results(self):
        """Get scan results."""
        alerts = self.zap.core.alerts(baseurl=self.target)

        # Group by risk level
        results = {
            'high': [],
            'medium': [],
            'low': [],
            'informational': []
        }

        for alert in alerts:
            risk = alert['risk'].lower()
            results[risk].append({
                'name': alert['alert'],
                'description': alert['description'],
                'solution': alert['solution'],
                'url': alert['url'],
                'param': alert.get('param', ''),
                'evidence': alert.get('evidence', '')
            })

        return results

    def report(self, results):
        """Generate security report."""
        print("\n" + "="*60)
        print("SECURITY SCAN RESULTS")
        print("="*60)

        for risk_level in ['high', 'medium', 'low', 'informational']:
            issues = results[risk_level]
            if issues:
                print(f"\n{risk_level.upper()} Risk Issues: {len(issues)}")
                for issue in issues[:5]:  # Show first 5
                    print(f"  - {issue['name']}")
                    print(f"    URL: {issue['url']}")
                    if issue['param']:
                        print(f"    Parameter: {issue['param']}")

        # Fail if high risk found
        if results['high']:
            raise Exception(f"Found {len(results['high'])} HIGH risk vulnerabilities!")

# Usage
scanner = SecurityScanner('http://localhost:3000')
results = scanner.scan()
scanner.report(results)
```
