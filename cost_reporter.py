import boto3
from datetime import date

ce = boto3.client('ce')

def get_costs():
    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': '2024-01-01', #specify start date here
            'End': str(date.today())
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[
            {'Type': 'DIMENSION', 'Key': 'SERVICE'}
        ]
    )

    for result in response['ResultsByTime']:
        for group in result['Groups']:
            service = group['Keys'][0]
            cost = group['Metrics']['UnblendedCost']['Amount']
            print(f"{service}: ${cost}")

if __name__ == "__main__":
    get_costs()