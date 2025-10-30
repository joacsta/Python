def pesquisabi(item, lista):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo+alto)//2
        chute = lista[meio]

        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio - 1
    return None

Minha_lista=[2, 14, 23, 43, 44, 73, 89, 154, 2231] 

print(pesquisabi(73, Minha_lista))
