import numpy
import hw3_Conversions as conv

def makeArrays(pos0, vel0, q1, Z):
    print "in makeArrays"
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
    
    acc0 = func.getAccel(func.coulombForce(q1, Z, pos0))
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
    print posX


    arrays = numpy.array([posX, posY, velX, velY, accX, accY])
    return arrays

    
    
def test(num):
    print "in test"
    return num
    
    