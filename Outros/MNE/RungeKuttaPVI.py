import math
import matplotlib.pyplot as plt

A_0 = 0.0       
B_0 = 1.0       
T_FINAL = 2.0    # y(4.0)
DT = 0.1        
DT_EXATO = 0.01 

#y'(x) = 1 - x + 4y
def f(x, y):
    return 1 - x + 4*y

def rk2(x_i, y_i, dx, f):
    k1 = f(x_i, y_i)
    k2 = f(x_i + dx/2, y_i + k1*dx/2)
    return y_i + dx * k2

def rk3(x_i, y_i, dx, f):
    k1 = f(x_i, y_i)
    k2 = f(x_i + dx/2, y_i + k1*dx/2)
    k3 = f(x_i + dx, y_i - dx*k1 + 2*dx*k2)
    return y_i + dx/6 * (k1 + 4*k2 + k3)

def rk4(x_i, y_i, dx, f):
    k1 = f(x_i, y_i)
    k2 = f(x_i + dx/2, y_i + k1*dx/2)
    k3 = f(x_i + dx/2, y_i + k2*dx/2)
    k4 = f(x_i + dx, y_i + k3*dx)
    return y_i + dx/6 * (k1 + 2*k2 + 2*k3 + k4)

def y_exato(x):
    # Esta é a solução analítica da EDO y' = 1 - x + 4y
    return (1/16)*(4*x - 3 + 19*math.exp(4*x))

xs = [A_0]
ys_rk2 = [B_0]
ys_rk3 = [B_0]
ys_rk4 = [B_0]
ys_exato = [B_0]

y_rk2 = B_0
y_rk3 = B_0
y_rk4 = B_0
x = A_0

# métodos numéricos até x = 4.0
while x < T_FINAL:
    y_rk2 = rk2(x, y_rk2, DT, f)
    y_rk3 = rk3(x, y_rk3, DT, f)
    y_rk4 = rk4(x, y_rk4, DT, f)
    
    x += DT
    
    xs.append(x)
    ys_rk2.append(y_rk2)
    ys_rk3.append(y_rk3)
    ys_rk4.append(y_rk4)
    ys_exato.append(y_exato(x))

print(f"resultado em x = 4.0:")
print(f"RK2: {ys_rk2[-1]}")
print(f"RK3: {ys_rk3[-1]}")
print(f"RK4: {ys_rk4[-1]}")
print(f"solucao exata: {ys_exato[-1]}")

plt.figure(figsize=(10, 6))
plt.plot(xs, ys_rk2, color="green", marker="o", linestyle="", label='RK2 (Ponto Médio)')
plt.plot(xs, ys_rk3, color="orange", marker="s", linestyle="", label='RK3')
plt.plot(xs, ys_rk4, color="red", marker="^", linestyle="", label='RK4')
plt.plot(xs, ys_exato, color="blue", linestyle="-", label='Solução Exata')

plt.title('Solução do PVI: y\' = 1 - x + 4y, y(0) = 1')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
plt.show()