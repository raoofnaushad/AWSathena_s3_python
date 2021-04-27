import boto3
import athena_from_s3
import S3_cleanup

params = {
    'region': 'ap-southeast-1',
    'database': 'mydatabase',
    'bucket': 'athena-test-buck',
    'path': 'temp/athena/output',
    'query': 'SELECT * FROM "mydatabase"."zipcode" limit 10;'
}


session = boto3.Session()

## Fucntion for obtaining query results and location 
location, data = athena_from_s3.query_results(session, params)
print("Locations: ",location)
print("Result Data: ")
print(data)
## Function for cleaning up the query results to avoid redundant data
S3_cleanup.clean_up()
