import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)

OMEGA_M = 4.0
OMEGA_C = 10.0 * OMEGA_M


def fun_1(x):
    return fun_2(x) * np.cos(OMEGA_C * x)

def fun_2(x):
    return (1 + 1.2 * np.cos(OMEGA_M * x))

fig, ax = plt.subplots(1, 1, figsize=(15, 10))

draw_fun(
    ax,
    fun_1,
    np.linspace(-5, 5, 40000),
    r"$y(t)=[1+1.2\cos(\Omega_1t)]\cdot\cos(\omega_ct)$"
)

draw_fun(
    ax,
    lambda x: np.abs(fun_2(x)),
    np.linspace(-5, 5, 40000),
    r"$y(t)=[1+1.2\cos(\Omega_1t)]\cdot\cos(\omega_ct)$",
    [],
    True
)

file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
