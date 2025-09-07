class Banco:
    def __init__(self, nome, saldo_atual, id):
        self.nome=nome
        self.saldo_atual=saldo_atual
        self.id=id

    def exibir_saldo(self):
        print(f"ID do usuário: {self.id}")
        print(f"Saldo atual: R$ {self.saldo_atual}\n") #mostra o saldo atual
    
    def deposito(self, deposito):
        self.saldo_atual += deposito #adicionando valor ao saldo
        print(f"Seu valor de R${deposito} foi acrescido!\nSeu saldo atual é de: R${self.saldo_atual}\n")
        self.exibir_saldo

    def saque(self, saque):
        if saque > self.saldo_atual:
            print("Saldo insuciente.")
        else:
            self.saldo_atual -= saque
            print(f"Saque de R${saque} realizado com sucesso! Seu saldo atual é de: R${self.saldo_atual}")

#conta1=Banco("Joao", 602, 29)
#conta1.saque(604)
#conta1.deposito(73)
#conta1.saque(604)
#onta1.exibir_saldo()