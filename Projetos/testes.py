# def nome():
#     name = input('Poderia nos dizer seu nome? ')
#     return name

# def intro():
#     name = nome()
#     print('Olá {}, seja bem vindo!'.format(name))


# intro()
# import random as r

# def gerador_cpf():
#     novo_cpf = ''
#     for i in range(11):
#         novo_cpf += str(r.randint(0,9))
#     print(novo_cpf)

# gerador_cpf()

# random_number = r.randint(1,9)
# empty_array_w_random_size = [None] * random_number

# for i in range(random_number):
#     empty_array_w_random_size[i] = r.randint(0,9)

# print(empty_array_w_random_size)

lista_de_tarefas = ['pao', 'quejo', 'alface', 'cebola', 'tomate']

for index, item in enumerate(lista_de_tarefas):
    index += 1
    print(f'[{index}] - {item} ()')