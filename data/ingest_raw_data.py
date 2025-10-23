
import duckdb

# Connect to DuckDB
conn = duckdb.connect('raw_bike_data.db')

csv_file = 'bikeshare_station_trips.csv'
table_name = 'bikeshare_station_trips'

# Read CSV into a new table
conn.execute(f"""
CREATE TABLE {table_name} AS
SELECT * FROM read_csv_auto('{csv_file}')
""")