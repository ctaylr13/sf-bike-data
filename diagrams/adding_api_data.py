from diagrams import Diagram, Cluster 
from diagrams.programming.language import Python
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.api import Endpoints
from diagrams.onprem.client import Client
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.analytics import Dbt


with Diagram("local_3", show=False):
    maps_elevation = Endpoints('elevation api')
    api_data = Python('station_elevation.py')
        # elevation_data =[Endpoints('/elevation'), Python('station_elevation.py')]
    with Cluster("Big Query Data"):
        initial_bike_data = [BigQuery("bikeshare_regions"),
        BigQuery("bikeshare_station_info"),
        BigQuery("bikeshare_station_status"),
        BigQuery("bikeshare_trips")]
    ingest_data = initial_bike_data >> \
        Python('download_bike_data.py') >> \
        Client('data/bike_data') >> \
        Python('ingest_raw_.py') >>  \
        PostgreSQL('local_db') 

    ingest_data >> Dbt('dbt things') 
    ingest_data >> api_data << maps_elevation
   