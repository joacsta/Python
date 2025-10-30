import numpy as np
import random
import matplotlib.pyplot as plt

def movimento_browniano(n=150):
    # Inicialização do grid
    grid = np.zeros((n, n), dtype=int)
    
    # Ponto central inicial
    center = n // 2
    grid[center, center] = 1
    Np = 1  # Número de pontos salvos
    
    # Arquivo de saída (simulado como uma lista)
    pontos_salvos = [(center, center)]
    
    while Np <= 0.1 * n * n:
        # Escolha aleatória de uma posição
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        
        # Se a posição já está ocupada, escolha outra
        if grid[i, j] == 1:
            continue
        
        # Movimento aleatório até encontrar um vizinho ocupado
        while True:
            # Escolha uma direção aleatória (N, S, L, O)
            direcao = random.choice(['N', 'S', 'L', 'O'])
            
            # Encontra o vizinho na direção escolhida (com tratamento de bordas)
            if direcao == 'N':
                vizinho_i, vizinho_j = (i-1) % n, j
            elif direcao == 'S':
                vizinho_i, vizinho_j = (i+1) % n, j
            elif direcao == 'L':
                vizinho_i, vizinho_j = i, (j+1) % n
            elif direcao == 'O':
                vizinho_i, vizinho_j = i, (j-1) % n
            
            # Verifica se o vizinho está ocupado
            if grid[vizinho_i, vizinho_j] == 1:
                # Marca a posição atual como ocupada
                grid[i, j] = 1
                Np += 1
                pontos_salvos.append((i, j))
                break
            else:
                # Move para a posição do vizinho
                i, j = vizinho_i, vizinho_j
    
    return pontos_salvos

def plot_pontos(pontos):
    x = [p[0] for p in pontos]
    y = [p[1] for p in pontos]
    
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, s=15, color='black')
    plt.title('Movimento Browniano - 10% do grid ocupado')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

# Executa a simulação
pontos = movimento_browniano(n=150)

# Plota os resultados
plot_pontos(pontos)