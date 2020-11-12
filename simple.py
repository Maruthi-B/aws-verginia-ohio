import boto3
session = boto3.Session(profile_name="Maruthi")
s3-client = session.client(service_name="s3")

