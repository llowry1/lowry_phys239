import numpy
import math
import scipy.special
import matplotlib.pyplot as plt


##Constants
m = 9.109e-31 #electron mass [kg]
q = 1.602e-19 #electron charge [C]
c = 3e8 #speed of light [m/s]
h = 6.626e-34 #plancks constant [m^2 kg/s]
k = 1.38e-23 #boltzmann constant [m^2 kg/s^2/K]


#Find the frequency corresponding to a given wavelength
##params: wave = the wavelength in um
##return: the frequency in Hz
def wavelengthToFreq(wave):
	c1 = c*(1e6)	#c [um/s]	
	return c1/wave




##Dust
def B_nu(temp, nu):
	B_nu = 2.0*h*(nu**3)/(c**2)
	B_nu = B_nu*((numpy.exp((h*nu)/(k*temp)) - 1)**(-1))
	return B_nu

#Find the opacity
##params: Q = Mie scattering cross section, a = grain size, rho = grain mass density
##return: the opacity kappa_nu
def opacity(Q, a, rho):
	return (3.0*Q)/(4.0*a*rho)




##Synchrotron (eq 6.36)
def syncP(p, w, B = 1e6, C = 2e64, alpha = math.pi/2.0):
	term1 = ((q**3)*B*C*(math.sin(alpha))*(math.sqrt(3)))/(2*(math.pi)*(c**2)*(p+1))
	gamma1 = scipy.special.gamma((p/4.0) + (19.0/12.0))
	gamma2 = scipy.special.gamma((p/4.0) - (1.0/12.0))
	term4 = ((m*c*w)/(3*q*B*(math.sin(alpha))))**(-1*(p-1)/2.0)
	P_w = term1*gamma1*gamma2*term4
	
	return P_w



##Bremsstrahlung (from notes)
def bremP(nu, T, n_e = 1, n_i = 1, g_ff = 1, z = 1):
	term1 = ((2.0**5)*(math.pi)*(q**6))/(3.0*m*(c**3))
	term2 = ((2.0*math.pi)/(3.0*k*m))**(0.5)
	term3 = (T**(-0.5))*(z**2)*n_e*n_i*g_ff
	term4 = numpy.exp(((-1)*h*nu)/(k*T))
	P_nu = term1*term2*term3*term4

	return P_nu
