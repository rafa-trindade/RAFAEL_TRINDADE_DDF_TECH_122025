# ------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------
import os
import sys
from typing import List
from pathlib import Path

import duckdb
from dotenv import load_dotenv

# ------------------------------------------------------------------
# PATH SETUP
# ------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(PROJECT_ROOT))

from config.data_connections import (
    get_s3_client,
    get_duckdb_connection,
)

# ------------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------------
load_dotenv(override=True)

BUCKET_NAME = "kaggle"
LANDING_BASE_PREFIX = "olist/landing/"
POSTGRES_SCHEMA = "raw"

# ------------------------------------------------------------------
# S3 HELPERS
# ------------------------------------------------------------------
def get_latest_run_id() -> str:
    """
    Retorna o run_id mais recente presente no bucket S3.
    """
    s3 = get_s3_client()

    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix=LANDING_BASE_PREFIX,
        Delimiter="/",
    )

    run_ids = [
        prefix["Prefix"]
        .rstrip("/")
        .split("/")[-1]
        .replace("run_id=", "")
        for prefix in response.get("CommonPrefixes", [])
        if "run_id=" in prefix["Prefix"]
    ]

    if not run_ids:
        raise RuntimeError(
            f"Nenhum run_id encontrado em s3://{BUCKET_NAME}/{LANDING_BASE_PREFIX}"
        )

    latest_run_id = sorted(run_ids)[-1]
    print(f"🧾 Último run_id encontrado: {latest_run_id}")

    return latest_run_id


def list_parquet_files(run_id: str) -> List[str]:
    """
    Lista todos os arquivos Parquet de um run_id específico.
    """
    s3 = get_s3_client()
    prefix = f"{LANDING_BASE_PREFIX}run_id={run_id}/"

    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix=prefix,
    )

    files = [
        obj["Key"]
        for obj in response.get("Contents", [])
        if obj["Key"].endswith(".parquet")
    ]

    return files


# ------------------------------------------------------------------
# POSTGRES (DUCKDB)
# ------------------------------------------------------------------
def attach_postgres(con: duckdb.DuckDBPyConnection):
    """
    Conecta o DuckDB ao PostgreSQL usando ATTACH.
    """
    postgres_url = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DB')}"
    )

    con.execute("INSTALL postgres; LOAD postgres;")
    con.execute("INSTALL httpfs; LOAD httpfs;")

    con.execute(
        f"ATTACH '{postgres_url}' AS postgres (TYPE POSTGRES);"
    )


def ensure_raw_schema(con: duckdb.DuckDBPyConnection):
    """
    Garante que o schema RAW exista no PostgreSQL.
    """
    con.execute(
        f"CREATE SCHEMA IF NOT EXISTS postgres.{POSTGRES_SCHEMA};"
    )


# ------------------------------------------------------------------
# LOAD LOGIC
# ------------------------------------------------------------------
def load_latest_run_to_postgres():
    """
    Pipeline:
    S3 (Landing) → PostgreSQL (Raw)
    """
    print("🚚 Iniciando carga: Landing (S3) → Raw (PostgreSQL)")

    run_id = get_latest_run_id()
    parquet_files = list_parquet_files(run_id)

    if not parquet_files:
        raise RuntimeError(
            f"Nenhum arquivo Parquet encontrado para run_id={run_id}"
        )

    con = get_duckdb_connection(
        memory_limit="6GB",
        threads=5,
    )

    try:
        attach_postgres(con)
        ensure_raw_schema(con)

        for key in parquet_files:
            filename = os.path.basename(key).replace(".parquet", "")

            table_name = (
                filename
                .replace("olist_", "")
                .replace("_dataset", "")
                .replace("_table", "")
            )

            s3_path = f"s3://{BUCKET_NAME}/{key}"

            print(f"  - 📥 Carregando tabela: {table_name}")

            con.execute(f"""
                CREATE OR REPLACE TABLE postgres.{POSTGRES_SCHEMA}.{table_name} AS
                SELECT
                    *,
                    '{run_id}' AS run_id,
                    current_timestamp AS ingested_at
                FROM read_parquet('{s3_path}');
            """)

        print(
            f"✅ Sucesso: {len(parquet_files)} tabelas carregadas "
            f"no schema '{POSTGRES_SCHEMA}'"
        )

    finally:
        con.close()


# ------------------------------------------------------------------
# PIPELINE
# ------------------------------------------------------------------
def run():

    print("🚀 Iniciando pipeline: Landing → Raw")
    load_latest_run_to_postgres()
    print("🏁 Pipeline finalizado com sucesso!")


# ------------------------------------------------------------------
# ENTRYPOINT
# ------------------------------------------------------------------
if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"❌ Erro durante execução do pipeline: {e}")
        raise
