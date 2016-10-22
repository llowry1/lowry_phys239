import numpy
import matplotlib.pyplot as plt
import random
import hw3_Conversions.py as conv

#Script to output answers to questions on HW3

#Question 1--------------------------------------------------------------------------------------------------------
print "Question 1:"

#Choose an initial position pos0 = (x0, y0) for the electron, in Bohr radii
r0 = random.randint(200,800)
theta0 = conv.deg_rad(random.randint(0,360))

x0 = r0*numpy.cos(theta0)
y0 = r0*numpy.sin(theta0)

pos0 = numpy.array([x0, y0])

#Set the initial velocity v0 of the electron in the x direction, in cm/s
v0 = numpy.array([0.0, conv.cm_bohr(1e7)])
