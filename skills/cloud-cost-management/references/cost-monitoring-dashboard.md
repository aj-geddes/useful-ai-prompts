# Cost Monitoring Dashboard

## Cost Monitoring Dashboard

```python
# Python cost monitoring tool
import boto3
from datetime import datetime, timedelta
from typing import Dict, List
import json

class CloudCostMonitor:
    def __init__(self):
        self.ce_client = boto3.client('ce')
        self.ec2_client = boto3.client('ec2')
        self.rds_client = boto3.client('rds')

    def get_monthly_costs_by_service(self, months=3) -> Dict:
        """Get monthly costs breakdown by service"""
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=30*months)

        response = self.ce_client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date.isoformat(),
                'End': end_date.isoformat()
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
            GroupBy=[
                {'Type': 'DIMENSION', 'Key': 'SERVICE'}
            ]
        )

        costs = {}
        for result in response['ResultsByTime']:
            for group in result['Groups']:
                service = group['Keys'][0]
                cost = float(group['Metrics']['UnblendedCost']['Amount'])

                if service not in costs:
                    costs[service] = []
                costs[service].append({
                    'date': result['TimePeriod']['Start'],
                    'cost': cost
                })

        return costs

    def identify_savings_opportunities(self) -> Dict:
        """Identify resources that can be optimized"""
        opportunities = {
            'unattached_ebs_volumes': [],
            'unassociated_eips': [],
            'underutilized_instances': [],
            'unattached_network_interfaces': []
        }

        # Check EBS volumes
        volumes_response = self.ec2_client.describe_volumes(
            Filters=[{'Name': 'status', 'Values': ['available']}]
        )

        for volume in volumes_response['Volumes']:
            opportunities['unattached_ebs_volumes'].append({
                'volume_id': volume['VolumeId'],
                'size_gb': volume['Size'],
                'estimated_monthly_cost': volume['Size'] * 0.10
            })

        # Check Elastic IPs
        addresses_response = self.ec2_client.describe_addresses()

        for address in addresses_response['Addresses']:
            if 'AssociationId' not in address:
                opportunities['unassociated_eips'].append({
                    'public_ip': address['PublicIp'],
                    'estimated_monthly_cost': 3.60
                })

        # Check underutilized instances
        instances_response = self.ec2_client.describe_instances()

        for reservation in instances_response['Reservations']:
            for instance in reservation['Instances']:
                opportunities['underutilized_instances'].append({
                    'instance_id': instance['InstanceId'],
                    'instance_type': instance['InstanceType'],
                    'state': instance['State']['Name'],
                    'recommendation': 'Consider downsizing or terminating'
                })

        return opportunities

    def calculate_potential_savings(self, opportunities: Dict) -> Dict:
        """Calculate potential monthly savings"""
        savings = {
            'ebs_volumes': sum(op['estimated_monthly_cost'] for op in opportunities['unattached_ebs_volumes']),
            'eips': sum(op['estimated_monthly_cost'] for op in opportunities['unassociated_eips']),
            'total_monthly': 0
        }

        savings['total_monthly'] = savings['ebs_volumes'] + savings['eips']
        savings['total_annual'] = savings['total_monthly'] * 12

        return savings

    def generate_cost_report(self) -> str:
        """Generate comprehensive cost report"""
        costs_by_service = self.get_monthly_costs_by_service()
        opportunities = self.identify_savings_opportunities()
        savings = self.calculate_potential_savings(opportunities)

        report = f"""
        ===== CLOUD COST REPORT =====
        Generated: {datetime.now().isoformat()}

        CURRENT COSTS BY SERVICE:
        """

        for service, costs in costs_by_service.items():
            total = sum(c['cost'] for c in costs)
            report += f"\n{service}: ${total:.2f}"

        report += f"""

        SAVINGS OPPORTUNITIES:
        - Unattached EBS Volumes: ${savings['ebs_volumes']:.2f}/month
        - Unassociated EIPs: ${savings['eips']:.2f}/month

        POTENTIAL MONTHLY SAVINGS: ${savings['total_monthly']:.2f}
        POTENTIAL ANNUAL SAVINGS: ${savings['total_annual']:.2f}
        """

        return report

# Usage
monitor = CloudCostMonitor()
print(monitor.generate_cost_report())
```
