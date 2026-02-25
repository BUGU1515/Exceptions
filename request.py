import requests

nome = input("Digite um número para descobrir o pokemon: ").strip().lower()
url = f"https://pokeapi.co/api/v2/pokemon/{nome}"

try:
    resposta = requests.get(url)
    dados = resposta.json()
    print("Nome:", dados["name"])

except ValueError:
    print("Erro: Digite apenas números.")