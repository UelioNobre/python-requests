import requests
from parsel import Selector

url = "https://books.toscrape.com/"
response = requests.get(url)
selector = Selector(response.text)

image = selector.css("div.image_container a").get()
print(image)
