import boto3
s3 = boto3.client('s3')
response = s3.list_buckets()

print("exisiting buckets")
for bucket in response['Buckets']:
    print(f' {bucket["Name"]}')