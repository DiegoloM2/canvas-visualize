import boto3
from botocore.exceptions import NoCredentialsError
import os
import json


SECRET_KEY = os.environ["AWS_S3_SECRET_ACCESS_KEY"]
ACCESS_KEY = os.environ['AWS_S3_ACCESS_KEY_ID']


def upload(txt, bucket, s3_file): 
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    if s3_file is None: 
        s3_file = os.path.basename(local_file)
    s3.put_object(Body = bytes(txt, "utf-8"),Bucket = bucket, Key = f"media/{s3_file}")
    print("Upload Successful")
    return True

def open(bucket, file): 
    client = boto3.client(
        's3', 
        aws_access_key_id=ACCESS_KEY, 
        aws_secret_access_key=SECRET_KEY)
    
    obj =  client.get_object(
        Bucket = bucket, 
        Key = f"media/{file}"
    )
    code = obj['Body'].read().decode('utf-8')
    return code
    
    