import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np

def get_odd(fun):
    return lambda x : (fun(x) - fun(-x)) / 2.0

def get_even(fun):
    return lambda x : (fun(x) + fun(-x)) / 2.0

def draw_fun(ax, fun, domain, title, mark_points=[], dotted=False, xlabel=r"$t$", ylabel=r"$f(t)$"):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    ax.set_title(title)

    codomain = fun(domain)
    if dotted:
        ax.plot(domain, codomain, linestyle=':')
    else:
        ax.plot(domain, codomain)

    for point in mark_points:
        value = fun(point)
        ax.scatter([point], [value], color='red')
        ax.annotate(f'({point:.2f}, {value:.2f})', xy=(point, value),
                    xytext=(point + 0.1, value), fontsize=16)

def draw_dirac(ax, title, points=[]):
    for point in points:
        arrow = patches.FancyArrowPatch((point, 0), (point, 1), arrowstyle="-|>",
                                        mutation_scale=25, color='blue')
        ax.add_patch(arrow)

    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$f(t)$")
    ax.set_title(title)
    ax.grid(True)

    ax.set_xlim(-2, 3)
    ax.set_ylim(-0.5, 1.5)
    ax.axvline(0, color='black', linewidth=1)
    ax.axhline(0, color='black', linewidth=1)

def naive_draw_dirac(ax, points, height=1):
    for point in points:
        arrow = patches.FancyArrowPatch((point, 0), (point, height), arrowstyle="-|>",
                                        mutation_scale=25, color='blue')
        ax.add_patch(arrow)

def draw_discrete_signal(ax, fun, domain, title, mark_points=[]):
    codomain = fun(domain)
    ax.grid(True)
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"$f[n]$")
    ax.set_title(title)

    ax.stem(domain, codomain)

    for point in mark_points:
        value = fun(point)
        ax.scatter([point], [value], color='red')
        ax.annotate(f'({point:.2f}, {value:.2f})', xy=(point, value),
                    xytext=(point + 0.1, value), fontsize=16)
