import os

palavra_secreta = 'paralelepipedo'
letras_adivinhadas = ''
tentativas = 0

while True:

    adivinhacao = input('Digite uma letra: ')
    tentativas += 1

    if len(adivinhacao) > 1:
        print('Digite APENAS uma letra: ')
        continue

    if adivinhacao in palavra_secreta:
        letras_adivinhadas += adivinhacao
    
    palavra_ocultada = ''
    for i in palavra_secreta:
        if i in letras_adivinhadas:
            palavra_ocultada += i
        else:
            palavra_ocultada += '*'

    print(palavra_ocultada)

    if palavra_ocultada == palavra_secreta:
        os.system('cls')
        print('PARABÉNS, VOCÊ CONCLUI O JOGO')
        print(f'Você tentou {tentativas} vezes')
        break


