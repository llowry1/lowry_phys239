import numpy
import matplotlib.pyplot as plt
import hw4_Functions as func
import os

##Script to output answers to questions on HW4



##Question 1--------------------------------------------------------------------------------------------------------
print "Question 1:"

#datafile = "testdatafile.txt"
datafile = "m82spec_formatted.txt"

##Load the downloaded M82 data into arrays
data = numpy.loadtxt(datafile, skiprows = 1, unpack = True)
#print data

wavelength = data[0]
l_nu = data[1]
l_nu_err = data[2]

##Plot the M82 data
plt.figure(1)
ax = plt.subplot(111)
plt.title("M82 Data")
plt.xlabel("Wavelength [um]")
plt.ylabel("L_nu [L_sun/Hz]")
ax.set_xscale("log")
ax.set_yscale("log")
plt.errorbar(wavelength, l_nu, yerr = l_nu_err)
plt.show() 
