nome = 'João Victor'
contador = 0
nome_alterado = f'*{nome[contador]}*'
novo_nome = ''

while contador < len(nome):
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1

novo_nome += '*'
print(novo_nome)
