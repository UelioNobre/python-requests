# python-requests

Repositório de alguns exemplos de raspagem de dados usando o módulo requests e parsel.

Um pequeno estudo sobre raspagem de dados, utilizando o módulo requests, parsel e Jupyter Notebook.

## Docker

Copiando arquivos para dentro de um container docker

```bash
docker cp books.json <container-name-or-id>:/tmp/books.json
docker exec <container-name-or-id> mongoimport --db library --jsonArray --file /tmp/books.json
```

## Mongo pelo terminal

Algumas formas de acessar o mongo pelo terminal.

```bash
## Simples
mongosh

# Expecificando a porta
mongosh --port <port_number>

# Outras opções
mongo --host <host_name> --port <port_number> -u <username> -p <password> --authenticationDatabase <auth_database>
```

---