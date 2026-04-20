This file outlines the approach used to implement a simple Binance data ETL pipeline

## File structure
Binance_api_etl/

├── .env

├── config.py

├── extract.py

├── transform.py

├── load.py

└── main.py

## Methodology

The .env file stores all the credentials including the API KEYs and Server credentials

Used a config.py file to fetch credentials from the .env file

**extract.py**

Uses get() request from requests module to get data from a public binance repository
A function extract_binance_data() to run the process
Uses a try and except block to implement the logic so that errors can be handled without crushing 
Initialy it was to be used with an API KEY but later realized that binance data can be obtained without having to use/expose an API KEY

**transform.py**

Uses a function transform_binance_data(data) 
The function uses the parameter "data" which is the output of extract.py
It then uses pandas to create a data frame from the data

**load.py**

This files loads the created data frame (structure data) from the output of transform.py 
Using sqlalchemy module and the database credentials stored in config.py
We create and use a function load_binance_data(data_frame) that takes an argument "data_frame" which is the output of the transform.py 
Use the .to_sql() function to load the data into an existing postgresql database 
Inside the the .to_sql() function, we define what the name of table, schema and using 'if_exits' we define what action to perform while writing into the database.

**main.py**

This file executes the whole ETL. 
Importing all the other functions extract_binance_data(),  transform_binance_data(data) and load_binance_data(data_frame), 
Then creating and using a function run_etl() we run the functions

## OUTPUT

Data uploaded on the database as viewed on DBeaver

<img width="2124" height="747" alt="image" src="https://github.com/user-attachments/assets/c9fc54a3-9786-4c5b-9440-9750561129c7" />



