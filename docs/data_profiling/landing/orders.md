# Relatório de Profiling: `landing/orders`

### 📦 Volumetria: `landing/orders`
|   qtd_arquivos |   registros |   colunas |   tamanho_comprimido_mib |   tamanho_descomprimido_mib |
|---------------:|------------:|----------:|-------------------------:|----------------------------:|
|              1 |      99.441 |         9 |                    10.28 |                       15.88 |

---

### 🧬 Schema: `landing/orders`
| column_name                   | column_type   | null   | key   | default   | extra   |
|:------------------------------|:--------------|:-------|:------|:----------|:--------|
| order_id                      | VARCHAR       | YES    |       |           |         |
| customer_id                   | VARCHAR       | YES    |       |           |         |
| order_status                  | VARCHAR       | YES    |       |           |         |
| order_purchase_timestamp      | VARCHAR       | YES    |       |           |         |
| order_approved_at             | VARCHAR       | YES    |       |           |         |
| order_delivered_carrier_date  | VARCHAR       | YES    |       |           |         |
| order_delivered_customer_date | VARCHAR       | YES    |       |           |         |
| order_estimated_delivery_date | VARCHAR       | YES    |       |           |         |
| run_id                        | BIGINT        | YES    |       |           |         |

---

### 📅 Campos de Data: `landing/orders`
#### ✅ Datas com tipagem (DATE / TIMESTAMP)
> ⚠️ Nenhuma coluna DATE ou TIMESTAMP encontrada.

#### ⚠️ Possíveis campos de data/hora sem tipagem (inferido pelo nome)

- `order_delivered_carrier_date`
- `order_delivered_customer_date`
- `order_estimated_delivery_date`
- `order_purchase_timestamp`


---

### 📊 Estatísticas por Coluna: `landing/orders`
| coluna                        |   distintos |   nulos |   duplicados | pct_nulos   | pct_duplicados   | cardinalidade   |
|:------------------------------|------------:|--------:|-------------:|:------------|:-----------------|:----------------|
| order_id                      |       99441 |       0 |            0 | 0.0%        | 0.0%             | ALTA            |
| customer_id                   |       99441 |       0 |            0 | 0.0%        | 0.0%             | ALTA            |
| order_status                  |           8 |       0 |        99433 | 0.0%        | 99.99%           | BAIXA           |
| order_purchase_timestamp      |       98875 |       0 |          566 | 0.0%        | 0.57%            | ALTA            |
| order_approved_at             |       90733 |     160 |         8708 | 0.16%       | 8.76%            | ALTA            |
| order_delivered_carrier_date  |       81018 |    1783 |        18423 | 1.79%       | 18.53%           | ALTA            |
| order_delivered_customer_date |       95664 |    2965 |         3777 | 2.98%       | 3.8%             | ALTA            |
| order_estimated_delivery_date |         459 |       0 |        98982 | 0.0%        | 99.54%           | MEDIA           |
| run_id                        |           1 |       0 |        99440 | 0.0%        | 100.0%           | BAIXA           |

---

### 🔟 Distribuição de Valores (Top 10): `landing/orders`
#### Coluna: `order_id`

| valor                            |   qtd |
|:---------------------------------|------:|
| 53cdb2fc8bc7dce0b6741e2150273451 |     1 |
| a4591c265e18cb1dcee52889e2d8acc3 |     1 |
| 6514b8ad8028c9f2cc2374ded245783f |     1 |
| e6ce16cb79ec1d90b1da9085a6118aeb |     1 |
| 85ce859fd6dc634de8d2f1e290444043 |     1 |
| 83018ec114eee8641c97e08f7b4e926f |     1 |
| 203096f03d82e0dffbc41ebc2e2bcfb7 |     1 |
| f848643eec1d69395095eb3840d2051e |     1 |
| 1790eea0b567cf50911c057cf20f90f9 |     1 |
| ee64d42b8cf066f35eac1cf57de1aa85 |     1 |

#### Coluna: `customer_id`

| valor                            |   qtd |
|:---------------------------------|------:|
| b0830fb4747a6c6d20dea0b8c802d7ef |     1 |
| ed0271e0b7da060a393796590e7b737a |     1 |
| 9bdf08b4b3b52b5526ff42d37d47f222 |     1 |
| 059f7fc5719c7da6cbafe370971a8d70 |     1 |
| 3a874b4d4c4b6543206ff5d89287f0c3 |     1 |
| 816f8653d5361cbf94e58c33f2502a5c |     1 |
| d9ef95f98d8da3b492bb8c0447910498 |     1 |
| cf8ffeddf027932e51e4eae73b384059 |     1 |
| c7340080e394356141681bd4c9b8fe31 |     1 |
| 756fb9391752dad934e0fe3733378e57 |     1 |

