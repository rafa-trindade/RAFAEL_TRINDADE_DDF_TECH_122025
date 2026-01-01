# ⚙️ dbt - Execução de Pipelines em VPS (PostgreSQL)

## 📌 Contexto

Este documento descreve a configuração e a execução dos pipelines **dbt**
utilizados no projeto, responsáveis pelas **transformações analíticas**
no **Data Warehouse PostgreSQL**, executando em uma **VPS dedicada**.

O objetivo é garantir **padronização, rastreabilidade, qualidade e
reprodutibilidade** das transformações de dados, seguindo a arquitetura
**Staging → Core → Marts**.


## 🧱 Estrutura de Diretórios

Os pipelines dbt são organizados em scripts de execução por camada:

```text
scripts/dbt/
  run_staging.sh
  run_core.sh
  run_marts.sh
```

Cada script executa exclusivamente os modelos da sua respectiva camada,
garantindo isolamento lógico e controle do fluxo de transformação.


## 🔧 Configuração Inicial

### Permissões de Execução dos Scripts

Antes da execução, é necessário garantir permissão de execução nos scripts:

```bash
chmod +x scripts/dbt/run_staging.sh
chmod +x scripts/dbt/run_core.sh
chmod +x scripts/dbt/run_marts.sh
```
Essa configuração permite que os scripts sejam executados diretamente
no ambiente Linux da VPS.

### Instalação das Dependências do dbt

O projeto utiliza pacotes externos definidos no arquivo packages.yml
(como dbt_utils).

Para instalar as dependências:

```bash
cd dbt
dbt deps
```

Esse comando deve ser executado:

- Na primeira execução do projeto
- Após atualização de dependências
- Em novos ambientes

## ▶️ Execução dos Pipelines

### 1️⃣ Staging

```bash
./scripts/dbt/run_staging.sh
```

### 2️⃣ Core

```bash
./scripts/dbt/run_core.sh
```

### 3️⃣ Marts

```bash
./scripts/dbt/run_marts.sh
```

## ⚠️ Observações

- A execução é manual, adequada ao contexto de PoC
- A arquitetura permite evolução futura para orquestração com Airflow e execução agendada