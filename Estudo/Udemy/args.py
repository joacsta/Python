# # vamos criar um codigo que multiplique toda a entrada
lista_entrada = []

entrada = input('digite varios numeros aqui: ')
try:
    if ',' in entrada:
        numeros = [int(n) for n in entrada.split(',')]
    elif ' ' in entrada:
        numeros = [int(n) for n in entrada.split()]
except:
    ...

def multiplicacao(*args):

    total = 1
    try:
        args = int(args)
    except:
        ...
    for i in args:
        total *= i
    
    return total

resultado_multiplicacao = multiplicacao(*numeros)
print(f'\nresultado: {resultado_multiplicacao}')

# def par_impar(*args):
#     for i in args:
#         # print(args, type(args), i)
#         mensagem = 'PAR' if i % 2 == 0 else 'IMPAR'
#         print(mensagem)

# par_impar(1, 2, 3, 4, 5)

