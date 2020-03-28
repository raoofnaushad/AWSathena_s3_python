import boto3
import pandas
import csv
import time


def query_results(session, params):
    ## Creating the Client for Athena
    client = boto3.client('athena')
    
    ## This function executes the query and returns the query execution ID
    response_query_execution_id = client.start_query_execution(
        QueryString = params['query'],
        QueryExecutionContext = {
            'Database' : params['database']
        },
        ResultConfiguration = {
            'OutputLocation': 's3://' + params['bucket'] + '/' + params['path']
        }
    )

    ## This function takes query execution id as input and returns the details of the query executed
    response_get_query_details = client.get_query_execution(
        QueryExecutionId = response_query_execution_id['QueryExecutionId']
    )

    print(response_get_query_details)

    # time.sleep(1)
    ## Condition for checking the details of response

    status = 'RUNNING'
    iterations = 5

    while (iterations>0):
        iterations = iterations - 1
        response_get_query_details = client.get_query_execution(
        QueryExecutionId = response_query_execution_id['QueryExecutionId']
        )
        status = response_get_query_details['QueryExecution']['Status']['State']
        print(status)
        if (status == 'FAILED') or (status == 'CANCELLED') :
            return False, False
            
        elif status == 'SUCCEEDED':
            location = response_get_query_details['QueryExecution']['ResultConfiguration']['OutputLocation']

            ## Function to get output results
            response_query_result = client.get_query_results(
                QueryExecutionId = response_query_execution_id['QueryExecutionId']
            )
            result_data = response_query_result['ResultSet']
            print("location: ", location)
            print("data: ", result_data)
            return location, result_data
        else:
            time.sleep(1)
        
    return False

