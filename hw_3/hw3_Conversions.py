import numpy

#Functions for converting between common units


#degrees to radians
def deg_rad(angle_deg):
	return angle_deg*((2*numpy.pi)/360.0)


#cm to Bohn radii
def cm_bohr(dist_cm):
	return dist_cm*(1.89e8)
