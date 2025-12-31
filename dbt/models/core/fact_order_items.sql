WITH order_items AS (
    SELECT
        order_id,
        order_item_id,
        product_id,
        price,
        freight_value
    FROM 
        {{ ref('stg_order_items') }}
), 

orders AS (
    SELECT
        order_id,
        customer_id,
        order_purchase_timestamp
    FROM 
        {{ ref('stg_orders') }}
), 

final AS (
    SELECT
        oi.order_id,
        oi.order_item_id,
        o.customer_id,
        oi.product_id,
        CAST(TO_CHAR(o.order_purchase_timestamp, 'YYYYMMDD') AS INT) AS chave_data,
        (EXTRACT(HOUR FROM o.order_purchase_timestamp) * 60 + EXTRACT(MINUTE FROM o.order_purchase_timestamp))::INT AS chave_hora,
        CAST(oi.price AS NUMERIC(12, 2)) AS price,
        CAST(oi.freight_value AS NUMERIC(12, 2)) AS freight_value,
        CAST(oi.price + oi.freight_value AS NUMERIC(12, 2)) AS total_item_value
    FROM 
        order_items AS oi
    INNER JOIN 
        orders AS o ON oi.order_id = o.order_id
    WHERE 
        o.order_purchase_timestamp IS NOT NULL
)

SELECT * FROM final