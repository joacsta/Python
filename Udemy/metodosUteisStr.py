# frase = '050.657.861-51'

# frase_dividida = frase.split('.')

# print(frase_dividida)

frase1 = "   Python ; SQL ; Java   "

lista_separada = [linguagens.strip() for linguagens in frase1.strip().split(";")]
lista_junta = ' | '.join(lista_separada)

print(lista_separada)
print(lista_junta)