def gerador_de_numeros(maximo):
    print("Iniciando o gerador...")
    numero_atual = 0
    while numero_atual < maximo:
        print(f"Produzindo o {numero_atual}")
        yield numero_atual # 1. Pausa a função e entrega o valor
        numero_atual += 1  # 2. Quando chamado de novo, continua daqui

# --- Como usar ---
print("Criando o gerador (nada foi executado ainda)...")
meu_gerador = gerador_de_numeros(3)
print(type(meu_gerador))

print("\n--- Puxando o primeiro item ---")
print(f"Recebido: {next(meu_gerador)}")

print("\n--- Puxando o segundo item ---")
print(f"Recebido: {next(meu_gerador)}")

print("\n--- Usando em um 'for' loop (o loop 'puxa' automaticamente) ---")
# O loop vai puxar o resto dos itens, um por um
for numero in meu_gerador:
    print(f"Recebido no loop: {numero}")