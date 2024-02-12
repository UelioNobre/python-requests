from pymongo import MongoClient

client = MongoClient()
db = client.library


books = db.books.find({})

print(list(books))
