# Catálogo de Dados  
## Tabela: mart_category_growth_monthly

---

## Descrição
Tabela analítica que apresenta a **receita mensal por categoria de produto**, permitindo a análise do **crescimento percentual em relação ao mês anterior**.

Cada linha representa o desempenho de uma **categoria de produto em um determinado mês e ano**.

---

## Granularidade
- Mensal
- Por categoria de produto

---

## Chave lógica
- product_category_name  
- ano  
- mes  

---

## Dicionário de Campos

### product_category_name
- **Descrição:** Nome da categoria do produto.
- **Observação:** Quando o produto não possui categoria, o valor exibido é `sem_categoria`.

---

### ano
- **Descrição:** Ano de referência da receita.

---

### mes
- **Descrição:** Mês de referência da receita.
- **Domínio:** 1 a 12

---

### receita_mensal
- **Descrição:** Valor total da receita da categoria no mês.

---

### receita_mes_anterior
- **Descrição:** Receita da mesma categoria no mês imediatamente anterior.

---

### crescimento_percentual
- **Descrição:** Percentual de crescimento da receita em relação ao mês anterior.
- **Observações:**
  - Pode ser **nulo** quando não existe mês anterior.
  - Pode ser **nulo** quando a receita do mês anterior é zero.
  - Valores negativos indicam queda de receita.

---

## Regras de Negócio
- A receita é calculada com base no valor total dos itens vendidos.
- O crescimento é calculado apenas quando há receita válida no mês anterior.
- Categorias inexistentes são agrupadas como `sem_categoria`.

---

## Uso Recomendado
- Análise de crescimento mês a mês (MoM)
- Acompanhamento de performance por categoria
- Dashboards financeiros e comerciais
- Análises de tendência e sazonalidade

---

## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise e visualização
