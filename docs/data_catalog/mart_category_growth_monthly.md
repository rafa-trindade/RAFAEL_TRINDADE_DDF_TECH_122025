# Catálogo de Dados - `mart_category_growth_monthly`


## Descrição
Tabela analítica que apresenta a **receita mensal por categoria de produto**, permitindo a análise do **crescimento percentual em relação ao mês anterior**.

Cada linha representa o desempenho de uma **categoria de produto em um determinado mês e ano**.


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
- **Observação:** Quando o produto não possui categoria, o valor exibido é `sem_categoria` (resultado da função `COALESCE`).

### `ano`
- **Descrição:** Ano de referência da receita.

### `mes`
- **Descrição:** Mês de referência da receita.
- **Domínio:** 1 a 12

### `receita_mensal`
- **Descrição:** Valor total da receita da categoria no mês de referência.
- **Cálculo:** `SUM(f.total_item_value)`

### `receita_mes_anterior`
- **Descrição:** Receita da mesma categoria no mês imediatamente anterior.
- **Cálculo:** Utiliza a função de janela `LAG(receita_mensal) OVER (PARTITION BY product_category_name ORDER BY ano, mes)`.

### `crescimento_percentual`
- **Descrição:** Percentual de crescimento da receita em relação ao mês anterior (MoM).
- **Cálculo:** `(receita_mensal - receita_mes_anterior) / receita_mes_anterior`.
- **Observações:**
  - Será **nulo** quando for o primeiro mês de registro para aquela categoria.
  - Será **nulo** quando a receita do mês anterior for zero, prevenindo erros de divisão por zero.
  - Valores negativos indicam queda de receita.


## Regras de Negócio
- A receita é calculada com base na soma dos valores totais dos itens vendidos (`total_item_value`).
- O cálculo do crescimento Mês-sobre-Mês (MoM) é realizado de forma particionada, garantindo que a comparação (`LAG`) ocorra apenas dentro da mesma categoria de produto.
- Categorias nulas são mapeadas para `sem_categoria`.


## Uso Recomendado
- Análise de crescimento mês a mês (MoM) por segmento.
- Acompanhamento de performance e identificação de categorias de alto crescimento ou em declínio.
- Dashboards financeiros e de performance de produto.


## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise de tendência e visualização gerencial.