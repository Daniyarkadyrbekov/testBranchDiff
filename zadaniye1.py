import math
import numpy as np
import matplotlib.pyplot as plt

a = -1 # left border
b = 1 # right border
n = 10 # number of approximation nodes
pn = 100 # number of plot nodes

def f(x):
    return (1 / (1 + 25 * (x ** 2)))

def l_i(i, x, x_nodes):
    numerator = 1
    denominator = 1
    for j in range(n):
        if j != i:
            numerator *= x - x_nodes[j]
            denominator *= x_nodes[i] - x_nodes[j]
    return numerator / denominator

def L(x, x_nodes, y_nodes):
    l = 0
    for i in range(n):
        l += y_nodes[i] * l_i(i, x, x_nodes)
    return l

def chebish(i, n):
    return math.cos((i + 0.5) * math.pi / n)

plotX = np.linspace(a, b, pn)
plotY = np.array([f(i) for i in plotX])

aproxX = np.linspace(a, b, n)
aproxY = np.array([f(i) for i in aproxX])

chebX = np.copy(aproxX)
for i in range(n):
    chebX[i] = chebish(i, n)
chebY = np.array([f(i) for i in chebX])

lY = np.array([L(i, aproxX, aproxY) for i in plotX])
lchebY = np.array([L(i, chebX, chebY) for i in plotX])

fig, ax = plt.subplots()
ax.plot(plotX, plotY, 'r', label="Function")
ax.plot(plotX, lY, 'b', label="Polynomial")
ax.plot(aproxX, aproxY, 'o', label="Polynomial")
ax.legend(loc='upper left')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Result')
plt.grid()
plt.show()

fig, ax = plt.subplots()
ax.plot(plotX, plotY, 'r', label="Function")
ax.plot(plotX, lchebY, 'b', label="Polynomial(Cheb nodes)")
ax.plot(chebX, chebY, 'o', label="Cheb nodes")
ax.legend(loc='upper left')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Result')
plt.grid()
plt.show()
