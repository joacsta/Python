import random

lista_numeros = [random.randint(1,50) for _ in range(10)]

def busca_menor(array):
    menor = array[0]
    menor_indice = 0
    for i in range(1,len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
    return menor_indice

def ordenacao_selecao(array):
    novo_array = []
    for i in range(len(array)):
        menor = busca_menor(array)
        novo_array.append(array.pop(menor))
    return novo_array

print(lista_numeros)
print(ordenacao_selecao(lista_numeros))