import boto3
import pandas as pd
from io import StringIO
import random
import datetime

BUCKET_NAME = 'bucket-name'
FILE_KEY = 'data.csv'

def lambda_handler(event, context):
    # Generate random data
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_value = random.randint(0, 100)
    
    # Create or update the CSV data
    try:
        s3 = boto3.client('s3')
        csv_obj = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
        df = pd.read_csv(csv_obj['Body'])
    except:
        # If the file doesn't exist, create a new dataframe
        df = pd.DataFrame(columns=['Time', 'Value'])
    
    df = pd.concat([df, pd.DataFrame({'Time': [time_now], 'Value': [new_value]})], ignore_index=True)
    
    # Save updated CSV to S3
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=BUCKET_NAME, Key=FILE_KEY, Body=csv_buffer.getvalue())
    
    return {
        'statusCode': 200,
        'body': 'Data updated successfully!'
    }
