This file outlines the approach used to implement a simple ETL pipeline to gather realtime weather data using weather API

## File structure
Weather_api_etl/

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

Uses get() request from requests module to get data from weather API 
A function extract_weather_data() to run the process
Uses a try and except block to implement the logic so that errors can be handled without crushing 

**transform.py**

Uses a function transform_weather_data(data) 
An if statement to check if the parsed parameter contains any data 
The function uses the parameter "data" which is the output of extract.py
Then creates a dictionary of the relevant field we want to pick from the data
It then uses pandas to create a data frame from the data

**load.py**

This files loads the created data frame (structure data) from the output of transform.py 
Using sqlalchemy module and the database credentials stored in config.py
We create and use a function load_weather_data(data_frame) that takes an argument "data_frame" which is the output of the transform.py 
Use the .to_sql() function to load the data into an existing postgresql database 
Inside the the .to_sql() function, we define what the name of table, schema and using 'if_exists' we define what action to perform while writing into the database(eg. append/replace).

**main.py**

This file executes the whole ETL. 
Importing all the other functions extract_weather_data(),  transform_weather_data(data) and load_weather_data(data_frame), 
Then creating and using a function run_etl() we run the functions

## OUTPUT

I created the table before running the pipeline as I have defined it to append data into the table if it exists
<img width="735" height="481" alt="image" src="https://github.com/user-attachments/assets/3fe13f38-d9aa-486e-90a5-4ad751bd988b" />

N/B: sqlalchemy creates the table automatically if the table does not exist

Data uploaded on the database as viewed on DBeaver
<img width="1095" height="314" alt="image" src="https://github.com/user-attachments/assets/fbd4ab89-46a3-49fc-a1f8-c24e9689d335" />




