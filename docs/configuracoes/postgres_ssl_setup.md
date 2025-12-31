# GUIA DE CONFIGURAÇÃO – POSTGRESQL COM SSL EM VPS (DOCKER)

## CONTEXTO
Este guia documenta a configuração de um banco PostgreSQL em container Docker, com SSL/TLS habilitado, executando em uma VPS dedicada. O objetivo é permitir acesso seguro por ferramentas externas, como a Dadosfera, durante processos de carga e exploração de dados.

---

## ESTRUTURA DE DIRETÓRIOS
No diretório do projeto foi criado um diretório exclusivo para os certificados SSL:

```text
pg_ssl/
  server.crt
  server.key
```

Esse diretório é montado no container PostgreSQL via volume.

---

## CRIAÇÃO DOS CERTIFICADOS SSL

1) Criar o diretório de certificados:
```bash
mkdir -p pg_ssl
```

2) Gerar certificado e chave privada:
```bash
openssl req -new -x509 -days 3650 -nodes \
  -out pg_ssl/server.crt \
  -keyout pg_ssl/server.key \
  -subj "/CN=postgres"
```

3) Ajustar permissões dos arquivos:
```bash
chmod 600 pg_ssl/server.key
chmod 644 pg_ssl/server.crt
```

---

## AJUSTE DE PROPRIEDADE DOS ARQUIVOS
O PostgreSQL exige que a chave privada pertença ao usuário do banco dentro do container. Na imagem oficial do PostgreSQL, o usuário possui UID 999.

Executar como root na VPS:
```bash
chown 999:999 pg_ssl/server.key
chown 999:999 pg_ssl/server.crt
```

---

## CONFIGURAÇÃO DO POSTGRESQL (SSL)
No arquivo postgresql.conf foram adicionadas as seguintes diretivas:

```text
ssl = on
ssl_cert_file = '/var/lib/postgresql/ssl/server.crt'
ssl_key_file  = '/var/lib/postgresql/ssl/server.key'
```

---

## SUBIDA DOS CONTAINERS
Sempre que houver alteração em certificados ou permissões:

```bash
docker compose down
docker compose up -d
```

---

## VALIDAÇÃO

Verificar containers ativos:
```bash
docker ps
```

Verificar logs do PostgreSQL:
```bash
docker logs postgres --tail 30
```

Mensagem esperada:
```text
database system is ready to accept connections
```

---

## RESULTADO FINAL
- PostgreSQL executando em container Docker
- SSL/TLS habilitado
- Comunicação criptografada via porta 5432
- Ambiente pronto para ingestão e catalogação de dados pela Dadosfera

---

## OBSERVAÇÕES
- Os certificados utilizados são autoassinados.
- O SSL garante segurança no transporte, mas não substitui políticas de acesso.