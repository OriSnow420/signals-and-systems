import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # A figure with a single axes

# What is an axes? An axes is an area where points in it can be expressed as an
# (x, y) - pair(2D case). Similar to a sub-picture.

# Figures keep track of its axes and other elements.

# Alternates:

# fig = plt.figure() # empty fig with no axes
# 1.
# fig, axs = plt.subplots(2, 2) # a fig with a 2x2 grid of axes
# ax = axs[0][0]
# 2.
# fig, axs = plt.subplot_mosaic([['left', 'right_top'], ['left', 'right_bottom']])
# ax = axs['left']
# # a fig with 3 axes: a tall, left one and two right axes.

ax.set_xlabel("I am an x-label")
ax.set_ylabel("I am a y-label")
ax.set_title("I am the title.")

# Each axes has two (or more) axis. E.G. ax.yaxis and ax.xaxis are two axis.

# Everything visible is called an Artist, including Figure, Axes, Axis, etc..

plt.show()
