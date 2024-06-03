import requests
from datetime import datetime

def fetch_url(url):
    response = requests.get(url)
    return response.text

def main():
    tempo_inicial = datetime.now()
    urls = ["https://example.com"] * 10 
    responses = [fetch_url(url) for url in urls]
    for response in responses:
        print(response[:100])
    tempo_final = datetime.now() - tempo_inicial
    print(tempo_final)

main()