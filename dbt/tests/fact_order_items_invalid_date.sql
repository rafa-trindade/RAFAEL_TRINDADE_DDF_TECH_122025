SELECT
    *
FROM 
    {{ ref('fact_order_items') }} AS f
LEFT JOIN 
    {{ ref('dim_date') }} AS d ON f.chave_data = d.chave_data
WHERE 
    d.chave_data IS NULL