WITH source AS (
    SELECT
        NULLIF(product_id, '') AS product_id,
        UPPER(TRIM(NULLIF(product_category_name, ''))) AS product_category_name,
        CAST(product_name_lenght AS INTEGER) AS product_name_length,
        CAST(product_description_lenght AS INTEGER) AS product_description_length
    FROM 
        {{ source('raw', 'products') }}
)

SELECT * FROM source