WITH source AS (
    SELECT
        NULLIF(order_id, '') AS order_id,
        CAST(order_item_id AS INTEGER) AS order_item_id,
        NULLIF(product_id, '') AS product_id,
        CAST(price AS NUMERIC(10, 2)) AS price,
        CAST(freight_value AS NUMERIC(10, 2)) AS freight_value
    FROM 
        {{ source('raw', 'order_items') }}
)

SELECT * FROM source