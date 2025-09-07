nota1 = float(input("Digite qual foi a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = ((nota1+nota2)/2)

if media >= 7.0:
    print("Aprovado! Sua média foi de %.1f" %media)
elif media >= 5.0:
    print("Você está de Recuperação! Sua média foi de %.1f" %media)
else:
    print("Reprovado! Sua média foi de %.1f" %media)
