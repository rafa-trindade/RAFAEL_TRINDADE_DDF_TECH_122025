#!/usr/bin/env bash
set -e

echo "🚀 Iniciando dbt - CORE (Star Schema)"

PROJECT_ROOT="/home/rafael/app/RAFAEL_TRINDADE_DDF_TECH_122025"
DBT_DIR="$PROJECT_ROOT/dbt"
REPORTS_DIR="$PROJECT_ROOT/reports"

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
# Seeds
# ----------------------------------
echo "🌱 dbt seed (core inputs)"
dbt seed \
  | tee "$REPORTS_DIR/dbt_seed_$(date +%Y%m%d_%H%M%S).log"

# ----------------------------------
# Core Models
# ----------------------------------
echo "📦 dbt run (core)"
dbt run --select core --fail-fast \
  | tee "$REPORTS_DIR/dbt_run_core_$(date +%Y%m%d_%H%M%S).log"

# ----------------------------------
# Core Tests
# ----------------------------------
echo "🧪 dbt test (core)"
dbt test --select core \
  | tee "$REPORTS_DIR/dbt_test_core_$(date +%Y%m%d_%H%M%S).log"

# ----------------------------------
# Docs
# ----------------------------------
echo "📚 Gerando dbt docs"
dbt docs generate \
  | tee "$REPORTS_DIR/dbt_docs_$(date +%Y%m%d_%H%M%S).log"

echo "✅ dbt CORE finalizado com sucesso"
