SELECT
    c.customer_id,
    c.customer_state,
    COUNT(DISTINCT f.order_id) AS total_pedidos,
    SUM(f.total_item_value) AS ltv,
    ROUND(SUM(f.total_item_value) / NULLIF(COUNT(DISTINCT f.order_id), 0), 2) AS ticket_medio_cliente
FROM 
    {{ ref('fact_order_items') }} AS f
JOIN 
    {{ ref('dim_customers') }} AS c ON f.customer_id = c.customer_id
GROUP BY 
    c.customer_id,
    c.customer_state