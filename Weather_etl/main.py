from extract import extract_weather_data
from transform import transform_weather_data
from load import load_weather_data

#single function to run the full pipeline
def run_etl():
    #calls the extract function
    raw_data = extract_weather_data()
    
    #calls the transform function and parses raw_data as input
    transformed_data = transform_weather_data(raw_data)
    
    #loads the transformed clean data and loads it into python
    load_weather_data(transformed_data)
    
if __name__ == "__main__":
    run_etl()
