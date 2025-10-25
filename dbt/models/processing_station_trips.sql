{{ config(materialized='view') }}

select
    trip_id,
    duration_sec,
    start_date,
    start_station_name,
    start_station_id,
    end_date,
    end_station_name,
    end_station_id,
    bike_number,
    subscriber_type,
    start_station_latitude AS start_station_lat,
    start_station_longitude AS start_station_long,
    end_station_latitude AS end_station_lat,
    end_station_longitude AS end_station_long,
    member_birth_year,
    member_gender,
    bike_share_for_all_trip,
    start_station_geom AS start_station_coords,
    end_station_geom AS end_station_coords
from {{ source('raw_bike_data', 'bikeshare_station_trips') }}
