SELECT
    station_id,
    name,
    short_name,
    lat,
    lon,
    region_id,
    capacity,
    has_kiosk,
    station_geom AS station_coords
from {{ source('raw_bike_data', 'bikeshare_station_info') }}