from sqlalchemy import create_engine
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require')

def load_weather_data(data_frame):
    
    data_frame.to_sql(name = 'weather_data', schema = 'etl_assignment', con=engine, if_exists = 'append', index = False)
    
    print(f"Loaded {len(data_frame)} records")
    
