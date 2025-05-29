import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)

OMEGA_M = 5
TAU = 0.3
OMEGA_S = 10.2


def basic_g(x):
    return np.piecewise(
        x,
        [
            (x < 0) & (x > -OMEGA_M),
            (x > 0) & (x < OMEGA_M),
            (x < -OMEGA_M) | (x > OMEGA_M),
        ],
        [lambda x: x / OMEGA_M + 1, lambda x: 1 - x / OMEGA_M, lambda _: 0],
    )


def sampled_g(x):
    return (
        TAU
        * np.sinc(x / TAU)
        * np.piecewise(
            x,
            [
                (x > -OMEGA_S) & (x < OMEGA_S),
                (x > -OMEGA_S + 2 * OMEGA_S) & (x < OMEGA_S + 2 * OMEGA_S),
                (x > -OMEGA_S - 2 * OMEGA_S) & (x < OMEGA_S - 2 * OMEGA_S),
            ],
            [
                basic_g,
                lambda x: basic_g(x - 2 * OMEGA_S),
                lambda x: basic_g(x + 2 * OMEGA_S),
            ],
        )
    )


fig, ax = plt.subplots(1, 1, figsize=(15, 10))

draw_fun(
    ax,
    sampled_g,
    np.linspace(-3 * OMEGA_S - 0.5, 3 * OMEGA_S + 0.5, 4000),
    r"$G_s(\omega)$",
    [],
    False,
    r"$\omega$",
    r"$G_s(\omega)$",
)

file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
