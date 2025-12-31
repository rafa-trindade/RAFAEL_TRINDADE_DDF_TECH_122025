# Relatório de Profiling: `landing/products`

### 📦 Volumetria: `landing/products`
|   qtd_arquivos |   registros |   colunas |   tamanho_comprimido_mib |   tamanho_descomprimido_mib |
|---------------:|------------:|----------:|-------------------------:|----------------------------:|
|              1 |      32.951 |        10 |                     1.34 |                        1.49 |

---

### 🧬 Schema: `landing/products`
| column_name                | column_type   | null   | key   | default   | extra   |
|:---------------------------|:--------------|:-------|:------|:----------|:--------|
| product_id                 | VARCHAR       | YES    |       |           |         |
| product_category_name      | VARCHAR       | YES    |       |           |         |
| product_name_lenght        | DOUBLE        | YES    |       |           |         |
| product_description_lenght | DOUBLE        | YES    |       |           |         |
| product_photos_qty         | DOUBLE        | YES    |       |           |         |
| product_weight_g           | DOUBLE        | YES    |       |           |         |
| product_length_cm          | DOUBLE        | YES    |       |           |         |
| product_height_cm          | DOUBLE        | YES    |       |           |         |
| product_width_cm           | DOUBLE        | YES    |       |           |         |
| run_id                     | BIGINT        | YES    |       |           |         |

---

### 📅 Campos de Data: `landing/products`
#### ✅ Datas com tipagem (DATE / TIMESTAMP)
> ⚠️ Nenhuma coluna DATE ou TIMESTAMP encontrada.

#### ⚠️ Possíveis campos de data/hora sem tipagem (inferido pelo nome)

> Nenhuma coluna com nome sugestivo de data encontrada.


---

### 📊 Estatísticas por Coluna: `landing/products`
| coluna                     |   distintos |   nulos |   duplicados | pct_nulos   | pct_duplicados   | cardinalidade   |
|:---------------------------|------------:|--------:|-------------:|:------------|:-----------------|:----------------|
| product_id                 |       32951 |       0 |            0 | 0.0%        | 0.0%             | ALTA            |
| product_category_name      |          73 |     610 |        32878 | 1.85%       | 99.78%           | MEDIA           |
| product_name_lenght        |          66 |     610 |        32885 | 1.85%       | 99.8%            | MEDIA           |
| product_description_lenght |        2960 |     610 |        29991 | 1.85%       | 91.02%           | ALTA            |
| product_photos_qty         |          19 |     610 |        32932 | 1.85%       | 99.94%           | BAIXA           |
| product_weight_g           |        2204 |       2 |        30747 | 0.01%       | 93.31%           | ALTA            |
| product_length_cm          |          99 |       2 |        32852 | 0.01%       | 99.7%            | MEDIA           |
| product_height_cm          |         102 |       2 |        32849 | 0.01%       | 99.69%           | MEDIA           |
| product_width_cm           |          95 |       2 |        32856 | 0.01%       | 99.71%           | MEDIA           |
| run_id                     |           1 |       0 |        32950 | 0.0%        | 100.0%           | BAIXA           |

---

### 🔟 Distribuição de Valores (Top 10): `landing/products`
#### Coluna: `product_id`

| valor                            |   qtd |
|:---------------------------------|------:|
| 3aa071139cb16b67ca9e5dea641aaa2f |     1 |
| 96bd76ec8810374ed1b65e291975717f |     1 |
| 9dc1a7de274444849c219cff195d0b71 |     1 |
| 2548af3e6e77a690cf3eb6368e9ab61e |     1 |
| 8c92109888e8cdf9d66dc7e463025574 |     1 |
| eb31436580a610f202c859463d8c7415 |     1 |
| f53103a77d9cf245e579ea37e5ec51f0 |     1 |
| 8b41fbc2b984a12030090112324d1bc4 |     1 |
| c78b767da00efb70c1bcccab87c28cd5 |     1 |
| e1d1d22e9f8122a4ec1533b032c12562 |     1 |

#### Coluna: `product_category_name`

| valor                  |   qtd |
|:-----------------------|------:|
| cama_mesa_banho        |  3029 |
| esporte_lazer          |  2867 |
| moveis_decoracao       |  2657 |
| beleza_saude           |  2444 |
| utilidades_domesticas  |  2335 |
| automotivo             |  1900 |
| informatica_acessorios |  1639 |
| brinquedos             |  1411 |
| relogios_presentes     |  1329 |
| telefonia              |  1134 |

#### Coluna: `product_name_lenght`

|   valor |   qtd |
|--------:|------:|
|      60 |  2182 |
|      59 |  2025 |
|      58 |  1887 |
|      57 |  1719 |
|      55 |  1683 |
|      56 |  1675 |
|      54 |  1439 |
|      53 |  1330 |
|      52 |  1259 |
|      50 |  1039 |

#### Coluna: `product_description_lenght`

|   valor |   qtd |
|--------:|------:|
|     nan |   610 |
|     404 |    94 |
|     729 |    86 |
|     703 |    66 |
|     651 |    66 |
|     184 |    65 |
|     236 |    65 |
|     303 |    63 |
|     352 |    62 |
|     375 |    60 |

#### Coluna: `product_photos_qty`

|   valor |   qtd |
|--------:|------:|
|       1 | 16489 |
|       2 |  6263 |
|       3 |  3860 |
|       4 |  2428 |
|       5 |  1484 |
|       6 |   968 |
|     nan |   610 |
|       7 |   343 |
|       8 |   192 |
|       9 |   105 |

#### Coluna: `product_weight_g`

|   valor |   qtd |
|--------:|------:|
|     200 |  2084 |
|     300 |  1561 |
|     150 |  1259 |
|     400 |  1206 |
|     100 |  1188 |
|     500 |  1112 |
|     250 |  1001 |
|     600 |   957 |
|     350 |   832 |
|     700 |   748 |

#### Coluna: `product_length_cm`

|   valor |   qtd |
|--------:|------:|
|      16 |  5520 |
|      20 |  2816 |
|      30 |  2029 |
|      18 |  1502 |
|      25 |  1387 |
|      17 |  1310 |
|      19 |  1270 |
|      40 |  1224 |
|      22 |   972 |
|      35 |   968 |

#### Coluna: `product_height_cm`

|   valor |   qtd |
|--------:|------:|
|      10 |  2548 |
|      15 |  2022 |
|      20 |  1991 |
|      16 |  1595 |
|      11 |  1551 |
|       5 |  1529 |
|      12 |  1522 |
|       8 |  1467 |
|       2 |  1357 |
|       7 |  1235 |

#### Coluna: `product_width_cm`

|   valor |   qtd |
|--------:|------:|
|      11 |  3718 |
|      20 |  3053 |
|      16 |  2808 |
|      15 |  2393 |
|      30 |  1786 |
|      12 |  1536 |
|      25 |  1329 |
|      14 |  1264 |
|      13 |  1133 |
|      17 |  1118 |

#### Coluna: `run_id`

|       valor |   qtd |
|------------:|------:|
| 2.02512e+13 | 32951 |



---

### 📏 Comprimento de Strings: `landing/products`
#### Coluna: `product_id`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        32 |        32 |        32 |

#### Coluna: `product_category_name`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|         3 |     14.96 |        46 |



---

