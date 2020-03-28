import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('athena-test-buck')
for obj in bucket.objects.filter(Prefix='Query-Results/'):
    s3.Object(bucket.name,obj.key).delete()