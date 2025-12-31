WITH source AS (
    SELECT
        NULLIF(customer_id, '') AS customer_id,
        NULLIF(customer_unique_id, '') AS customer_unique_id,
        CAST(customer_zip_code_prefix AS INTEGER) AS customer_zip_code_prefix,
        UPPER(TRIM(NULLIF(customer_city, ''))) AS customer_city,
        UPPER(TRIM(NULLIF(customer_state, ''))) AS customer_state
    FROM 
        {{ source('raw', 'customers') }}
)

SELECT * FROM source