import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)

OMEGA_M = 4.0
OMEGA_C = 16.0


def fun_1(x):
    return np.cos(OMEGA_M * x) * np.cos(OMEGA_C * x)


def fun_2(x):
    return (1 + 0.8 * np.cos(OMEGA_M * x)) * np.cos(OMEGA_C * x)


fig, axs = plt.subplots(2, 2, figsize=(15, 10))


draw_fun(
    axs[0][0],
    fun_1,
    np.linspace(-5, 4, 400),
    r"$y_1(t)=\cos(\Omega_1t)\cdot\cos(\omega_ct)$",
)

draw_fun(
    axs[0][1],
    fun_2,
    np.linspace(-5, 5, 400),
    r"$y_2(t)=[1+0.8\cos(\Omega_1t)]\cdot\cos(\omega_ct)$",
)

draw_dirac(
    axs[1][0],
    r"$Y_1(\omega)$",
    [-5 * OMEGA_M, -3 * OMEGA_M, 3 * OMEGA_M, 5 * OMEGA_M],
    np.pi / 2,
    (-5 * OMEGA_M - 1, 5 * OMEGA_M + 1),
    (-0.5, np.pi / 1.8),
)

draw_dirac(
    axs[1][1],
    r"$Y_2(\omega)$",
    [-5 * OMEGA_M, -3 * OMEGA_M, 3 * OMEGA_M, 5 * OMEGA_M],
    np.pi * 0.4,
    (-5 * OMEGA_M - 1, 5 * OMEGA_M + 1),
    (-0.5, np.pi + 0.5),
)

naive_draw_dirac(axs[1][1], [-4 * OMEGA_M, 4 * OMEGA_M], np.pi)

file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
