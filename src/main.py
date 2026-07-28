from run_pipeline import run_pipeline

def lambda_handler(event, context):
    run_pipeline()
    return {
        'statusCode': 200,
        'body': 'Weather data pipeline executed successfully.'
    }

if __name__ == "__main__":
    run_pipeline()

