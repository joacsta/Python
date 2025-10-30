import os

mensagens = []
# lista

nome = input("Nome: ")

while True:

    os.system("clear")

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'],"|",m['texto'])

    print("_____________________________")

    texto = input("chat:")
    if texto == 'fim':
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
        })
        