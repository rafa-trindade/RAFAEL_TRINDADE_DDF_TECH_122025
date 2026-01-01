# 🏗️ Data Architecture - Mapeamento de Arquitetura do Projeto

Este documento descreve a **arquitetura técnica da Prova de Conceito (PoC)** em execução, detalhando como os componentes se integram para viabilizar os processos de **ingestão, processamento, transformação, validação, armazenamento e consumo analítico de dados**.

A solução segue padrões modernos de **Lakehouse + Data Warehouse Analítico**, priorizando **simplicidade operacional**, **portabilidade** e **boas práticas de engenharia de dados**.

---

## 🛠️ Arquitetura Geral da Solução (PoC)

![Arquitetura Geral](../images/arquitetura_proposta.png)

### Visão Geral

O fluxo de dados inicia-se na ingestão de arquivos CSV do **dataset Olist (Kaggle)**, executada em uma **VPS**, onde os dados são armazenados no **Data Lake (MinIO)** na camada *Landing*.  
Os dados passam por etapas de **carga com DuckDB**, modelagem analítica com **dbt no PostgreSQL**, validações de qualidade e são consumidos por ferramentas de **visualização, catálogo e aplicações analíticas**, todas executadas em ambiente **local containerizado dentro da VPS**.


---

## 🧱 Componentes da Arquitetura

| Componente | Papel na Arquitetura | Responsabilidades Técnicas | Diferencial Estratégico |
|-----------|---------------------|----------------------------|-------------------------|
| **Kaggle API** | **Fonte de Dados** | Download automatizado do dataset Olist em formato CSV por meio de scripts Python. | Fonte pública realista para validação da arquitetura e dos pipelines. |
| **Python (Ingestão)** | **Camada de Ingestão** | Extração dos dados via Kaggle API, leitura de arquivos CSV, conversão para formato Parquet e armazenamento no MinIO. | Flexibilidade para tratamento inicial dos dados e fácil integração com bibliotecas analíticas. |
| **MinIO (S3-compatible)** | **Data Lake (Landing / Bronze / Silver / Gold)** | Armazenamento de dados brutos e processados em formato Parquet na camada landing. | Compatibilidade com S3 API, permitindo migração futura para AWS ou outros clouds sem refatoração. |
| **DuckDB** | **Engine de Processamento Analítico** | Leitura de arquivos Parquet no MinIO, execução de transformações SQL vetorizadas e carga dos dados transformados no Data Warehouse PostgreSQL. | Alta performance analítica local para transformação de dados, sem dependência de clusters distribuídos. |
| **dbt (Core + Postgres)** | **Transformações e Modelagem Analítica** | Criação de modelos analíticos no PostgreSQL, testes de integridade, documentação e versionamento lógico do warehouse. | Padronização de transformações e governança leve, alinhada a boas práticas modernas. |
| **Pandera** | **Qualidade e Validação de Dados** | Validação de schema **antes da persistência dos dados na camada Landing do MinIO**, garantindo conformidade na ingestão. | Detecção precoce de inconsistências e garantia de contratos de dados desde a origem. |
| **PostgreSQL** | **Data Warehouse Analítico** | Persistência de dados modelados para consumo por BI e aplicações analíticas. | Banco relacional robusto, amplamente adotado e integrado ao ecossistema dbt/BI. |
| **Docker** | **Infraestrutura e Isolamento** | Containerização de serviços (PostgreSQL, MinIO, aplicações) executados em uma VPS, garantindo reprodutibilidade do ambiente. | Facilidade de setup local, isolamento de serviços e portabilidade para outros ambientes ou cloud. |
| **Dadosfera** | **Catálogo de Dados e Governança** | Exposição de metadados, documentação e exploração dos datasets analíticos. | Visibilidade, governança e descoberta de dados em ambiente analítico. |
| **Metabase** | **Visualização Analítica (BI)** | Criação de dashboards e análises exploratórias integrado à plataforma Dadosfera e utilizando a pipeline local como fonte de dados. | Ferramenta integrada à camada de governança e visualização da Dadosfera para rápida validação analítica em PoCs. |
| **Streamlit** | **Data App Analítico** | Desenvolvimento de aplicações interativas para exploração e visualização de dados a partir do Data Warehouse PostgreSQL. | Agilidade na criação de interfaces analíticas diretamente conectadas ao DW, sem necessidade de front-end complexo. |


---

## 🔄 Fluxo de Dados (End-to-End)

1. **Ingestão**
   - Download dos dados via **Kaggle API** por meio de scripts **Python**
   - Validação de schema, tipos e regras de negócio com **Pandera**
   - Conversão dos arquivos CSV para **Parquet**
   - Armazenamento dos dados validados no **MinIO - Camada Landing**

2. **Carga para o Data Warehouse**
   - Leitura dos arquivos **Parquet** armazenados na camada Landing do **MinIO**
   - Utilização do **DuckDB exclusivamente como engine de carga**
   - Transferência dos dados do Data Lake para a camada **Raw** do **Data Warehouse PostgreSQL**

3. **Modelagem Analítica no Data Warehouse**
   - Transformações de dados realizadas integralmente no **PostgreSQL** utilizando **dbt**
   - Organização dos dados nas camadas **Raw**, **Staging**, **Core** e **Marts**, sendo que na camada **Core** é aplicada a modelagem dimensional em **Star Schema (Kimball)**
   - Execução de **dbt tests** para validação de integridade, consistência e regras de negócio

4. **Consumo Analítico**
   - Exploração e visualização de dados por meio do **Metabase**, integrado à **Dadosfera**, com **catalogação da pipeline e dos ativos de dados** dentro da plataforma
   - Desenvolvimento de **aplicações analíticas interativas com Streamlit**, consumindo dados diretamente do **Data Warehouse PostgreSQL**


---

## 📦 Stack Tecnológica (Requirements)

- **Ingestão e Preparação de Dados:** kaggle, pandas, pyarrow, python-dotenv  
- **Qualidade de Dados (Pré-Landing):** pandera  
- **Data Lake (S3-compatible):** MinIO, boto3  
- **Engine de Carga para o DW:** duckdb  
- **Data Warehouse:** PostgreSQL, psycopg2-binary, SQLAlchemy  
- **Transformações e Modelagem Analítica:** dbt-core, dbt-postgres  
- **Visualização e Data Apps:** streamlit, plotly, tabulate  
- **Governança e Catálogo:** Dadosfera, Metabase  
- **Infraestrutura:** Docker  

---

## 🎯 Considerações Finais

Esta arquitetura foi projetada para **validar conceitos**, **experimentar boas práticas modernas de dados** e **demonstrar viabilidade técnica**, sendo executada integralmente em uma **VPS**, com baixo custo operacional e alta flexibilidade para evolução futura.

A solução pode ser facilmente expandida para:
- Orquestração dos pipelines com **Apache Airflow**
- Migração da infraestrutura para **cloud providers** (AWS, GCP ou Azure)
- Migração das **transformações, documentação e governança de dados** para a plataforma **Dadosfera**
