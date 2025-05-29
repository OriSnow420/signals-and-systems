import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *
import math

plt.rc("text", usetex=True)


def base_fun(x):
    return np.cos(2 * np.pi * x) * np.exp(-x)


def fun_1(x):
    return np.piecewise(
        x,
        [
            (x >= 0) & (x <= 1.25),
            (x > 1.25) & (x <= 2.5),
            (x >= -1.25) & (x < 0),
            (x >= -2.5) & (x < -1.25),
        ],
        [
            base_fun,
            lambda x: -base_fun(2.5 - x),
            lambda x: -base_fun(-x),
            lambda x: base_fun(x + 2.5),
        ],
    )


def fun_2(x):
    return np.piecewise(
        x,
        [
            (x >= 0) & (x <= 1.25),
            (x > 1.25) & (x <= 2.5),
            (x >= -1.25) & (x < 0),
            (x >= -2.5) & (x < -1.25),
        ],
        [
            base_fun,
            lambda x: -base_fun(2.5 - x),
            lambda x: base_fun(-x),
            lambda x: -base_fun(x + 2.5),
        ],
    )


fig, axs = plt.subplots(1, 2, figsize=(10, 5))

draw_fun(axs[0], fun_1, np.linspace(-2.5, 2.5, 400), r"(1)")
draw_fun(axs[1], fun_2, np.linspace(-2.5, 2.5, 400), r"(2)")

file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
