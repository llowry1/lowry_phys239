import numpy
import hw2_Conversions as conv
from astropy import constants


#Determine the column density in cm^-2 assuming a uniform number density
#params: number density [cm^-3], depth [pc]
#return: column density [cm^-2]
def findColDensity(n, depth):
	#convert pc to cm
	depth = conv.pc_cm(depth)
	#return column density
	return depth*n

#Determine the cross section in cm^2 given column density and optical depth
#params: column density [cm^-2], optical depth
#return: cross section [cm^2]
def findCrossSection(colDens, optDepth):
	#return cross section
	return optDepth/colDens
