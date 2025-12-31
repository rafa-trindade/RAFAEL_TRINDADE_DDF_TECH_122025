# Relatório de Profiling: `landing/geolocation`

### 📦 Volumetria: `landing/geolocation`
|   qtd_arquivos | registros   |   colunas |   tamanho_comprimido_mib |   tamanho_descomprimido_mib |
|---------------:|:------------|----------:|-------------------------:|----------------------------:|
|              1 | 1.000.163   |         6 |                    16.55 |                       17.81 |

---

### 🧬 Schema: `landing/geolocation`
| column_name                 | column_type   | null   | key   | default   | extra   |
|:----------------------------|:--------------|:-------|:------|:----------|:--------|
| geolocation_zip_code_prefix | BIGINT        | YES    |       |           |         |
| geolocation_lat             | DOUBLE        | YES    |       |           |         |
| geolocation_lng             | DOUBLE        | YES    |       |           |         |
| geolocation_city            | VARCHAR       | YES    |       |           |         |
| geolocation_state           | VARCHAR       | YES    |       |           |         |
| run_id                      | BIGINT        | YES    |       |           |         |

---

### 📅 Campos de Data: `landing/geolocation`
#### ✅ Datas com tipagem (DATE / TIMESTAMP)
> ⚠️ Nenhuma coluna DATE ou TIMESTAMP encontrada.

#### ⚠️ Possíveis campos de data/hora sem tipagem (inferido pelo nome)

> Nenhuma coluna com nome sugestivo de data encontrada.


---

### 📊 Estatísticas por Coluna: `landing/geolocation`
| coluna                      |   distintos |   nulos |   duplicados | pct_nulos   | pct_duplicados   | cardinalidade   |
|:----------------------------|------------:|--------:|-------------:|:------------|:-----------------|:----------------|
| geolocation_zip_code_prefix |       19015 |       0 |       981148 | 0.0%        | 98.1%            | MEDIA           |
| geolocation_lat             |      717360 |       0 |       282803 | 0.0%        | 28.28%           | ALTA            |
| geolocation_lng             |      717613 |       0 |       282550 | 0.0%        | 28.25%           | ALTA            |
| geolocation_city            |        8011 |       0 |       992152 | 0.0%        | 99.2%            | MEDIA           |
| geolocation_state           |          27 |       0 |      1000136 | 0.0%        | 100.0%           | BAIXA           |
| run_id                      |           1 |       0 |      1000162 | 0.0%        | 100.0%           | BAIXA           |

---

### 🔟 Distribuição de Valores (Top 10): `landing/geolocation`
#### Coluna: `geolocation_zip_code_prefix`

|   valor |   qtd |
|--------:|------:|
|   24220 |  1146 |
|   24230 |  1102 |
|   38400 |   965 |
|   35500 |   907 |
|   11680 |   879 |
|   22631 |   832 |
|   30140 |   810 |
|   11740 |   788 |
|   38408 |   773 |
|   28970 |   743 |

#### Coluna: `geolocation_lat`

|    valor |   qtd |
|---------:|------:|
| -27.1021 |   314 |
| -23.4959 |   190 |
| -23.506  |   141 |
| -23.4906 |   127 |
| -23.0055 |   102 |
| -23.0046 |    89 |
| -22.9659 |    89 |
| -15.8415 |    85 |
| -23.5372 |    83 |
| -23.4919 |    82 |

#### Coluna: `geolocation_lng`

|    valor |   qtd |
|---------:|------:|
| -48.6296 |   314 |
| -46.8747 |   190 |
| -46.7174 |   141 |
| -46.869  |   127 |
| -43.376  |   102 |
| -46.5463 |    91 |
| -43.39   |    89 |
| -43.3199 |    89 |
| -48.024  |    85 |
| -46.594  |    83 |

#### Coluna: `geolocation_city`

| valor                 |    qtd |
|:----------------------|-------:|
| sao paulo             | 135800 |
| rio de janeiro        |  62151 |
| belo horizonte        |  27805 |
| são paulo             |  24918 |
| curitiba              |  16593 |
| porto alegre          |  13521 |
| salvador              |  11865 |
| guarulhos             |  11340 |
| brasilia              |  10470 |
| sao bernardo do campo |   8112 |

#### Coluna: `geolocation_state`

| valor   |    qtd |
|:--------|-------:|
| SP      | 404268 |
| MG      | 126336 |
| RJ      | 121169 |
| RS      |  61851 |
| PR      |  57859 |
| SC      |  38328 |
| BA      |  36045 |
| GO      |  20139 |
| ES      |  16748 |
| PE      |  16432 |

#### Coluna: `run_id`

|       valor |         qtd |
|------------:|------------:|
| 2.02512e+13 | 1.00016e+06 |



---

### 📏 Comprimento de Strings: `landing/geolocation`
#### Coluna: `geolocation_city`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|         2 |     10.47 |        38 |

#### Coluna: `geolocation_state`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|         2 |         2 |         2 |



---

