import hw2_Functions as func
import hw2_Conversions as conv
import numpy


#Script to output answers to questions on HW2

#Given variables:
depth = 100 #[pc]
n = 1 #[cm^-1]



#Question1
print "Question 1:"

#find the column density
colDens = func.findColDensity(n, depth)
print "\tColumn Density of the cloud: ", colDens, " cm^-2"

#find the cross sections for given optical depths
optDepths = numpy.array([1e-2, 1, 1e2])
crossSects = func.findCrossSection(colDens, optDepths)
print "\tCross Section assuming total optical depth of..."
print "\t\ta) 10^-3: ", crossSects[0], " cm^2"
print "\t\tb) 1: ", crossSects[1], " cm^2"
print "\t\tc) 10^3: ", crossSects[2], " cm^2"

