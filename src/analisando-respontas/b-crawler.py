import requests
from parsel import Selector
from rich import print


def request_page(url):
    response = requests.get(url).text
    selector = Selector(response)
    return selector


def get_data(html):
    data = html.css("div.image_container a::attr(href)").getall()
    return data


def get_next_page(html):
    next_page = html.css(".next a::attr(href)").get()
    return next_page


def get_urls(base_url, urls):
    paths = [base_url + url for url in urls]
    return paths


base_url = "https://books.toscrape.com/catalogue/"
next_page = "page-1.html"
limit = 3
counter = 0
urls = []

while next_page:
    html = request_page(base_url + next_page)
    images = get_data(html)
    urls.extend(get_urls(base_url, images))

    if limit is None:
        next_page = get_next_page(html)
    else:
        counter += 1
        next_page = get_next_page(html)
        if counter >= limit:
            next_page = None

    # print(f"urls: {urls}")
    print(f"base_url: {base_url}")
    print(f"next_page: {next_page}")

print(urls)
