# %%
# PATH SETUP #####################################
##################################################
from pathlib import Path
import sys

PROJECT_ROOT = Path().resolve()
while PROJECT_ROOT.name != "scripts":
    PROJECT_ROOT = PROJECT_ROOT.parent
PROJECT_ROOT = PROJECT_ROOT.parent

sys.path.insert(0, str(PROJECT_ROOT))


# %%
# IMPORTS E CONFIGURAÇÃO #########################
##################################################
from config.data_connections import get_duckdb_connection
from scripts.utils.profiling_utils import (
    init_md_report,
    print_and_save_md,
    df_to_md,
)

con = get_duckdb_connection(
    memory_limit="2GB",
    threads=4,
)

PARQUET_GLOB = (
    "s3://kaggle/olist/landing/"
    "run_id=*/olist_geolocation_dataset.parquet"
)

latest_run_id = con.execute("""
    SELECT run_id
    FROM read_parquet(
        ?, 
        hive_partitioning=1
    )
    ORDER BY run_id DESC
    LIMIT 1
""", [PARQUET_GLOB]).fetchone()[0]

run_id_path = (
    str(latest_run_id)[:8] + "_" + str(latest_run_id)[8:]
)

md_file = init_md_report(
    report_filename="geolocation.md",
    dataset_name="landing/geolocation",
    layer="landing",
)

# %%
# VOLUMETRIA ####################################
##################################################
md = "### 📦 Volumetria: `landing/geolocation`\n"

try:
    df_files = con.execute("""
        SELECT
            COUNT(DISTINCT file_name) AS qtd_arquivos,
            SUM(total_compressed_size) AS tamanho_comprimido_bytes,
            SUM(total_uncompressed_size) AS tamanho_descomprimido_bytes
        FROM parquet_metadata(?)
        WHERE file_name LIKE ?
    """, [
        PARQUET_GLOB,
        f"%run_id={run_id_path}%"
    ]).df()

    df_files["tamanho_comprimido_mib"] = (
        df_files["tamanho_comprimido_bytes"] / 1024 / 1024
    ).round(2)

    df_files["tamanho_descomprimido_mib"] = (
        df_files["tamanho_descomprimido_bytes"] / 1024 / 1024
    ).round(2)

    total_registros = con.execute("""
        SELECT COUNT(*)
        FROM read_parquet(
            ?, 
            hive_partitioning=1
        )
        WHERE run_id = ?
    """, [PARQUET_GLOB, latest_run_id]).fetchone()[0]

    total_colunas = con.execute("""
        SELECT COUNT(*)
        FROM (
            DESCRIBE
            SELECT *
            FROM read_parquet(
                ?, 
                hive_partitioning=1
            )
            WHERE run_id = ?
        )
    """, [PARQUET_GLOB, latest_run_id]).fetchone()[0]

    df_files["registros"] = f"{total_registros:,}".replace(",", ".")
    df_files["colunas"] = total_colunas

    md += df_files[
        [
            "qtd_arquivos",
            "registros",
            "colunas",
            "tamanho_comprimido_mib",
            "tamanho_descomprimido_mib",
        ]
    ].to_markdown(index=False)

except Exception:
    md += "> ⚠️ Não há arquivos Parquet disponíveis para análise de volume."

print_and_save_md(md, md_file)


# %% 
# SCHEMA #########################################
##################################################
md = "### 🧬 Schema: `landing/geolocation`\n"

df_schema = con.execute("""
    DESCRIBE
    SELECT *
    FROM read_parquet(
        ?, 
        hive_partitioning=1
    )
    WHERE run_id = ?
""", [PARQUET_GLOB, latest_run_id]).df()

md += df_schema.to_markdown(index=False)

print_and_save_md(md, md_file)



# %%  
# CAMPOS DATE/TIME ###############################
##################################################
md = "### 📅 Campos de Data: `landing/geolocation`\n"

date_cols_typed = df_schema[
    df_schema["column_type"].str.contains("DATE|TIMESTAMP", case=False, na=False)
]["column_name"].tolist()

date_name_patterns = r"(?:^|_)(date|dt|data|dat|safra|hor|timestamp)(?:$|_)"

date_cols_by_name = df_schema[
    df_schema["column_name"].str.contains(date_name_patterns, case=False, na=False)
]["column_name"].tolist()

date_cols_suspect = sorted(set(date_cols_by_name) - set(date_cols_typed))

# DATAS TIPADAS
md += "#### ✅ Datas com tipagem (DATE / TIMESTAMP)\n"

