# tuplas são listas imutáveis

nomes = ['joao', 'maria', 'sandy'] #lista
nome = 'joao', 'maria', 'sandy' #tupla
nomes.append('francisco')
nomes.pop()

nomes = enumerate(nomes)

for i in nomes:
    print(i)