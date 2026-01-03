# Catálogo de Dados  - `mart_product_category_performance`


## Descrição
Tabela analítica que apresenta as principais métricas de desempenho (receita, volume e ticket médio) **mensalmente por categoria de produto**.

Este modelo é fundamental para avaliar o tamanho e a saúde financeira de cada grupo de produtos no negócio.


## Granularidade
- Mensal
- Por Categoria de Produto


## Chave lógica
- `product_category_name` 
- `ano`  
- `mes`  


## Dicionário de Campos

### `product_category_name`
- **Descrição:** Nome da categoria do produto.
- **Observação:** Produtos sem categoria definida são rotulados como `sem_categoria`.

### `ano`
- **Descrição:** Ano de referência da performance da categoria.

### `mes`
- **Descrição:** Mês de referência da performance da categoria.
- **Domínio:** 1 a 12

### `receita_categoria`
- **Descrição:** Valor total da receita bruta gerada pela categoria no mês.
- **Cálculo:** `SUM(total_item_value)`

### `itens_vendidos`
- **Descrição:** Quantidade total de itens (linhas de pedido) vendidos na categoria durante o mês.
- **Cálculo:** `COUNT(order_item_id)`

### `ticket_medio_categoria`
- **Descrição:** Valor médio de cada item vendido na categoria.
- **Cálculo:** `receita_categoria / itens_vendidos`. Arredondado para duas casas decimais.
- **Observações:** O valor é `NULL` se não houver itens vendidos, prevenindo divisão por zero.


## Regras de Negócio
- A performance é agregada no nível Categoria x Ano x Mês.
- Valores de categoria nulos na origem são consolidados como `sem_categoria`.
- A receita é obtida diretamente do valor total do item de pedido.
- O Ticket Médio é calculado como uma média simples por item.


## Uso Recomendado
- Análise de volume de vendas por categoria.
- Monitoramento do ticket médio.
- Identificação de categorias de alto volume ou alto valor.
- Dashboards de performance comercial mensal.


## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise, BI e Visualização de Performance.
- **Fontes:** `fact_order_items`, `dim_products`, `dim_date`