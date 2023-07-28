# DATA VISUALISATION

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('weather_data.db')

# Load data into a pandas DataFrame
df = pd.read_sql_query('SELECT * FROM Weather', conn)

# Close the connection
conn.close()

# Convert the 'timestamp' column (assuming it's a timestamp) to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

# Set the 'timestamp' column as the index
df.set_index('timestamp', inplace=True)

# Create the plot
fig, ax = plt.subplots()

df['temperature_c'].plot(ax=ax)

# Set the date format to show hours
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

# Set the x-axis limits to match the range of your data
ax.set_xlim(df.index.min(), df.index.max())

# Other plot settings
ax.set_title('Temperature Over Time')
ax.set_xlabel('Time')
ax.set_ylabel('Temperature (°C)')

# Show the plot
print(df)
plt.style.use('seaborn')  # use seaborn style
df['temperature_c'].plot(color='red', linewidth=2, linestyle='--', marker='o')
plt.title('Temperature Over Time', fontsize=16, color='blue')
plt.xlabel('Time', fontsize=14, color='blue')
plt.ylabel('Temperature (°C)', fontsize=14, color='blue')
plt.xticks(fontsize=12, color='green')
plt.yticks(fontsize=12, color='green')
plt.grid(color='gray', linestyle='-', linewidth=0.5)
plt.show()

