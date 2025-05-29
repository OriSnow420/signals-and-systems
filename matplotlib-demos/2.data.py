import matplotlib.pyplot as plt
import numpy as np


# Example from https://matplotlib.org/stable/users/explain/quick_start.html#types-of-inputs-to-plotting-functions
def colorful_linear():
    np.random.seed(20250226)  # seed the random number generator.
    data = {
        "a": np.arange(50),
        "c": np.random.randint(0, 50, 50),
        "d": np.random.randn(50),
    }
    data["b"] = data["a"] + 10 * np.random.randn(50)
    data["d"] = np.abs(data["d"]) * 100  # Numpy stuff

    fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")

    # Plotting expect numpy.array or anything that can be converted to it.
    # It can parse a dict
    ax.scatter("a", "b", c="c", s="d", data=data)
    ax.set_xlabel("entry a")
    ax.set_ylabel("entry b")

    plt.show()


colorful_linear()
