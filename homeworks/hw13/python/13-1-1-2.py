# cSpell:words mathcal mathrm
import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)


def s_fun_1(x):
    return (3 * (x**3)) / (x - 0.98)


def s_fun_2(x):
    return ((0.9 + (1 / x)) ** 2) / (0.64 * (x**-2) + 1)


def s_fun_3(x):
    return (x**2 - 1.1429 * x + 1.1429) / (x**2 - x + 0.875)


fig, axs = plt.subplots(3, 2, figsize=(15, 10))

draw_fun(
    axs[0][0],
    get_amplitude(s_fun_1, z_transform=True),
    np.linspace(0, 2 * np.pi, 400),
    r"(4)$|\mathcal F(\omega)|$",
    [],
    False,
    r"$\omega$",
    r"$|\mathcal F(\omega)|$",
)

draw_fun(
    axs[1][0],
    get_amplitude(s_fun_2, z_transform=True),
    np.linspace(0, 2 * np.pi, 400),
    r"(5)$|\mathcal F(\omega)|$",
    [],
    False,
    r"$\omega$",
    r"$|\mathcal F(\omega)|$",
)

draw_fun(
    axs[2][0],
    get_amplitude(s_fun_3, z_transform=True),
    np.linspace(0, 2 * np.pi, 400),
    r"(6)$|\mathcal F(\omega)|$",
    [],
    False,
    r"$\omega$",
    r"$|\mathcal F(\omega)|$",
)

draw_fun(
    axs[0][1],
    get_angle(s_fun_1, z_transform=True),
    np.linspace(0, 2 * np.pi, 400),
    r"(4)$\mathrm{Arg}\mathcal F(\omega)$",
    [],
    False,
    r"$\omega$",
    r"$\mathrm{Arg}\mathcal F(\omega)$",
)

draw_fun(
    axs[1][1],
    get_angle(s_fun_2, z_transform=True),
    np.linspace(0, 2 * np.pi, 400),
    r"(5)$\mathrm{Arg}\mathcal F(\omega)$",
    [],
    False,
    r"$\omega$",
    r"$\mathrm{Arg}\mathcal F(\omega)$",
)

draw_fun(
    axs[2][1],
    get_angle(s_fun_3, z_transform=True),
    np.linspace(0, 2 * np.pi, 400),
    r"(6)$\mathrm{Arg}\mathcal F(\omega)$",
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
