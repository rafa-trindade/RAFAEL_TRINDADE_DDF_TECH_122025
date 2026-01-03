# Catálogo de Dados  - `mart_sales_monthly`


## Descrição
Tabela analítica que consolida a **receita total de vendas a nível mensal**, focada no acompanhamento do **crescimento mês a mês** (Month-over-Month - MoM).

Esta tabela é essencial para monitorar tendências macro de desempenho financeiro e sazonalidade.


## Granularidade
- Mensal (Ano e Mês)


## Chave lógica
- `ano`  
- `mes`  


## Dicionário de Campos

### `ano`
- **Descrição:** Ano de referência da receita consolidada.

### `mes`
- **Descrição:** Mês de referência da receita consolidada.
- **Domínio:** 1 a 12

### `receita_mensal`
- **Descrição:** Valor total da receita bruta consolidada para o respectivo mês e ano.
- **Origem:** Somatório de `total_item_value`.

### `crescimento_mom`
- **Descrição:** Taxa de crescimento percentual da receita em comparação com o mês imediatamente anterior.
- **Cálculo:** `(Receita Atual - Receita Mês Anterior) / Receita Mês Anterior`
- **Observações:**
  - O valor é apresentado em formato decimal (fração), arredondado para 4 casas. Ex: 0.1000 = 10% de crescimento.
  - Será **nulo** para o primeiro mês registrado na base de dados (não há mês anterior para comparação).
  - Será **nulo** se a receita do mês anterior for zero (evita divisão por zero).


## Regras de Negócio
- A agregação é feita pelo somatório da receita total dos itens vendidos (`total_item_value`) para cada combinação única de ano e mês.
- O cálculo do crescimento MoM é realizado usando a função de janela `LAG` ordenada cronologicamente.
- A receita é considerada a receita bruta dos itens.


## Uso Recomendado
- Acompanhamento de indicadores financeiros e KPIs executivos.
- Análise de tendências de crescimento e sazonalidade.
- Criação de dashboards de performance comercial.


## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise e visualização de séries temporais de receita.