class BaseDados:
    def __init__(self):
        self.dados = {}
    
    def inserir_cliente(self, id, nome):
            if 'clientes' not in self.dados:
                self.dados['clientes'] = {id: nome}
            else:
                 self.dados['clientes'].udpate({id: nome})
    def lista_clientes(self):
         for id, nome in self.dados['clientes'].itens():
              print(id, nome)

    def apaga_cliente(self, id):
         del self.dados['clientes'][id]

bd = BaseDados()
bd.dados(1, "joao")
bd.dados(2, "henrique")
