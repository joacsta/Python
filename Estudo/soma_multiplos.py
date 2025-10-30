#multiplos de 3 e 5

x = 0
y = 0
n = int(input())
#multiplos=[]

if n < 0:
    print("Fim")
while x < n:        
    x += 1
    if x % 3  == 0 or x % 5 == 0:
        y += x
        print(x,end=" ")
        
print("\nSoma dos múltiplos:", y)