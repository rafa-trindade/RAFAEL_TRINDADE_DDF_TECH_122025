WITH base AS (
    SELECT
        COALESCE(p.product_category_name, 'sem_categoria') AS product_category_name,
        d.ano,
        d.mes,
        SUM(f.total_item_value) AS receita_mensal
    FROM 
        {{ ref('fact_order_items') }} AS f
    JOIN 
        {{ ref('dim_products') }} AS p ON f.product_id = p.product_id
    JOIN 
        {{ ref('dim_date') }} AS d ON f.chave_data = d.chave_data
    GROUP BY 
        1, 2, 3
)

SELECT
    product_category_name,
    ano,
    mes,
    receita_mensal,
    LAG(receita_mensal) OVER (PARTITION BY product_category_name ORDER BY ano, mes) AS receita_mes_anterior,
    CASE
        WHEN LAG(receita_mensal) OVER (PARTITION BY product_category_name ORDER BY ano, mes) IS NULL THEN NULL
        WHEN LAG(receita_mensal) OVER (PARTITION BY product_category_name ORDER BY ano, mes) = 0 THEN NULL
        ELSE ROUND((receita_mensal - LAG(receita_mensal) OVER (PARTITION BY product_category_name ORDER BY ano, mes)) / LAG(receita_mensal) OVER (PARTITION BY product_category_name ORDER BY ano, mes), 4)
    END AS crescimento_percentual
FROM 
    base
ORDER BY 
    product_category_name, ano, mes