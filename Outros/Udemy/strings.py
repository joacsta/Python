# Exercício

# Peça ao usuário para digitar seu nome,
# sua idade. Se nome e idade forem digitados exiba.

# Se nada for digitado: "Campos vazios"
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

# quando não há condições estabelecidas o if sugere True, por isso o not.
if (not nome or not idade):
    print('Um ou mais campos vazios')
    exit()

if (' ' in nome):
    linha6 = f'Seu nome ({nome}) contém espaço'
else:
    linha6 = f'Seu nome ({nome}) NÃO contém espaço'

print(f'Seu nome é: {nome}')
print(f'Seu nome invertido é {nome[::-1]}')
print(f'Seu nome tem {len(nome)} letras')
print(f'A primeira letra do seu nome é "{nome[0]}"')
print(f'A ultima letra do seu nome é "{nome[-1]}"')
print(linha6)

