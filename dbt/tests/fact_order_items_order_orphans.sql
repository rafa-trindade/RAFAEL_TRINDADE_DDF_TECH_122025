SELECT
    *
FROM 
    {{ ref('fact_order_items') }}
WHERE 
    order_id IS NULL