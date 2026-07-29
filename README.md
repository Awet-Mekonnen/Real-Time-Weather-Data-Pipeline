# Real-Time Weather Data Pipeline

An end-to-end serverless AWS project that automatically collects real-time weather data from the Open-Meteo APT every hour, stores it in Amazon S3, catalogs it using AWS Glue, queries it with Amazon Athena, and visualizes insights through an interactive Streamlit dashboard.

---

## Dashboard Preview

![alt text](<Dashboard 1-1.png>) 
![alt text](<Current Weather-1.png>) 
![alt text](<Temp Stats-1.png>) 
![alt text](<Humidity Stat-1.png>) 
![alt text](<Wind Speed Stats-1.png>)
![alt text](<Latest Records Stats-1.png>) 

---

## Data Flow

Open-Meteo API -> Amazon EventBridge -> AWS Lambda (Python) -> Amazon S3 -> AWS Glue Crawler -> Amazon Athena -> Streamlit Dashboard

---

## Features

- Authomated hourly weather data collection
- Fully serverless AWS architecture
- Cloud-based data lake using Amazon S3
- Metadata cataloging with AWS Glue
- SQL analytics using Amazon Athena
- Interactive Streamlit dashboard
- Weather trends and statistics
- Time range filtering
- Downloadable CSV reports
- Responsive Plotly visualizations

---

## Technologies Used

### Programming

- Python
- SQL

### AWS

- AWS Lambda
- Amazon EventBridge
- Amazon S3
- AWS Glue
- Amazon Athena
- AWS SAM

### Python Libraries

- Streamlit
- Plotly
- Pandas
- Requests
- PyAthena
- Boto3

---

# Project Structure

```text
Cloud-Data-Pipeline/

├── dashboard/
│   ├── app.py
│   ├── about.py
│   ├── charts.py
│   ├── metrics.py
│   ├── overview.py
│   ├── queries.py
│   ├── table.py
│   ├── utils.py
│   └── requirements.txt
│
├── src/
│   ├── main.py
│   ├── run_pipeline.py
│   ├── weather_api.py
│   ├── storage.py
│   ├── data_transformer.py
│   └── config.py
│
├── docs/
│
├── template.yaml
├── README.md
└── requirements.txt
```

---

## How It Works

### 1. Data Collection

Amazon EventBridge triggers an AWS Lambda function every hour.

The Lambda function retrieves real-time weather data from the Open-Meteo API.

---

### 2. Data Storage

The weather data is stored as JSON files inside an Amazon S3 bucket.

Example:

```
raw/
    year = 2026/
        month = 07/
            day = 27/
                weather_20260727_HHMMSS.json
```

---

### 3. Data Catalog

AWS Glue automatically crawls the S3 bucket and updates the metadata catalog.

---

### 4. Data Analysis

Amazon Athena performs SQL queries directly on the data stored in Amazon S3.

---

### 5. Dashboard

A Streamlit dashboard connects to Athena to provide:

- Current Weather
- Past Trends
- Summary Statistics
- Interactive charts
- CSV Downloads

---

## Dashboard Features

### Current Weather

Displays the latest:

- Temperature
- Humidity
- Wind Speed

---

### Statistics

For each metric:

- Average
- Maximum
- Minimum

---

### Charts

Interactive Plotly Visualizations for:

- Temperature
- Humidity
- Wind Speed

---

### Time Filters

Users can view:

- Last 24 Hours
- Last 7 Days
- Last 30 Days
- All Data

---

## Development Journey

This project was developed incrementally, with each AWS service tested independently before integrating the complete pipeline.

### Step 1: Weather API

- Build a Python client using the `requests` library.
- Retrieved real-time weather data from the Open-Meteo API.
- Validated the JSON response locally.

### Step 2: Amazon S3

- Used the AWS SDK for Python (`boto3`) to upload JSON files.
- Organized files into a date-based folder structure.
- Verified uploads through the AWS Console.

### Step 3: AWS Lambda

- Refactored the application into reusable modules.
- Added a `lambda_handler()` entry point.
- Packaged and deployed the code using AWS SAM.
     After making changes to the Lambda source code:
        1. Updated the files in the `src/` directory.
        2. Built the application:
            ```bash
            sam build
            ```
        3. Deployed the Updated Lambda function:
            ```bash
            sam deploy
            ```
        4. Verify the deploymend by running a Lambda test event.
        5. Confirmed that:
            - EventBridge triggers the function.
            - New files are uploaded to Amazon S3
            - AWS Glue catalogs the new data.
            - Amazon Athena returns the updated records.
            - The Streamlit dashboard displays the latest weather data.

### Step 4: EventBridge

- Created an hourly EventBridge rule.
- Verified automatic Lambda execution.
- Confirmed that new weather files appeared in S3 every hour.

### Step 5: AWS Glue

- Configured a crawler to catalog the weather data.
- Integrated Athena with the Streamlit Dashboard.

### Step 6: Amazon Athena

- Queried the S3 data using SQL.
- Integrated Athena with the Streamlit Dashboard.

## Step 7: Streamlit Dashboard

- Build an interactive dashboard with:
    - Current weather metrics
    - Summary statistics
    - Interactive Plotly charts
    - Time filters
    - CSV exports

---

## Challenges and Solutions

### Lambda couldn't import `requests`

Packaged dependencies with AWS SAM before deployment.

### Lambda couldn't write to data/raw

Deteced the Lambda environment and uploaded directly to S3 instead of writing to the deployment package.

### CloudFormation stack entered "ROLLBACK_COMPLETE"

Deleted the failed stack and redeploed after fixing the template.

### Reserved environment variables (AWS_REGION)

Removed the reserved key from the Lambda configuration.

### Athena timestamp type mismatch

Used from_iso8601_timestamp() to convert ISO 8601 strings for filtering.

### Lambda package exceeded the deployment size limit

Exculded unnecessary files (such as the virtual environment) from the deployment package

---

## Lessons Learned

During this project I learned how to:

- Build an end-to-end pipeline
- Delpoy AWS Lambda using AWS SAM
- Debug Lambda Deployment issues
- Work with IAM permissions
- Query cloud data using Athena
- Build interactive Streamlit Dashboards
- Organize cloud storage using S3
- Integrate multiple AWS services into a complete workflow

---

## Future Improvemnts

- Deploy Streamlit to AWS App Runner
- Dockerize the Dashboard
- Store data as Parquet
- Partition Athena Tables
- Add CloudWatch monitoring
- CI/CD with Github Actions
- Add weather alerts
- Multi-city support

---

## Developer

** Awet Tesfai **

Bachelors in Computer Science

Aspiring Data Engineer

