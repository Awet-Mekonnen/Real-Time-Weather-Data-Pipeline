from pyathena import connect 
# connect is used to help connect to the weather pipeline database
import pandas as pd
import streamlit as st
import os

# Fetch credentials from Streamlit Secrets (or fallback to environment variables)
aws_access_key = st.secrets.get("AWS_ACCESS_KEY_ID", os.getenv("AWS_ACCESS_KEY_ID"))
aws_secret_key = st.secrets.get("AWS_SECRET_ACCESS_KEY", os.getenv("AWS_SECRET_ACCESS_KEY"))
aws_region = st.secrets.get("AWS_DEFAULT_REGION", os.getenv("AWS_DEFAULT_REGION", "us-east-1"))

# Declare Variables for the AWS Region, Database name, and S3 bucket file path
REGION = "us-east-1"
DATABASE = "weather-pipeline-2026-db"
S3_STAGING_DIR = "s3://weather-pipeline-2026/weather-pipeline-2026-athena-results"

@st.cache_data(ttl=300) #This function call helps store the the caches of the data

# This function is used to run the query fetched 
# from the app file to stream on the dashboard
def run_query(query):
    # Connect is used to connect to the AWS server 
    # and fetch the table from the database
    conn = connect(
        aws_access_key_id = aws_access_key,
        aws_secret_access_key = aws_secret_key,
        region_name = REGION,
        s3_staging_dir = S3_STAGING_DIR,
        schema_name = DATABASE
    )

    df = pd.read_sql(query, conn)
    conn.close()

    try:
        return df
    except DatabaseError as e:
        # Print the underlying AWS Athena error message
        print("Root Athena Error:", e)
        if e.__cause__:
            print("Cause:", e.__cause__)
        raise e
