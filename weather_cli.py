# weather_cli.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Fetches and displays weather for a given city.
    """
    if not API_KEY:
        return "Error: API key not found. Please set OPENWEATHER_API_KEY in .env file."

    # Parameters for the API request
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        data = response.json()

        # Extracting relevant information
        weather_description = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        city = data['name']
        country = data['sys']['country']

        # Formatting the output
        output = (
            f"\nWeather in {city}, {country}:\n"
            f"----------------------------------\n"
            f"Description: {weather_description}\n"
            f"Temperature: {temp}°C\n"
            f"Feels Like: {feels_like}°C\n"
        )
        return output

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return f"Error: City '{city_name}' not found."
        elif response.status_code == 401:
            return "Error: Invalid API key. Please check your .env file."
        else:
            return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An other error occurred: {err}"


if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_report = get_weather(city)
    print(weather_report)