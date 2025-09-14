import os
import time as t

def menu_principal():
    print(
"""
Olá!
Bem-vindo ao Gerenciador de Tarefas - V: 0.1
(Digite [0] para limpar a tela)

Selecione o que deseja fazer:
    
    1 - Adicionar tarefas
    2 - Editar uma tarefa
    3 - Excluir uma tarefa
    4 - Visualizar lista de tarefas

Digite [s] para sair.
"""
    )

lista_provisoria = []
lista_tarefas = []

def add_multiplas_tarefas():

    def looping():
        while True:
            entrada_tarefa = input('Digite as tarefas: ')        
            if entrada_tarefa == '0':
                break
            else:
                lista_provisoria.append(entrada_tarefa)

        for index, tarefa in enumerate(lista_provisoria, start = 1):
            lista_tarefas.append(f'{index} - {tarefa}')

        print(f'\nTotal de {len(lista_provisoria)} tarefas adicionadas.')
        return lista_tarefas

    def add_tarefas(*args):
        args = looping()
        return args

    tarefas_adds = add_tarefas()
    # for tarefinhas in tarefas_adds:
    #     print(f'[]|{tarefinhas}')
    


# for index, tarefas in enumerate(tarefas_adds, start = 1):
#     print(f'{index} - {tarefas}')
# def edit_tarefa():
#     pass

# def delete_tarefa():
#     pass

# def view_tarefa():
#     pass

while True:
    menu_principal()
    entrada = input("O que deseja fazer? ")

    if entrada.lower().startswith('s'):
        print("Saindo...")
        break
    elif entrada == '1':
        if entrada == '0':
            print('Retornando ao menu principal...')
            continue
        print('')
        while True:
            add_multiplas_tarefas()
            msg = input('\nDeseja adicionar mais?' \
            '\n[1] p/ sim | [0] p/ não'\
            '\nResposta: ')
            if msg == '0':
                print('\nRetornando ao menu principal...')
                break
            elif msg == '1':
                lista_provisoria.append(add_multiplas_tarefas())
            else:
                print('opção inválida')

    elif entrada == '2':
        ...
    elif entrada == '3':
        ... 
    elif entrada == '4':
        if lista_tarefas:
            os.system('clear')
            print('LISTA DE TAREFAS\n')
            for tarefas in lista_tarefas:
                print(tarefas)
            t.sleep(30)
            os.system('clear')
        else:
            print('\nlista vazia...')
            t.sleep(1)
            os.system('clear')    
            continue
    elif entrada == '0':
        os.system('clear')
        continue
    else:
        print('\nENTRADA INVÁLIDA, DIGITE APENAS NÚMEROS')
        t.sleep(2)
        os.system('clear')
        continue