from google.cloud import bigquery
import pandas as pd

# Initialize BigQuery client
client = bigquery.Client()

# Specify the table
table_id = 'bigquery-public-data.san_francisco_bikeshare.bikeshare_trips'

# Load table data into a pandas DataFrame
table_data = client.query(f'SELECT * FROM `{table_id}`').result().to_dataframe()

# Save to CSV
table_data.to_csv('bikeshare_station_trips.csv', index=False)

print("Table downloaded and saved as 'bikeshare_station_trips.csv'")