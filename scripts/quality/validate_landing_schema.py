import os
os.environ["DISABLE_PANDERA_IMPORT_WARNING"] = "True"

from pathlib import Path
from datetime import datetime

import pandas as pd
import pandera.pandas as pa

from scripts.quality.schemas import LANDING_SCHEMAS


# ------------------------------------------------------------
# Report path
# ------------------------------------------------------------
REPORT_PATH = (
    Path(__file__).resolve().parents[2]
    / f"reports/pandera/landing/schema_report.log"
)

REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Validation function
# ------------------------------------------------------------
def validate_landing_schema(
    dataset_name: str,
    parquet_path: Path,
    run_id: str,
) -> None:
    print(f"🔎 Validando schema (Pandera): {dataset_name}")

    df = pd.read_parquet(parquet_path)
    schema = LANDING_SCHEMAS[dataset_name]
    
    rows, cols = df.shape
    status = "UNKNOWN"
    error_msg = "None"

    try:
        schema.validate(df, lazy=True)

        status = "SUCCESS"
        print(f"✅ Schema válido: {dataset_name}")

    except pa.errors.SchemaErrors as exc:
        status = "FAILED"
        error_msg = exc.failure_cases.to_json(orient="records")

        print(f"❌ Schema inválido: {dataset_name}")
        raise

    finally:
            timestamp = datetime.utcnow().isoformat()
            log_entry = (
                f"RUN_ID: {run_id} | "
                f"TIMESTAMP: {timestamp} | "
                f"STATUS: {status} | "
                f"DATASET: {dataset_name} | "
                f"FILE: {parquet_path.name} | "
                f"ROWS: {rows} | "
                f"COLS: {cols} | "
                f"ERRORS: {error_msg}\n"
            )
            
            with REPORT_PATH.open("a", encoding="utf-8") as f:
                f.write(log_entry)