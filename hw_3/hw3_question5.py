import numpy
import matplotlib.pyplot as plt
import random
import hw3_Conversions as conv
import hw3_Functions as func


##Question 5--------------------------------------------------------------------------------------------------------
print "\nQuestion 5:"
print "\tSee plots of peak frequency vs. b and v0"
print "\t*Note: the limited resolution of the Fourier transform constrains the resolution with which we can determine the peak frequency, but the general trend is still visible."

x0 = -250000
Z = 4
##Determine how changing b affects the peak frequency

##Specify range of impact parameters to look at
impactParams = numpy.linspace(2000, 10000, 100)
vel0 = numpy.array([conv.cm_bohr(5e7), 0.0])

##Make an array to hold the peak frequencies associated with each impact parameter
peakFreqs = numpy.zeros(len(impactParams))

i4 = 0
for b in impactParams:
    pos0 = numpy.array([x0,b])
    ##make arrays to hold the times and corresponding position, velocity, and acceleration components
    num = 10000
    times, timestep = numpy.linspace(0, 5e-11, num, retstep = True) #[s]
    #posX = numpy.zeros(len(times))
    #posY = numpy.zeros(len(times))
    #velX = numpy.zeros(len(times))
    #velY = numpy.zeros(len(times))
    accX = numpy.zeros(len(times))
    accY = numpy.zeros(len(times))
    
    ##set initial position, velocity, and acceleration
    #posX[0] = pos0[0]
    #posY[0] = pos0[1]
    #velX[0] = vel0[0]
    #velY[0] = vel0[1]
    
    acc0 = func.getAccel(func.coulombForce(1, Z, pos0))
    accX[0] = acc0[0]
    accY[0] = acc0[1]
    
    
    i = 0
    for time in times:
   	if i == 0:
  		prevPos = pos0
  		prevVel = vel0
  		prevAcc = acc0	
   	else:
  		vel = prevVel + prevAcc*timestep
  		#velX[i] = vel[0]
  		#velY[i] = vel[1]
  		pos = prevPos + vel*timestep
  		#posX[i] = pos[0]
  		#posY[i] = pos[1]
  		acc = func.getAccel(func.coulombForce(1, Z, pos))
  		accX[i] = acc[0]
  		accY[i] = acc[1]
  		
  		prevPos = pos
  		prevVel = vel
  		prevAcc = acc
  		
   	i = i+1
   
    ##take the FT of the x component of the acceleration
    ftXb = numpy.fft.fft(accX)
    n = accX.size
    freqs = numpy.fft.fftfreq(n, timestep)
    
    ftXb = numpy.square(numpy.abs(ftXb))
    
    freqs = freqs[0:n/2]
    ftXb = ftXb[0:n/2]
    
    peak = numpy.amax(ftXb)
    w = numpy.where(ftXb == peak)
    w1 = w[0][0]

    peakFreqs[i4] = freqs[w1]

    
    #plt.figure()
    #plt.plot(freqs, ftXb)
    #plt.plot(freqs, ftXb, 'r.')
    #plt.plot(freqs[w1], peak, 'go')
    #plt.show()
    
    i4 = i4+1
    
plt.figure()
plt.title("Dependence on Impact Paramter b")
plt.xlabel("Impact parameter b (a0)")
plt.ylabel("Peak Frequency (Hz)")
plt.plot(impactParams, peakFreqs, 'go')
plt.show()
