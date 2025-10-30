qtd=0
soma=0
media=0
valor = float(input("Digite um Valor: "))

while (valor > 0.0): #enquanto não digitar 0, os valores vão ser perguntados
    soma = soma+valor
    qtd = qtd+1
    #entrada de valores
    valor = float(input("Digite um valor: "))

media = soma/qtd

print("\nTotal da Soma: ", soma)
print("Quantidade de valores digitados: ", qtd)
print("Média: %.1f\n" %media)