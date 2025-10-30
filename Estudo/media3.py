def notas():
    n = float(input())
    return n

def media(n1, n2, n3, n4):
    
    notamedia=((n1*2)+(n2*3)+(n3*4)+(n4*1)) / 10
    print("Media: %.1f" %notamedia)

    if notamedia < 5.0:
        print("Aluno reprovado.")
    elif notamedia < 6.9:
        print("Aluno em exame.")
        notaexame=float(input(""))
        print("Nota do exame:", notaexame)
        mediafinal=(notaexame + notamedia) / 2
        if mediafinal > 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print("Media final: %.1f" %mediafinal)

    elif notamedia > 7.0:
        print("Aluno aprovado.")

a=notas()
b=notas()
c=notas()
d=notas()

media(a,b,c,d)
