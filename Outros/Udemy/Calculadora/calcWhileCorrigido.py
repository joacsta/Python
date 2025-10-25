while True:
    numero1 = input("Digite um número")
    numero2 = input("Digite outro número")
    operador = input("Digite um operador")
    
    num_valido = None
    num_f1 = 0
    num_f2 = 0


    try:
        numf1 = float(numero1)
        numf2 = float(numero2)
        num_valido = True
    except:
        num_valido = None

    if num_valido is None:
        print('Um dos números digitados são inválidos.')
        continue
        
    operadores = '+-/*'

    if operador not in operadores:
         print('operador inválido')
         continue 

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        print(f' {num_f1} + {num_f2}')
    elif operador == '-':
        print(num_f1 - num_f2)
    elif operador == '*':
        print(num_f1 * num_f2)
    elif operador == '/':
        print(num_f1 / num_f2)
    else:
        print('Erro.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        exit()
    