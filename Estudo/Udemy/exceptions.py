# introduçaõ try/except

# try -> tenta executar um codigo
# except -> ocorreu algum erro ao tentar executar

numero_s = input('Digite um número: ')
  
try:
    print('STR:', numero_s)
    numero_f = float(numero_s)
    print('Float:', numero_f)
    print(f'o dobro de {numero_s} é {numero_f * 2}!')
except:
    print('isso não é um número.')