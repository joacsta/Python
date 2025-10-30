def meu_decorator(funcao):
    def wrapper():
        print('antes da funcao')
        funcao()
        print('depois da funcao')
    return wrapper

@meu_decorator
def minha_funcao():
    print('executando minha funcao...')

minha_funcao()