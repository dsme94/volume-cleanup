#!/usr/bin/env python
"""EBS Volume cleanup"""

import boto3
import os

# Get region from lambda environment variable
REGION = os.environ.get('region')

# Setup connection to AWS 
EC2 = boto3.client('ec2', region_name=REGION)

def lambda_handler(event, context):
    """Main function"""
    cleanup_unattached(EC2)

def cleanup_unattached(client):
    """Cleanup volume function"""

    # Set volumes to be an array and get list of volumes
    volumes = []
    volumes = client.describe_volumes()

    # For each volume in the volumes array
    for volume in volumes['Volumes']:
        # If the volume status is available
        if volume['State'] == 'available':
            # Inform that the volume will be delete and delete
            print "Deleting: ", volume['VolumeId']
            client.delete_volume(VolumeId=volume['VolumeId'])
        else:
            continue

if __name__ == '__main__':
    lambda_handler(None, None)
