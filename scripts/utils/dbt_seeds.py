# ------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------
import sys
import os
import requests
from pathlib import Path
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv

# ------------------------------------------------------------------
# PATH SETUP
# ------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

# ------------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------------
load_dotenv(override=True)

API_KEY = os.getenv("INVERTEXTO_API_KEY")

INPUT_CSV = PROJECT_ROOT / "data/landing/csv/olist_orders_dataset.csv"
SEEDS_PATH = PROJECT_ROOT / "dbt/seeds"
SEEDS_PATH.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------
# API FERIADOS (NACIONAL)
# ------------------------------------------------------------------
def get_feriados(year):
    url = f"https://api.invertexto.com/v1/holidays/{year}?token={API_KEY}"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        return {f["date"]: f["name"] for f in data}
    else:
        print(f"Erro ao buscar feriados {year}: {resp.text}")
        return {}

def fetch_feriados(start_year, end_year):
    feriados = {}
    for ano in range(start_year, end_year + 1):
        feriados.update(get_feriados(ano))
    return feriados

# ------------------------------------------------------------------
# GERADOR DIM_DATE DINÂMICO
# ------------------------------------------------------------------
def generate_seed_dim_date(min_date, max_date):
    print(f"📅 Gerando seed_dim_date (Brasil) de {min_date.date()} até {max_date.date()}...")

    feriados = fetch_feriados(start_year=min_date.year, end_year=max_date.year)
    datas = pd.date_range(start=min_date, end=max_date)

    dias_semana_pt = {
        "Monday": "Segunda-feira",
        "Tuesday": "Terça-feira",
        "Wednesday": "Quarta-feira",
        "Thursday": "Quinta-feira",
        "Friday": "Sexta-feira",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }

    df = pd.DataFrame({
        "chave_data": datas.strftime("%Y%m%d").astype(int),
        "data": datas.date,
        "ano": datas.year,
        "mes": datas.month,
        "dia": datas.day,
        "nome_dia_semana": datas.strftime("%A").map(dias_semana_pt),
        "fim_de_semana": (datas.weekday >= 5).astype(int),
        "trimestre": datas.quarter,
        "alta_temporada": (datas.month == 7).astype(int),
        "feriado": datas.strftime("%Y-%m-%d").isin(feriados.keys()).astype(int),
        "nome_feriado": datas.strftime("%Y-%m-%d").map(feriados).fillna("")
    })

    output_path = SEEDS_PATH / "dim_date.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ dim_date.csv gerado com {len(df)} dias.")


# ------------------------------------------------------------------
# DIMENSÃO DE TEMPO
# ------------------------------------------------------------------
def generate_seed_dim_time():
    print("⏰ Gerando seed_dim_time...")

    tempos = pd.date_range("00:00", "23:59", freq="1min").time

    df = pd.DataFrame({
        # 🔑 Minutos desde meia-noite (0–1439)
        "chave_hora": [t.hour * 60 + t.minute for t in tempos],

        "hora_24h": [t.strftime("%H:%M") for t in tempos],
        "hora": [t.hour for t in tempos],
        "minuto": [t.minute for t in tempos],

        "periodo": [
            "Manhã" if 5 <= t.hour <= 11 else
            "Tarde" if 12 <= t.hour <= 17 else
            "Noite" if 18 <= t.hour <= 23 else
            "Madrugada"
            for t in tempos
        ]
    })

    df.to_csv(SEEDS_PATH / "dim_time.csv", index=False)
    print("✅ dim_time.csv gerado.")

# ------------------------------------------------------------------
# PROCESSAMENTO E IDENTIFICAÇÃO DE RANGE
# ------------------------------------------------------------------
def process_data_and_seeds():
    if not INPUT_CSV.exists():
        print(f"❌ ERRO: Arquivo {INPUT_CSV} não encontrado!")
        return

    print(f"📖 Analisando datas em: {INPUT_CSV.name}")

    col_ref = 'order_purchase_timestamp'
    df_orders = pd.read_csv(INPUT_CSV, usecols=[col_ref])
    
    df_orders[col_ref] = pd.to_datetime(df_orders[col_ref], errors='coerce')
    df_orders = df_orders.dropna(subset=[col_ref])
    
    if df_orders.empty:
        print("❌ ERRO: A coluna de data está vazia ou mal formatada.")
        return

    min_date = df_orders[col_ref].min()
    max_date = df_orders[col_ref].max()

    generate_seed_dim_date(min_date, max_date)
    generate_seed_dim_time()

# ------------------------------------------------------------------
# ENTRYPOINT
# ------------------------------------------------------------------
if __name__ == "__main__":
    process_data_and_seeds()