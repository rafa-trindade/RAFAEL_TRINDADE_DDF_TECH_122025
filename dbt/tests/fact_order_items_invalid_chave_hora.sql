SELECT
    *
FROM 
    {{ ref('fact_order_items') }}
WHERE 
    chave_hora < 0
    OR chave_hora > 1439