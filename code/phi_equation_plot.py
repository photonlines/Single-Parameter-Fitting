import pylab
import numpy as np
from mpmath import sin, pi

NUM_POINTS = 500

def squared(num):
    return num ** 2

def phi(x):
    return float(squared(sin(2 * pi * x)))

coordinate_points = []
x_values = np.linspace(0, 1, NUM_POINTS)

for x in x_values:
    y = phi(x)
    coordinate_points.append([x, y])

coordinate_points = np.array(coordinate_points)

def draw_scatterplot(coordinate_points):
    pylab.plot(coordinate_points[:, 0], coordinate_points[:, 1], '.')
    pylab.show()

draw_scatterplot(coordinate_points)