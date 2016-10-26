import numpy
import matplotlib.pyplot as plt
import random
import hw3_Conversions as conv
import hw3_Functions as func
import hw3_Functions2 as func2

##Script to output answers to questions on HW3



##Question 1--------------------------------------------------------------------------------------------------------
print "Question 1:"

##Choose an initial position pos0 = (x0, y0) for the electron, in Bohr radii, and assume it is coming from the left (x0 < 0)
#r0 = 4000
#theta0 = conv.deg_rad(150)
#r0 = random.randint(200,800)
#theta0 = conv.deg_rad(random.randint(90,270))

#x0 = r0*numpy.cos(theta0)
#y0 = r0*numpy.sin(theta0)

x0 = -250000
y0 = 5000

pos0 = numpy.array([x0, y0])

##Set the initial velocity vel0 of the electron in the x direction, in Bohr radii/s
vel0 = numpy.array([conv.cm_bohr(5e7), 0.0])


print "\tInitial position: ", pos0
print "\tInitial velocity: ", vel0

plt.figure(0)
plt.title("Initial Position")
plt.xlim(-300000,300000)
plt.ylim(-10000,10000)
plt.xlabel("x position (a0)")
plt.ylabel("y position (a0)")
plt.plot(pos0[0], pos0[1], 'bo')
plt.grid()
plt.axhline(y=0, color = 'k')
plt.axvline(x=0, color = 'k')
plt.plot(0,0, 'r8', markersize = 10)
plt.show()


##Question 2/3--------------------------------------------------------------------------------------------------------
print "\nQuestion 2-3:"
print "\tSee plots of position, velocity, and acceleration"


##assume charge of the particle at the origin is Ze = 4e
Z = 4
q1 = 1

##make arrays to hold the times and corresponding position, velocity, and acceleration components
num = 10000
times, timestep = numpy.linspace(0, 5e-11, num, retstep = True) #[s]
posX = numpy.zeros(len(times))
posY = numpy.zeros(len(times))
velX = numpy.zeros(len(times))
velY = numpy.zeros(len(times))
accX = numpy.zeros(len(times))
accY = numpy.zeros(len(times))

##set initial position, velocity, and acceleration
posX[0] = pos0[0]
posY[0] = pos0[1]
velX[0] = vel0[0]
velY[0] = vel0[1]

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
		velX[i] = vel[0]
		velY[i] = vel[1]
		pos = prevPos + vel*timestep
		posX[i] = pos[0]
		posY[i] = pos[1]
		acc = func.getAccel(func.coulombForce(1, Z, pos))
		accX[i] = acc[0]
		accY[i] = acc[1]
		
		prevPos = pos
		prevVel = vel
		prevAcc = acc
		
	i = i+1


#print func2.test(5)
#posXtest = func2.makeArrays(pos0, vel0, q1, Z)
#print posXtest

#print posX
#print posY
#print velX
#print velY
#print accX
#print accY


##Plot positions
plt.figure(1)
plt.title("Position")
plt.xlabel("x position (a0)")
plt.ylabel("y position (a0)")

i1 = 0
for num in posX:
	if i1 == 0:
		plt.plot(posX[i1], posY[i1], 'r*', markersize = 15)
	else:
		plt.plot(posX[i1], posY[i1], 'b.')
	i1 = i1 + 1

plt.grid()
plt.xlim(-300000, 300000)
plt.ylim(-10000, 10000)
plt.axhline(y=0, color = 'k')
plt.axvline(x=0, color = 'k')
plt.plot(0,0, 'r8', markersize = 10)

##Plot velocities
plt.figure(2)
plt.title("Velocity")
plt.xlabel("x velocity (a0/s)")
plt.ylabel("y velocity (a0/s)")#

i2 = 0
for num in velX:
	if i2 == 0:
		plt.plot(velX[i2], velY[i2], 'r*', markersize = 15)
	else:
		plt.plot(velX[i2], velY[i2], 'b.')
	i2 = i2 + 1

plt.grid()
plt.axhline(y=0, color = 'k')
plt.axvline(x=0, color = 'k')

