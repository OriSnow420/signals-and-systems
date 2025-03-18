import sys
sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc('text', usetex=True)

def fun_1(x):
    return np.piecewise(x, [
        x <= -1, (x > -1) & (x <= 0), (x > 0) & (x <= 0.5), x > 0.5
    ], [
        lambda x : 0, lambda x : x + 1, lambda x : 1, lambda x : 0
    ])

def fun_2(x):
    return np.piecewise(x, [
        x <= -4, (x > -4) & (x <= 0), (x > 0) & (x < 4), x >= 4
    ], [
        lambda x: 0, lambda x: x + 4, lambda x: 2, lambda x: 0
    ])

fig, axs = plt.subplots(2,2)

draw_fun(axs[0][0], get_odd(fun_1), np.linspace(-2, 2, 400), r"(1)$f_o(t)$")
draw_fun(axs[0][1], get_even(fun_1), np.linspace(-2, 2, 400), r"(1)$f_e(t)$")

draw_discrete_signal(axs[1][0], get_odd(fun_2), np.array(range(-5, 6)), r"(2)$f_o[n]$")
draw_discrete_signal(axs[1][1], get_even(fun_2), np.array(range(-5, 6)), r"(2)$f_e[n]$")

plt.tight_layout()
plt.savefig("../images/part2_essential.png")
plt.show()