if not date_cols_typed:
    md += "> ⚠️ Nenhuma coluna DATE ou TIMESTAMP encontrada.\n\n"
else:
    for col in date_cols_typed:
        md += f"**Coluna:** `{col}`\n\n"

        df_datas = con.execute("""
            SELECT
                MIN("{col}") AS min_data,
                MAX("{col}") AS max_data
            FROM read_parquet(
                ?, 
                hive_partitioning=1
            )
            WHERE run_id = ?
        """.format(col=col), [PARQUET_GLOB, latest_run_id]).df()

        md += df_datas.to_markdown(index=False)
        md += "\n"

# POSSÍVEIS DATAS
md += "#### ⚠️ Possíveis campos de data/hora sem tipagem (inferido pelo nome)\n\n"

if not date_cols_suspect:
    md += "> Nenhuma coluna com nome sugestivo de data encontrada.\n"
else:
    for col in date_cols_suspect:
        md += f"- `{col}`\n"

print_and_save_md(md, md_file)


# %% 
# ESTATÍSTICA POR COLUNA #########################
##################################################
md = "### 📊 Estatísticas por Coluna: `landing/geolocation`\n"

cols = df_schema["column_name"].tolist()
selects = []

for col in cols:
    selects.append(f"""
        SELECT
            '{col}' AS coluna,
            COUNT(DISTINCT "{col}") AS distintos,
            COUNT(*) FILTER (WHERE "{col}" IS NULL) AS nulos,
            COUNT(*) - COUNT(DISTINCT "{col}") AS duplicados,
            ROUND(COUNT(*) FILTER (WHERE "{col}" IS NULL) * 100.0 / COUNT(*), 2) || '%' AS pct_nulos,
            ROUND((COUNT(*) - COUNT(DISTINCT "{col}")) * 100.0 / COUNT(*), 2) || '%' AS pct_duplicados,
            CASE
                WHEN COUNT(DISTINCT "{col}") <= 0.001 * {total_registros} THEN 'BAIXA'
                WHEN COUNT(DISTINCT "{col}") <= 0.05 * {total_registros} THEN 'MEDIA'
                ELSE 'ALTA'
            END AS cardinalidade
        FROM read_parquet(
            '{PARQUET_GLOB}',
            hive_partitioning=1
        )
        WHERE run_id = {latest_run_id}
    """)

sql_column_statistics = " UNION ALL ".join(selects)
df_column_statistics = con.execute(sql_column_statistics).df()

md += df_column_statistics.to_markdown(index=False)

print_and_save_md(md, md_file)



# %%  
# DISTRIBUIÇÃO POR VALORES (TOP 10) ##############
##################################################
md = "### 🔟 Distribuição de Valores (Top 10): `landing/geolocation`\n"

for col in df_column_statistics["coluna"]:
    md += f"#### Coluna: `{col}`\n\n"

    df_top10 = con.execute(f"""
        SELECT
            "{col}" AS valor,
            COUNT(*) AS qtd
        FROM read_parquet(
            '{PARQUET_GLOB}',
            hive_partitioning=1
        )
        WHERE run_id = {latest_run_id}
        GROUP BY "{col}"
        ORDER BY qtd DESC
        LIMIT 10
    """).df()

    md += df_top10.to_markdown(index=False)
    md += "\n\n"

print_and_save_md(md, md_file)



# %% 
# STRINGS: MED, MIN, MÁX #########################
##################################################
md = "### 📏 Comprimento de Strings: `landing/geolocation`\n"

string_cols = df_schema[
    df_schema["column_type"].str.contains("VARCHAR|STRING", case=False, na=False)
]["column_name"].tolist()

if not string_cols:
    md += "> ⚠️ Nenhuma coluna do tipo STRING ou VARCHAR encontrada.\n"
else:
    for col in string_cols:
        md += f"#### Coluna: `{col}`\n"

        df_str_len = con.execute(f"""
            SELECT
                MIN(LENGTH("{col}")) AS min_len,
                ROUND(AVG(LENGTH("{col}")), 2) AS avg_len,
                MAX(LENGTH("{col}")) AS max_len
            FROM read_parquet(
                '{PARQUET_GLOB}',
                hive_partitioning=1
            )
            WHERE run_id = {latest_run_id}
              AND "{col}" IS NOT NULL
        """).df()

        md += df_to_md(df_str_len)
        md += "\n\n"

print_and_save_md(md, md_file)
