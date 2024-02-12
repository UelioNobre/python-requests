import requests
from parsel import Selector
from rich import print

# Define a primeira página como próxima a ter seu conteúdo recuperado
URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = "page-1.html"
limit = 3
counter = 0

while next_page_url:
    # Busca o conteúdo da próxima página
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)
    # Imprime os produtos de uma determinada página
    for product in selector.css(".product_pod"):
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").get()
        print(title, price)
    # Descobre qual é a próxima página

    if limit is None:
        next_page_url = selector.css(".next a::attr(href)").get()
    else:
        counter += 1
        next_page_url = selector.css(".next a::attr(href)").get()
        if counter >= limit:
            next_page_url = None
    # next_page_url = selector.css(".next a::attr(href)").get()
