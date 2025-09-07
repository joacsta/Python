class Banco:
    def __init__(self, nome, saldo, id):
        self.nome= nome
        self.saldo= saldo
        self.id= id

        #INSTANCIAS
    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo}")
    
    def exibir_id(self):
        print(f"Nome do cliente: {self.nome}")
        print(f"ID do cliente: {self.id}")

    def deposito(self, depositar):
        self.saldo = self.saldo + depositar
        print(f"Valor de R${depositar} depositado.")
        print(f"Seu saldo atual é de R${self.saldo}")

    def saque(self,sacar):
        if sacar > self.saldo:
            print("AVISO!\nSaldo insuciente em sua conta.")
            print(f"Valor do saque: R${sacar} | Seu saldo atual: R${self.saldo}")
        else:
            self.saldo = self.saldo - sacar
            print(f"Saque de R${sacar} realizado com sucesso!")
            print(f"Saldo atual: R${self.saldo}")

conta1= Banco("Jorge", 146, 12)
conta1.exibir_id()
conta1.exibir_saldo()
conta1.deposito(46)
conta1.saque(10)