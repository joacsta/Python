class Main:
    pass

print("Testando o projeto...")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("João", "99925-8489")
conta = Conta(c1._nome, 6565, 0)

#print(c1)
print("Nome:", c1._nome)
print("Telefone:", c1._telefone)
print("|", conta.titular, "| ID:", conta.numero, "| Saldo: R$", conta.saldo, "|")