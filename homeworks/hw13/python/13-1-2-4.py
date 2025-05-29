# cSpell:words mathcal mathrm
import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)


def s_fun_1(x):
    return (
        (x - 1)
        * (x + 0.9)
        * (x - 0.9j)
        * (x + 0.9j)
        / ((x - 0.5 + 0.6j) * (x - 0.5 - 0.6j))
    )


def s_fun_2(x):
    return (x - 1) / (x + 0.8)


fig, axs = plt.subplots(2, 2, figsize=(15, 10))

draw_fun(
    axs[0][0],
    get_amplitude(s_fun_1, z_transform=True),
    np.linspace(0, 2 * np.pi, 400),
    r"(7)$|\mathcal F(\omega)|$",
    [],
    False,
    r"$\omega$",
    r"$|\mathcal F(\omega)|$",
)

draw_fun(
    axs[1][0],
    get_amplitude(s_fun_2, z_transform=True),
    np.linspace(0, 2 * np.pi, 400),
    r"(8)$|\mathcal F(\omega)|$",
    [],
    False,
    r"$\omega$",
    r"$|\mathcal F(\omega)|$",
)

draw_fun(
    axs[0][1],
    get_angle(s_fun_1, z_transform=True),
    np.linspace(0, 2 * np.pi, 400),
    r"(r)$\mathrm{Arg}\mathcal F(\omega)$",
    [],
    False,
    r"$\omega$",
    r"$\mathrm{Arg}\mathcal F(\omega)$",
)

draw_fun(
    axs[1][1],
    get_angle(s_fun_2, z_transform=True),
    np.linspace(0, 2 * np.pi, 400),
    r"(8)$\mathrm{Arg}\mathcal F(\omega)$",
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
