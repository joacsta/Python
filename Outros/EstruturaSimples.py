A=input("Informe um valor para a variável A: ")
B=input("Informe um valor para a variável B: ")

if (A>B):
    aux=A; 
    A=B;    #variavel auxiliar para trocar os valores
    B=aux;

print("\nO valor da variável A agora é:", A)
print("O valor da variável B agora é:", B)

