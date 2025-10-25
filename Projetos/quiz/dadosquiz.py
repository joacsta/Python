import json
import random as r

quiz_JSON = """
[
    {
        "pergunta": "Qual é a capital do Japão?",
        "opcoes": ["Pequim", "Seul", "Tóquio", "Bangkok"],
        "resposta": "Tóquio"
    },
    {
        "pergunta": "Quanto é 2 + 2?",
        "opcoes": ["3", "4", "5", "8"],
        "resposta": "4"
    },
    {
        "pergunta": "Qual elemento químico tem o símbolo 'Au'?",
        "opcoes": ["Prata", "Ouro", "Cobre"],
        "resposta": "Ouro"
    },
    {
        "pergunta": "Quem pintou a Mona Lisa?",
        "opcoes": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "resposta": "Leonardo da Vinci"
    },
    {
        "pergunta": "Em que ano o Titanic afundou?",
        "opcoes": ["1905", "1912", "1918", "1923"],
        "resposta": "1912"
    },
    {
        "pergunta": "Qual é a organela celular responsável pela respiração celular (a 'casa de força' da célula)?",
        "opcoes": ["Núcleo", "Ribossomo", "Mitocôndria", "Lisossomo", "Cloroplasto"],
        "resposta": "Mitocôndria"
    },
    {
        "pergunta": "Quem escreveu a obra 'Dom Quixote'?",
        "opcoes": ["William Shakespeare", "Miguel de Cervantes", "Dante Alighieri"],
        "resposta": "Miguel de Cervantes"
    },
    {
        "pergunta": "Qual é o maior planeta do nosso sistema solar?",
        "opcoes": ["Terra", "Marte", "Júpiter", "Saturno"],
        "resposta": "Júpiter"
    },
    {
        "pergunta": "Qual país sediou a primeira Copa do Mundo de Futebol em 1930?",
        "opcoes": ["Brasil", "Itália", "Uruguai"],
        "resposta": "Uruguai"
    },
    {
        "pergunta": "O que significa a sigla 'HTML' em desenvolvimento web?",
        "opcoes": [
            "HyperText Markup Language",
            "High-Tech Modern Language",
            "Hyperlink and Text Markup Language",
            "Home Tool Markup Language"
        ],
        "resposta": "HyperText Markup Language"
    },
    {
        "pergunta": "Qual das seguintes cidades não é uma capital de estado do Brasil?",
        "opcoes": ["Boa Vista", "Macapá", "Campinas", "Florianópolis"],
        "resposta": "Campinas"
    }
]
"""

quiz_dict = json.loads(quiz_JSON)

