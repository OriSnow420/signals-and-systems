import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *
import math

plt.rc("text", usetex=True)

sqrt_5_over_2 = (5 ** 0.5) / 2


fig, axs = plt.subplots(1, 2, figsize=(10, 5))

draw_discrete_signal(axs[0],
    lambda x: np.array([0.5, 0, 0.5, 0.5, sqrt_5_over_2, 0.5, sqrt_5_over_2, 0.5, 0.5, 0, 0.5]), np.array(range(-5, 6)), r"$|F_n|$")
draw_discrete_signal(axs[1],
    lambda x: np.array([np.pi * 2 / 3, 0, np.pi / 3, np.pi / 4, math.atan(2), 0, -math.atan(2), -np.pi / 4, -np.pi / 3, 0, -np.pi * 2 / 3]), np.array(range(-5, 6)), r"$\theta_n$")


file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
