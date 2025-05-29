# cSpell:words mathcal mathrm
import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)


def s_fun_1(x):
    return x / ((x + 1) * (x + 2))


def s_fun_2(x):
    return (x + 150) / (x * x + 2 * x + 1)


def s_fun_3(x):
    return (x * x - x + 3) / (x * x + x + 3)


fig, axs = plt.subplots(3, 2, figsize=(15, 10))

draw_fun(
    axs[0][0],
    get_amplitude(s_fun_1),
    np.linspace(-4, 4, 400),
    r"(1)$|\mathcal F(\omega)|$",
    [],
    False,
    r"$\omega$",
    r"$|\mathcal F(\omega)|$",
)

draw_fun(
    axs[1][0],
    get_amplitude(s_fun_2),
    np.linspace(-4, 4, 400),
    r"(2)$|\mathcal F(\omega)|$",
    [],
    False,
    r"$\omega$",
    r"$|\mathcal F(\omega)|$",
)

draw_fun(
    axs[2][0],
    get_amplitude(s_fun_3),
    np.linspace(-4, 4, 400),
    r"(3)$|\mathcal F(\omega)|$",
    [],
    False,
    r"$\omega$",
    r"$|\mathcal F(\omega)|$",
)

draw_fun(
    axs[0][1],
    get_angle(s_fun_1),
    np.linspace(-np.pi, np.pi, 400),
    r"(1)$\mathrm{Arg}\mathcal F(\omega)$",
    [],
    False,
    r"$\omega$",
    r"$\mathrm{Arg}\mathcal F(\omega)$",
)

draw_fun(
    axs[1][1],
    get_angle(s_fun_2),
    np.linspace(-np.pi, np.pi, 400),
    r"(2)$\mathrm{Arg}\mathcal F(\omega)$",
    [],
    False,
    r"$\omega$",
    r"$\mathrm{Arg}\mathcal F(\omega)$",
)

draw_fun(
    axs[2][1],
    get_angle(s_fun_3),
    np.linspace(-np.pi, np.pi, 400),
    r"(3)$\mathrm{Arg}\mathcal F(\omega)$",
    [],
    False,
    r"$\omega$",
    r"$\mathrm{Arg}\mathcal F(\omega)$",
)

file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
