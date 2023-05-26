import numpy as np
import matplotlib.pyplot as plt


def ysol(x):
    ye = np.exp(np.sin(x))

    return ye


def edo(x0, y0):
    dy = y0*np.cos(x0)

    return dy


def k1(x0, y0, h):
    k1_value = (edo(x0, y0)*h)

    return k1_value


def k2(x0, y0, h):
    k2_value = (edo(x0 + h/2, y0 + k1(x0, y0, h)/2)*h)

    return k2_value


def k3(x0, y0, h):
    k3_value = (edo(x0 + h/2, y0 + k2(x0, y0, h)/2)*h)

    return k3_value


def k4(x0, y0, h):
    k4_value = (edo(x0 + h, y0 + k3(x0, y0, h))*h)

    return k4_value


def y(x0, y0, h):
    y_value = y0 + ((k1(x0, y0, h) + 2*k2(x0, y0, h) +
                    2*k3(x0, y0, h) + k4(x0, y0, h))/6)

    return y_value


ye1 = ysol(0.1)
ye2 = ysol(0.2)
ye3 = ysol(0.3)
ye4 = ysol(0.4)
ye5 = ysol(0.5)
ye6 = ysol(0.6)
ye7 = ysol(0.7)
ye8 = ysol(0.8)
ye9 = ysol(0.9)
ye10 = ysol(1)

y0 = 1
y1 = y(0, 1, 0.1)
y2 = y(0.1, y1, 0.1)
y3 = y(0.2, y2, 0.1)
y4 = y(0.3, y3, 0.1)
y5 = y(0.4, y4, 0.1)
y6 = y(0.5, y5, 0.1)
y7 = y(0.6, y6, 0.1)
y8 = y(0.7, y7, 0.1)
y9 = y(0.8, y8, 0.1)
y10 = y(0.9, y9, 0.1)

print("Soluções exatas para x entre 0.1 e 1")
print("-"*50)
print(f"ye1 = {ye1}\nye2 = {ye2}\nye3 = {ye3}\nye4 = {ye4}\nye5 = {ye5}\nye6 = {ye6}\nye7 = {ye7}\nye8 = {ye8}\nye9 = {ye9}\nye10 = {ye10}\n")

print("Soluções aproximadas o usando o método RK4")
print("-"*50)

print(f"y1 = {y1}\ny2 = {y2}\ny3 = {y3}\ny4 = {y4}\ny5 = {y5}\ny6 = {y6}\ny7 = {y7}\ny8 = {y8}\ny9 = {y9}\ny10 = {y10}\n")

print("Diferença entre as soluções")
print("-"*50)
print(f"dif1 = {ye1-y1}\ndif2 = {ye2-y2}\ndif3 = {ye3-y3}\ndif4 = {ye4-y4}\ndif5 = {ye5-y5}\ndif6 = {ye6-y6}\ndif7 = {ye7-y7}\ndif8 = {ye8-y8}\ndif9 = {ye9-y9}\ndif10 = {ye10-y10}\n")


x = np.arange(0, 1.1, 0.1)
y = ysol(x)
yk = ([y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10])
fig, varx = plt.subplots()
varx.plot(x, y, label='var 1')
varx.plot(x, yk, label='var 1')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(["RK de ordem 4", "Solução exata"], loc=2)


plt.show()
