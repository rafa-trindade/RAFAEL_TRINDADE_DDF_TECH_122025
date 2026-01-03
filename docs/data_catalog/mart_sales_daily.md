# Catálogo de Dados  - `mart_sales_daily`


## Descrição
Tabela analítica que consolida as principais métricas de vendas, incluindo receita, volume de itens e número de pedidos, no **nível diário**. É a base fundamental para o acompanhamento da performance de vendas.

Cada linha representa o desempenho comercial em um **determinado dia**.


## Granularidade
- Diária (Agregado por data)


## Chave lógica
- `data`


## Dicionário de Campos

### `data`
- **Descrição:** Data da referência da venda.

### `receita_diaria`
- **Descrição:** Valor total da receita bruta gerada no dia.

### `itens_vendidos`
- **Descrição:** Número total de itens de pedido vendidos e processados na data.

### `pedidos`
- **Descrição:** Contagem de pedidos distintos realizados no dia.
- **Observação:** Um único pedido pode conter múltiplos itens.

### `ticket_medio`
- **Descrição:** Valor médio de cada item vendido (ticket médio por item).
- **Observação:** Calculado pela divisão da `receita_diaria` pelo total de `itens_vendidos`. Arredondado para 2 casas decimais.


## Regras de Negócio
- A agregação de valores é realizada considerando o item do pedido (`order_item_id`), e não o pedido completo (`order_id`).
- O cálculo do ticket médio é baseado no item, e não no pedido (cálculo: Receita / Total de Itens).
- A data utilizada para a agregação é a data do item (derivada da dimensão de data).


## Uso Recomendado
- Acompanhamento diário da performance de vendas (Receita e Volume).
- Monitoramento de KPIs de volume (pedidos e itens vendidos).
- Análise de picos de venda e sazonalidade.
- Base para projeções de curto prazo.


## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise, BI e visualização (Vendas/Comercial)