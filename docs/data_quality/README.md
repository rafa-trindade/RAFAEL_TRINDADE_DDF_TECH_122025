# ✅ Data Quality - Mapeamento e Implementação no Projeto

Este documento descreve como a **qualidade de dados** é garantida ao longo do pipeline,
desde a **ingestão no Data Lake** até a **modelagem analítica no Data Warehouse**.

A estratégia adotada segue o princípio de **qualidade distribuída por camada**,
aplicando validações adequadas ao papel de cada estágio da arquitetura.


## 🎯 Objetivos da Estratégia de Data Quality

- Detectar problemas **o mais cedo possível** no pipeline
- Garantir **contratos de dados explícitos**
- Evitar propagação de erros para camadas analíticas
- Permitir **auditoria, rastreabilidade e reprocessamento**
- Separar claramente **qualidade técnica** de **qualidade de negócio**


## 🧱 Visão Geral por Camada

| Camada | Ferramenta | Tipo de Validação | Objetivo |
|------|-----------|------------------|----------|
| Ingestão / Landing | Pandera | Schema, tipos, estrutura | Garantir conformidade técnica na entrada |
| DW - Core | dbt tests | Relacionamentos, regras de negócio | Garantir modelo dimensional correto |


# 📥 Data Quality na Ingestão (Pré-Landing)

### Ferramenta
- **Pandera (pandera.pandas)**

### Quando ocorre
- **Antes da persistência dos dados na camada Landing do MinIO**

### Objetivo
Garantir que **somente dados estruturalmente válidos** sejam armazenados no Data Lake.


## 📐 Contratos de Schema (Pandera)

Cada dataset possui um **schema explícito**, definindo:

- Nome das colunas
- Tipo de dado esperado
- Permissão de nulos
- Estrutura mínima obrigatória

#### Datasets validados

| Dataset | Colunas | Observações |
|------|--------|-------------|
| `olist_customers_dataset` | 6 | Identificadores e localização |
| `olist_geolocation_dataset` | 6 | Coordenadas e localização |
| `olist_order_items_dataset` | 8 | Itens de pedido e valores |
| `olist_orders_dataset` | 9 | Ciclo de vida do pedido |
| `olist_products_dataset` | 10 | Atributos físicos do produto |

Todos os schemas incluem a coluna técnica `run_id`, garantindo rastreabilidade por execução.


## 🔎 Processo de Validação (Pandera)

1. Leitura do arquivo Parquet
2. Aplicação do schema Pandera correspondente
3. Registro detalhado do resultado em log técnico




## 📁 Evidências e Logs (Pandera)

Resultados organizados por camada:

```text
reports/pandera/landing
```

## 📝 Evidência - Log de Validação (Pandera)

```text
RUN_ID: 20251231_162832 | TIMESTAMP: 2025-12-31T16:28:36.733100 | STATUS: SUCCESS | DATASET: olist_order_items_dataset | FILE: olist_order_items_dataset.parquet | ROWS: 112650 | COLS: 8 | ERRORS: None
RUN_ID: 20251231_162832 | TIMESTAMP: 2025-12-31T16:28:37.411663 | STATUS: SUCCESS | DATASET: olist_customers_dataset | FILE: olist_customers_dataset.parquet | ROWS: 99441 | COLS: 6 | ERRORS: None
RUN_ID: 20251231_162832 | TIMESTAMP: 2025-12-31T16:28:38.683886 | STATUS: SUCCESS | DATASET: olist_orders_dataset | FILE: olist_orders_dataset.parquet | ROWS: 99441 | COLS: 9 | ERRORS: None
RUN_ID: 20251231_162832 | TIMESTAMP: 2025-12-31T16:28:40.847217 | STATUS: SUCCESS | DATASET: olist_geolocation_dataset | FILE: olist_geolocation_dataset.parquet | ROWS: 1000163 | COLS: 6 | ERRORS: None
RUN_ID: 20251231_162832 | TIMESTAMP: 2025-12-31T16:28:41.016000 | STATUS: SUCCESS | DATASET: olist_products_dataset | FILE: olist_products_dataset.parquet | ROWS: 32951 | COLS: 10 | ERRORS: None
```

Esses logs funcionam como **evidência auditável de qualidade técnica**.


# 🏗️ Data Quality no Data Warehouse (dbt)

Após a carga no Data Warehouse, a qualidade passa a ser garantida por **dbt tests**,
executados diretamente sobre os modelos analíticos.

## 🧪 Tipos de Testes Implementados

### 1️⃣ Testes Estruturais
- `not_null`
- `unique`
- Combinação única de colunas

### 2️⃣ Integridade Referencial
- `relationships` entre fatos e dimensões

