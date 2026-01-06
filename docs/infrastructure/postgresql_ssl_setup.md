## 🔐 PostgreSQL com SSL em VPS (Docker)

### 📌 Contexto

Este documento descreve a configuração de um banco PostgreSQL executando
em container Docker, com **SSL/TLS habilitado**, em uma **VPS dedicada**.

O objetivo é garantir **comunicação segura e criptografada** entre o banco
de dados e ferramentas externas, como a **Dadosfera**, durante processos
de ingestão, transformação e exploração de dados.

---

### 🧱 Estrutura de Diretórios (SSL)

No diretório do projeto foi criado um diretório exclusivo para os certificados SSL:

```text
pg_ssl/
  server.crt
  server.key
```

O diretório `pg_ssl/` é montado no container PostgreSQL por meio de um volume
definido no arquivo `docker-compose.yml`.

---

### 🔐 Criação dos Certificados SSL

#### 1️⃣ Criar o diretório de certificados

```bash
mkdir -p pg_ssl
```

---

#### 2️⃣ Gerar certificado e chave privada (autoassinados)

```bash
openssl req -new -x509 -days 3650 -nodes \
  -out pg_ssl/server.crt \
  -keyout pg_ssl/server.key \
  -subj "/CN=postgres"
```

---

#### 3️⃣ Ajustar permissões dos arquivos

```bash
chmod 600 pg_ssl/server.key
chmod 644 pg_ssl/server.crt
```

---

### 👤 Ajuste de Propriedade dos Arquivos

O PostgreSQL exige que a chave privada pertença ao usuário do banco
dentro do container.

Na imagem oficial do PostgreSQL, esse usuário possui UID 999.

Executar como root na VPS:

```bash
chown 999:999 pg_ssl/server.key
chown 999:999 pg_ssl/server.crt
```

---

### ⚙️ Configuração do PostgreSQL (SSL)

No arquivo `postgresql.conf`, foram adicionadas as seguintes diretivas:

```text
ssl = on
ssl_cert_file = '/var/lib/postgresql/ssl/server.crt'
ssl_key_file  = '/var/lib/postgresql/ssl/server.key'
```

Essas configurações habilitam o SSL/TLS, garantindo comunicação criptografada na porta padrão 5432.

> As diretivas acima podem ser aplicadas por meio de um arquivo
> `postgresql.conf` customizado ou configuradas diretamente no
> `docker-compose.yml`, dependendo da estratégia adotada no projeto.

---

### 🚀 Subida dos Containers

Sempre que houver alteração nos certificados ou permissões:

```bash
docker compose down
docker compose up -d
```

---

### ✅ Validação

#### Verificar containers ativos

```bash
docker ps
```

---

#### Verificar logs do PostgreSQL

```bash
docker logs postgres --tail 30
```

Mensagem esperada:

```text
database system is ready to accept connections
```

---

#### 🧠 Resultado Final

- PostgreSQL em container Docker
- SSL/TLS habilitado
- Comunicação criptografada
- Ambiente pronto para ingestão e catalogação de dados pela Dadosfera

---

### ⚠️ Observações

Os certificados SSL são montados no container por meio de volume Docker.
As diretivas necessárias estão documentadas neste guia, e sua aplicação
(por arquivo `postgresql.conf` customizado ou via `docker-compose.yml`)
depende da estratégia adotada no ambiente.

Os certificados utilizados são autoassinados.

O SSL protege o transporte dos dados, mas não substitui políticas adequadas de
autenticação, autorização e controle de acesso.