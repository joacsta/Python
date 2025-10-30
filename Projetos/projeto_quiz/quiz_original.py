import random as r
import dadosquiz as d

perguntas_acertadas = 0

for i, questao in enumerate(d.quiz_dict, 1):
    print(f'{i}) {questao['pergunta']}\n')
    for j, o in enumerate(questao["opcoes"], 1):
        print(f'{j}) {o}')  
    resposta = input('\nResposta: ')
    
    resposta_certa = False
    if resposta.isdigit():
        opcao_correta_enumerada = (questao["opcoes"].index(questao['resposta']) + 1)
        if int(resposta) == int(opcao_correta_enumerada):
            resposta_certa =  True
        else:
            str(resposta) == questao['resposta']
    else:
        if resposta.lower().strip() == questao['resposta'].lower().strip():
            resposta_certa = True
        else:
            resposta_certa = False 
    perguntas_acertadas += 1 if resposta_certa else 0    
    saida_terminal = 'Certo! :D' if resposta_certa else 'Errado! :('

    print(f'\n{saida_terminal}\n')

print(f'parabéns!\nvoce concluiu o quiz!\ntotal de acertos: {perguntas_acertadas}')

    