import duckdb
import requests
from dotenv import load_dotenv
import os



# Connect to your DuckDB database
conn = duckdb.connect('raw_bike_data.db')

# Add the 'elevation' column if it doesn't exist
conn.execute("ALTER TABLE raw_bike_data.main.bikeshare_station_info ADD COLUMN IF NOT EXISTS elevation FLOAT;")

# Query to get station_id, lat, lon
query = "SELECT station_id, lat, lon FROM raw_bike_data.main.bikeshare_station_info;"
rows = conn.execute(query).fetchall()

load_dotenv() 
# Your API key
api_key = os.environ.get('GOOGLE_MAPS')

# Loop through each station and update elevation
for row in rows:
    station_id, lat, lon = row
    url = f"https://maps.googleapis.com/maps/api/elevation/json?locations={lat},{lon}&key={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK' and 'results' in data and len(data['results']) > 0:
        elevation = data['results'][0]['elevation']
        # Update the station with the elevation
        conn.execute(
            "UPDATE raw_bike_data.main.bikeshare_station_info SET elevation = ? WHERE station_id = ?",
            (elevation, station_id)
        )
        print(f"Updated station {station_id} with elevation {elevation} meters.")
    else:
        print(f"Error fetching elevation for station {station_id}: {data['status']}")

# Close connection
conn.close()
