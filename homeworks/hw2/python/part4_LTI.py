import sys

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *


def fun(x):
    return np.piecewise(
        x,
        [(x < 0) & (x > 2), (x >= 0) & (x < 1), (x >= 1) & (x <= 2)],
        [lambda x: 0, lambda x: 2 * x, lambda x: 4 - 2 * x],
    )


plt.rc("text", usetex=True)

fig, axs = plt.subplots(2)

draw_fun(
    axs[0],
    lambda x: fun(x) - fun(x - 2),
    np.linspace(-0.5, 4.5, 400),
    r"$y_2(t)$",
    [],
    False,
    r"$t$",
    r"$y_2(t)$",
)

draw_fun(
    axs[1],
    lambda x: fun(x + 1) + 0.5 * fun(x),
    np.linspace(-1.5, 2.5, 400),
    r"$y_3(t)$",
    [],
    False,
    r"$t$",
    r"$y_3(t)$",
)

plt.tight_layout()
plt.savefig("../images/part4_LTI.png")
plt.show()
