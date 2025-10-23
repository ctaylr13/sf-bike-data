from diagrams import Diagram, Cluster
from diagrams.programming.language import Python
from diagrams.gcp.analytics import BigQuery
from diagrams.onprem.client import Client
from diagrams.onprem.database import PostgreSQL


with Diagram("local_workflow", show=False):
    with Cluster("Big Query Data"):
        initial_bike_data = [BigQuery("bikeshare_regions"),
        BigQuery("bikeshare_station_info"),
        BigQuery("bikeshare_station_status"),
        BigQuery("bikeshare_trips")]

    initial_bike_data >> \
    Python('download_bike_data.py') >> \
    Client('data/bike_data') >> \
    Python('ingest_raw_.py') >>  \
    PostgreSQL('local_db')
