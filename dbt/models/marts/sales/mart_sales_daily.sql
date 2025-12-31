WITH base AS (
    SELECT
        f.order_id,
        f.order_item_id,
        f.total_item_value,
        d.data
    FROM 
        {{ ref('fact_order_items') }} AS f
    JOIN 
        {{ ref('dim_date') }} AS d ON f.chave_data = d.chave_data
)

SELECT
    data,
    SUM(total_item_value) AS receita_diaria,
    COUNT(order_item_id) AS itens_vendidos,
    COUNT(DISTINCT order_id) AS pedidos,
    ROUND(SUM(total_item_value) / NULLIF(COUNT(order_item_id), 0), 2) AS ticket_medio
FROM 
    base
GROUP BY data
ORDER BY data