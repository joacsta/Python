import random as r
import pprint

# --- 1. Nossa "Semente" ---
# Esta é uma solução de Sudoku válida e conhecida.
# Vamos usá-la como base para criar outras.
BASE_SEMENTE = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 1, 5, 6, 4, 8, 9, 7],
    [5, 6, 4, 8, 9, 7, 2, 3, 1],
    [8, 9, 7, 2, 3, 1, 5, 6, 4],
    [3, 1, 2, 6, 4, 5, 9, 7, 8],
    [6, 4, 5, 9, 7, 8, 3, 1, 2],
    [9, 7, 8, 3, 1, 2, 6, 4, 5]
]

def criar_tabuleiro_sudoku():
    # --- 2. Embaralhar os Números (Mapeamento) ---
    
    # Cria a lista [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numeros_mapa = list(range(1, 10))
    # Embaralha. Ex: [4, 8, 1, 3, 9, 5, 2, 7, 6]
    r.shuffle(numeros_mapa) 
    
    # Cria um dicionário de substituição
    # Onde o número '1' da semente vira '4' (numeros_mapa[0])
    # Onde o número '2' da semente vira '8' (numeros_mapa[1])
    # ...
    # (A sintaxe {semente: ...} é uma "Dict Comprehension")
    mapa_substituicao = {semente: embaralhado for semente, embaralhado in enumerate(numeros_mapa, start=1)}

    # Cria o tabuleiro temporário substituindo os números
    tabuleiro_temp = []
    for linha_semente in BASE_SEMENTE:
        nova_linha = []
        for numero_semente in linha_semente:
            # Substitui o número da semente (ex: 1) pelo número embaralhado (ex: 4)
            nova_linha.append(mapa_substituicao[numero_semente])
        tabuleiro_temp.append(nova_linha)

    # --- 3. Embaralhar as Linhas DENTRO dos Blocos ---
    
    # Define a ordem das linhas para o primeiro bloco (0, 1, 2)
    ordem_bloco_1 = [0, 1, 2]
    r.shuffle(ordem_bloco_1) # ex: [2, 0, 1]

    # Define a ordem das linhas para o segundo bloco (3, 4, 5)
    ordem_bloco_2 = [3, 4, 5]
    r.shuffle(ordem_bloco_2) # ex: [3, 5, 4]

    # Define a ordem das linhas para o terceiro bloco (6, 7, 8)
    ordem_bloco_3 = [6, 7, 8]
    r.shuffle(ordem_bloco_3) # ex: [8, 6, 7]
    
    # Junta as ordens para ter a ordem final das 9 linhas
    ordem_final_linhas = ordem_bloco_1 + ordem_bloco_2 + ordem_bloco_3
    # ex: [2, 0, 1, 3, 5, 4, 8, 6, 7]

    # Cria a matriz final remontando o tabuleiro na ordem de linhas embaralhada
    matriz_sudoku = [tabuleiro_temp[i] for i in ordem_final_linhas]

    return matriz_sudoku

# --- Execução ---
matriz_a = criar_tabuleiro_sudoku()
pprint.pprint(matriz_a)