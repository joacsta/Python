import os

mensagens = [] #--> isso é uma lista
nome = input("Nome do usuário: ")

while True:

    os.system("clear")

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
            
    print("-----------")
    
    texto = input("Digite aqui sua mensagem: ")
    if texto == 'fim' or texto == 0:
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
                    }) 
        


        

