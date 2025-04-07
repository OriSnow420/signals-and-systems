import sys

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *
import os

plt.rc("text", usetex=True)


def fun_1(x):
    return np.piecewise(
        x,
        [x <= -1, (x > -1) & (x <= 0), (x > 0) & (x <= 0.5), x > 0.5],
        [lambda x: 0, lambda x: x + 1, lambda x: 1, lambda x: 0],
    )

fig, ax = plt.subplots(1, 1)

draw_fun(ax, get_even(fun_1), np.linspace(-2, 2, 400), r"$R(-\omega)$'s inverse fourier transform")

file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
