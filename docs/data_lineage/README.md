# 🔗 Data Lineage - Dataset Olist (Clientes e Pedidos)

Este documento descreve o **data lineage end-to-end** da Prova de Conceito (PoC), detalhando a origem dos dados, os processos de ingestão, carga e transformação, bem como a evolução dos dados ao longo das camadas do **Data Lake (Landing)** e do **Data Warehouse Analítico**.

## 📥 Ingestão - `olist/landing_*`

- **Fonte:** Externa (Kaggle - Dataset Olist)
- **Frequência:** Sob demanda (execução manual)
- **Formato de Origem:** CSV
- **Formato Persistido:** Parquet
- **Ambiente de Execução:** VPS
- **Ferramentas:** Python, Kaggle API, Pandera, MinIO

## ✅ Data Lineage - Olist

## 1. Visão Geral

| Item        | Valor |
|------------|-------|
| Origem     | Kaggle - Dataset Olist |
| Domínio    | Orders / Customers / Products |
| Lake       | Landing (MinIO) |
| Warehouse  | Raw → Staging → Core → Marts |
| Execução   | VPS (ambiente containerizado) |


## 2. Lineage por Camada

### 2.1 Fonte → Landing (Data Lake)

**Origem:** Kaggle (CSV)  
**Destino:** `olist/landing_*` (Parquet no MinIO)

kaggle/olist_.csv
→ validação de schema (Pandera)
→ conversão para Parquet
→ olist/landing_*


| Etapa | Processo | Descrição | Ações / Regras | Resultado Esperado |
|------:|----------|-----------|----------------|-------------------|
| 1 | Extração | Download dos datasets Olist via Kaggle API | Autenticação e versionamento manual | Arquivos CSV disponíveis localmente |
| 2 | Validação de Schema | Validação técnica antes da persistência | Validação de schema | Dados conformes à especificação |
| 3 | Conversão de Formato | Padronização para formato analítico | CSV → Parquet | Arquivos otimizados para leitura |
| 4 | Persistência | Escrita no Data Lake | Upload no MinIO (Landing) | Dados disponíveis no Lake |

📌 **Observação:**  
Nesta etapa **não são aplicadas regras de negócio**, apenas validações técnicas com **Pandera**.

---

### 2.2 Landing → Raw (Data Warehouse)

**Origem:** `olist/landing_*`  
**Destino:** `dw_raw.*` 
**Materialização:** `Table` 


olist/landing_*
→ leitura Parquet
→ carga com DuckDB
→ dw_raw.*


| Etapa | Processo | Descrição | Ações / Regras | Resultado Esperado |
|------:|----------|-----------|----------------|-------------------|
| 1 | Leitura | Leitura dos arquivos Parquet no MinIO | Acesso S3-compatible | Dados disponíveis para carga |
| 2 | Carga | Transferência para o DW | DuckDB como engine de carga | Tabelas Raw no PostgreSQL |
| 3 | Persistência | Armazenamento bruto no DW | Estrutura espelhada da origem | Histórico fiel à fonte |

📌 **Observação:**  
A camada **Raw no DW** mantém os dados **sem transformações semânticas**, preservando a estrutura original.

---

### 2.3 Raw → Staging (Data Warehouse)

**Origem:** `dw_raw.*`  
**Destino:** `dw_staging.stg_*`  
**Materialização:** `View` 

dw_raw.*
→ padronização
→ limpeza leve
→ dw_staging.stg_*


| Etapa | Processo | Descrição | Ações / Regras | Resultado Esperado |
|------:|----------|-----------|----------------|-------------------|
| 1 | Padronização | Ajustes técnicos | Naming convention, tipos, datas | Dados consistentes |
| 2 | Limpeza | Tratamento de valores inválidos | Nulls, formatos, duplicidades técnicas | Base estável para modelagem |
| 3 | Testes | Validação técnica | dbt tests (not null, unique) | Qualidade garantida |

---

### 2.4 Staging → Core (Star Schema - Kimball)

**Origem:** `dw_staging.stg_*`  
**Destino:** `dw_core.dim/fact_*`  
**Materialização:** `Table` 

dw_staging.stg_*
→ modelagem dimensional
→ fatos e dimensões
→ dw_core.dim/fact_*


| Etapa | Processo | Descrição | Ações / Regras | Resultado Esperado |
|------:|----------|-----------|----------------|-------------------|
| 1 | Modelagem Dimensional | Aplicação do Star Schema (Kimball) | Criação de tabelas fato e dimensões | Modelo analítico consistente |
| 2 | Chaves | Definição de relacionamentos | Chaves naturais e técnicas | Integridade dimensional |
| 3 | Regras de Negócio | Aplicação de semântica | Status, métricas, filtros | Dados alinhados ao negócio |

📌 **Observação:**  
A camada **Core** representa a **verdade analítica** do negócio.

---

### 2.5 Core → Marts (Consumo)

**Origem:** `dw_core.dim/fact_*`  
**Destino:** `dw_marts.mart_*`  
**Materialização:** `Table`

dw_core.dim/fact_*
→ agregações
→ métricas
→ dw_marts.mart_*


| Etapa | Processo | Descrição | Ações / Regras | Resultado Esperado |
|------:|----------|-----------|----------------|-------------------|
| 1 | Agregações | Simplificação para consumo | Métricas e KPIs | Consultas performáticas |
| 2 | Especialização | Marts por domínio | customers, products, sales | Consumo otimizado |
| 3 | Testes | Validação final | dbt tests | Confiabilidade analítica |


## 3. Consumo e Governança

- **Metabase**
  - Dashboards analíticos
  - Integrado à **Dadosfera**
  - Pipeline e ativos **catalogados**

- **Streamlit**
  - Aplicações analíticas interativas
  - Consumo direto do **Data Warehouse (PostgreSQL)**


## 4. Observações Finais

- O Data Lake possui **apenas a camada Landing**
- **Não há Bronze / Silver no Lake** (arquitetura de referência)
- Todas as transformações semânticas ocorrem no **Data Warehouse**
- DuckDB atua **exclusivamente como engine de carga**
- A arquitetura segue boas práticas de **ELT moderno**
- Execução integral em **VPS**, com containers Docker

