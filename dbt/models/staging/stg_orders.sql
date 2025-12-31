WITH source AS (
    SELECT
        NULLIF(order_id, '') AS order_id,
        NULLIF(customer_id, '') AS customer_id,
        CAST(NULLIF(order_purchase_timestamp, '') AS TIMESTAMP) AS order_purchase_timestamp,
        CAST(NULLIF(order_delivered_carrier_date, '') AS TIMESTAMP) AS order_delivered_carrier_date,
        CAST(NULLIF(order_delivered_customer_date, '') AS TIMESTAMP) AS order_delivered_customer_date,
        CAST(NULLIF(order_estimated_delivery_date, '') AS TIMESTAMP) AS order_estimated_delivery_date
    FROM 
        {{ source('raw', 'orders') }}
)

SELECT * FROM source