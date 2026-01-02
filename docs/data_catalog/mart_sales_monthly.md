# Catálogo de Dados  
## Tabela: mart_sales_monthly

---

## Descrição
Tabela analítica que consolida as **vendas mensais**, apresentando a receita total do mês e o **crescimento percentual em relação ao mês anterior (MoM)**.

Cada linha representa o desempenho de vendas de **um mês específico**.

---

## Granularidade
- Mensal

---

## Chave lógica
- ano  
- mes  

---

## Dicionário de Campos

### ano
- **Descrição:** Ano de referência das vendas.

---

### mes
- **Descrição:** Mês de referência das vendas.
- **Domínio:** 1 a 12

---

### receita_mensal
- **Descrição:** Valor total da receita gerada no mês.

---

### crescimento_mom
- **Descrição:** Crescimento percentual da receita em relação ao mês anterior (Month over Month).
- **Observações:**
  - Pode ser **nulo** quando não existe mês anterior.
  - Pode ser **nulo** quando a receita do mês anterior é zero.
  - Valores negativos indicam queda de receita.

---

## Regras de Negócio
- A receita mensal é calculada a partir da soma do valor total dos itens vendidos.
- O crescimento MoM compara a receita do mês atual com a do mês imediatamente anterior.
- O crescimento é calculado apenas quando há receita válida no mês anterior.

---

## Uso Recomendado
- Análise de evolução mensal de vendas
- Monitoramento de crescimento ou retração
- Análises de tendência e sazonalidade
- Dashboards executivos e financeiros

---

## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise de vendas mensais
