# Relatório de Profiling: `landing/order_items`

### 📦 Volumetria: `landing/order_items`
|   qtd_arquivos |   registros |   colunas |   tamanho_comprimido_mib |   tamanho_descomprimido_mib |
|---------------:|------------:|----------:|-------------------------:|----------------------------:|
|              1 |      112.65 |         8 |                     6.25 |                        8.81 |

---

### 🧬 Schema: `landing/order_items`
| column_name         | column_type   | null   | key   | default   | extra   |
|:--------------------|:--------------|:-------|:------|:----------|:--------|
| order_id            | VARCHAR       | YES    |       |           |         |
| order_item_id       | BIGINT        | YES    |       |           |         |
| product_id          | VARCHAR       | YES    |       |           |         |
| seller_id           | VARCHAR       | YES    |       |           |         |
| shipping_limit_date | VARCHAR       | YES    |       |           |         |
| price               | DOUBLE        | YES    |       |           |         |
| freight_value       | DOUBLE        | YES    |       |           |         |
| run_id              | BIGINT        | YES    |       |           |         |

---

### 📅 Campos de Data: `landing/order_items`
#### ✅ Datas com tipagem (DATE / TIMESTAMP)
> ⚠️ Nenhuma coluna DATE ou TIMESTAMP encontrada.

#### ⚠️ Possíveis campos de data/hora sem tipagem (inferido pelo nome)

- `shipping_limit_date`


---

### 📊 Estatísticas por Coluna: `landing/order_items`
| coluna              |   distintos |   nulos |   duplicados | pct_nulos   | pct_duplicados   | cardinalidade   |
|:--------------------|------------:|--------:|-------------:|:------------|:-----------------|:----------------|
| order_id            |       98666 |       0 |        13984 | 0.0%        | 12.41%           | ALTA            |
| order_item_id       |          21 |       0 |       112629 | 0.0%        | 99.98%           | BAIXA           |
| product_id          |       32951 |       0 |        79699 | 0.0%        | 70.75%           | ALTA            |
| seller_id           |        3095 |       0 |       109555 | 0.0%        | 97.25%           | MEDIA           |
| shipping_limit_date |       93318 |       0 |        19332 | 0.0%        | 17.16%           | ALTA            |
| price               |        5968 |       0 |       106682 | 0.0%        | 94.7%            | ALTA            |
| freight_value       |        6999 |       0 |       105651 | 0.0%        | 93.79%           | ALTA            |
| run_id              |           1 |       0 |       112649 | 0.0%        | 100.0%           | BAIXA           |

---

### 🔟 Distribuição de Valores (Top 10): `landing/order_items`
#### Coluna: `order_id`

| valor                            |   qtd |
|:---------------------------------|------:|
| 8272b63d03f5f79c56e9e4120aec44ef |    21 |
| ab14fdcfbe524636d65ee38360e22ce8 |    20 |
| 1b15974a0141d54e36626dca3fdc731a |    20 |
| 428a2f660dc84138d969ccd69a0ab6d5 |    15 |
| 9ef13efd6949e4573a18964dd1bbe7f5 |    15 |
| 9bdc4d4c71aa1de4606060929dee888c |    14 |
| 73c8ab38f07dc94389065f7eba4f297a |    14 |
| 37ee401157a3a0b28c9c6d0ed8c3b24b |    13 |
| 3a213fcdfe7d98be74ea0dc05a8b31ae |    12 |
| 637617b3ffe9e2f7a2411243829226d0 |    12 |

#### Coluna: `order_item_id`

|   valor |   qtd |
|--------:|------:|
|       1 | 98666 |
|       2 |  9803 |
|       3 |  2287 |
|       4 |   965 |
|       5 |   460 |
|       6 |   256 |
|       7 |    58 |
|       8 |    36 |
|       9 |    28 |
|      10 |    25 |

#### Coluna: `product_id`

| valor                            |   qtd |
|:---------------------------------|------:|
| aca2eb7d00ea1a7b8ebd4e68314663af |   527 |
| 99a4788cb24856965c36a24e339b6058 |   488 |
| 422879e10f46682990de24d770e7f83d |   484 |
| 389d119b48cf3043d311335e499d9c6b |   392 |
| 368c6c730842d78016ad823897a372db |   388 |
| 53759a2ecddad2bb87a079a1f1519f73 |   373 |
| d1c427060a0f73f6b889a5c7c61f2ac4 |   343 |
| 53b36df67ebb7c41585e8d54d6772e08 |   323 |
| 154e7e31ebfa092203795c972e5804a6 |   281 |
| 3dd2a17168ec895c781a9191c1e95ad7 |   274 |

#### Coluna: `seller_id`

| valor                            |   qtd |
|:---------------------------------|------:|
| 6560211a19b47992c3666cc44a7e94c0 |  2033 |
| 4a3ca9315b744ce9f8e9374361493884 |  1987 |
| 1f50f920176fa81dab994f9023523100 |  1931 |
| cc419e0650a3c5ba77189a1882b7556a |  1775 |
| da8622b14eb17ae2831f4ac5b9dab84a |  1551 |
| 955fee9216a65b617aa5c0531780ce60 |  1499 |
| 1025f0e2d44d7041d6cf58b6550e0bfa |  1428 |
| 7c67e1448b00f6e969d365cea6b010ab |  1364 |
| ea8482cd71df3c1969d7b9473ff13abc |  1203 |
| 7a67c85e85bb2ce8582c35f2203ad736 |  1171 |

#### Coluna: `shipping_limit_date`

| valor               |   qtd |
|:--------------------|------:|
| 2017-07-21 18:25:23 |    21 |
| 2018-03-01 02:50:48 |    21 |
| 2017-08-30 14:30:23 |    20 |
| 2017-11-30 10:30:51 |    15 |
| 2017-12-21 02:30:41 |    15 |
| 2017-02-03 21:44:49 |    15 |
| 2018-02-28 11:48:12 |    14 |
| 2018-06-13 17:30:35 |    13 |
| 2018-04-19 02:30:52 |    13 |
| 2018-04-25 22:11:43 |    13 |

#### Coluna: `price`

|   valor |   qtd |
|--------:|------:|
|   59.9  |  2481 |
|   69.9  |  1987 |
|   49.9  |  1953 |
|   89.9  |  1548 |
|   99.9  |  1432 |
|   39.9  |  1339 |
|   29.9  |  1318 |
|   79.9  |  1214 |
|   19.9  |  1201 |
|   29.99 |  1176 |

#### Coluna: `freight_value`

|   valor |   qtd |
|--------:|------:|
|   15.1  |  3707 |
|    7.78 |  2262 |
|   14.1  |  1875 |
|   11.85 |  1846 |
|   18.23 |  1575 |
|    7.39 |  1521 |
|   16.11 |  1152 |
|   15.23 |  1010 |
|    8.72 |   921 |
|   16.79 |   873 |

#### Coluna: `run_id`

|       valor |    qtd |
|------------:|-------:|
| 2.02512e+13 | 112650 |



---

### 📏 Comprimento de Strings: `landing/order_items`
#### Coluna: `order_id`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        32 |        32 |        32 |

#### Coluna: `product_id`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        32 |        32 |        32 |

#### Coluna: `seller_id`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        32 |        32 |        32 |

#### Coluna: `shipping_limit_date`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        19 |        19 |        19 |



---

