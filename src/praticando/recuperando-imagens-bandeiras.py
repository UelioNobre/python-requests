import requests
from parsel import Selector
from rich import print

url = "https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"
response = requests.get(url)
selector = Selector(response.text)

results = []

flags = selector.css(".gallerybox")
for flag in flags:
    results.append(
        {
            "name": flag.css("img::attr(alt)").get(),
            "image": "https:" + flag.css("img::attr(src)").get(),
        }
    )

print(results)
