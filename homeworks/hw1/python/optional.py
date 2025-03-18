import sys
sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc('text', usetex=True)


def fun1(x):
    return np.exp(-x / (1e-6)) * 1e3

def fun2(x):
    return np.sinc(x) * np.sinc(x / 3.0) * np.sinc(x / 5.0) * np.sinc(x / 7.0)

def fun3(x):
    return np.sinc(5e-2 * np.pi * x)

def fun4(x):
    return np.sin(2 * np.pi / x) * np.heaviside(x, 0.5)

def fun5(x):
    # print(x - np.floor(x))
    return 1.0 / (x - np.floor(x) + 1e-6)

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
draw_fun(axs[0][0], fun1, np.linspace(0, 1e-5, 400), "Optional(1)", [], False, r"$t/\mathrm{s}$", r"$U_\mathrm{out}(t)/\mathrm{V}$")

draw_fun(axs[0][1], fun2, np.linspace(-5, 5, 400), "Optional(2)", [0])

draw_discrete_signal(axs[0][2], fun3, np.array(range(-20, 20)), "Optional(3)", [0])

draw_fun(axs[1][0], fun4, np.linspace(-2, 6, 4000), "Optional(4)", [0.8, 4.0])

draw_fun(axs[1][1], fun5, np.linspace(-2.8, 2.5, 400), "Optional(5)", [-1e-6])

axs[1][1].set_ylim(0, 10)
fig.delaxes(axs[1][2])

plt.tight_layout()
plt.savefig("../images/optional.png")
plt.show()
