#!/usr/bin/env bash
set -e

echo "🚀 Iniciando dbt - MARTS (Analytics Layer)"

PROJECT_ROOT="/home/rafael/app/RAFAEL_TRINDADE_DDF_TECH_122025"
DBT_DIR="$PROJECT_ROOT/dbt"
REPORTS_DIR="$PROJECT_ROOT/reports/dbt/marts"

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

# ----------------------------------
# MARTS Models
# ----------------------------------
echo "📊 dbt run (marts)"
dbt run --select marts --fail-fast \
  | tee "$REPORTS_DIR/dbt_run_marts_$(date +%Y%m%d_%H%M%S).log"

# ----------------------------------
# MARTS Tests
# ----------------------------------
echo "🧪 dbt test (marts)"
dbt test --select marts \
  | tee "$REPORTS_DIR/dbt_test_marts_$(date +%Y%m%d_%H%M%S).log"

# ----------------------------------
# Docs
# ----------------------------------
echo "📚 Gerando dbt docs"
dbt docs generate \
  | tee "$REPORTS_DIR/dbt_docs_marts_$(date +%Y%m%d_%H%M%S).log"

echo "✅ dbt MARTS finalizado com sucesso"
