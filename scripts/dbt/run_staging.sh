#!/usr/bin/env bash
set -e

echo "🚀 Iniciando dbt - STAGING"

PROJECT_ROOT="/home/rafael/app/RAFAEL_TRINDADE_DDF_TECH_122025"
DBT_DIR="$PROJECT_ROOT/dbt"
REPORTS_DIR="$PROJECT_ROOT/reports/dbt/staging"

mkdir -p "$REPORTS_DIR"

# ----------------------------------
# Virtualenv
# ----------------------------------
if [ -d "$PROJECT_ROOT/.venv" ]; then
  echo "🐍 Ativando virtualenv"
  source "$PROJECT_ROOT/.venv/bin/activate"
fi

# ----------------------------------
# Env vars
# ----------------------------------
if [ -f "$PROJECT_ROOT/.env" ]; then
  echo "🔐 Carregando .env"
  export $(grep -v '^#' "$PROJECT_ROOT/.env" | xargs)
fi

cd "$DBT_DIR"

# ----------------------------------
# Debug
# ----------------------------------
echo "🔍 dbt debug"
dbt debug

echo "🧹 dbt clean"
dbt clean

echo "📦 dbt deps"
dbt deps

# ----------------------------------
# Staging Models
# ----------------------------------
echo "📦 dbt run (staging)"
dbt run --select staging --fail-fast \
  | tee "$REPORTS_DIR/dbt_run_staging_$(date +%Y%m%d_%H%M%S).log"


echo "✅ dbt STAGING finalizado com sucesso"
