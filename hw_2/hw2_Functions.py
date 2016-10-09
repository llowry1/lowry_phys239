import numpy
import hw2_Conversions as conv
from astropy import constants


#Determine the column density in cm^-2 assuming a uniform number density
##params: n = number density [cm^-3], d = depth [pc]
##return: column density [cm^-2]
def findColDensity(n, d):
	#convert pc to cm
	d = conv.pc_cm(d)
	#return column density
	return d*n

#Determine the cross section in cm^2 given column density and optical depth
##params: colDens = column density [cm^-2], optDepth = optical depth
##return: cross section [cm^2]
def findCrossSection(colDens, optDepth):
	#return cross section
	return optDepth/colDens

#Determine the absorption coefficient given number density and cross section
##params: n = number density [cm^-3], crossSect = cross section [cm^2]
##return: absorption coefficient [cm^-1]
def findAbsorptionCoeff(n, crossSect):
	return n*crossSect



#Given the number density, cross section, initial intensity, and source funtion determine the specific intensity a distance d away for a single frequency
#Uses given number of steps to incrementally calculate the specific intensity
##params: numSteps = number of steps to calculate at, n = number density [cm^-1], crossSect = cross section [cm^2], initI = initial intensity [W/m^2/Hz/sr], sourceFunc = source function [W/m^2/Hz/sr], d = total distance d [pc]
##return: the specific intensity at distance d [W/m^2/Hz/sr]
def findSpecificIntensity_singleFreq(numSteps, n, crossSect, initI, sourceFunc, d):
	
	#Eq of Radiative Transfer:
	#	dI_nu = alpha_nu*(S_nu - I_nu)*ds

	#convert pc to cm
	d = conv.pc_cm(d)
	print "d in cm: ", d

	#form arrays to hold distances and the intensity at each distance, and determine the distance step in cm
	dists, ds = numpy.linspace(0, d, num = numSteps, retstep = True)
	print "ds in cm: ", ds
	intensities = numpy.zeros(len(dists))
	intensities[0] = initI

	#calculate the absorption coefficient
	alpha_nu = findAbsorptionCoeff(n, crossSect)
	print "alpha_nu in cm^-1: ", alpha_nu

	#loop through the distance steps and calculate the change in specific intensity relative to the previous step
	currI = initI
	for i in range(len(intensities)):
		intensities[i] = currI
		print "currI: ", currI
		print "intensities[",i,"]: ", intensities[i]

		dI = alpha_nu*(sourceFunc - currI)*ds
		nextI = currI + dI
		print "nextI: ", nextI

		currI = nextI
	
	#print the specific intensity at distance d
	print intensities
	print intensities[len(intensities) - 1]

	return intensities[-1]


	
