from extract import extract_binance_data
from transform import transform_binance_data
from load import load_binance_data


def run_etl():
    
    raw_data = extract_binance_data()
    
    structured_data = transform_binance_data(raw_data)
    
    load_binance_data(structured_data)
    
if  __name__ == "__main__":
    run_etl()
    