import os

def menu_principal():
    print(
"""
Olá!
Bem-vindo ao Gerenciador de Tarefas - V: 0.1

Selecione o que deseja fazer:
    
    1 - Criar uma tarefa
    2 - Editar uma tarefa
    3 - Excluir uma tarefa
    4 - Visualizar lista de tarefas

Digite [s] para sair.
"""
    )

lista_de_tarefas = []

def add_tarefa():
    while True:
        tarefa = input('\nQue tarefa você deseja adicionar à sua lista? \nDigite [0] para retornar ao menu.\n')
        if tarefa == '0':
            break
        lista_de_tarefas.append(tarefa)
        print('Tarefa adicionada com sucesso!\n')
        for index, item in enumerate(lista_de_tarefas):
            index += 1
            print(f'[{index}] - {item} ()')
        
def edit_tarefa():
    pass

def delete_tarefa():
    pass

def view_tarefa():
    pass

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
        add_tarefa()
    elif entrada == '2':
        ...
    elif entrada == '3':
        ... 
    elif entrada == '4':
        ... 
    else:
        os.system('clear')
        continue