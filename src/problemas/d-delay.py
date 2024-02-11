import requests

response = None

try:
    response = requests.get("https://httpbin.org/delay/3", timeout=2)
    response.raise_for_status()
except requests.Timeout:
    response = requests.get("https://httpbin.org/delay/7", timeout=10)
finally:
    print(response.status_code)
