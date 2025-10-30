def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    #len = retorna o numero de itens para o container

    while baixo <= alto:

        meio = (baixo+alto)//2
        chute = lista[meio]
        
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

minha_lista = [1, 3, 5, 7, 9, 8, 23, 24, 34, 53, 233, 2894]

print ("O número selecionado está no índice:",pesquisa_binaria(minha_lista, 8))