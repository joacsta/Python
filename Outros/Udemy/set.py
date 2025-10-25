import random as r
from collections import Counter

contador = 0

lista_numeros = [
    [r.randint(0, 9) for _ in range(r.randint(1,9))]
    for _ in range(r.randint(1,9))
]

for lista in lista_numeros:
    print(lista)
print('')
     
for lista in lista_numeros:
    qtd_numeros = Counter(lista)
    contador = 0
    for l in lista:
        print(l)
        if qtd_numeros[l] > 1:
            contador += 1
        else:
            continue

    if contador != 0:
        print(f'\ntotal: {contador} repeticoes')
    else:
        print('\nnenhum numero repete')
    print('')

# for lista in lista_numeros:
#     conjunto = set(lista)
#     print(conjunto)
