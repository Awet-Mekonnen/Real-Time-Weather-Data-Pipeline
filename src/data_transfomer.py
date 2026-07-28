# This function is used to transform the data collected from the API
def transform_data(data):
    return {
        "timestamp": data["timestamp"],
        "temperature": data["current"]["temperature_2m"],
        "humidity": data["current"]["relative_humidity_2m"],
        "wind_speed": data["current"]["wind_speed_10m"],
        "timezone": data["timezone"],
        "latitude": data["latitude"],
        "longitude": data["longitude"]
    }