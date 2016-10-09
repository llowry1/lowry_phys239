import hw2_Functions as func
import hw2_Conversions as conv
import numpy
import matplotlib.pyplot as plt


#Script to output answers to questions on HW2

#Given variables:
depth = 100 #[pc]
n = 1 #[cm^-1]



#Question 1--------------------------------------------------------------------------------------------------------
print "Question 1:"

#find the column density
colDens = func.findColDensity(n, depth)
print "\tColumn Density of the cloud: ", colDens, " cm^-2"

#find the cross sections for given optical depths
optDepths = numpy.array([1e-3, 1, 1e3])
crossSects = func.findCrossSection(colDens, optDepths)
print "\tCross Section assuming total optical depth of..."
print "\t\ta) 10^-3: ", crossSects[0], " cm^2"
print "\t\tb) 1: ", crossSects[1], " cm^2"
print "\t\tc) 10^3: ", crossSects[2], " cm^2"


#Question 2--------------------------------------------------------------------------------------------------------
print "\nQuestion 2:"
print "\tSee findSpecificIntensity_singleFreq function in hw2_Functions.py"

#find final specific intensity assumptions listed below
dists, intensities = func.findSpecificIntensity_singleFreq(1000, n, 1e-20, 1.0, 0.5, depth)
print "\tI(d = 100pc) = ", intensities[-1]
print "\tAssumptions: 1000 steps, cross section = 10^-20 cm^2, I_0 = 1 W/m^2/Hz/sr, and S_nu = 0.5 W/m^2/Hz/sr"

#plot the intensity as a function of distance s
plt.figure(0)
plt.title('Question 2: Radiative Transfer (emission + absorption) for Single Frequency\nn = 1 cm^-3, sigma_nu = 10^-20 cm^2, I_nu(s=0) = 1.0 W/m^2/Hz/sr, S_nu = 0.5 W/m^2/Hz/sr')
plt.xlabel('Distance s [cm]')
plt.ylabel('I_nu(s) [W/m^2/Hz/sr]')
plt.plot(dists, intensities)
#plt.show()


#Question 3--------------------------------------------------------------------------------------------------------
print "\nQuestion 3:"
print "\tSee genCrossSectionForFreqs function in hw2_Functions.py"

#make an array of frequencies assuming mostly visible light (~400-800 THz)
freqs = numpy.linspace(400, 800, 500)

#generate gaussian distributions of cross sections assuming max values calculated in Question 1
crossSect_1a = func.genCrossSectionForFreqs(freqs, crossSects[0], 'Gaussian')
crossSect_1b = func.genCrossSectionForFreqs(freqs, crossSects[1], 'Gaussian')
crossSect_1c = func.genCrossSectionForFreqs(freqs, crossSects[2], 'Gaussian')

#plot the cross sections as a function of frequency
plt.figure(1)
plt.suptitle('Question 3: Cross Section as a function of Frequency (Gaussian Distribution)')

plt.subplot(131)
plt.xlabel('Frequency nu [THz]')
plt.ylabel('Cross Section sigma(nu) [cm^2]')
plt.plot(freqs, crossSect_1a)

plt.subplot(132)
plt.xlabel('Frequency nu [THz]')
plt.ylabel('Cross Section sigma(nu) [cm^2]')
plt.plot(freqs, crossSect_1b)

plt.subplot(133)
plt.xlabel('Frequency nu [THz]')
plt.ylabel('Cross Section sigma(nu) [cm^2]')
plt.plot(freqs, crossSect_1c)

#plt.show()


#Question 4--------------------------------------------------------------------------------------------------------
print "\nQuestion 4:"

maxI_nu0 = 1.0
minI_nu0 = 0.2
maxS_nu = 1.0
minS_nu = 0.2

'''
#for 4a, tau_nu(d) >> 1 ==> set tau_nu(d) = 1000
tau_4a = 1000000
maxCrossSect_4a = func.findCrossSection(colDens, tau_4a)
crossSect_4a = func.genCrossSectionForFreqs(freqs, maxCrossSect_4a, 'Gaussian')

finalIntensities_4a = numpy.array([])

for sigma in crossSect_4a:
	finalIntensities_4a = numpy.append(finalIntensities_4a, func.findFinalSpecificIntensity_singleFreq(1000, n, sigma, maxI_nu0, minS_nu, depth))


plt.figure(2)
plt.plot(freqs, finalIntensities_4a)
plt.show()
'''

#for 4b, 4c, and 4d, tau_nu(d) < 1
tau_4bcd = 0.5
maxCrossSect_4bcd = func.findCrossSection(colDens, tau_4bcd)
crossSect_4bcd = func.genCrossSectionForFreqs(freqs, maxCrossSect_4bcd, 'Gaussian')

#for 4b, I_nu0 = 0.0
finalIntensities_4b = numpy.array([])
for sigma in crossSect_4bcd:
	finalIntensities_4b = numpy.append(finalIntensities_4b, func.findFinalSpecificIntensity_singleFreq(1000, n, sigma, 0, minS_nu, depth))


plt.figure(3)
plt.plot(freqs, finalIntensities_4b)


#for 4c, I_nu0 < S_nu
finalIntensities_4c = numpy.array([])
for sigma in crossSect_4bcd:
	finalIntensities_4c = numpy.append(finalIntensities_4c, func.findFinalSpecificIntensity_singleFreq(1000, n, sigma, minI_nu0, maxS_nu, depth))


plt.figure(4)
plt.plot(freqs, finalIntensities_4c)


#for 4d, I_nu0 > S_nu
finalIntensities_4d = numpy.array([])
for sigma in crossSect_4bcd:
	finalIntensities_4d = numpy.append(finalIntensities_4d, func.findFinalSpecificIntensity_singleFreq(1000, n, sigma, maxI_nu0, minS_nu, depth))


plt.figure(5)
plt.plot(freqs, finalIntensities_4d)




plt.show()



