MENU_PRINCIPAL = \
"""
Olá!
Bem-vindo ao Gerenciador de Tarefas - V: 0.2
|Python 3.14|
(Digite [0] para limpar a tela ou para retornar.)

Digite o número ou o que deseja fazer:
    
    1 - Adicionar tarefas
    2 - Editar uma tarefa
    3 - Excluir tarefas
    4 - Visualizar lista de tarefas

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

lista_tarefas = ['fazer uma coisa', 'fazer outra coisa', 'fazer tal coisa', 'fazer mais uma coisa']

def menu_principal():
    return print(MENU_PRINCIPAL)

def add_tarefas(*args):
    for arg in args:
       lista_tarefas.append(arg)
    for indice, tarefa in enumerate(lista_tarefas, start=1):
       print(f'{indice}) {tarefa}')
    return lista_tarefas

def editar_tarefa(indice_valor: int):
    indice_valor -= 1
    if 0 <= indice_valor < len(lista_tarefas):
        print(f'voce selecionou: {lista_tarefas[indice_valor]}')
    else:
        print(f'indice {indice_valor} nao definido.')
    return lista_tarefas

def excluir_tarefas(*args):
    indices_a_excluir = set(args)
    print(f'indices que serao excluidos: {indices_a_excluir}')
    lista_atualizada = []
    for indice, tarefa in enumerate(lista_tarefas, start=1):
        if indice not in indices_a_excluir:
            lista_atualizada.append(tarefa)
    return lista_atualizada

def visualizar_tarefas():
    print(TITULO)
    for tarefa in lista_tarefas:
        print(f'{checkbox_vazio} - {tarefa}')

# data e horario
# checkboxes
# categorias
