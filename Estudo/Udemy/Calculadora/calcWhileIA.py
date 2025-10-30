print("\n|| CALCULADORA DE NÚMEROS INTEIROS ||")

while True:
    num1 = input("Digite o primeiro número inteiro: ")
    try:
        num1 = int(num1)
    except:
        print("Isso não é um número inteiro. Tente novamente.")

while True:
    num2 = input("Digite o segundo número inteiro: ")
    try:
        num2 = int(num2)
    except:
        print("Isso não é um número inteiro. Tente novamente.")

print("\nOperações disponíveis:")
print(" '+' para Adição")
print(" '-' para Subtração")
print(" '*' para Multiplicação")
print(" '/' para Divisão")

while True:
    operacao = input("Selecione a operação desejada: ")
    if operacao in '+-*/':
        break
    print("Operador inválido. Tente novamente.")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 == 0:
        resultado = "Erro: divisão por zero."
    else:
        resultado = num1 / num2

print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
