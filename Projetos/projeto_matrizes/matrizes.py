import random as r
import pprint

def pp(funcao):
    return pprint.pprint(funcao)

def criar_matriz(valor):
    lista_numeros = [numero for numero in range(1,10)]
    r.shuffle(lista_numeros)
    matriz = [
        [lista_numeros[(linhas * 3) + colunas] for colunas in range(valor)]
        for linhas in range(valor)
    ]
    return matriz

def duplicar_matriz():
    matriz_completa = [criar_matriz(3) for _ in range(9)]
    return matriz_completa
    
matriz_a = duplicar_matriz()
pp(matriz_a)
