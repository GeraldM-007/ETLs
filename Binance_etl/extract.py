import requests 
from config import API_KEY

def extract_binance_data():
    url = f"https://api.binance.com/api/v3/ticker/24hr"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    except response.excemptions.RequestException as e:
        #print the error if any
        print(f"Error fetching weather data: {e}")
        return None
    
