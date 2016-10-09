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


#Question 2
print "\nQuestion 2:"
print "\tSee findSpecificIntensity_singleFreq function in hw2_Functions.py"

#find final specific intensity assumptions listed below
I_d = func.findSpecificIntensity_singleFreq(1000, n, 1e-20, 1.0, 0.5, depth)
print "\tI(d = 100pc) = ", I_d
print "\tAssumptions: 1000 steps, cross section = 10^-20 cm^2, I_0 = 1 W/m^2/Hz/sr, and S_nu = 0.5 W/m^2/Hz/sr"

#Question 3
print "\nQuestion 3:"


#Question 4
print "\nQuestion 4:"

