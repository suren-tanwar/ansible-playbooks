# pip install boto3
# python task4.py run this
# configure aws from local

import boto3

def get_services_by_region():
    # Get a list of regions
    ec2_client = boto3.client('ec2', region_name='us-east-1')  # Using us-east-1, but you can change it to any other region
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Iterate through each region
    for region in regions:
        print(f"\nRegion: {region}")

        # List EC2 instances
        ec2_resource = boto3.resource('ec2', region_name=region)
        ec2_instances = ec2_resource.instances.all()
        for instance in ec2_instances:
            print(f"  EC2 Instance: {instance.id}")
            print(f"    State: {instance.state['Name']}")
            print(f"    Instance Type: {instance.instance_type}")
            print(f"    Launch Time: {instance.launch_time}")

        # List S3 buckets
        s3_client = boto3.client('s3', region_name=region)
        s3_buckets = s3_client.list_buckets()['Buckets']
        for bucket in s3_buckets:
            print(f"  S3 Bucket: {bucket['Name']}")
            print(f"    Creation Date: {bucket['CreationDate']}")
        # List RDS instances
        rds_client = boto3.client('rds', region_name=region)
        rds_instances = rds_client.describe_db_instances()['DBInstances']
        for rds_instance in rds_instances:
            print(f"    DB Instance Identifier: {rds_instance['DBInstanceIdentifier']}")
            print(f"    Engine: {rds_instance['Engine']}")
            print(f"    Status: {rds_instance['DBInstanceStatus']}")

# Describe detail about the services
def describe_service(service_name, region):
    session = boto3.Session(region_name=region)
    client = session.client(service_name)
    try:
        response = client.describe_instances()  # You can replace this with appropriate describe method for each service
        print(f"Details for {service_name} in {region}:\n")
        print(response)
        print("\n" + "="*50 + "\n")
    except Exception as e:
        print(f"Failed to describe {service_name} in {region}: {str(e)}\n")

def list_detailed_services():
    regions = ['us-east-1', 'ap-south-1', 'eu-west-1']  # Add more regions as needed
    services = ['ec2', 'rds', 's3']  # Add more AWS service names as needed

    for service in services:
        for region in regions:
            describe_service(service, region)

if __name__ == "__main__":
    print("List AWS Services Region-wise:")
    get_services_by_region()

    print("\nList Detailed AWS Services:")
    list_detailed_services()

