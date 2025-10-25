def executa(funcao, *args):
    return funcao(*args)

def soma(a, b):
    return a + b

print(
    executa(lambda x,y: x + y, 2,3)
    ,executa(soma, 2,3)
)