##Plot accelerations
plt.figure(3)
plt.title("Acceleration")
plt.xlabel("x acceleration (a0/s^2)")
plt.ylabel("y acceleration (a0/s^2)")

i3 = 0
for num in accX:
	if i3 == 0:
		plt.plot(accX[i3], accY[i3], 'r*', markersize = 15)
	else:
		plt.plot(accX[i3], accY[i3], 'b.')
	i3 = i3 + 1

plt.grid()
plt.axhline(y=0, color = 'k')
plt.axvline(x=0, color = 'k')

##Plot accelerations as a function of time
plt.figure(4)
plt.suptitle("Acceleration Components")
plt.subplot(121)
plt.title("Acceleration x")
plt.xlabel("time (s)")
plt.ylabel("x acceleration (a0/s^2)")
plt.plot(times, accX)
plt.subplot(122)
plt.title("Acceleration y")
plt.xlabel("time (s)")
plt.ylabel("y acceleration (a0/s^2)")
plt.plot(times, accY)


##Question 4--------------------------------------------------------------------------------------------------------
print "\nQuestion 4:"
print "\tSee plots of Fourier Transforms"

##Take the Fourier transforms of the x- and y-components of the acceleration
ftX = numpy.fft.fft(accX)
n = accX.size
freqs = numpy.fft.fftfreq(n, timestep)

#print "Highest Freq: ", freqs[-1]
#print "Num Freqs: ", len(freqs)
#print "Freq Step: ", freqs[-1] - freqs[-2]

plt.figure(5)
plt.suptitle("FT: Acceleration X")
plt.subplot(121)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (arbitrary units)")
plt.plot(freqs, numpy.square(numpy.abs(ftX)), 'b')
plt.plot(freqs, numpy.square(numpy.abs(ftX)), 'r.')
plt.subplot(122)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (arbitrary units)")
plt.plot(freqs, numpy.square(numpy.abs(ftX)), 'b')
plt.plot(freqs, numpy.square(numpy.abs(ftX)), 'r.')
plt.xlim(0, 2e12)


ftY = numpy.fft.fft(accY)
plt.figure(6)
plt.suptitle("FT: Acceleration Y")
plt.subplot(121)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (arbitrary units)")
plt.plot(freqs, numpy.square(numpy.abs(ftY)), 'b')
plt.plot(freqs, numpy.square(numpy.abs(ftY)), 'r.')
plt.subplot(122)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (arbitrary units)")
plt.plot(freqs, numpy.square(numpy.abs(ftY)), 'b')
plt.plot(freqs, numpy.square(numpy.abs(ftY)), 'r.')
plt.xlim(0, 2e12)


##Take the Fourier Transform of the magnitude of the acceleration
acc = numpy.sqrt(numpy.square(accX) + numpy.square(accY))
ft = numpy.fft.fft(acc)

plt.figure(7)
plt.suptitle("FT: Acceleration (a = ((a_x)^2 + (a_y)^2)^(1/2))")
plt.subplot(121)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (arbitrary units)")
plt.plot(freqs, numpy.square(numpy.abs(ft)), 'b')
plt.plot(freqs, numpy.square(numpy.abs(ft)), 'r.')
plt.subplot(122)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (arbitrary units)")
plt.plot(freqs, numpy.square(numpy.abs(ft)), 'b')
plt.plot(freqs, numpy.square(numpy.abs(ft)), 'r.')
plt.xlim(0, 2e12)
plt.show()


##Question 5--------------------------------------------------------------------------------------------------------
print "\nQuestion 5:"
print "See plots of peak frequency vs. b and v0"


##Determine how changing b affects the peak frequency

##Specify range of impact parameters to look at
impactParams = numpy.arange(2000, 10000, 100)
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
    
    peak = numpy.amax(ftXb)
    w = numpy.where(ftXb == peak)
    w1 = w[0][0]
    print w1
    peakFreqs[i4] = freqs[w1]
    print peakFreqs[i4]
    
    i4 = i4+1
    
#plt.figure()
#plt.plot(b, peakFreqs)
#
#plt.show()
