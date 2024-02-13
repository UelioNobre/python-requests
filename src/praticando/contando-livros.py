from pymongo import MongoClient
from pymongoexplain import ExplainableCollection
from rich import print

# Mais detalhes sobre aggregate:
# https://pymongo.readthedocs.io/en/stable/examples/aggregation.html

host = "localhost"
port = 27017

explain = None

with MongoClient(host, port) as client:
    db = client.library
    pipeline = [
        # Separa cada categoria em um documento separado
        # Com isso, cada "separação" terá um "_id"
        {"$unwind": "$categories"},
        # Filtra apenas os livros com status 'publish'
        {"$match": {"status": "PUBLISH"}},
        # Agrupa por categoria e conta o número de livros em cada categoria
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        # Ordena os resultados
        {"$sort": {"count": -1}},
    ]

    # Executando a agregação
    result = list(db.books.aggregate(pipeline))

    # Exibindo o resultado
    for category_count in result:
        category = category_count["_id"]
        total = category_count["count"]
        print("{:>30} {:>4}".format(category, total))

    explain = ExplainableCollection(db.books).aggregate(pipeline)

print("")
print("Detalhes da consulta")
print(explain["serverInfo"])
print(explain["command"]["pipeline"])
