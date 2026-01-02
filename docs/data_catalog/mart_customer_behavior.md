# Catálogo de Dados  
## Tabela: mart_customer_behavior

---

## Descrição
Tabela analítica que consolida **informações de comportamento de compra dos clientes**.  
Apresenta métricas de volume de pedidos, valor total gasto (LTV) e ticket médio por cliente.

Cada linha representa **um cliente único**, considerando todo o seu histórico de compras.

---

## Granularidade
- Por cliente

---

## Chave lógica
- customer_id

---

## Dicionário de Campos

### customer_id
- **Descrição:** Identificador único do cliente.

---

### customer_state
- **Descrição:** Estado (UF) do cliente.

---

### total_pedidos
- **Descrição:** Quantidade total de pedidos realizados pelo cliente.
- **Observação:** Considera pedidos distintos.

---

### ltv
- **Descrição:** Valor total gasto pelo cliente ao longo do tempo.
- **Conceito:** Lifetime Value (LTV).

---

### ticket_medio_cliente
- **Descrição:** Valor médio gasto por pedido pelo cliente.
- **Observação:** Calculado apenas quando o cliente possui pedidos válidos.

---

## Regras de Negócio
- O total de pedidos considera apenas pedidos distintos.
- O LTV é a soma do valor total dos itens comprados pelo cliente.
- O ticket médio é obtido dividindo o LTV pelo total de pedidos.
- Clientes sem pedidos não possuem ticket médio calculado.

---

## Uso Recomendado
- Análise de comportamento e perfil de clientes
- Segmentação por valor (LTV)
- Avaliação de ticket médio por cliente
- Dashboards de CRM e performance comercial

---

## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise de clientes
