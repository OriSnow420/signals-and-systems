import sys

sys.path.append("../../..")
import matplotlib.pyplot as plt
import numpy as np
from toolkit.tools import *

plt.rc("text", usetex=True)


def fun_1(x):
    return np.piecewise(
        x,
        [(x <= 0) & (x >= 2), (x > 0) & (x < 2)],
        [lambda x: 0, lambda x: -0.5 * x + 1],
    )


def fun_2(x):
    return np.piecewise(
        x,
        [x <= 0.0, (x > 0.0) & (x < 4.0), x >= 4.0],
        [lambda x: 1.0, lambda x: -0.25 * x + 1.0, lambda x: 0.0],
    )


def discrete_impulse(x):
    return np.piecewise(x, [x == 0, x != 0], [lambda x: 1.0, lambda x: 0.0])


fig, axs = plt.subplots(2, 4, figsize=(15, 10))

draw_discrete_signal(
    axs[0][0],
    lambda x: fun_2(x - 3),
    np.linspace(-2, 8, 11),
    r"$f_1[n]=f[n-3]$",
    [3, 7],
)

draw_discrete_signal(
    axs[0][1], lambda x: fun_2(2 * x), np.linspace(-2, 8, 11), r"$f_2[n]=f[2n]$", [0, 2]
)

# draw_dirac(axs[0][2], r"$f_3(t)=f(0.5t+1)$", [-4])
draw_fun(
    axs[0][2],
    lambda x: fun_1(0.5 * x + 1),
    np.linspace(-5, 4, 400),
    r"$f_3(t)=f(0.5t+1)$",
    [-2 + 1e-6, 2],
)
naive_draw_dirac(axs[0][2], [-4])

draw_fun(
    axs[0][3],
    lambda x: 2 * fun_1(-x - 1),
    np.linspace(-5, 4, 400),
    r"$f_4(t)=2f(-t-1)$",
    [-3, -1 - 1e-6],
)
naive_draw_dirac(axs[0][3], [0], 2)

draw_discrete_signal(
    axs[1][0],
    lambda x: fun_2(1 - x) * discrete_impulse(x - 1),
    np.linspace(-8, 2, 11),
    r"$f_1[n]=f[1-n]\cdot\delta[n-1]$",
)

draw_discrete_signal(
    axs[1][1], lambda x: fun_2(x**2), np.linspace(-2, 8, 11), r"$f_2[n]=f[n^2]$"
)

draw_fun(
    axs[1][2],
    lambda x: fun_1(x**0.5),
    np.linspace(0, 5, 40000),
    r"$f_3(t)=f(t^{0.5})$",
    [1e-6, 4],
)

draw_fun(
    axs[1][3],
    lambda x: fun_1(0.5 * x + 1) * np.heaviside(x, 0.5),
    np.linspace(-1, 5, 400),
    r"$f_4(t)=f(\frac12t+1)\cdot u(t)$",
    [1e-6, 2],
)

plt.savefig("../images/part2_transform.png")
plt.tight_layout()
plt.show()
