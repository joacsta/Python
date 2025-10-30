import random as r
import dadosquiz as d

perguntas_acertadas = 0
r.shuffle(d.quiz_dict)

for i, questao in enumerate(d.quiz_dict, 1):
    print(f"{i}) {questao['pergunta']}\n")    
    for j, o in enumerate(questao["opcoes"], 1):
        print(f"    {j}) {o}")
    
    resposta = input("\nResposta: ")

    resposta_certa = False
    if resposta.isdigit():
        try:
            opcao_correta_enumerada = questao["opcoes"].index(questao["resposta"]) + 1
            resposta_certa = True if int(resposta) == opcao_correta_enumerada else False  
        except ValueError:
            resposta_certa = False
    else:
        if resposta.lower().strip() == questao["resposta"].lower().strip():
            resposta_certa = True

    if resposta_certa:
        perguntas_acertadas += 1
        saida_terminal = "Certo! :D"
    else:
        saida_terminal = "Errado! :("

    print(f"\n{saida_terminal}\n")

print(f"Parabéns!\nVocê concluiu o quiz!\nTotal de acertos: {perguntas_acertadas}")