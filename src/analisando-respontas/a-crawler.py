import requests
from parsel import Selector

base_url = "https://books.toscrape.com/"
response = requests.get(base_url)
selector = Selector(response.text)

thumb_a_href = "div.image_container a::attr(href)"

for url in selector.css(thumb_a_href).getall():
    thumb_response = requests.get(base_url + url)
    thumb_selector = Selector(thumb_response.text)
    title = thumb_selector.css("div.product_main h1::text").get()

    print(title)
