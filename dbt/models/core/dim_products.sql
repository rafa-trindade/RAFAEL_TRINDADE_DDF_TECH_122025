WITH products AS (
    SELECT DISTINCT
        product_id,
        product_category_name,
        product_name_length,
        product_description_length
    FROM 
        {{ ref('stg_products') }}
)

SELECT * FROM products