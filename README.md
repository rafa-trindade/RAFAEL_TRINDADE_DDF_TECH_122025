# RAFAEL TRINDADE - DDF_TECH_122025

## 📌 Introdução
Este repositório contém a resolução do Case Técnico para a posição Engenheiro de Dados Júnior na **Dadosfera**. O projeto foca em uma empresa de E-commerce, utilizando o dataset brasileiro da Olist (Kaggle) para construir uma plataforma de dados ponta a ponta, integrando engenharia moderna, modelagem dimensional e visualiação de dados.

---

## 🛠️ Arquitetura Geral da Solução
A arquitetura proposta segue padrões modernos de **Lakehouse** + **Data Warehouse Analítico**, combinando **MinIO**, **DuckDB**, **PostgreSQL**, **dbt**, **Pandera** e **Dadosfera**.

### 📌 Arquitetura Proposta:

![Arquitetura](docs/data_architecture/arquitetura_proposta.png)

### Principais componentes:

- **Fonte de Dados:** Kaggle - Olist (CSV)
- **Data Lake:** MinIO camada Landing (extra: Bronze, Silver, Gold) 
- **Engine de Processamento:** DuckDB
- **Data Warehouse:** PostgreSQL (Docker)
- **Transformações:** dbt
- **Qualidade de Dados:** Pandera + dbt tests
- **Analytics & BI:** Dadosfera + Metabase
- **Data Apps:** Streamlit

---

## 📚 Mapeamento da Documentação

### 🏗️ Data Architecture
📁 `docs/data_architecture/`

Descreve a arquitetura técnica do projeto em execução:
- Componentes da stack (MinIO, PostgreSQL, DuckDB, Pandera, Docker)
- Papéis e responsabilidades de cada serviço
- Integração entre ingestão, processamento e armazenamento

---

### 🏛️ Data Governance
📁 `docs/data_governance/`

Centraliza as políticas e diretrizes do projeto e mapeia como a solução atende,
na prática, aos pilares de **Data Governance**.
- Política de retenção baseada em execuções técnicas (`run_id`)
- Definição de contratos gerais de qualidade de dados
- Estratégias seguras de reprocessamento e rollback
- Suporte nativo à auditoria, observabilidade e controle de custos
- Governança aplicada via código e automação

---

### 🧬 Data Lineage
📁 `docs/data_lineage/`

Documenta a rastreabilidade ponta a ponta dos dados:
- Origem dos dados
- Transformações por camada (Landing → Raw → Staging → Core → Marts → Dadosfera)

---

### 🧱 Data Modeling
📁 `docs/data_modeling/`

- Documenta as decisões de modelagem de dados adotadas no projeto:
- Modelagem OLTP dos dados de origem
- Modelagem OLAP orientada a analytics
- Diagramas e imagens das estruturas de dados

---

### 🔍 Data Observability
📁 `docs/data_observability/`

Mapeia como o projeto atende aos pilares de Data Observability:
- Freshness
- Volume
- Schema
- Distribution
- Lineage
- Quality
- Reliability e Reprocessamento

A observabilidade emerge como resultado das decisões de arquitetura e governança.

---

### 📊 Data Profiling
📁 `docs/data_profiling/`

Apresenta análises exploratórias e estatísticas dos dados:
- Volume por camada
- Cardinalidade
- Distribuição de valores
- Percentual de nulos

Utilizado como base para qualidade e observabilidade.

---

### ⚙️ Configurações de Infraestrutura
📁 `docs/configuracoes/`

- Centraliza guias técnicos de configuração do ambiente de infraestrutura e serviços
utilizados no projeto:
- Configuração do PostgreSQL em Docker com SSL/TLS habilitado
- Criação, permissões e montagem segura de certificados SSL
- Suporte a acesso seguro por ferramentas externas (ex: Dadosfera)

---

# 📑 Itens do Case

## Item 0 - Agilidade e Planejamento

### Metodologia

O planejamento do projeto foi realizado seguindo boas práticas do PMBOK, combinado com metodologias ágeis.

**Gestão:** Quadro Kanban para controle de tarefas, entregas técnicas e milestones do projeto.

![Quadro GitHub Projects](docs/images/project.png)


## Item 1 - Base de Dados
**Dataset:** Brazilian E-Commerce Dataset by Olist (Kaggle).

**Justificativa:** 
- Dataset real, amplamente utilizado em projetos analíticos
- Domínio aderente ao cenário de e-commerce
- Volume superior a 100.000 registros
- Contém dados transacionais e descritivos

