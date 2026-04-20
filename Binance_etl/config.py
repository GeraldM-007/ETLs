import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

DB_USER = os.getenv('USER')
DB_PASSWORD = os.getenv('PASSWORD')
DB_HOST = os.getenv('HOST')
DB_DATABASE = os.getenv('DATABASE')
DB_PORT = os.getenv('PORT')

