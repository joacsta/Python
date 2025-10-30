def notas():
    nota=float(input("Digite sua primeira nota: "))
    return nota

def calcmedia(nota1, nota2):

    media=(nota1 + nota2)/2

    if media >= 7.0:
        print("Aprovado! Sua nota foi de: %.1f" %media)
    else:
        print("Reprovado! Sua nota foi de: %.1f" %media)

a=notas()
b=notas()

calcmedia(a,b)