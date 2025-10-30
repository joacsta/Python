linguagens=[] #Lista vazia
linguagens.append("Java");
linguagens.append("Python");
linguagens.append("PHP");
linguagens.append("C");
#a função .append add o termo no final da lista

print("Linguagens:", linguagens)

linguagem = linguagens.pop(1)
#operação classica de pilhas
#mas da pra usar pra remover o append

print("Elemento removido: " + linguagem)

print("Linguagens:", linguagens)