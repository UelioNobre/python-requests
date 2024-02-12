# import requests
# from parsel import Selector


# base_url = "https://books.toscrape.com/"
# thumb_a_href = "div.image_container a::attr(href)"
# next_page_url = "/"


# response = requests.get(base_url + next_page_url)
# selector = Selector(response.text)
# next_page_url = "/"


# for url in selector.css(thumb_a_href).getall():
#     thumb_response = requests.get(base_url + url)
#     thumb_selector = Selector(thumb_response.text)
#     title = thumb_selector.css("div.product_main h1::text").get()

#     print(title)

# next_page_url = selector.css(".next a::attr(href)").get()

# variavel para simular a saida
next_page_url = "/"
limite = 3
incrementador = 0

while next_page_url:
    print(f"Existe: {next_page_url}")

    incrementador += 1

    if incrementador >= limite:
        next_page_url = None
