# Jared Accu Weather!

This project is a simple script that fetches weather data from the [OpenWeatherMap API](https://openweathermap.org/api) and stores it in a SQLite database. The data includes the current weather conditions and temperature for a specified location.

## Features

- Fetches real-time weather data from OpenWeatherMap API.
- Stores data in a SQLite database, which can be easily queried for analysis and visualization.

## Setup

1. Clone the repository.
```bash
git clone https://github.com/Jared223/JaredAccuWeather.git
```
2. Navigate to the code directory, open the app.py file
3. Change the latitude and longitude for your desired location
4. Run the code
5. The database will be populated with the weather information, ready for analysis!

## Requirements

This project uses the following external Python libraries:

- [requests](https://docs.python-requests.org/en/latest/): For making HTTP requests to the OpenWeatherMap API.
- [sqlite3](https://docs.python.org/3/library/sqlite3.html): For creating and interacting with the SQLite database.
