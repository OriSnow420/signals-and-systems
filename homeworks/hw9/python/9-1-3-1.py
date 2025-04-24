import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)


fig, axs = plt.subplots(2, 1, figsize=(15, 10))

draw_dirac(
    axs[0],
    r"$F(\omega)$",
    [-18 * np.pi, -12 * np.pi, 12 * np.pi, 18 * np.pi],
    np.pi * np.pi,
    (-19 * np.pi, 19 * np.pi),
    (-0.5, np.pi * np.pi + 0.5),
)

draw_dirac(
    axs[1],
    r"$Y_2(\omega)$",
    [
        -18 * np.pi - 40 * np.pi,
        -12 * np.pi - 40 * np.pi,
        12 * np.pi - 40 * np.pi,
        18 * np.pi - 40 * np.pi,
        -18 * np.pi,
        -12 * np.pi,
        12 * np.pi,
        18 * np.pi,
        -18 * np.pi + 40 * np.pi,
        -12 * np.pi + 40 * np.pi,
        12 * np.pi + 40 * np.pi,
        18 * np.pi + 40 * np.pi,
    ],
    np.pi * np.pi,
    (-59 * np.pi, 59 * np.pi),
    (-0.5, np.pi * np.pi + 0.5),
)

file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
