import numpy
import math
import matplotlib.pyplot as plt
import hw4_Functions as func
import os

##Script to output answers to questions on HW4

figcount = 0

##Question 1--------------------------------------------------------------------------------------------------------
print "Question 1:"

#datafile = "testdatafile.txt"
datafile = "m82spec_formatted.txt"

##Load the downloaded M82 data into arrays
data = numpy.loadtxt(datafile, skiprows = 1, unpack = True)
#print data

wavelength = data[0]
freq = func.wavelengthToFreq(wavelength)
l_nu = data[1]
l_nu_err = data[2]

##Plot the M82 data
figcount = figcount + 1
plt.figure(figcount)
ax = plt.subplot(111)
plt.title("M82 Data")
plt.xlabel("Frequency [Hz]")
plt.ylabel("L_nu [L_sun/Hz]")
ax.set_xscale("log")
ax.set_yscale("log")
plt.errorbar(freq, l_nu, yerr = l_nu_err)
#plt.show()



##Question 2--------------------------------------------------------------------------------------------------------
print "Question 2:"

##Question 2b - Dust------------------------------------------------------------------------------------------------
print "2b - Dust:"

D_M82 = 1.08e17 #[m] = 11.42 million ly
M_dust = 1e39 #[kg] = 500 million solar masses

print "Obtained data on Q_abs from https://www.astro.princeton.edu/~draine/dust/dust.diel.html and used the PAHion_30 data set assuming a grain size of 3.548e-4 um"
print "Assumed a grain mass density of 4.4e-23 kg/m^3 assuming M_dust/M_gal ~ 0.01 (from https://www.astro.umd.edu/~richard/ASTRO620/A620_2015_dust.pdf) and rho_gal = M_gal/V_gal"

#download dust grain data
dust_data = numpy.loadtxt("PAHion_30_set1.txt", skiprows = 2, usecols = [0, 2], unpack = True)
dust_size = 3.548e-04 #[um]
#dust_data = numpy.loadtxt("PAHion_30_set2.txt", skiprows = 2, usecols = [0, 2], unpack = True)
#dust_size = 1e-02 #[um]
dust_wavelengths = dust_data[0]
dust_freqs = func.wavelengthToFreq(dust_wavelengths)
dust_Q = dust_data[1]

figcount = figcount + 1
plt.figure(figcount)
plt.title("Mie Scattering Cross Section Q_abs")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Q_abs")
plt.loglog(dust_freqs, dust_Q)

#get dust_rho from M_gal/Mdust ~ 100
dust_rho = 4.4e-23 #[kg/m^3]

opacity = func.opacity(dust_Q, dust_size, dust_rho)

figcount = figcount + 1
plt.figure(figcount)
plt.title("Opacity")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Opacity")
plt.loglog(dust_freqs, opacity)


B_nu = numpy.array([])
for f in dust_freqs:
	B = func.B_nu(200, f)
	B_nu = numpy.append(B_nu, B)

print len(freq)
print len(B_nu)


figcount = figcount + 1
plt.figure(figcount)
plt.title("Blackbody B_nu")
plt.xlabel("Frequency [Hz]")
plt.ylabel("B_nu")
plt.loglog(dust_freqs, B_nu, 'bo')

M_dust = M_dust*(1e-11)
S_nu = (M_dust/(D_M82**2))*opacity*B_nu


figcount = figcount + 1
plt.figure(figcount)
plt.title("S_nu")
plt.xlabel("Frequency [Hz]")
plt.ylabel("S_nu")
plt.xlim(freq[-1], freq[0])
plt.loglog(dust_freqs, S_nu)
plt.loglog(freq, l_nu)



##Question 2c - Synchrotron-----------------------------------------------------------------------------------------
print "2c - Synchrotron:"

omega = 2*math.pi*freq

Psync = numpy.array([])
for w in omega:
	Pw = func.syncP(2.4, w)
	#print Pw
	Psync = numpy.append(Psync, Pw)


figcount = figcount + 1
plt.figure(figcount)
plt.title("Synchrotron Component")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Power")
plt.loglog(freq, Psync)
plt.loglog(freq, l_nu)




##Question 2d - Bremsstrahlung--------------------------------------------------------------------------------------
print "2d - Bremsstrahlung:"

Pbrem = numpy.array([])
for f in freq:
	P = func.bremP(f, 1000, g_ff = 1e80)
	Pbrem = numpy.append(Pbrem, P)

figcount = figcount + 1
plt.figure(figcount)
plt.title("Bremsstrahlung Component")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Power")
plt.loglog(freq, Pbrem)
plt.loglog(freq, l_nu)


##Question 2d - Bremsstrahlung--------------------------------------------------------------------------------------


figcount = figcount + 1
plt.figure(figcount)
plt.title("All Components")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Power")
plt.loglog(dust_freqs, S_nu, label = "Dust")
plt.loglog(freq, Psync, label = "Synchrotron")
plt.loglog(freq, Pbrem, label = "Bremsstrahlung")
plt.loglog(freq, l_nu)
plt.show()





plt.show()

