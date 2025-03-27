import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
from scipy.integrate import quad

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
        if isinstance(value, tuple):
            value = value[0]
        ax.scatter([point], [value], color='red')
        ax.annotate(f'({point:.2f}, {value:.2f})', xy=(point, value),
                    xytext=(point + 0.1, value), fontsize=16)

def draw_convolve(ax, fun1, fun2, left1, right1, left2, right2, title, mark_points=[], dotted=False, xlabel=r"$t$", ylabel=r"$f(t)$"):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    ax.set_title(title)

    length1 = int((right1 - left1) * 400)
    length2 = int((right2 - left2) * 400)
    length = min(length1, length2)

    domain1 = np.linspace(left1, right1, length1)
    domain2 = np.linspace(left2, right2, length2)
    codomain = np.convolve(fun1(domain1), fun2(domain2)) / 400

    num = codomain.size

    left = left1 + left2
    right = right1 + right2

    if dotted:
        ax.plot(np.linspace(left, right, num), codomain, linestyle=':')
    else:
        ax.plot(np.linspace(left, right, num), codomain)

    for point in mark_points:
        index = int((point - left) / (right - left) * num)
        value = codomain[index]
        ax.scatter([point], [value], color='red')
        ax.annotate(f'({point:.3f}, {value:.3f})', xy=(point, value),
                    xytext=(point + 0.1, value), fontsize=16)

def get_convolution_fun(fun_1, fun_2, left_lim=-10, right_lim=10):
    return lambda x: quad(lambda t: fun_1(t) * fun_2(x-t), left_lim, right_lim)

def np_convolution(fun_1, fun_2, left_lim=-5, right_lim=5):
    def convolve(x):
        result = []
        convolve_fun = get_convolution_fun(fun_1, fun_2, left_lim, right_lim)
        if isinstance(x, np.array([]).__class__):
            for i in x:
                result.append(convolve_fun(i))
            return np.array(result)
        return convolve_fun(x)
    return convolve

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
        
def draw_discrete_list(ax, codomain, domain, title):
    ax.grid(True)
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"$f[n]$")
    ax.set_title(title)

    print(codomain)
    ax.stem(domain, codomain)
    

def iterative_solve_convolution(fun_x, fun_y, num):
    result = []
    for n in range(num):
        minus = 0
        for m, h_m in enumerate(result):
            minus += fun_x(n - m) * h_m
        result.append((fun_y(n) - minus) / fun_x(0))
    return result
