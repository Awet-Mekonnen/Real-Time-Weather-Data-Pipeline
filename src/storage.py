import boto3
import os
import json
from config import s3, BUCKET_NAME
from datetime import datetime, timezone


def upload_to_s3(file_path, s3_key):
    # Upload the specified file to the S3 bucket with the given key
    s3.upload_file(file_path, BUCKET_NAME, s3_key)
    print(f"Uploaded {file_path} to s3://{BUCKET_NAME}/{s3_key}")

def save_data(data):
    # Save the weather data to a JSON file in the "data" directory and make sure the directory exists
    os.makedirs("data/raw", exist_ok = True)

    # Create a timestamp for the filename in the format "YYYYMMDD_HHMMSS"
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    # Save the weather data to a JSON file with the timestamp in the filename
    filename = f"data/raw/weather_{timestamp}.json"   
    
    with open(filename, "w") as f: # Open the file in write mode and save the data as JSON with indentation for readability
        json.dump(data, f,  separators = (',', ':'))

    upload_to_s3(filename, f"raw/{filename.split('/')[-1]}")  # Upload the file to S3 with a key that includes the "raw/" prefix
    print(f"Weather data saved to {filename}")