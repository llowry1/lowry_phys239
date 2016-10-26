import numpy
import hw3_Conversions as conv


#Constants
k = 8.9875517873681764e9 #Coulomb constant [N*m^2/C^2]
k = conv.m_bohr(conv.m_bohr(k)) #Coulomb constant [N*a0^2/C^2]
m_e = 9.10938356e-31 #electron mass [kg]

#Find the Coulomb force on a charged particle due to a charged particle located at the origin
##params: q1 = the charge of (negative) particle 1 [e], q2 = the charge of particle 2 [e], pos = an array with the x,y position coordinates of particle 1 [a0]
##return: an array with the x,y components of the resultant force vector [N]
def coulombForce(q1, q2, pos):
	q1 = conv.e_Coulomb(q1)
	q2 = conv.e_Coulomb(q2)
	x = pos[0]
	y = pos[1]
	r_sq = (x**2) + (y**2)
	theta = numpy.arctan2(y, x)

	force = ((-1)*k*q1*q2)/r_sq
	f_x = force*numpy.cos(theta)
	f_y = force*numpy.sin(theta)

	return numpy.array([f_x, f_y])

#Get acceleration of electron from a force acting on it
##params: force = an array with the x,y components of the acting force [N]
##return: an array with the x,y components of the resultant acceleration vector [a0/s^2]
def getAccel(force):
	a_x = conv.m_bohr(force[0]/m_e)
	a_y = conv.m_bohr(force[1]/m_e)
	
	return numpy.array([a_x, a_y])

#Get the position, velocity, and acceleration of an electron after some time t given its initial position, velocity, and acceleration
##params: pos0 = an array with the x,y initial position coordinates [a0], vel0 = an array with the x,y components of the initial velocity vector [a0/s], acc0 = an array with the x,y components of the initial acceleration vector [a0/s^2], t = the time interval [s]
##return: an array containing arrays with x,y components of the new position, velocity, and acceleration vectors
def getPosAndVel(pos0, vel0, acc0, t):
	acc = acc0
	vel = vel0 + acc*t
	pos = pos0 + vel*t

	return numpy.array([pos, vel, acc])
	
def test(num):
        return num
		

#
def makeArrays(pos0, vel0, q1, Z):
    
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
    
    
        arrays = numpy.array([posX, posY, velX, velY, accX, accY])
        return arrays
