import requests

resposta = requests.get("https://api.chucknorris.io/jokes/random")
dados = resposta.json()

print(f'a piada de hoje é {dados['value']}')