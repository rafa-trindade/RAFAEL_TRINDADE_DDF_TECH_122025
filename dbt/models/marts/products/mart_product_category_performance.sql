WITH base AS (
    SELECT
        COALESCE(p.product_category_name, 'sem_categoria') AS product_category_name,
        d.ano,
        d.mes,
        f.order_item_id,
        f.total_item_value
    FROM 
        {{ ref('fact_order_items') }} AS f
    JOIN 
        {{ ref('dim_products') }} AS p ON f.product_id = p.product_id
    JOIN 
        {{ ref('dim_date') }} AS d ON f.chave_data = d.chave_data
)

SELECT
    product_category_name,
    ano,
    mes,
    SUM(total_item_value) AS receita_categoria,
    COUNT(order_item_id) AS itens_vendidos,
    ROUND(SUM(total_item_value) / NULLIF(COUNT(order_item_id), 0), 2) AS ticket_medio_categoria
FROM 
    base
GROUP BY product_category_name, ano, mes
ORDER BY ano, mes, receita_categoria DESC