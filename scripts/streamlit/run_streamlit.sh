#!/usr/bin/env bash
set -e

echo "🚀 Iniciando Streamlit..."

# ----------------------------------
# Config
# ----------------------------------
APP_DIR="/home/rafael/app/RAFAEL_TRINDADE_DDF_TECH_122025"
STREAMLIT_APP="data_app/streamlit.py"
VENV_PATH="$APP_DIR/.venv"
PORT=8501

# ----------------------------------
# Virtualenv
# ----------------------------------
cd "$APP_DIR"

if [ -d "$VENV_PATH" ]; then
  echo "🐍 Ativando virtualenv"
  source "$VENV_PATH/bin/activate"
else
  echo "⚠️ Virtualenv não encontrado em $VENV_PATH"
fi

# ----------------------------------
# Run
# ----------------------------------
nohup streamlit run "$STREAMLIT_APP" \
  --server.port "$PORT" \
  --server.address 0.0.0.0 \
  > scripts/streamlit/logs/streamlit.log 2>&1 &

echo "✅ Streamlit rodando na porta $PORT"
