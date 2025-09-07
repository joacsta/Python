import math
import matplotlib.pyplot as plt

A_0 = 0.0
B_0 = 1.0
T_FINAL = 8.0
h = 0.1
h_exato = 0.01  # passo menor para solução exata

# edo: dy/dt = sin²(t) * y
def f(a, b):
    return math.sin(a)**2 * b

# euler (RungeKutta de ordem 1)
def euler(a_i, b_i, da, f):
    return b_i + da * f(a_i, b_i)

# RungeKutta de ordem 2
def rk2(a_i, b_i, da, f):
    k1 = f(a_i, b_i)
    k2 = f(a_i + da/2, b_i + k1*da/2)
    return b_i + da * k2

# RungeKutta de ordem 3
def rk3(a_i, b_i, da, f):
    k1 = f(a_i, b_i)
    k2 = f(a_i + da/2, b_i + k1*da/2)
    k3 = f(a_i + da, b_i - da*k1 + 2*da*k2)
    return b_i + da/6 * (k1 + 4*k2 + k3)

# RungeKutta de ordem 4
def rk4(a_i, b_i, da, f):
    k1 = f(a_i, b_i)
    k2 = f(a_i + da/2, b_i + k1*da/2)
    k3 = f(a_i + da/2, b_i + k2*da/2)
    k4 = f(a_i + da, b_i + k3*da)
    return b_i + da/6 * (k1 + 2*k2 + 2*k3 + k4)

# solucao exata
def y_exato(t_0, y_0, t):
    exp_arg = 1/2 * ((t-t_0) - (math.sin(t) * math.cos(t) - math.sin(t_0) * math.cos(t_0)))
    return y_0 * math.exp(exp_arg)

# calculo da solucao exata p plotagem
t_exato = A_0
bs_exato = []
as_exato = []

while t_exato <= T_FINAL:
    as_exato.append(t_exato)
    bs_exato.append(y_exato(A_0, B_0, t_exato))
    t_exato += h_exato

#métodos numéricos
ts = [A_0]
ys_rk2 = [B_0]
ys_rk3 = [B_0]
ys_rk4 = [B_0]

# PVI
y_rk2 = B_0
y_rk3 = B_0
y_rk4 = B_0
t = A_0

# aplicacao dos metodos numéricos
while t < T_FINAL:
    y_rk2 = rk2(t, y_rk2, h, f)
    y_rk3 = rk3(t, y_rk3, h, f)
    y_rk4 = rk4(t, y_rk4, h, f)
    
    t += h
    
    ts.append(t)
    ys_rk2.append(y_rk2)
    ys_rk3.append(y_rk3)
    ys_rk4.append(y_rk4)

# plotagem
plt.figure(figsize=(10, 6))
plt.plot(ts, ys_rk2, color="green", marker="o", linestyle="", label='RK2 (Ponto Médio)')
plt.plot(ts, ys_rk3, color="orange", marker="s", linestyle="", label='RK3')
plt.plot(ts, ys_rk4, color="red", marker="^", linestyle="", label='RK4')
plt.plot(as_exato, bs_exato, color="blue", linestyle="-", label='Solução Exata')

plt.title('Comparação de Métodos Runge-Kutta (h=0.1)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()

#rungekutta de ordem 4 é o mais próximo da solucao exata.