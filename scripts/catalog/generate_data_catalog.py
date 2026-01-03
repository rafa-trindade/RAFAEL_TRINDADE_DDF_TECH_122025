import os
import time
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import errors


BASE_DIR = Path(__file__).resolve().parents[2]
SQL_SCRIPTS_DIR = BASE_DIR / "dbt/models/marts/"
OUTPUT_DIR = BASE_DIR / "docs/data_catalog"

# --------------------------------------------------
# Inicialização do Cliente Gemini
# --------------------------------------------------
load_dotenv(BASE_DIR / ".env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ Erro: GEMINI_API_KEY não encontrada no arquivo .env")

client = genai.Client(api_key=GEMINI_API_KEY)

# --------------------------------------------------
# Prompt com Exemplo Real (Few-Shot)
# --------------------------------------------------
CATALOG_PROMPT = """
Você é um Engenheiro de Analytics especialista em dbt e Governança de Dados.
Sua missão é converter SQLs de models dbt em arquivos de Catálogo de Dados Markdown.

### EXEMPLO DE REFERÊNCIA (SIGA RIGOROSAMENTE ESTE PADRÃO) ###

SQL DE ENTRADA:
```sql
WITH base AS (
    SELECT
        COALESCE(p.product_category_name, 'sem_categoria') AS product_category_name,
        d.ano,
        d.mes,
        f.order_item_id,
        f.total_item_value
    FROM 
        {{ ref('fact_order_items') }} AS f
    JOIN 
        {{ ref('dim_products') }} AS p ON f.product_id = p.product_id
    JOIN 
        {{ ref('dim_date') }} AS d ON f.chave_data = d.chave_data
)

SELECT
    product_category_name,
    ano,
    mes,
    SUM(total_item_value) AS receita_categoria,
    COUNT(order_item_id) AS itens_vendidos,
    ROUND(SUM(total_item_value) / NULLIF(COUNT(order_item_id), 0), 2) AS ticket_medio_categoria
FROM 
    base
GROUP BY product_category_name, ano, mes
ORDER BY ano, mes, receita_categoria DESC

MARKDOWN GERADO (SAÍDA ESPERADA):
# Catálogo de Dados  - `mart_category_growth_monthly`


## Descrição
Tabela analítica que apresenta a **receita mensal por categoria de produto**, permitindo a análise do **crescimento percentual em relação ao mês anterior**.

Cada linha representa o desempenho de uma **categoria de produto em um determinado mês e ano**.


## Granularidade
- Mensal
- Por Categoria de Produto


## Chave lógica
- `product_category_name` 
- `ano`  
- `mes`  


## Dicionário de Campos

### `product_category_name`
- **Descrição:** Nome da categoria do produto.
- **Observação:** Quando o produto não possui categoria, o valor exibido é `sem_categoria`.

### `ano`
- **Descrição:** Ano de referência da receita.

### `mes`
- **Descrição:** Mês de referência da receita.
- **Domínio:** 1 a 12

### `receita_mensal`
- **Descrição:** Valor total da receita da categoria no mês.

### `receita_mes_anterior`
- **Descrição:** Receita da mesma categoria no mês imediatamente anterior.

### `crescimento_percentual`
- **Descrição:** Percentual de crescimento da receita em relação ao mês anterior.
- **Observações:**
  - Pode ser **nulo** quando não existe mês anterior.
  - Pode ser **nulo** quando a receita do mês anterior é zero.
  - Valores negativos indicam queda de receita.


## Regras de Negócio
- A receita é calculada com base no valor total dos itens vendidos.
- O crescimento é calculado apenas quando há receita válida no mês anterior.
- Categorias inexistentes são agrupadas como `sem_categoria`.


## Uso Recomendado
- Análise de crescimento mês a mês (MoM)
- Acompanhamento de performance por categoria
- Dashboards financeiros e comerciais
- Análises de tendência e sazonalidade


## Camada de Dados
- **Tipo:** Data Mart
- **Finalidade:** Análise e visualização


NOME DO MODEL: {model_name} SQL PARA PROCESSAR:
{sql}
"""

# --------------------------------------------------
# Funções de Processamento
# --------------------------------------------------
def read_sql_file(path: Path) -> str:

    return path.read_text(encoding="utf-8")

def generate_markdown(sql: str, model_name: str) -> str:

    prompt = CATALOG_PROMPT.format(sql=sql, model_name=model_name)
    
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest", 
            contents=prompt
        )
        
        if response.text:
            return response.text.strip()
        return "⚠️ Erro: O modelo retornou uma resposta vazia."
        
    except errors.ClientError as e:
        if "429" in str(e):
            print("🕒 Cota atingida. Aguardando 60 segundos...")
            time.sleep(60)
            return generate_markdown(sql, model_name)
        raise e

def save_markdown(content: str, output_path: Path):

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")

# --------------------------------------------------
# ENTRYPOINT
# --------------------------------------------------
def main():
    
    sql_files = list(SQL_SCRIPTS_DIR.rglob("*.sql"))

    if not sql_files:
        print(f"⚠️ Nenhum arquivo SQL encontrado em: {SQL_SCRIPTS_DIR}")
        return

    print(f"🚀 Iniciando geração de catálogo para {len(sql_files)} arquivos encontrados...\n")

    for sql_file in sql_files:
        model_name = sql_file.stem
        print(f"📄 Processando: {sql_file.name} (encontrado em {sql_file.parent.name})")
        
        try:
            sql_content = read_sql_file(sql_file)
            markdown = generate_markdown(sql_content, model_name)
            
            output_file = OUTPUT_DIR / f"{model_name}.md"
            save_markdown(markdown, output_file)
            
            print(f"✅ Salvo em: docs/data_catalog/{output_file.name}")
            
            time.sleep(10) 
            
        except Exception as e:
            print(f"❌ Erro ao processar {model_name}: {e}")

    print(f"\n🎉 Processo finalizado! Todos os arquivos estão em: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()