import numpy as np
import math
import constants_1U as C1U

Re = C1U.R_EARTH
GM = C1U.G* C1U.M_EARTH
h= C1U.MODEL_STEP ## timestep

#RV_0 and dT are the input to the j2.py (states- position and velocity in ECI frame in m and m/s)
#output is states after certain time in the orbit with effect of j2

#for now this test RV_0 is of spacketrack report 3
RV_0 =np.array ([2.328966083033799659e+06 ,-5.995216038277293555e+06,1.719978735358979320e+06,2.911101021348036738e+03,-0.9816403338867760340e+03,-7.090499329297967961e+03])
#RV_0 = ... input for state
dT = C1U.dT

RV_0 = np.reshape(RV_0, (1,6))
RV = RV_0.copy() # initializing the RV 
N = np.size(dT)
j2_output = np.zeros([N,7]) # creating a matrix to store the output,

def j2fcn(Re,GM,J2, t, RV_s):
    RV = RV_s.copy()
    r = np.sqrt((RV[0,0])**2+ (RV[0,1])**2+ (RV[0,2])**2 )
    r2 = r**2
    r3 = r2*r
    RVdot = np.zeros([1,6]);
  
    #print(RVdot)
    #print(RVdot[0,1])
    #print( np.shape(RVdot))
    A1 = -GM/r3
    A2 = 1.5*J2*Re**2/r2
    A3 = 3*A2
    A4 = 5*A2*(RV[0,2]**2)/r2
 
    RVdot[0,3] = A1*RV[0,0]*(1+A2-A4);
    RVdot[0,4] = A1*RV[0,1]*(1+A2-A4);
    RVdot[0,5] = A1*RV[0,2]*(1+A3-A4);
    RVdot[0,0] = RV[0,3];   
    RVdot[0,1] = RV[0,4];
    RVdot[0,2] = RV[0,5];
    return RVdot


def rk4J2(t,RV_p,Re,GM,J2,j2fcn,h): #This is Runge Kutta-4 solver for ordinary differential equation.
	#RV_0	#position and velocity  at t = t0	
    #RV_p   #position and velocity  at previous instant

	#rk-4 routine
	k1 = h*j2fcn(Re,GM,J2, t, RV_p)
	k2 = h*j2fcn(Re,GM,J2, t+0.5*h, RV_p+0.5*k1)
	k3 = h*j2fcn(Re,GM,J2, t+0.5*h, RV_p+0.5*k2)
	k4 = h*j2fcn(Re,GM,J2, t+h, RV_p+k3)

	RV_new = RV_p.copy()+ (1.0/6.0)*(k1 + 2.*k2 + 2.*k3 + k4)	

	return t, RV_new

for i in range(0,N):
    t =dT[i] 
    j2_output[i,0],RV_new  = rk4J2(t,RV,Re,GM,J2,j2fcn,h)
    j2_output[i,1:7] = RV_new.copy()    
    RV= RV_new.copy()
    
np.savetxt("j2_output.csv", j2_output, delimiter=",") #Saves j2_output to csv file


