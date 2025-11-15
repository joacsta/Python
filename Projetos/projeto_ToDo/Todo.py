import os
import time
from datetime import datetime
from data_json import visualizar_tarefas_json

MENU_PRINCIPAL = \
"""
Olá!
Bem-vindo ao Gerenciador de Tarefas - V: 0.3

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
lista_tarefas = []

for tarefa in visualizar_tarefas_json["tarefas"]:
    lista_tarefas.append(tarefa)

def resposta_usuario_indice(funcao):
    entrada_indices = input('')
    try:
        if not entrada_indices:
            return
        else:
            lista_indices = [
                int(i.strip()) for i in entrada_indices.split(',')
            ]
            funcao(*lista_indices)
            print('Procedimento realizado com sucesso!')
            time.sleep(2)
    except ValueError:
        print('Erro.')
    return lista_tarefas

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
    print(f'Atualmente, você tem {numero_de_tarefas_lista} tarefas para fazer.\n')
    novas_tarefas = input(
        'Pressione [Enter] para voltar ao menu.'
        '\nDigite as tarefas que voce deseja adicionar '
        '(caso queira adicionar mais de uma tarefa, separe por vírgulas):\n\n'
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
    print()
    print(
        'Pressione [Enter] para voltar ao menu.'
        '\nDigite o índice da tarefa que deseja editar: '
    )
    resposta_user = input('')
    if not resposta_user:
        return
    else:
        try:
            int(resposta_user)
            editar_tarefa(resposta_user)
        except ValueError:
            print('Erro. Digite apenas o número do índice.')
        finally:
            print('Procedimento realizado com sucesso.')

def excluir_tarefas(*args):
    indices_a_excluir = set(args)
    lista_atualizada = []
    for indice, tarefa in enumerate(lista_tarefas, start=1):
        if indice not in indices_a_excluir:
            lista_atualizada.append(tarefa)
    lista_tarefas[:] = lista_atualizada

def visualizar_tarefas():
    for indice, tarefas in enumerate(lista_tarefas, start=1):
        print(f'{checkbox_vazio} {indice}) {tarefas}') 

def executar_excluir_tarefas():
    limpar_terminal()
    visualizar_tarefas()
    print()
    print(
        'Pressione [Enter] para voltar ao menu.'
        '\nDigite os índices a serem excluídos (separe por vírgulas): '
    )
    resposta_usuario_indice(excluir_tarefas)


def executar_visualizar_tarefas():
    limpar_terminal()
    if not lista_tarefas:
        print('Nenhuma tarefa cadastrada por enquanto.')
        time.sleep(2)
        return
    else:
        print(TITULO)
        visualizar_tarefas()
        resposta_user = input(
            '\nPressione [Enter] para voltar ao menu.'
        )
        if not resposta_user:
            return


opcoes_menu = {
    'adicionar': executar_add_tarefas,
    'editar': executar_editar_tarefa,
    'excluir': executar_excluir_tarefas,
    'visualizar': executar_visualizar_tarefas,

    '1': executar_add_tarefas,
    '2': executar_editar_tarefa,
    '3': executar_excluir_tarefas,
    '4': executar_visualizar_tarefas,
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
            print('Opção inválida.')
            time.sleep(1)
            limpar_terminal()

if __name__ == '__main__':
    main()