### 3️⃣ Regras de Negócio
- Expressões booleanas
- Faixas válidas
- Cálculos derivados


## 📊 Regras de Qualidade - Modelos Analíticos

### 📌 `fact_order_items`

- Chave composta única: `(order_id, order_item_id)`
- Nenhuma chave nula
- Relacionamentos obrigatórios:
  - `dim_customers`
  - `dim_products`
  - `dim_date`
  - `dim_time`
- Regras financeiras:
  - `price >= 0`
  - `freight_value >= 0`
  - `total_item_value = price + freight_value`
- Regra temporal:
  - `chave_hora` entre `0` e `1439`

---

### 📌 Dimensões

#### `dim_customers`
- `customer_id` único e não nulo
- Cidade e estado obrigatórios

#### `dim_products`
- `product_id` único e não nulo

#### `dim_date` (seed)
- `chave_data` única e não nula

#### `dim_time` (seed)
- `chave_hora` única
- Regra: `between 0 and 1439`


## 📁 Evidências e Logs (dbt)

Resultados organizados por camada:

```text
reports/dbt/staging
reports/dbt/core
reports/dbt/marts
```

## 📝 Evidência - Log de Validação (dbt)

```text
[0m15:00:59  Running with dbt=1.11.2
[0m15:00:59  Registered adapter: postgres=1.10.0
[0m15:01:00  Found 15 models, 31 data tests, 2 seeds, 5 sources, 577 macros
[0m15:01:00  
[0m15:01:00  Concurrency: 1 threads (target='dev')
[0m15:01:00  
...
[0m15:01:01  14 of 31 START test not_null_dim_time_chave_hora ............................... [RUN]
[0m15:01:01  14 of 31 PASS not_null_dim_time_chave_hora ..................................... [[32mPASS[0m in 0.03s]
[0m15:01:01  15 of 31 START test not_null_fact_order_items_chave_data ....................... [RUN]
[0m15:01:01  15 of 31 PASS not_null_fact_order_items_chave_data ............................. [[32mPASS[0m in 0.05s]
[0m15:01:01  16 of 31 START test not_null_fact_order_items_chave_hora ....................... [RUN]
[0m15:01:01  16 of 31 PASS not_null_fact_order_items_chave_hora ............................. [[32mPASS[0m in 0.05s]
[0m15:01:01  17 of 31 START test not_null_fact_order_items_customer_id ...................... [RUN]
[0m15:01:01  17 of 31 PASS not_null_fact_order_items_customer_id ............................ [[32mPASS[0m in 0.04s]
[0m15:01:01  18 of 31 START test not_null_fact_order_items_freight_value .................... [RUN]
[0m15:01:01  18 of 31 PASS not_null_fact_order_items_freight_value .......................... [[32mPASS[0m in 0.05s]
[0m15:01:01  19 of 31 START test not_null_fact_order_items_order_id ......................... [RUN]
[0m15:01:01  19 of 31 PASS not_null_fact_order_items_order_id ............................... [[32mPASS[0m in 0.04s]
[0m15:01:01  20 of 31 START test not_null_fact_order_items_order_item_id .................... [RUN]
[0m15:01:01  20 of 31 PASS not_null_fact_order_items_order_item_id .......................... [[32mPASS[0m in 0.05s]
[0m15:01:01  21 of 31 START test not_null_fact_order_items_price ............................ [RUN]
[0m15:01:01  21 of 31 PASS not_null_fact_order_items_price .................................. [[32mPASS[0m in 0.05s]
[0m15:01:01  22 of 31 START test not_null_fact_order_items_product_id ....................... [RUN]
[0m15:01:01  22 of 31 PASS not_null_fact_order_items_product_id ............................. [[32mPASS[0m in 0.05s]
...
[0m15:01:02  
[0m15:01:02  Finished running 31 data tests in 0 hours 0 minutes and 2.15 seconds (2.15s).
[0m15:01:02  
[0m15:01:02  [32mCompleted successfully[0m
[0m15:01:02  
[0m15:01:02  Done. PASS=31 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=31

```

Esses logs funcionam como **evidência auditável de qualidade técnica**.


## 🧠 Princípios-Chave

- **Fail fast**
- **Qualidade como código**
- **Separação clara de responsabilidades**
  - Pandera → qualidade técnica
  - dbt → qualidade semântica e analítica
- **Observabilidade nativa via logs**


## 🧩 Conclusão

A estratégia de Data Quality deste projeto demonstra que é possível garantir
**confiabilidade analítica em nível de produção** utilizando:

- Contratos explícitos
- Validações automatizadas
- Evidências auditáveis
- Integração com lineage e observabilidade

A qualidade é tratada como **parte estrutural da arquitetura de dados**, e não
como uma etapa isolada do pipeline.
