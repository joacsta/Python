import operator

operacoes = {
    '+': ('soma', operator.add),
    '-': ('subtracao', operator.sub),
    '*': ('multiplicacao', operator.mul),
    '/': ('divisao', operator.truediv),
}

num_int1 = 0
num_int2 = 0
num_int = 0
contador = 0
menu = "Operações:\n'+' p/ Adição\n'-' p/ Subtração\n'*' p/ Multiplicação\n'/' p/ Divisão"

print("\n||CALCULADORA DE NÚMEROS INTEIROS||")

while contador < 2:
    num = input('Digite o número INTEIRO aqui: ')
    contador += 1
    if contador == 1:
        try:
            num_int = int(num)
            num_int1 = num_int
        except:
            print('Isso não é um número inteiro.')

    if contador == 2:
        try:
            num_int = int(num)
            num_int2 = num_int
        except:
            print('Isso não é um número inteiro.')
        
        print(menu)
        operacao = input('Selecione a operação desejada: ')
        
        if len(operacao) > 1:
            operacao = operacao[0]
        if operacao not in operacoes:
            print('Operador inválido.')
        else:
            (operacao_nome, operacao_func) = operacoes[operacao]
            print(f'A {operacao_nome} entre {num_int1} e {num_int2} é de {operacao_func(num_int1, num_int2)}')
            # print('Resultado:', eval(f'{num_int1} {operacao} {num_int2}'))

