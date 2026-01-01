#!/usr/bin/env bash

PID=$(ps aux | grep "streamlit run data_app/streamlit.py" | grep -v grep | awk '{print $2}')

if [ -z "$PID" ]; then
  echo "❌ Streamlit não está rodando"
else
  kill -9 "$PID"
  echo "🛑 Streamlit parado (PID $PID)"
fi