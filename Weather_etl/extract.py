import requests
from config import WEATHER_API_KEY

def extract_weather_data():
    url = f"https://api.weatherapi.com/v1/forecast.json?q=Nairobi&key={WEATHER_API_KEY}"
    
    #to catch and handle errors preventing the program from crashing
    try:
        response = requests.get(url)
        response.raise_for_status() #automatically raises an error 
        return response.json() #returns the response data in json format
    
    #to catch all request related errors
    except requests.exceptions.RequestException as e: 
        #print the error if any
        print(f"Error fetching weather data: {e}")
        return None
    
