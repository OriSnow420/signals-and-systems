import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)


def fun_1(x):
    return ((2**0.5) * 2) * (
        np.heaviside(x - 2, 1)
        - np.heaviside(x - 4, 0)
        + np.heaviside(x + 4, 1)
        - np.heaviside(x + 2, 0)
    )


def fun_2(x):
    return (np.pi / 4) * (
        np.heaviside(x - 2, 1)
        - np.heaviside(x - 4, 0)
        - np.heaviside(x + 4, 1)
        + np.heaviside(x + 2, 0)
    )


fig, axs = plt.subplots(1, 2, figsize=(10, 5))

draw_discrete_signal(axs[0], fun_1, np.array(range(-7, 7)), r"$|F_n|$")
draw_discrete_signal(axs[1], fun_2, np.array(range(-7, 7)), r"$\theta_n$")


file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
