# crie uma função que encontra o primeiro duplicado, considerando o segundo número
# como uma duplicação. retorne a duplicacao considerada
#     requisitos:
#         a ordem do numero  duplicado é considerado a partir da segunda
#         ocorrencia do numero, ou seja, um numero duplicado em si

#     ex:
#         [1,2,3,3,2,1] = 1, 2, 3 são duplicados, retorne 3
#         [1,2,3,4,5,6] = nao há duplicados, retorne -1


import pprint as pp
import random as r
from collections import Counter 

numero_aleatorio = r.randint(1, 5)

lista_num_int = [
    [r.randint(0, 9) for _ in range(10) ]
    for _ in range(5)
]

pp.pprint(lista_num_int)
print()

# lista de numeros
for lista in lista_num_int:
    print(f'{lista}')
print('')

# numeros de cada lista
for lista in lista_num_int:
    counter = Counter(lista)
    repetidos = [(key, value) for key, value in counter.items() if value > 1]
    if repetidos:
        for num, value in repetidos:
            print(f'numero que se repetiu: {num}, ele repetiu {value} vezes')
    else:
        print("essa tabela nao tem repetidos")
print()

# lista dos numeros sem se repetir
for lista in lista_num_int:  
    lista_setada = set(lista)
    print(lista_setada)
