import requests
import json
import os
from datetime import datetime, timezone
import data_transfomer

def fetch_weather():
    # Create a URL for the Open-Meteo API with the desired parameters
    url = os.getenv("URL")

    # Grab the weather data from the API and raise an error if the request fails
    response = requests.get(url)
    response.raise_for_status()

    # Parse the JSON response into a Python dictionary and add a timestamp for when the data was fetched
    data = response.json()
    data["timestamp"] = datetime.now(timezone.utc).isoformat()
    
    processed_data = data_transfomer.transform_data(data)
    return processed_data