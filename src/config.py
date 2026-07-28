import boto3
import os
from dotenv import load_dotenv
    
load_dotenv() # Load environment variables from a .env file

s3 = boto3.client("s3", region_name=os.getenv("AWS_REGION"))  # Create an S3 client using the default AWS credentials and region
BUCKET_NAME = os.getenv("AWS_BUCKET_NAME") # Define the name of the S3 bucket to upload the weather data to
AWS_REGION = os.getenv("AWS_REGION", "us-east-1") # Define the AWS region where the S3 bucket is located

s3 = boto3.client("s3", region_name=AWS_REGION)  # Create an S3 client using the default AWS credentials and region