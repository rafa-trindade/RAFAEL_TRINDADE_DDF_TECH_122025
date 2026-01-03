# Catálogo de Dados  - `mart_sales_weekda`


## Descrição
Tabela analítica que consolida as **métricas chave de vendas** (receita, pedidos e ticket médio) agregadas por **Dia da Semana**.

Esta tabela é ideal para identificar padrões de sazonalidade semanal e o desempenho comercial em cada dia.


## Granularidade
- Por Dia da Semana


## Chave lógica
- `nome_dia_semana`


## Dicionário de Campos

### `nome_dia_semana`
- **Descrição:** Nome completo do dia da semana (e.g., 'Segunda-feira', 'Sábado').
- **Fonte:** Derivado da dimensão de data (`dim_date`).

### `total_pedidos`
- **Descrição:** Contagem distinta do número total de pedidos realizados no dia da semana correspondente.

### `receita_total`
- **Descrição:** Valor total da receita bruta gerada por todos os itens vendidos no dia da semana.

### `ticket_medio`
- **Descrição:** Valor médio das transações (baseado no valor unitário do item de pedido).
- **Cálculo:** `AVG(total_item_value)`


## Regras de Negócio
- A agregação é feita utilizando o nome do dia da semana, consolidando dados de todos os anos e meses presentes na base.
- A receita total considera a soma do valor final dos itens de pedido.
- O cálculo de `total_pedidos` utiliza uma contagem distinta (`DISTINCT`) de `order_id`.


## Uso Recomendado
- Análise de sazonalidade semanal de vendas.
- Otimização de logística e pessoal com base nos dias de maior movimento.
- Dashboards de desempenho comercial por dia de operação.


## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise e visualização (Reporting)