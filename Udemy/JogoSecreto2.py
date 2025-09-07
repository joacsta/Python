import os

palavra_secreta = 'hidroponica'
tentativas = 0
letra_acertada = ''

while True:

    entrada = input('Digite a letra para ver se faz parte da palavra: ')
    tentativas += 1


    if len(entrada) == len(palavra_secreta) and entrada == palavra_secreta:
        if tentativas > 0:
            os.system('clear')
            print(f'você descobriu a palavra apenas com {tentativas} tentativas! parabéns!!')
            break

    if len(entrada) > 1:
        print('digite APENAS uma letra')
        continue

    if entrada in palavra_secreta:
        letra_acertada += entrada
    
    palavra_ocultada = ''
    for i in palavra_secreta:
        if i in letra_acertada:
            palavra_ocultada += i
        else:
            palavra_ocultada += '*'

    print(palavra_ocultada)

    if palavra_ocultada == palavra_secreta:
        os.system('clear')
        print('parabéns, você concluiu o jogo!')
        print(f'total de tentativas: {tentativas}')
        break