import logging
import boto3
from botocore.exceptions import ClientError
import datetime

time = (int((datetime.datetime.timestamp(datetime.datetime.now()))))
AWS_REGION = 'eu-north-1'
AWS_BUCKET = (f"nazar{time}")


def lambda_handler(event, context):
    response = create_bucket(AWS_BUCKET, region=AWS_REGION)
    print(response)
     
def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=AWS_BUCKET)
        else:
            s3_client = boto3.client('s3', region_name=AWS_REGION)
            location = {'LocationConstraint': AWS_REGION}
            s3_client.create_bucket(Bucket=AWS_BUCKET,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True