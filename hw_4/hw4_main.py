import numpy
import matplotlib.pyplot as plt
import hw4_Functions as func
import os

##Script to output answers to questions on HW4



##Question 1--------------------------------------------------------------------------------------------------------
print "Question 1:"

#datafile = "m82spec_formatted.txt"
datafile = "test.txt"


##Load the downloaded data into arrays
data = numpy.loadtxt(datafile,delimiter=',')


print data