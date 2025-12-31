WITH base AS (
    SELECT
        d.ano,
        d.mes,
        f.total_item_value
    FROM 
        {{ ref('fact_order_items') }} AS f
    JOIN 
        {{ ref('dim_date') }} AS d ON f.chave_data = d.chave_data
), 

agg AS (
    SELECT
        ano,
        mes,
        SUM(total_item_value) AS receita_mensal
    FROM 
        base
    GROUP BY 
        ano,
        mes
)

SELECT
    ano,
    mes,
    receita_mensal,
    ROUND(
        (receita_mensal - LAG(receita_mensal) OVER (ORDER BY ano, mes)) / 
        NULLIF(LAG(receita_mensal) OVER (ORDER BY ano, mes), 0), 
        4
    ) AS crescimento_mom
FROM 
    agg
ORDER BY ano, mes