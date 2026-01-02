# 🔐 PostgreSQL com SSL em VPS (Docker)

## 📌 Contexto

Este documento descreve a configuração de um banco PostgreSQL executando
em container Docker, com **SSL/TLS habilitado**, em uma **VPS dedicada**.

O objetivo é garantir **comunicação segura e criptografada** entre o banco
de dados e ferramentas externas, como a **Dadosfera**, durante processos
de ingestão, transformação e exploração de dados.

## 🧱 Estrutura de Diretórios (SSL)

No diretório do projeto foi criado um diretório exclusivo para os certificados SSL:

```text
pg_ssl/
  server.crt
  server.key
```

Esse diretório é montado no container PostgreSQL via volume Docker.


## 🔐 Criação dos Certificados SSL

### 1️⃣ Criar o diretório de certificados

```bash
mkdir -p pg_ssl
```

### 2️⃣ Gerar certificado e chave privada (autoassinados)

```bash
openssl req -new -x509 -days 3650 -nodes \
  -out pg_ssl/server.crt \
  -keyout pg_ssl/server.key \
  -subj "/CN=postgres"
```

### 3️⃣ Ajustar permissões dos arquivos

```bash
chmod 600 pg_ssl/server.key
chmod 644 pg_ssl/server.crt
```

## 👤 Ajuste de Propriedade dos Arquivos

O PostgreSQL exige que a chave privada pertença ao usuário do banco
dentro do container.

Na imagem oficial do PostgreSQL, esse usuário possui UID 999.

Executar como root na VPS:

```bash
chown 999:999 pg_ssl/server.key
chown 999:999 pg_ssl/server.crt
```

## ⚙️ Configuração do PostgreSQL (SSL)

No arquivo `postgresql.conf`, foram adicionadas as seguintes diretivas:

```text
ssl = on
ssl_cert_file = '/var/lib/postgresql/ssl/server.crt'
ssl_key_file  = '/var/lib/postgresql/ssl/server.key'
```

Essas configurações habilitam o SSL/TLS, garantindo comunicação criptografada
na porta padrão 5432.

## 🚀 Subida dos Containers

Sempre que houver alteração nos certificados ou permissões:

```bash
docker compose down
docker compose up -d
```

## ✅ Validação

### Verificar containers ativos

```bash
docker ps
```

### Verificar logs do PostgreSQL

```bash
docker logs postgres --tail 30
```

Mensagem esperada:

```text
database system is ready to accept connections
```

## 🧠 Resultado Final

- PostgreSQL em container Docker
- SSL/TLS habilitado
- Comunicação criptografada
- Ambiente pronto para ingestão e catalogação de dados pela Dadosfera


## ⚠️ Observações

Certificados utilizados são autoassinados

O SSL protege o transporte dos dados, mas não substitui políticas de autenticação e controle de acesso
