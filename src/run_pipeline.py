import weather_api
import storage
import json

def run_pipeline():
    weather_data = weather_api.fetch_weather()

    # Save the fetched weather data to a JSON file and upload it to S3
    storage.save_data(weather_data)

    # Print the fetched weather data to the console for verification
    print(json.dumps(weather_data, indent=4))