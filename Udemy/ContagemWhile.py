frase = "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Necessitatibus aliquid cum molestias dolorum numquam debitis quisquam dignissimos laborum pariatur minus. Facere repudiandae similique ipsam dolorem at ratione quisquam eveniet repellat?"

i = 0
maior_frequencia = 0
caractere_mais_frequente = ''

while i < len(frase):
    caractere_atual = frase[i]
    frequencia_caractere = frase.count(caractere_atual)

    if caractere_atual == ' ':
        i += 1
        continue

    if maior_frequencia <= frequencia_caractere:
        maior_frequencia = frequencia_caractere
        caractere_mais_frequente = caractere_atual

    i += 1

print(f'\nA letra que apareceu mais vezes na frase foi a letra "{caractere_mais_frequente}".')
print(f'Ela apareceu {maior_frequencia} vezes.\n')
