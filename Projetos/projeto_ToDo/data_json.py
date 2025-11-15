import json

lista_tarefas_json =""" 
    [
        {
            "tarefas": "fazer uma coisa",
            "tarefa_concluida": false
        },
        {
            "tarefas": "fazer tal coisa",
            "tarefa_concluida": false
        },
        {
            "tarefas": "fazer mais uma coisa",
            "tarefa_concluida": false
        },
        {
            "tarefas": "fazer outra coisa",
            "tarefa_concluida": false
        }
    ]
"""

visualizar_tarefas_json = json.loads(lista_tarefas_json)