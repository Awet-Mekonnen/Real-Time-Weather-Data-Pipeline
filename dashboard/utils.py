from pyathena import connect # connect is used to help connect to the weather pipeline database
import pandas as pd
import streamlit as st

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
        region_name = REGION,
        s3_staging_dir = S3_STAGING_DIR,
        schema_name = DATABASE
    )

    df = pd.read_sql(query, conn)
    conn.close()

    return df