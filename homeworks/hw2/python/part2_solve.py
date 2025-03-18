import sys
sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc('text', usetex=True)

def fun_1(x):
    return np.piecewise(x, [
        x < -1, (x >= -1) & (x < 0), x >= 0
    ], [
        lambda x: 0, lambda x: 2 * x + 2, lambda x: 0
    ])

def fun_2(x):
    return np.piecewise(x, [
        (x < -1.5) & (x > 1.5), (x >= -1.5) & (x <= -1.0), (x <= 1.5) & (x >= 1.0), (x > -1.0) & (x < 1.0)
    ], [
        lambda x: 0, lambda x: 2 * x + 3, lambda x: -2 * x + 3, lambda x: 1
    ])

fig, axs = plt.subplots(1, 2)

draw_fun(axs[0], fun_1, np.linspace(-1.5, 1.5, 400), r"1.$x(t)$")
draw_fun(axs[1], fun_2, np.linspace(-2, 2, 400), r"2.$x(t)$")

plt.tight_layout()
plt.savefig("../images/part2_solve.png")
plt.show()
