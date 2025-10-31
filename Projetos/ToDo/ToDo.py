import os
import time
from datetime import datetime

MENU_PRINCIPAL = \
"""
Olá!
Bem-vindo ao Gerenciador de Tarefas - V: 0.2
(Digite [0] para limpar a tela ou para retornar.)

Digite o número ou o que deseja fazer:
    
    1 - Adicionar tarefas;
    2 - Editar uma tarefa;
    3 - Excluir tarefas;
    4 - Visualizar lista de tarefas;

Digite [s] para sair.
"""
TITULO = \
"""
====================
  Lista de Tarefas
====================
"""

checkbox_vazio = '\u2610'
checkbox_marcado = '\u2611' 

lista_tarefas = [
    'fazer uma coisa',
    'fazer outra coisa',
    'fazer tal coisa',
    'fazer mais uma coisa'
]

def getdate():
    data_hora_atual = datetime.now()
    hora = data_hora_atual.strftime('%H:%M')
    data = data_hora_atual.strftime('%d/%m/%Y')
    print(f'{hora} | {data}')

def limpar_terminal():
    os.system('clear')

def menu_principal():
    getdate()
    return print(MENU_PRINCIPAL)

def add_tarefas(*args):
    for arg in args:
       lista_tarefas.append(arg)
    return lista_tarefas

def executar_add_tarefas():
    limpar_terminal()
    numero_de_tarefas_lista = len(lista_tarefas)
    print(f'Atualmente, você tem {numero_de_tarefas_lista} tarefas para fazer.')
    novas_tarefas = input(
        'Pressione [Enter] para voltar ao menu.'
        '\nDigite as tarefas que voce deseja adicionar '
        '(Caso queira adicionar mais de uma tarefa, separe por vírgulas): '
    )
    if not novas_tarefas:
        return
    else:
        lista_novas_tarefas = [
            tarefas.strip() for tarefas in novas_tarefas.split(',')
        ]
        add_tarefas(*lista_novas_tarefas)
        print('Tarefa(s) adicionada(s) com êxito!')
        time.sleep(2)

def editar_tarefa(indice_valor: int):
    indice_valor -= 1
    if 0 <= indice_valor < len(lista_tarefas):
        print(f'Voce selecionou: {lista_tarefas[indice_valor]}')
        lista_tarefas[indice_valor] = input('Como deseja alterar? ')
    return lista_tarefas

def executar_editar_tarefa():
    limpar_terminal()
    visualizar_tarefas()
    indice_buscado = input(
        'Pressione [Enter] para voltar ao menu.'
        '\nDigite o índice da tarefa que deseja editar: '
    )
    try:
        if not indice_buscado:
            return
        else:
            editar_tarefa(int(indice_buscado))
            print('Alteração realizada com sucesso.')
            time.sleep(2)
    except ValueError:
        print('Erro. Um número inteiro precisa ser digitado.')
        time.sleep(2)
        return

def excluir_tarefas(*args):
    indices_a_excluir = set(args)
    lista_atualizada = []
    for indice, tarefa in enumerate(lista_tarefas, start=1):
        if indice not in indices_a_excluir:
            lista_atualizada.append(tarefa)
    lista_tarefas[:] = lista_atualizada

def executar_excluir_tarefas():
    limpar_terminal()
    visualizar_tarefas()
    excluir_indices = input(
        'Pressione [Enter] para voltar ao menu.'
        '\nDigite os índices a serem excluídos (separe por vírgulas): '
    )
    try:
        if not excluir_indices:
            return
        else:
            lista_exclusao = {
                int(indice.strip()) for indice in excluir_indices.split(',')
            }
            excluir_tarefas(*lista_exclusao)
            print('Procedimento realizado com sucesso.')
            time.sleep(2)
    except ValueError:
        print('Erro.')

def visualizar_tarefas():
    print(TITULO)
    for indice, tarefa in enumerate(lista_tarefas, start=1):
        print(f'{checkbox_vazio} {indice}) {tarefa}')
    print(f'\nTotal de tarefas: {len(lista_tarefas)}')

def executar_visualizar_tarefas():
    limpar_terminal()
    while True:
        visualizar_tarefas()
        user_input = input('\nPressione [Enter] para voltar ao menu.')
        if not user_input:
            limpar_terminal()
            break
        else:
            limpar_terminal()

opcoes_menu = {
    'adicionar': executar_add_tarefas,
    'editar': executar_editar_tarefa,
    'excluir': executar_excluir_tarefas,
    'visualizar': visualizar_tarefas,

    '1': executar_add_tarefas,
    '2': executar_editar_tarefa,
    '3': executar_excluir_tarefas,
    '4': executar_visualizar_tarefas,
    '0': limpar_terminal,
}

def main():
    while True:
        limpar_terminal()
        menu_principal()
        usuario_input = input('O que deseja fazer? ').strip()
        if usuario_input.lower().startswith('s'):
            print('Encerrando...')
            break
        funcao_executar = opcoes_menu.get(usuario_input)
        if funcao_executar:
            funcao_executar()
        else:
            limpar_terminal()

if __name__ == '__main__':
    main()