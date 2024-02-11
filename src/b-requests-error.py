from requests import get, HTTPError
from rich import print

url = "http://httpbin.org/status/404"

try:
    response = get(url)
    response.raise_for_status()
except HTTPError as err:
    print("Erro ao requisitar a página")
    print(err)
