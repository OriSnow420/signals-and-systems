import sys

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)


def fun_1(x):
    return 2 * np.exp(-x / 3.0) * np.heaviside(x, 0.5)


def fun_2(x):
    return np.cos(2 * np.pi * x) * np.heaviside(-x, 0.5)


def fun_3(x):
    return np.exp(-x / 15.0) * np.sin(np.pi * x) * np.heaviside(x, 0.5)


def fun_5(x):
    return np.sin(0.1 * np.pi * x) * np.exp(-x / 15.0) * np.heaviside(x, 1)


def fun_6(x):
    return np.sin(np.pi / 5.0 * (x**2))


fig, axs = plt.subplots(2, 3, figsize=(15, 10))
draw_fun(
    axs[0][0],
    fun_1,
    np.linspace(-2, 6, 400),
    r"$f(t) = 2 e^{- \frac{t}{3}} \cdot u(t)$",
    [1e-6],
)

draw_fun(
    axs[0][1],
    fun_2,
    np.linspace(-6, 2, 400),
    r"$f(t)=\cos{2\pi t}\cdot u(-t)$",
    [-4, -1.5],
)

draw_fun(axs[0][2], lambda x: np.exp(-x / 15.0), np.linspace(-2, 50, 400), "", [], True)

draw_fun(
    axs[0][2], lambda x: -np.exp(-x / 15.0), np.linspace(-2, 50, 400), "", [], True
)

draw_fun(
    axs[0][2],
    fun_3,
    np.linspace(-2, 50, 400),
    r"$f(t)=e^{-\frac{t}{15}}\cdot\sin(\pi t)\cdot u(t)$",
)

draw_dirac(axs[1][0], r"$f(t)=\delta [\cos(2\pi t)]$", np.array(range(-2, 3)) + 0.5)

draw_discrete_signal(
    axs[1][1],
    fun_5,
    np.array(range(-2, 50)),
    r"$f[n]=\sin(0.1\pi\cdot n)\cdot e^{-\frac{n}{15}}\cdot u[n]$",
)

draw_discrete_signal(
    axs[1][2],
    fun_6,
    np.array(range(-3, 20)),
    r"$f[n]=\sin{\left(\frac{\pi}{5}\cdot n^2\right)}$",
    [2, 7],
)

plt.savefig("../images/essential.png")
plt.tight_layout()
plt.show()