**Principais tabelas:**
- `olist_orders_dataset`
- `olist_order_items_dataset`
- `olist_products_dataset`
- `olist_customers_dataset`
- `olist_geolocation_dataset`


## Item 2 e 3 - Integrar e Explorar (Dadosfera)

### Estratégia de Ingestão

A ingestão foi dividida em etapas claras:

**Extração Kaggle → MinIO (Landing)**

- Scripts em Python
- Versionamento por `run_id`
- Dados armazenados em formato parquet
- Verificação de Qualidade com Pandera

**Carga Analítica no Data Warehouse**

- PostgreSQL utilizado como Data Warehouse analítico
- Transformações realizadas com dbt
- Construção do Star Schema (Kimball) diretamente no DW
- Aplicação de testes de qualidade (dbt tests)
- Microtransformações simuladas no contexto analítico
- Motor de processamento na camada de ingestão: DuckDB

**Lakehouse: Landing → Bronze / Silver / Gold (Arquitetura Bônus)**

- Organização incremental
- Padronização de schemas
- Preparação para consumo por modelos de ML

**Carga e catalogação dos dados utilizando o módulo de Coleta da Dadosfera.**

- Módulo de Coleta da Dadosfera
- Execução a partir de VPS dedicada
- PostgreSQL em container com SSL habilitado

A **carga** foi realizada a partir de uma VPS dedicada, configurada para permitir integração segura com a plataforma.

A **catalogação dos dados** foi realizada diretamente na plataforma Dadosfera, onde os ativos ingeridos foram registrados, descritos e organizados, possibilitando sua exploração, governança e reutilização.

**Ativo na Dadosfera:** [[PIPELINE](https://app.dadosfera.ai/pt-BR/collect/pipelines/fb3dc75a-11f8-4c61-99c4-e804871d166d)]  [[LINK PARA O DATASET CATALOGADO](https://app.dadosfera.ai/pt-BR/catalog/data-assets?pipeline_id=fb3dc75a-11f8-4c61-99c4-e804871d166d&pipeline_name=RAFAEL%20TRINDADE%20-%20DDF_TECH_122025)]


## Item 4 - Data Quality

### Abordagem

A qualidade dos dados foi tratada desde o início do pipeline.

### Ferramentas Utilizadas

- **Pandera (Python)** - validação de schemas
- **dbt tests** - testes analíticos

### Entregável

Geração de relatório de qualidade para identificação de nulos e tipos incorretos.

**Resultado:** [[PANDERA REPORTS](https://github.com/rafa-trindade/RAFAEL_TRINDADE_DDF_TECH_122025/tree/main/reports/pandera)]  [[DBT REPORTS](https://github.com/rafa-trindade/RAFAEL_TRINDADE_DDF_TECH_122025/tree/main/reports/dbt)]


## Item 6 - Modelagem de Dados

Modelagem dimensional seguindo os princípios de Ralph Kimball.

**Esquema:** Star Schema (Tabelas Fato e Dimensão).<br>
**Justificativa:** Otimização para consultas analíticas e performance no BI.

### Estrutura Final

**Fato:**

- `fact_order_items`

**Dimensões:**

- `dim_customers`
- `dim_products`
- `dim_geolocation`
- `dim_date` *(dbt_seed)*
- `dim_time` *(dbt_seed)*

### `modelo_olap`

![Modelagem](docs/data_modeling/olap.png)

### origem: `modelo_oltp`

![oltp](docs/data_modeling/oltp.png)

---

## Item 7 - Analisar (Visualização)
Dashboard interativo construído na Dadosfera (Metabase).
* **Análises:** 
* **Query SQL:** [LINK PARA O ARQUIVO SQL DE CONSULTA]

---

## Item 8 - Pipelines

Pipeline de processamento automatizado utilizando os Steps da Dadosfera.

**Status:** [[PIPELINE](https://app.dadosfera.ai/pt-BR/collect/pipelines/fb3dc75a-11f8-4c61-99c4-e804871d166d)]

---

## Item 9 - Data App (Streamlit)
Desenvolvimento de um Data App utilizando o Streamlit.
* **URL do App:** [[STREAMLIT VPS](http://54.39.98.107:8501/)]


---

## Item 10 - Apresentação (Pitch Técnico)
Apresentação da solução e demonstração da viabilidade de substituição da arquitetura atual pela Dadosfera.

👉 **[LINK PARA O VÍDEO NO YOUTUBE - NÃO LISTADO]**

---

**Portfólio:** [https://rafa-trindade.github.io/](https://rafa-trindade.github.io/)<br>
**LinkedIn:** [https://www.linkedin.com/in/rafatrindade/](https://www.linkedin.com/in/rafatrindade/)