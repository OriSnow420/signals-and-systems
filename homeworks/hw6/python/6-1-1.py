import sys
import os

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *
import math

plt.rc("text", usetex=True)

E = 3
TAU = 8

def fun_1(x):
    return np.abs(E / (x * TAU)) * np.sqrt(1 + (2 / np.abs(x)) * np.abs(np.sin(x * TAU / 2)))

fig, ax = plt.subplots(1, 1, figsize=(10, 5))

draw_fun(ax, fun_1, np.linspace(-2.5, 2.5, 400), r"(1)$|F(\omega)|$")

file_name, _ = os.path.splitext(os.path.basename(__file__))
plt.tight_layout()
plt.savefig("../images/" + file_name + ".png")
plt.show()
