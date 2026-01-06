## 🚀 Guia de Execução do Projeto

Este guia descreve o passo a passo para executar o projeto, desde a configuração do ambiente até a visualização da aplicação analítica.

---

### 📦 Pré-requisitos

- Linux / macOS
- Python Utilizado 3.12.3
- Docker e Docker Compose
- Git (para clonar o repositório)
- Acesso à internet (download do dataset Kaggle)

---

### 🔐 1. Configuração de Variáveis de Ambiente

Crie o arquivo `.env` a partir do template `.env.example`:

```bash
cp .env.example .env
```
Edite o arquivo `.env` e configure as variáveis de ambiente necessárias, incluindo o endpoint e as credenciais do MinIO (S3), as configurações de conexão do PostgreSQL (Docker) e as credenciais da API do Kaggle.

---

### 🐘 2. Subir o PostgreSQL (Data Warehouse)

O PostgreSQL é executado via Docker Compose:

```bash
docker compose up -d
```

⚠️ Certifique-se de que o PostgreSQL esteja em execução antes de iniciar as etapas de ingestão de dados.

---

### 🐍 3. Instalar Dependências Python

#### 🧪 3.1 Criação e ativação do ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

---

#### 📦 3.2 Instalação das dependências do projeto

```bash
pip install -r requirements.txt
```

---

### ☁️ 4. Ingestão de Dados - Kaggle → Data Lake (MinIO)

Executa o pipeline de ingestão do dataset Olist, convertendo CSV para Parquet e carregando no Data Lake (camada Landing).

```bash
python -m scripts.ingestion.kaggle_to_bucket
```

---

### 🏗️ 5. Ingestão de Dados - Data Lake → Data Warehouse

Executa a carga da camada Landing (MinIO) para a camada Raw no PostgreSQL, utilizando DuckDB como engine de processamento.

```bash
python -m scripts.ingestion.bucket_to_dw
```

---

### 🔧 6. Transformações com dbt

#### 6.1 Garantir permissão de execução nos scripts

Antes da execução, é necessário garantir permissão de execução nos scripts:


```bash
chmod +x scripts/dbt/run_staging.sh
chmod +x scripts/dbt/run_core.sh
chmod +x scripts/dbt/run_marts.sh
```

---

#### 6.2 Instalar dependências do dbt

O projeto utiliza pacotes externos definidos no arquivo `packages.yml`,
como o `dbt_utils`.

Para instalar as dependências:

```bash
cd dbt
dbt deps
cd ..
```

Esse comando deve ser executado:

- Na primeira execução do projeto
- Após atualização de dependências
- Em novos ambientes

---

#### 6.3 Criar seeds do dbt

Execute o script responsável por criar e carregar os seeds do dbt no diretório `dbt/seeds`:

```bash
python -m scripts.utils.dbt_seeds
```

⚠️ Importante: os seeds devem ser criados antes da execução das transformações (staging, core e marts).

---

#### 6.4 Execução dos Pipelines

#### 1️⃣ Staging

```bash
./scripts/dbt/run_staging.sh
```

---

#### 2️⃣ Core

```bash
./scripts/dbt/run_core.sh
```

---

#### 3️⃣ Marts

```bash
./scripts/dbt/run_marts.sh
```

---

### 🏛️ 7. Governança e Qualidade de Dados

#### 📚 Gerar catálogo de dados (camada Marts)

```bash
python -m scripts.catalog.generate_data_catalog
```

#### 🔍 Profiling dos dados (Landing - MinIO)

```bash
python -m scripts.profiling.landing.customers
python -m scripts.profiling.landing.geolocation
python -m scripts.profiling.landing.order_items
python -m scripts.profiling.landing.orders
python -m scripts.profiling.landing.products
```

---


### 📊 8. Aplicação Analítica (Streamlit)

#### ▶️ Subir a aplicação

```bash
./scripts/streamlit/run_streamlit.sh
```

A aplicação pode ser acessada via:

- http://<IP_DO_SERVIDOR>:8501
- http://localhost:8501

#### ⏹️ Parar a aplicação

```bash
./scripts/streamlit/stop_streamlit.sh
```

### ⚠️ Observações

> Fluxo resumido do pipeline:
> Kaggle → MinIO (Landing) → PostgreSQL (Raw) → dbt (Staging / Core / Marts) → Streamlit

- A execução do projeto é manual, adequada ao contexto de Prova de Conceito (PoC)
- A arquitetura foi projetada para permitir evolução futura com orquestração via Airflow e execução agendada
