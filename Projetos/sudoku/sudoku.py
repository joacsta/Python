import random as r


lista_numeros = [x for x in range(1,10)]
escolha_aleatoria = r.choice(lista_numeros)
r.shuffle(lista_numeros)
print(lista_numeros)
