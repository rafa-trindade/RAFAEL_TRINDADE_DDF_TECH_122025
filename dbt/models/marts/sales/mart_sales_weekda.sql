SELECT
    d.nome_dia_semana,
    COUNT(DISTINCT f.order_id) AS total_pedidos,
    SUM(f.total_item_value) AS receita_total,
    AVG(f.total_item_value) AS ticket_medio
FROM 
    {{ ref('fact_order_items') }} AS f
JOIN 
    {{ ref('dim_date') }} AS d ON f.chave_data = d.chave_data
GROUP BY 1
ORDER BY receita_total DESC