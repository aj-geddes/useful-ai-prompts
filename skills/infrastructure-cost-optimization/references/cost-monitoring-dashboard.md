# Cost Monitoring Dashboard

## Cost Monitoring Dashboard

```python
# cost-monitoring.py
import boto3
import json
from datetime import datetime, timedelta

class CostOptimizer:
    def __init__(self):
        self.ce_client = boto3.client('ce')
        self.ec2_client = boto3.client('ec2')
        self.rds_client = boto3.client('rds')

    def get_daily_costs(self, days=30):
        """Get daily costs for past N days"""
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)

        response = self.ce_client.get_cost_and_usage(
            TimePeriod={
                'Start': str(start_date),
                'End': str(end_date)
            },
            Granularity='DAILY',
            Metrics=['BlendedCost'],
            GroupBy=[
                {'Type': 'DIMENSION', 'Key': 'SERVICE'}
            ]
        )

        return response

    def find_underutilized_instances(self):
        """Find EC2 instances with low CPU usage"""
        cloudwatch = boto3.client('cloudwatch')
        instances = []

        ec2_instances = self.ec2_client.describe_instances()
        for reservation in ec2_instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']

                # Check CPU utilization
                response = cloudwatch.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName='CPUUtilization',
                    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                    StartTime=datetime.now() - timedelta(days=7),
                    EndTime=datetime.now(),
                    Period=3600,
                    Statistics=['Average']
                )

                if response['Datapoints']:
                    avg_cpu = sum(d['Average'] for d in response['Datapoints']) / len(response['Datapoints'])
                    if avg_cpu < 10:  # Less than 10% average
                        instances.append({
                            'InstanceId': instance_id,
                            'Type': instance['InstanceType'],
                            'AverageCPU': avg_cpu,
                            'Recommendation': 'Downsize or terminate'
                        })

        return instances

    def estimate_reserved_instance_savings(self):
        """Estimate potential savings from reserved instances"""
        response = self.ce_client.get_reservation_purchase_recommendation(
            Service='EC2',
            LookbackPeriod='THIRTY_DAYS',
            PageSize=100
        )

        total_savings = 0
        for recommendation in response.get('Recommendations', []):
            summary = recommendation['RecommendationSummary']
            savings = float(summary['EstimatedMonthlyMonthlySavingsAmount'])
            total_savings += savings

        return total_savings

    def generate_report(self):
        """Generate comprehensive cost optimization report"""
        print("=== Cost Optimization Report ===\n")

        # Daily costs
        print("Daily Costs:")
        costs = self.get_daily_costs(7)
        for result in costs['ResultsByTime']:
            date = result['TimePeriod']['Start']
            total = result['Total']['BlendedCost']['Amount']
            print(f"  {date}: ${total}")

        # Underutilized instances
        print("\nUnderutilized Instances:")
        underutilized = self.find_underutilized_instances()
        for instance in underutilized:
            print(f"  {instance['InstanceId']}: {instance['AverageCPU']:.1f}% CPU - {instance['Recommendation']}")

        # Reserved instance savings
        print("\nReserved Instance Savings Potential:")
        savings = self.estimate_reserved_instance_savings()
        print(f"  Estimated Monthly Savings: ${savings:.2f}")

# Usage
if __name__ == '__main__':
    optimizer = CostOptimizer()
    optimizer.generate_report()
```
