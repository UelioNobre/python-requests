import sys
import re

from pymongo import MongoClient
from rich import print


def find_book(technology):
    titles = []
    regex = re.compile(technology, re.IGNORECASE)

    with MongoClient() as client:
        db = client.library

        query = {"categories": {"$regex": regex}}
        projection = {"title": 1}

        books = db.books.find(query, projection)
        for cursor in books:
            titles.append(cursor["title"])

    return titles


if __name__ == "__main__":
    print("Executar esse script")
    technology = sys.argv[1]
    books = find_book(technology)

    if len(books) < 1:
        print(f"Nenhum livro encontrado com essa categoria: {technology}")
    else:
        print(books)
