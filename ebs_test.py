from ebs import cleanup_unattached
from moto import mock_ec2
import boto3

@mock_ec2
def test_cleanup_unattached():
    client = boto3.client('ec2', region_name='us-east-1')

    client.create_volume(Size=10, AvailabilityZone='us-east-1a')
    cleanup_unattached(client)

if __name__ == '__main__':
    test_cleanup_unattached()