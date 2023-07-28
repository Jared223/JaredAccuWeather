# CONNECTING TO API AND MAKING DATABASE WITH RESULTS

import requests
import sqlite3
import time


# Setting up and connecting to database

conn = sqlite3.connect('weather_data.db')

cur = conn.cursor()

timestamp = int(time.time()) # get timestamp

# Create table
cur.execute('''
    CREATE TABLE IF NOT EXISTS Weather (
        id INTEGER PRIMARY KEY,
        location TEXT,
        weather_main TEXT,
        weather_description TEXT,
        temperature_c REAL,
        timestamp INTEGER
    )
''')

# Setting latitude and longitude information, and API Key

lat = 51.51
lon = -0.12
apiKey = 'e1985d57baf12fc90046cb533d0e2a20'

# Set API url

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}'

# Request information to openweathermap

r = requests.get(url)

# Get response

response = r.json()

# Setting response variables

weather_main = response['weather'][0]['main']
weather_description = response['weather'][0]['description']

temperature = response['main']['temp']

temperature_celsius = temperature - 273.15
temperature_celsius = round(temperature_celsius, 1)

location = response['name']

# Insert weather data into table
cur.execute('''
    INSERT INTO Weather (location, weather_main, weather_description, temperature_c, timestamp) 
    VALUES (?, ?, ?, ?, ?)
''', (location, weather_main, weather_description, temperature_celsius, timestamp))

# Commit changes
conn.commit()

# Close connection
conn.close()

df = [weather_main]



