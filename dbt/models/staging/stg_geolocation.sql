WITH source AS (
    SELECT
        CAST(geolocation_zip_code_prefix AS INTEGER) AS geolocation_zip_code_prefix,
        CAST(geolocation_lat AS DOUBLE PRECISION) AS geolocation_lat,
        CAST(geolocation_lng AS DOUBLE PRECISION) AS geolocation_lng,
        UPPER(TRIM(NULLIF(geolocation_city, ''))) AS geolocation_city,
        UPPER(TRIM(NULLIF(geolocation_state, ''))) AS geolocation_state
    FROM 
        {{ source('raw', 'geolocation') }}
)

SELECT * FROM source