#### Coluna: `order_status`

| valor       |   qtd |
|:------------|------:|
| delivered   | 96478 |
| shipped     |  1107 |
| canceled    |   625 |
| unavailable |   609 |
| invoiced    |   314 |
| processing  |   301 |
| created     |     5 |
| approved    |     2 |

#### Coluna: `order_purchase_timestamp`

| valor               |   qtd |
|:--------------------|------:|
| 2018-08-02 12:06:09 |     3 |
| 2017-11-20 11:46:30 |     3 |
| 2018-07-28 13:11:22 |     3 |
| 2018-04-11 10:48:14 |     3 |
| 2018-08-02 12:06:07 |     3 |
| 2018-06-01 13:39:44 |     3 |
| 2018-03-31 15:08:21 |     3 |
| 2017-11-20 10:59:08 |     3 |
| 2018-08-02 12:05:26 |     3 |
| 2018-02-19 15:37:47 |     3 |

#### Coluna: `order_approved_at`

| valor               |   qtd |
|:--------------------|------:|
|                     |   160 |
| 2018-02-27 04:31:10 |     9 |
| 2017-11-07 07:30:38 |     7 |
| 2017-12-05 10:30:42 |     7 |
| 2018-02-27 04:31:01 |     7 |
| 2018-07-05 16:33:01 |     7 |
| 2017-11-07 07:30:29 |     7 |
| 2018-02-06 05:31:52 |     7 |
| 2018-01-10 10:32:03 |     7 |
| 2018-05-15 03:55:59 |     6 |

#### Coluna: `order_delivered_carrier_date`

| valor               |   qtd |
|:--------------------|------:|
|                     |  1783 |
| 2018-05-09 15:48:00 |    47 |
| 2018-05-10 18:29:00 |    32 |
| 2018-05-07 12:31:00 |    21 |
| 2018-07-24 16:07:00 |    16 |
| 2018-05-02 15:15:00 |    16 |
| 2018-08-03 15:10:00 |    15 |
| 2018-05-16 13:44:00 |    15 |
| 2018-08-08 15:01:00 |    15 |
| 2018-07-17 14:16:00 |    15 |

#### Coluna: `order_delivered_customer_date`

| valor               |   qtd |
|:--------------------|------:|
|                     |  2965 |
| 2018-05-14 20:02:44 |     3 |
| 2018-05-08 23:38:46 |     3 |
| 2018-05-08 19:36:48 |     3 |
| 2016-10-27 17:32:07 |     3 |
| 2017-06-19 18:47:51 |     3 |
| 2018-02-14 21:09:19 |     3 |
| 2018-07-24 21:36:42 |     3 |
| 2017-12-02 00:26:45 |     3 |
| 2017-07-31 18:17:45 |     2 |

#### Coluna: `order_estimated_delivery_date`

| valor               |   qtd |
|:--------------------|------:|
| 2017-12-20 00:00:00 |   522 |
| 2018-03-12 00:00:00 |   516 |
| 2018-05-29 00:00:00 |   513 |
| 2018-03-13 00:00:00 |   513 |
| 2018-02-14 00:00:00 |   507 |
| 2017-12-18 00:00:00 |   493 |
| 2018-05-28 00:00:00 |   492 |
| 2018-03-06 00:00:00 |   492 |
| 2018-02-06 00:00:00 |   491 |
| 2018-07-05 00:00:00 |   490 |

#### Coluna: `run_id`

|       valor |   qtd |
|------------:|------:|
| 2.02512e+13 | 99441 |



---

### 📏 Comprimento de Strings: `landing/orders`
#### Coluna: `order_id`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        32 |        32 |        32 |

#### Coluna: `customer_id`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        32 |        32 |        32 |

#### Coluna: `order_status`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|         7 |      8.98 |        11 |

#### Coluna: `order_purchase_timestamp`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        19 |        19 |        19 |

#### Coluna: `order_approved_at`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        19 |        19 |        19 |

#### Coluna: `order_delivered_carrier_date`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        19 |        19 |        19 |

#### Coluna: `order_delivered_customer_date`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        19 |        19 |        19 |

#### Coluna: `order_estimated_delivery_date`
|   min_len |   avg_len |   max_len |
|----------:|----------:|----------:|
|        19 |        19 |        19 |



---

