import random

numeros = [i for i in range(1, 10)]
random.shuffle(numeros)
matriz = [numeros[i:i+3] for i in range(0, 9, 3)]

for m in matriz:
    print(m)


