import pandas as pd

def transform_weather_data(data):
    if not data:
        print("No data to trandsform!")
        return None
    
    #picking the relevant fields from the response and converting it into a dictionary
    data_dict = {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "local_time": data["location"]["localtime"],
            "temperature_c": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "wind_kph": data["current"]["wind_kph"],
            "humidity": data["current"]["humidity"],
    }
    
    #functions converts the data_dict to a data frame and returns it as result
    return pd.DataFrame([data_dict])
    