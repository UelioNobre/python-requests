import requests
from parsel import Selector

url = "https://books.toscrape.com/"
response = requests.get(url)
selector = Selector(response.text)

image = selector.css("img.thumbnail").get()
print(f"Uma imagem:\n{image}", end="\n" * 2)

images = selector.css("img.thumbnail").getall()
print("Todas as imagens:")
for thumbnail in images:
    print(thumbnail)
