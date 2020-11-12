import boto3
session = boto3.Session(profile_name="Maruthi")
s3_client = session.client(service_name="s3")
for each_bucket in s3_client.list_buckets():
    print(each_bucket.get('Name')


