from sqlalchemy import create_engine
from config import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}")

def load_binance_data(data_frame):
    
    data_frame.to_sql(name = 'binance_data', schema = 'etl_assignment', con = engine, if_exists = 'replace', index = False)
    
    print(f"Loaded {len(data_frame)} records")
    