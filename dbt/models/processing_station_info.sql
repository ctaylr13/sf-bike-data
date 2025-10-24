SELECT
    station_id,
    name,
    short_name,
    lat,
    lon,
    region_id,
    capacity,
    has_kiosk,
    station_geom
from {{ source('raw_bike_data', 'bikeshare_station_info') }}
LIMIT 100