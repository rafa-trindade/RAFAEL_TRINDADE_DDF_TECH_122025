# Catálogo de Dados  
## Tabela: mart_product_category_performance



## Descrição
Tabela analítica que apresenta a **performance mensal das categorias de produtos**, consolidando informações de receita, volume de itens vendidos e ticket médio por categoria.

Cada linha representa o desempenho de **uma categoria de produto em um determinado mês e ano**.



## Granularidade
- Mensal
- Por categoria de produto



## Chave lógica
- product_category_name  
- ano  
- mes  



## Dicionário de Campos

### product_category_name
- **Descrição:** Nome da categoria do produto.
- **Observação:** Produtos sem categoria definida são agrupados como `sem_categoria`.



### ano
- **Descrição:** Ano de referência das vendas.



### mes
- **Descrição:** Mês de referência das vendas.
- **Domínio:** 1 a 12



### receita_categoria
- **Descrição:** Valor total da receita da categoria no mês.



### itens_vendidos
- **Descrição:** Quantidade total de itens vendidos na categoria no mês.



### ticket_medio_categoria
- **Descrição:** Valor médio de receita por item vendido na categoria.
- **Observação:** Calculado apenas quando há itens vendidos.



## Regras de Negócio
- A receita considera a soma do valor total dos itens vendidos.
- O ticket médio é calculado dividindo a receita pelo total de itens vendidos.
- Categorias inexistentes ou nulas são tratadas como `sem_categoria`.



## Uso Recomendado
- Análise de performance por categoria
- Comparação entre categorias
- Avaliação de ticket médio por categoria
- Dashboards de vendas e produto



## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise de produtos e vendas
