import boto3

def clean_up():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('athena-test-buck')
    for obj in bucket.objects.filter(Prefix='Query-Results/'):
        s3.Object(bucket.name,obj.key).delete()

    for obj in bucket.objects.filter(Prefix='temp/'):
        s3.Object(bucket.name, obj.key).delete()

