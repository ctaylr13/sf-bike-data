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
    start_station_latitude,
    start_station_longitude,
    end_station_latitude,
    end_station_longitude,
    member_birth_year,
    member_gender,
    bike_share_for_all_trip,
    start_station_geom,
    end_station_geom
from {{ source('raw_bike_data', 'bikeshare_station_trips') }}
LIMIT 100
