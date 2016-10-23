import numpy
import hw3_Conversions as conv


#Constants
k = 8.9875517873681764e9 #Coulomb constant [N*m^2/C^2]
k = conv.m_bohr(conv.m_bohr(k)) #Coulomb constant [N*a0^2/C^2]
m_e = 9.10938356e-31 #electron mass [kg]

#Find the Coulomb force on a charged particle due to a charged particle located at the origin
##params: q1 = the charge of particle 1 [e], q2 = the charge of particle 2 [e], pos = an array with the x,y position coordinates of particle 1 [a0]
##return: an array with the x,y components of the resultant force vector [N]
def coulombForce(q1, q2, pos):
	q1 = conv.e_Coulomb(q1)
	q2 = conv.e_Coulomb(q2)
	x = pos[0]
	y = pos[1]
	r_sq = (x^2) + (y^2)
	theta = numpy.arctan2(x, y)

	force = (k*q1*q2)/r_sq
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
		




