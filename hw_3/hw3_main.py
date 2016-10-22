import numpy
import matplotlib.pyplot as plt
import random
import hw3_Conversions as conv
import hw3_Functions as func

#Script to output answers to questions on HW3

#Question 1--------------------------------------------------------------------------------------------------------
print "Question 1:"

#Choose an initial position pos0 = (x0, y0) for the electron, in Bohr radii
r0 = random.randint(200,800)
theta0 = conv.deg_rad(random.randint(0,360))

x0 = r0*numpy.cos(theta0)
y0 = r0*numpy.sin(theta0)

pos0 = numpy.array([x0, y0])

#Set the initial velocity v0 of the electron in the x direction, in Bohr radii/s
v0 = numpy.array([0.0, conv.cm_bohr(1e7)])


print "\tInitial position: ", pos0
print "\tInitial velocity: ", v0

plt.figure(0)
plt.title("Initial Position")
plt.xlim(-800,800)
plt.ylim(-800,800)
plt.xlabel("x position (a0)")
plt.ylabel("y position (a0)")
plt.plot(pos0[0], pos0[1], 'bo')
plt.grid()
plt.axhline(y=0, xmin = -800, xmax = 800, color = 'k')
plt.axvline(x=0, ymin = -800, ymax = 800, color = 'k')
plt.show()


#Question 2--------------------------------------------------------------------------------------------------------
print "\nQuestion 2:"


