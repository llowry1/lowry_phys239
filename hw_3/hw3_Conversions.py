import numpy

#Functions for converting between common units


#degrees to radians
def deg_rad(angle_deg):
	return angle_deg*((2*numpy.pi)/360.0)


#cm to Bohr radii
def cm_bohr(dist_cm):
	return dist_cm*(1.89e8)

#m to Bohr radii
def m_bohr(dist_m):
	return dist_m*(1.89e10)

#Bohr radii to m
def bohr_m(dist_bohr):
	return dist_bohr/(1.89e10)


#elementary charge to Coulombs
def e_Coulomb(charge_e):
	return charge_e*(1.6021e-19)
