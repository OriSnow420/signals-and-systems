import sys

sys.path.append("../../..")
import numpy as np
from toolkit.tools import *


def fun_1(x):
    return np.piecewise(
        x,
        [x == 0, x == 1, (x != 0) & (x != 1)],
        [lambda x: 1, lambda x: 2, lambda x: 0],
    )


def fun_2(x):
    return (np.e ** (-0.5 * x)) * np.heaviside(x, 0.5)


print(iterative_solve_convolution(fun_1, fun_2, 6))
