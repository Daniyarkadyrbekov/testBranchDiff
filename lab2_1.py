import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * np.exp(x)

def diff2(x_0,h,f):
    difF2 = ((1/(2*h))*f(x_0+h))-((1/(2*h))*f(x_0-h))
    return difF2

def diff4(x_0, h, f):
    A = 1 / (12 * h)
    B = -2 / (3 * h)
    C = 0
    D = -B
    E = -A

    difF4 = A * f(x_0 - 2 * h) + B * f(x_0 - h) + C * f(x_0) + D * f(x_0 + h) + E * f(x_0 + 2 * h)

    return difF4

def derivative(x_0, h, f, func):
    n = len(h)
    # g = []
    g = np.copy(h)

    for i in range(n - 1):
        g[i] = func(x_0, h[i], f)

    return g

num = 113
x_0 = 2

h = np.logspace(-16, 0, 70, endpoint=True)

real_g = x_0 * np.exp(x_0) + np.exp(x_0)
g_diff2 = derivative(x_0, h, f, diff2)
g_diff4 = derivative(x_0, h, f, diff4)

E_diff2 = np.abs(g_diff2 - real_g)
E_diff4 = np.abs(g_diff4 - real_g)

n1_1 = h[:47]
n1_2 = h[46:]
h1_1 = 2 / n1_1 / 10 ** 16;
h1_2 = n1_2 ** 2  # /10**16);

n2_1 = h[:57]
n2_2 = h[56:]
h2_1 = 2 / n2_1 / 10 ** 16;
h2_2 = n2_2 ** 4 / 7  # /10**16);

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes[0].loglog(h, E_diff2, 'or', label="$E_{diff2}$")
axes[0].loglog(n1_1, h1_1, '--', linewidth=1.5, label="$h^{-1}$")
axes[0].loglog(n1_2, h1_2, 'b', linewidth=1.5, label="$h^{2}$")
axes[0].legend(loc='upper right')
axes[0].grid(True)
axes[0].set_xlabel('$h$')
axes[0].set_ylabel('$E$')

axes[1].loglog(h, E_diff4, 'or', label="$E_{diff4}$")
axes[1].loglog(n2_1, h2_1, '--', linewidth=1.5, label="$h^{-1}$")
axes[1].loglog(n2_2, h2_2, 'b', linewidth=1.5, label="$h^{4}$")
axes[1].legend(loc='upper right');
axes[1].grid(True)
axes[1].set_xlabel('$h$')
axes[1].set_ylabel('$E$')

fig.savefig("lab2_1.pdf")