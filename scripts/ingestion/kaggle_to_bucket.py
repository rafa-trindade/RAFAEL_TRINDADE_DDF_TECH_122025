# ------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------
import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime, timezone

import pandas as pd
from dotenv import load_dotenv

# ------------------------------------------------------------------
# PATH SETUP
# ------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(PROJECT_ROOT))

from config.data_connections import get_s3_client
from scripts.utils.lake_retetions import cleanup_old_runs

# ------------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------------
load_dotenv(override=True)

os.environ["KAGGLE_CONFIG_DIR"] = str(
    (PROJECT_ROOT / "config").resolve()
)

DATASET = "olistbr/brazilian-ecommerce"
BUCKET_NAME = "kaggle"

# ------------------------------------------------------------------
# DATASETS SELECIONADOS
# ------------------------------------------------------------------
ALLOWED_DATASETS = {
    "olist_products_dataset",
    "olist_order_items_dataset",
    "olist_orders_dataset",
    "olist_customers_dataset",
    "olist_geolocation_dataset",
}

# ------------------------------------------------------------------
# VERSIONAMENTO
# ------------------------------------------------------------------
RUN_ID = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

LANDING_BASE_PATH = "olist/landing/"
LANDING_PATH = f"{LANDING_BASE_PATH}run_id={RUN_ID}/"

MAX_LANDING_RUNS = int(os.getenv("LANDING_MAX_RUNS", 3))

# ------------------------------------------------------------------
# LOCAL PATHS
# ------------------------------------------------------------------
RAW_DIR = PROJECT_ROOT / "data/landing/olist/raw"
PARQUET_DIR = PROJECT_ROOT / "data/landing/olist/parquet"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PARQUET_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------
# KAGGLE DOWNLOAD
# ------------------------------------------------------------------
def download_kaggle_dataset():
    print("📥 Baixando dataset do Kaggle...")

    subprocess.run(
        [
            "kaggle",
            "datasets",
            "download",
            "-d",
            DATASET,
            "-p",
            str(RAW_DIR),
            "--unzip",
        ],
        check=True,
    )

    print("✅ Download concluído")


# ------------------------------------------------------------------
# LIMPEZA DE DIRETÓRIO PARQUET
# ------------------------------------------------------------------
def clean_parquet_dir():
    print("🧹 Limpando diretório de Parquet...")

    for file in PARQUET_DIR.glob("*.parquet"):
        file.unlink()


# ------------------------------------------------------------------
# CSV → Parquet (somente selecionados)
# ------------------------------------------------------------------
def csv_to_parquet():
    print("🔄 Convertendo CSV para Parquet (datasets permitidos)...")

    for csv_file in RAW_DIR.glob("*.csv"):
        dataset_name = csv_file.stem

        if dataset_name not in ALLOWED_DATASETS:
            print(f"  - Ignorado: {csv_file.name}")
            continue

        parquet_file = PARQUET_DIR / f"{dataset_name}.parquet"

        print(f"  - {csv_file.name} → {parquet_file.name}")

        df = pd.read_csv(csv_file)

        df.to_parquet(
            parquet_file,
            engine="pyarrow",
            index=False,
        )

    print("✅ Conversão concluída")


# ------------------------------------------------------------------
# UPLOAD LANDING (somente selecionados)
# ------------------------------------------------------------------
def upload_to_minio():
    print("☁️ Enviando Parquets permitidos para o MinIO (Landing)...")

    s3 = get_s3_client()

    for parquet_file in PARQUET_DIR.glob("*.parquet"):
        dataset_name = parquet_file.stem

        if dataset_name not in ALLOWED_DATASETS:
            print(f"  - Ignorado no upload: {parquet_file.name}")
            continue

        object_key = f"{LANDING_PATH}{parquet_file.name}"

        print(f"  - s3://{BUCKET_NAME}/{object_key}")

        s3.upload_file(
            Filename=str(parquet_file),
            Bucket=BUCKET_NAME,
            Key=object_key,
        )

    print("✅ Upload concluído")


# ------------------------------------------------------------------
# PIPELINE
# ------------------------------------------------------------------
def run():
    print("🚀 Iniciando Landing: Olist (Kaggle)")
    print(f"🧾 run_id = {RUN_ID}")
    print(f"🧹 Política de retenção: manter {MAX_LANDING_RUNS} runs")

    download_kaggle_dataset()

    clean_parquet_dir()
    csv_to_parquet()
    upload_to_minio()

    print("🧹 Aplicando política de retenção...")
    cleanup_old_runs(
        bucket=BUCKET_NAME,
        base_path=LANDING_BASE_PATH,
        max_runs=MAX_LANDING_RUNS,
        protect_run_id=RUN_ID,
    )

    print("🏁 Landing Olist finalizada com sucesso!")


# ------------------------------------------------------------------
# ENTRYPOINT
# ------------------------------------------------------------------
if __name__ == "__main__":
    run()
