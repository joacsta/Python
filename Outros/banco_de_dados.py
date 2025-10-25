import sqlite3

conexao = sqlite3.connect('tarefas.db')
cursor = conexao.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tarefas(
        id INTEGER PRIMARY KEY,
        descricao TEXT NOT NULL
        )
    """)

cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", ("Estudar Dataclasses",))
cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", ("Testar o sqlite3",))
conexao.commit()

print('minhas tarefas')
for linha in cursor.execute('SELECT id, descricao FROM TAREFAS'):
    print(linha)

conexao.close()