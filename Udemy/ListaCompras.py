lista = []

def verificar_lista():
    if not lista:
        print('a lista está vazia, adicione algo primeiro')
        
def enumerar_lista():
    for i in enumerate(lista):
        indice, nome = i
        print(indice, nome)

while True:

    resposta = input('\no que deseja fazer?\n' \
    '[i]nserir [l]istar ou [a]pagar\n'
    'se quiser [s]air\n')

    if resposta.lower().startswith('i'):

        novo_item  = input('O que deseja inserir: ')
        lista.append(novo_item)
        print('item adicionado!')

    elif resposta.lower().startswith('l'):
        if verificar_lista():
            continue
        enumerar_lista()
        
    elif resposta.lower().startswith('a'):
        if verificar_lista():
            continue
        enumerar_lista()
        resposta = input('qual item deseja apagar? digite apenas o índice. ')

        try:
            resposta = int(resposta)
            lista.pop(resposta)
            print(f'indice {resposta} removido.')
            verificar_lista()
        except:
            print('isso não é um índice ou não está presente na lista.')
            continue

    elif resposta.lower().startswith('s'):
        print('saindo...')
        break

    else:
        print('resposta inválida')


    
        

        
