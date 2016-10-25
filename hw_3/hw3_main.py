import numpy
import matplotlib.pyplot as plt
import random
import hw3_Conversions as conv
import hw3_Functions as func

#Script to output answers to questions on HW3


#Question 1--------------------------------------------------------------------------------------------------------
print "Question 1:"

#Choose an initial position pos0 = (x0, y0) for the electron, in Bohr radii, and assume it is coming from the left (x0 < 0)
#r0 = 4000
#theta0 = conv.deg_rad(150)
#r0 = random.randint(200,800)
#theta0 = conv.deg_rad(random.randint(90,270))

#x0 = r0*numpy.cos(theta0)
#y0 = r0*numpy.sin(theta0)

x0 = -50000
y0 = 5000

pos0 = numpy.array([x0, y0])

#Set the initial velocity v0 of the electron in the x direction, in Bohr radii/s
vel0 = numpy.array([conv.cm_bohr(5e7), 0.0])


print "\tInitial position: ", pos0
print "\tInitial velocity: ", vel0

plt.figure(0)
plt.title("Initial Position")
plt.xlim(-2000,2000)
plt.ylim(-2000,2000)
plt.xlabel("x position (a0)")
plt.ylabel("y position (a0)")
plt.plot(pos0[0], pos0[1], 'bo')
plt.grid()
plt.axhline(y=0, xmin = -2000, xmax = 2000, color = 'k')
plt.axvline(x=0, ymin = -2000, ymax = 2000, color = 'k')
plt.plot(0,0, 'r8', markersize = 10)
plt.show()


#Question 2--------------------------------------------------------------------------------------------------------
print "\nQuestion 2-3:"


#assume charge of the particle at the origin is Ze = 4e
Z = 4
q1 = 1

#make arrays to hold the times and corresponding position, velocity, and acceleration components
num = 1000000
times, timestep = numpy.linspace(0, 1e-11, num, retstep = True) #[s]
posX = numpy.zeros(len(times))
posY = numpy.zeros(len(times))
velX = numpy.zeros(len(times))
velY = numpy.zeros(len(times))
accX = numpy.zeros(len(times))
accY = numpy.zeros(len(times))

#set initial position, velocity, and acceleration
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

#print posX
#print posY
#print velX
#print velY
#print accX
#print accY


#Plot positions
#plt.figure(1)
#plt.title("Position")
#plt.xlabel("x position (a0)")
#plt.ylabel("y position (a0)")

#i1 = 0
#for num in posX:
#	if i1 == 0:
#		plt.plot(posX[i1], posY[i1], 'r*', markersize = 15)
#	else:
#		plt.plot(posX[i1], posY[i1], 'b.')
#	i1 = i1 + 1
#
#plt.grid()
#plt.axhline(y=0, color = 'k')
#plt.axvline(x=0, color = 'k')
#plt.plot(0,0, 'r8', markersize = 10)

#Plot velocities
#plt.figure(2)
#plt.title("Velocity")
#plt.xlabel("x velocity (a0/s)")
#plt.ylabel("y velocity (a0/s)")#
#
#i2 = 0
#for num in velX:
#	if i2 == 0:
#		plt.plot(velX[i2], velY[i2], 'r*', markersize = 15)
#	else:
#		plt.plot(velX[i2], velY[i2], 'b.')
#	i2 = i2 + 1
#
#plt.grid()
#plt.axhline(y=0, color = 'k')
#plt.axvline(x=0, color = 'k')

#Plot accelerations
#plt.figure(3)
#plt.title("Acceleration")
#plt.xlabel("x acceleration (a0/s^2)")
#plt.ylabel("y acceleration (a0/s^2)")
#
#i3 = 0
#for num in accX:
#	if i3 == 0:
#		plt.plot(accX[i3], accY[i3], 'r*', markersize = 15)
#	else:
#		plt.plot(accX[i3], accY[i3], 'b.')
#	i3 = i3 + 1

#plt.grid()
#plt.axhline(y=0, color = 'k')
#plt.axvline(x=0, color = 'k')


plt.figure(4)
plt.subplot(121)
plt.title("Acceleration x")
plt.xlabel("Time (s)")
plt.ylabel("x-Acceleration (a0/s^2)")
plt.plot(times, accX)
plt.subplot(122)
plt.title("Acceleration y")
plt.xlabel("Time (s)")
plt.ylabel("y-Acceleration (a0/s^2)")
plt.plot(times, accY)


#Question 2--------------------------------------------------------------------------------------------------------
print "\nQuestion 4:"

ftX = numpy.fft.fft(accX)
n = accX.size
freqs = numpy.fft.fftfreq(n, timestep)
plt.figure()
plt.plot(freqs, ftX, 'b')
plt.plot(freqs, ftX, 'r.')
plt.show()



