# Catálogo de Dados  
## Tabela: mart_sales_weekda

---

## Descrição
Tabela analítica que consolida as **vendas por dia da semana**, permitindo analisar o comportamento de pedidos, receita e ticket médio conforme o dia.

Cada linha representa **um dia da semana**.

---

## Granularidade
- Por dia da semana

---

## Chave lógica
- nome_dia_semana

---

## Dicionário de Campos

### nome_dia_semana
- **Descrição:** Nome do dia da semana (ex.: Segunda-feira, Terça-feira).

---

### total_pedidos
- **Descrição:** Quantidade total de pedidos distintos realizados no dia da semana.

---

### receita_total
- **Descrição:** Valor total da receita gerada no dia da semana.

---

### ticket_medio
- **Descrição:** Valor médio de receita por item vendido no dia da semana.
- **Observação:** Calculado a partir da média do valor dos itens vendidos.

---

## Regras de Negócio
- O total de pedidos considera apenas pedidos distintos.
- A receita total é calculada a partir do valor total dos itens vendidos.
- O ticket médio representa a média do valor dos itens, e não a média por pedido.

---

## Uso Recomendado
- Análise de performance por dia da semana
- Identificação dos dias com maior volume de vendas
- Planejamento de campanhas e ações comerciais
- Dashboards operacionais e estratégicos

---

## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise de vendas por dia da semana
