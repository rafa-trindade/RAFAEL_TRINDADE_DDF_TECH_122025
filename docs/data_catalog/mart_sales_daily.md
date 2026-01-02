# Catálogo de Dados  
## Tabela: mart_sales_daily



## Descrição
Tabela analítica que consolida as **vendas diárias**, apresentando métricas de receita, volume de itens vendidos, quantidade de pedidos e ticket médio.

Cada linha representa o desempenho de vendas de **um dia específico**.



## Granularidade
- Diária



## Chave lógica
- data



## Dicionário de Campos

### data
- **Descrição:** Data de referência das vendas.



### receita_diaria
- **Descrição:** Valor total da receita gerada no dia.



### itens_vendidos
- **Descrição:** Quantidade total de itens vendidos no dia.



### pedidos
- **Descrição:** Quantidade total de pedidos distintos realizados no dia.



### ticket_medio
- **Descrição:** Valor médio de receita por item vendido no dia.
- **Observação:** Calculado apenas quando há itens vendidos.



## Regras de Negócio
- A receita diária é calculada a partir do valor total dos itens vendidos.
- O total de pedidos considera apenas pedidos distintos.
- O ticket médio é calculado dividindo a receita pelo total de itens vendidos.



## Uso Recomendado
- Análise de vendas diárias
- Monitoramento de performance ao longo do tempo
- Identificação de picos e quedas de vendas
- Dashboards operacionais e financeiros



## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise de vendas
