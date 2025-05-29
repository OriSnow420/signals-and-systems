# cSpell:words mathcal mathrm
import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)


def s_fun_1(x):
    return (x - 3) / (x + 1)


def s_fun_2(x):
    return x / ((x + 0.5 - 1.0j) * (x + 0.5 + 1.0j))


fig, axs = plt.subplots(2, 2, figsize=(15, 10))

draw_fun(
    axs[0][0],
    get_amplitude(s_fun_1),
    np.linspace(-10, 10, 400),
    r"(3)$|\mathcal F(\omega)|$",
    [],
    False,
    r"$\omega$",
    r"$|\mathcal F(\omega)|$",
)

draw_fun(
    axs[1][0],
    get_amplitude(s_fun_2),
    np.linspace(-10, 10, 400),
    r"(4)$|\mathcal F(\omega)|$",
    [],
    False,
    r"$\omega$",
    r"$|\mathcal F(\omega)|$",
)

draw_fun(
    axs[0][1],
    get_angle(s_fun_1),
    np.linspace(-10, 10, 400),
    r"(3)$\mathrm{Arg}\mathcal F(\omega)$",
    [],
    False,
    r"$\omega$",
    r"$\mathrm{Arg}\mathcal F(\omega)$",
)

draw_fun(
    axs[1][1],
    get_angle(s_fun_2),
    np.linspace(-10, 10, 400),
    r"(4)$\mathrm{Arg}\mathcal F(\omega)$",
    [],
    False,
    r"$\omega$",
    r"$\mathrm{Arg}\mathcal F(\omega)$",
)

file_name, _ = os.path.splitext(os.path.basename(__file__))
os.makedirs("../images", exist_ok=True)
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
