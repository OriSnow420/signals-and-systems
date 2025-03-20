import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)


def fun_1(x):
    return np.piecewise(
        x,
        [(x <= -2) & (x > 1), (x > -2) & (x <= 0), (x > 0) & (x <= 1)],
        [lambda x: 0, lambda x: 0.5 * x + 1, lambda x: 1]
    )


def fun_2(x):
   return np.piecewise(
       x, 
       [(x < -1.5) & (x > 1.5), (x >= -1.5) & (x < -0.5), (x >= -0.5) & (x < 1), (x >= 1) & (x <= 2)],
       [lambda x: 0, lambda x: 1, lambda x: -1, lambda x: x - 2]
   )


fig, axs = plt.subplots(1, 3, figsize=(15, 5))

draw_fun(axs[0], fun_1, np.linspace(-2, 2, 400), r"$f_1(t)$")
draw_fun(axs[1], fun_2, np.linspace(-2, 2, 400), r"$f_2(t)$")

draw_convolve(axs[2], fun_1, fun_2, -2, 1, -1.5, 2, r"$f_1*f_2(t)$", [0, -1, 2, 3-1e-4])
# draw_fun(axs[2], np_convolution(fun_1, fun_2), np.linspace(-4, 4, 400), r"$f_1*f_2$", [-1, 0, 2, 3])

file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
