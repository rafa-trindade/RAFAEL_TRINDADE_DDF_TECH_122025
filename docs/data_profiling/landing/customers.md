# Relatório de Profiling: `landing/customers`

### 📦 Volumetria: `landing/customers`
|   qtd_arquivos |   registros |   colunas |   tamanho_comprimido_mib |   tamanho_descomprimido_mib |
|---------------:|------------:|----------:|-------------------------:|----------------------------:|
|              1 |      99.441 |         6 |                     6.69 |                        7.48 |

---

### 🧬 Schema: `landing/customers`
| column_name              | column_type   | null   | key   | default   | extra   |
|:-------------------------|:--------------|:-------|:------|:----------|:--------|
| customer_id              | VARCHAR       | YES    |       |           |         |
| customer_unique_id       | VARCHAR       | YES    |       |           |         |
| customer_zip_code_prefix | BIGINT        | YES    |       |           |         |
| customer_city            | VARCHAR       | YES    |       |           |         |
| customer_state           | VARCHAR       | YES    |       |           |         |
| run_id                   | BIGINT        | YES    |       |           |         |

---

### 📅 Campos de Data: `landing/customers`
#### ✅ Datas com tipagem (DATE / TIMESTAMP)
> ⚠️ Nenhuma coluna DATE ou TIMESTAMP encontrada.

#### ⚠️ Possíveis campos de data/hora sem tipagem (inferido pelo nome)

> Nenhuma coluna com nome sugestivo de data encontrada.


---

### 📊 Estatísticas por Coluna: `landing/customers`
| coluna                   |   distintos |   nulos |   duplicados | pct_nulos   | pct_duplicados   | cardinalidade   |
|:-------------------------|------------:|--------:|-------------:|:------------|:-----------------|:----------------|
| customer_id              |       99441 |       0 |            0 | 0.0%        | 0.0%             | ALTA            |
| customer_unique_id       |       96096 |       0 |         3345 | 0.0%        | 3.36%            | ALTA            |
| customer_zip_code_prefix |       14994 |       0 |        84447 | 0.0%        | 84.92%           | ALTA            |
| customer_city            |        4119 |       0 |        95322 | 0.0%        | 95.86%           | MEDIA           |
| customer_state           |          27 |       0 |        99414 | 0.0%        | 99.97%           | BAIXA           |
| run_id                   |           1 |       0 |        99440 | 0.0%        | 100.0%           | BAIXA           |

---

### 🔟 Distribuição de Valores (Top 10): `landing/customers`
#### Coluna: `customer_id`

| valor                            |   qtd |
|:---------------------------------|------:|
| 4e7b3e00288586ebd08712fdd0374a03 |     1 |
| fd826e7cf63160e536e0908c76c3f441 |     1 |
| 5adf08e34b2e993982a47070956c5c65 |     1 |
| eabebad39a88bb6f5b52376faec28612 |     1 |
| 206f3129c0e4d7d0b9550426023f0a08 |     1 |
| a7c125a0a07b75146167b7f04a7f8e98 |     1 |
| c5c61596a3b6bd0cee5766992c48a9a1 |     1 |
| 154c4ded6991bdfa3cd249d11abf4130 |     1 |
| 2938121a40a20953c43caa8c98787fcb |     1 |
| 237098a64674ae89babdc426746260fc |     1 |

#### Coluna: `customer_unique_id`

| valor                            |   qtd |
|:---------------------------------|------:|
| 8d50f5eadf50201ccdcedfb9e2ac8455 |    17 |
| 3e43e6105506432c953e165fb2acf44c |     9 |
| 1b6c7548a2a1f9037c1fd3ddfed95f33 |     7 |
| 6469f99c1f9dfae7733b25662e7f1782 |     7 |
| ca77025e7201e3b30c44b472ff346268 |     7 |
| 47c1a3033b8b77b3ab6e109eb4d5fdf3 |     6 |
| f0e310a6839dce9de1638e0fe5ab282a |     6 |
| 63cfc61cee11cbe306bff5857d00bfe4 |     6 |
| 12f5d6e1cbf93dafd9dcc19095df0b3d |     6 |
| dc813062e0fc23409cd255f7f53c7074 |     6 |

#### Coluna: `customer_zip_code_prefix`

|   valor |   qtd |
|--------:|------:|
|   22790 |   142 |
|   24220 |   124 |
|   22793 |   121 |
|   24230 |   117 |
|   22775 |   110 |
|   29101 |   101 |
|   13212 |    95 |
|   35162 |    93 |
|   22631 |    89 |
|   38400 |    87 |

#### Coluna: `customer_city`

| valor                 |   qtd |
|:----------------------|------:|
| sao paulo             | 15540 |
| rio de janeiro        |  6882 |
| belo horizonte        |  2773 |
| brasilia              |  2131 |
| curitiba              |  1521 |
| campinas              |  1444 |
| porto alegre          |  1379 |
| salvador              |  1245 |
| guarulhos             |  1189 |
| sao bernardo do campo |   938 |

#### Coluna: `customer_state`

| valor   |   qtd |
|:--------|------:|
| SP      | 41746 |
| RJ      | 12852 |
| MG      | 11635 |
| RS      |  5466 |
| PR      |  5045 |
| SC      |  3637 |
| BA      |  3380 |
| DF      |  2140 |
| ES      |  2033 |
| GO      |  2020 |

#### Coluna: `run_id`

|       valor |   qtd |
|------------:|------:|
| 2.02512e+13 | 99441 |



---

### 📏 Comprimento de Strings: `landing/customers`
#### Coluna: `customer_id`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        32 |        32 |        32 |

#### Coluna: `customer_unique_id`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        32 |        32 |        32 |

#### Coluna: `customer_city`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|         3 |     10.34 |        32 |

#### Coluna: `customer_state`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|         2 |         2 |         2 |



---

