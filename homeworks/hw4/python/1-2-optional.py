import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)


def fun_1(x):
    return np.sin(np.pi * x) * (np.heaviside(x, 0.5) - np.heaviside(x - 1, 0.5))


def fun_2(x):
    return np.piecewise(
        x,
        [(x < 0) & (x > 2), (x >= 0) & (x <= 1), (x > 1) & (x <= 2)],
        [lambda x: 0, lambda x: x, lambda x: 1]
    )


fig, axs = plt.subplots(3, 3, figsize=(10, 6))

for i in range(8):
    draw_fun(axs[i // 3][i % 3], fun_2, np.linspace(-2, 4, 400), r"$t=" + str() + r"$")
    draw_fun(
        axs[i // 3][i % 3],
        lambda x: fun_1(-0.5 + i * 0.5 - x),
        np.linspace(-2, 4, 400),
        r"$t=" + str(i * 0.5 - 0.5) + r"$",
    )

draw_convolve(axs[2][2], fun_2, fun_1, -0.2, 2.2, -0.2, 1.2, r"$f_1*f_2(t)$")

file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
