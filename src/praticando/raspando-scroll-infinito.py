# Em poucas palavras, a técnica de Infinite Scroll entra em
# ação quando o objeto window emite algum evento, informando que o usuário rolou a página e atingiu uma determinada "altura".
# Caso sim, uma chamada a alguma API (interna/externa), uma requisição é feita para buscar mais dados.
# No contexto dos módulos "requests" e "parsel", onde a UI não faz
# parte de seus respectivos contextos, observar o comportamento da
# é um bom caminho para se começar a entender como realmente acontece.

# Por "debaixo dos panos", a página (http://quotes.toscrape.com/scroll)
# faz uma requisição ao endereço `http://quotes.toscrape.com/api/quotes`,
# utilizando a variável querystring "?page" com um valor númerico. Esse
# valor númerico representa um multiplicador.

# Com isso, a página irá requisitar uma pequena quantia de dados.

# Em muitos casos são vistos, na parte inferior ou superior dos resultados
# exibidos inicialmente, uma série de links informando cada porção de dados.
# O nome desses links, geralmente, são chamados de links da paginação.

# Ao observar esse comportamento, ao invés de tentar simular a ação de rolar
# a página para baixo utilizando somente as bibliotecas "requests" e "parsel",
# é mais conveniente consumir o mesmo endereço que o script do evento faz.

import json
import requests
from rich import print

url = "http://quotes.toscrape.com/api/quotes?page="
page = 1
next = True
results = []

try:
    while next:
        print(f"Página: {page}")
        response = requests.get(url + str(page))
        response.raise_for_status()
        data = json.loads(response.text)
        quotes = data["quotes"]
        next = data["has_next"]
        page += 1

        results.extend(
            [str(quote["text"]).replace("“", "") for quote in quotes],
        )

except requests.HTTPError as e:
    print()
    print(f"### HTTPError {url + str(page)}")
    print(f"### Erro original: {e}", end="\n" * 2)
except requests.exceptions.RequestException as e:
    print()
    print(f"### RequestException {url + str(page)}")
    print(f"### Erro original: {e}", end="\n" * 2)

print("Citações encontradas: ")
print(results)
