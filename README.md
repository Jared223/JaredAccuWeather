# Jared Accu Weather!

This project is a simple script that fetches weather data from the [OpenWeatherMap API](https://openweathermap.org/api) stores it in a SQLite database, and allows for data visualisation using pandas and matplotlib. The data includes the current weather conditions and temperature for a specified location.

## Features

- Fetches real-time weather data from OpenWeatherMap API.
- Stores data in a SQLite database, which can be easily queried for analysis and visualisation.
- Visualises weather data over time with a separate Python script.

## Setup

1. Clone the repository.
```bash
git clone https://github.com/Jared223/JaredAccuWeather.git
```
2. Navigate to the code directory, open the app.py file
3. Change the latitude and longitude for your desired location
4. Run the code
5. The database will be populated with the weather information, ready for analysis!
6. Run graphs.py to generate a graph showing the temperature by time. 

## Requirements

This project uses the following external Python libraries:

- [requests](https://docs.python-requests.org/en/latest/): For making HTTP requests to the OpenWeatherMap API.
- [sqlite3](https://docs.python.org/3/library/sqlite3.html): For creating and interacting with the SQLite database.
- [time](https://docs.python.org/3/library/time.html): For keeping track of time
- [pandas](https://pandas.pydata.org/): For creating data frame
- [Matplotlib](https://matplotlib.org): For plotting the data

The app.py script fetches the current weather data from the OpenWeatherMap API and stores it in a SQLite database. The data includes the location name, current weather condition, weather description, and temperature.

The graphs.py script fetches the stored data from the SQLite database, and plots the temperature over time. It provides a clear visualisation of how the temperature changes over time.

The application is designed to be run regularly at regular intervals. This ensures that the database is populated with a significant amount of data points, thereby providing a more comprehensive and detailed visualisation of temperature changes over time.

This project serves as a practical example of how to work with APIs, databases, and data visualisation in Python, and could serve as a starting point for more complex weather data analysis and visualisation projects.
