import random as r

def menu_principal():
    print(
"""
O que deseja fazer?
    
    1 - Validar um CPF
    2 - Gerar um CPF

Se deseja sair, tecle [s].
"""
    )

def gerador_nove_digitos():
    novo_cpf = ''
    for i in range(9):
        novo_cpf += str(r.randint(0,9))
    return novo_cpf

def formatar_cpf():
    cpf_formatado = ''
    cpf = input('Digite o cpf: ')

    for i in cpf:
        if i.isdigit():
            cpf_formatado += i
        else:
            continue

    cpf_repetido = (cpf_formatado == cpf_formatado[0] * len(cpf_formatado))

    if cpf_repetido:
        print('entrada invalida')
        exit()

    cpf_verificacao = cpf_formatado
    cpf_formatado = cpf_formatado[0:9:]  #limita 9 caracteres
    cpf_formatado = cpf_formatado[::-1]  #inverte o cpf
    return cpf_formatado, cpf_verificacao

def validar_cpf():

    cpf_formatado, verifica_cpf = formatar_cpf()

    while len(cpf_formatado) < 11:

        soma_cpf = 0
        contador = 2

        for j in cpf_formatado:
            calc = (int(j) * contador)
            soma_cpf += calc
            contador += 1

        resto = soma_cpf % 11

        if resto < 2:
            digito_verificador = '0'
        if resto >= 2:
            digito_verificador = eval('11 - resto')
            digito_verificador = str(digito_verificador)

        cpf_formatado = digito_verificador + cpf_formatado

    cpf_formatado = cpf_formatado[::-1]

    if cpf_formatado == verifica_cpf:
        print('\ncpf valido')
    else:
        print('\ncpf invalido')

def gerar_cpf():

    cpf_formatado = gerador_nove_digitos()

    while len(cpf_formatado) < 11:

        soma_cpf = 0
        contador = 2

        for j in cpf_formatado:
            calc = (int(j) * contador)
            soma_cpf += calc
            contador += 1

        resto = soma_cpf % 11

        if resto < 2:
            digito_verificador = '0'
        if resto >= 2:
            digito_verificador = eval('11 - resto')
            digito_verificador = str(digito_verificador)

        cpf_formatado = digito_verificador + cpf_formatado

    cpf_formatado = cpf_formatado[::-1]
    print(f'\nseu novo cpf é {cpf_formatado}.')

while True:

    menu_principal()
    entrada = input('O que deseja fazer? ')

    if entrada.lower().startswith('s'):
        print('saindo...')
        break
    elif entrada == '1':
        validar_cpf()
    elif entrada == '2':
        gerar_cpf()
    else:
        print('opcao invalida')
        continue
    
