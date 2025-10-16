import random as r

index_aleatorio = r.randint(1,10)
numero_aleatorio = r.randint(1,10)

lista_de_numeros = [
    [r.randint(0,9) for _ in range(index_aleatorio)]
    for _ in range(numero_aleatorio)
]

def encontrar_numeros_duplicados(lista_de_numeros):
    numeros_encontrados = set()
    encontrou_numero = None

    for numero in lista_de_numeros:
        if numero in numeros_encontrados:
            encontrou_numero = numero
            break

        numeros_encontrados.add(numero)
    return encontrou_numero

for lista in lista_de_numeros:
    print(lista, encontrar_numeros_duplicados(lista))