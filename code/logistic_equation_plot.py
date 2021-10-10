import pylab
import numpy

def logistic_equation(x, growth_factor):
    return growth_factor * x * ( 1 - x )

GROWTH_RATE = 4
coordiante_points = []
x = 0.1

# Do this 500 times
for _ in range(500):
    y = logistic_equation(x, GROWTH_RATE)
    # Add the point (x, y) to our list of coordinates to graph
    coordiante_points.append( [x, y] )
    # We feed in our output value into our next input and repeat the same process
    x = y

# Convert the coordinate point list of lists into a 2D numpy array.
coordiante_points = numpy.array(coordiante_points)

# This draws a scatter plot of the (x, y) values
def draw_scatterplot( coordinate_points ):
    pylab.plot(coordinate_points[:,0], coordinate_points[:,1], '.')
    pylab.show()

draw_scatterplot( coordiante_points )