# Catálogo de Dados  - `mart_customer_behavior`


## Descrição
Tabela analítica que consolida métricas essenciais de **comportamento de compra e valor** dos clientes (Lifetime Value - LTV).

Esta tabela é utilizada para **segmentação**, análise de valor e identificação dos clientes mais engajados. Cada linha representa um cliente único.


## Granularidade
- Por Cliente (Unidade: `customer_id`)


## Chave lógica
- `customer_id`


## Dicionário de Campos

### `customer_id`
- **Descrição:** Identificador único do cliente.

### `customer_state`
- **Descrição:** Sigla do estado (UF) de residência do cliente.
- **Domínio:** Estados brasileiros (e.g., SP, RJ, MG).

### `total_pedidos`
- **Descrição:** Número total de pedidos únicos realizados pelo cliente.

### `ltv`
- **Descrição:** Lifetime Value do cliente, calculado como o valor total dos itens comprados por este cliente ao longo do tempo.
- **Observação:** É a soma dos campos `total_item_value`.

### `ticket_medio_cliente`
- **Descrição:** Valor médio gasto pelo cliente por pedido.
- **Cálculo:** `ltv` / `total_pedidos`.
- **Observação:** Arredondado para duas casas decimais.


## Regras de Negócio
- O cálculo do LTV considera apenas o valor dos itens, excluindo frete e taxas externas não presentes em `fact_order_items`.
- O ticket médio é protegido contra divisão por zero (`NULLIF`).
- A agregação é estritamente no nível do cliente.


## Uso Recomendado
- Segmentação de clientes (Análise de valor, RFM)
- Estratégias de retenção e marketing
- Análise de dispersão de LTV por estado
- Visualizações de performance de clientes de alto valor


## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise Comportamental e LTV (Lifetime Value)