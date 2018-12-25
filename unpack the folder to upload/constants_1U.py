#Constants used in the code for simulation of 1U satellite

import numpy as np
import datetime as dt
from math import sqrt

#--------Earth and environment
W_EARTH = 7.2921150e-5; # rotation velocity of the earth (rad per second)
G = 6.67408e-11; #universal gravitational constant, SI
M_EARTH = 5.972e24; #mass of earth, kg
R_EARTH = 6371.0e3; #radius of earth, m

AU = 149597870610.0 #Distance between sun and earth in meters
R_SUN = 695500000.0 #Radius of the Sun in meters

#v_w_IO_o = np.array([0., np.sqrt(G*M_EARTH/(R_EARTH + ALTITUDE)**3), 0.]) #w of ecif wrt orbit in orbit frame

#------------date format yyyy,mm,dd
LINE1 = ('1 41783U 16059A   18093.17383152  .00000069  00000-0  22905-4 0  9992') #Insert TLE Here
LINE2 = ('2 41783  98.1258 155.9141 0032873 333.2318  26.7186 14.62910114 80995') 
# below is spacetrack .. just for testing
LINE1 = ('1 88888U 16059A   80275.98708465 +.00073094 +13844-3 +66816-4 0  9998') #Insert TLE Here
LINE2 = ('2 88888  72.8435 115.9689 0086731  52.6988 110.5714 16.05824518   105') 

### add TT and dT in constants
TT = 1440#100.0 # total time in minutes   ##add in constant
dT = np.linspace(0.0,TT*60.0,(TT*60*10 + 1)) #np.linspace(0.0,TT*60.0,(100*60*10 + 1)) ## dT is in seconds. total 100 minutes here. 10 is for 1/timestep
####ADDED following block ......these data based on spacetrack report3 page 81
MeanMo = 16.05824518#14.62910114  #16.05824518
Eccen = 0.0086731#0.0032873     # 0.0086731
Incl_deg =72.8435 #98.1258  #72.8435
MeanAnamoly_deg = 110.5714#26.7186  #110.5714
ArgP = 52.6988#333.2318 #52.6988
RAAN_deg = 115.9689 #155.9141  # 115.9689
DMeanMotion =.00073094
DDMeanMotion =0.13844e-3
BStar =0.66816e-4#0.22905e-4 #7e-07

EPOCH = dt.datetime(2018, 4, 03, 12, 50, 19)	#date of epoch of TLE t=0 -- in future should be extracted from TLE
EQUINOX = dt.datetime(2018, 3, 20, 13, 05, 00)	#day of equinox
STEPRUT = 1.002738 #sidereal time = stperut * universal time

#-- --------Satellite structural properties (assumed to be uniform with small off-diagonal)
MASS_SAT = 0.850	#in kg
Lx = 0.1	#in meters

Ixx = 0.00152529
Iyy = 0.00145111
Izz = 0.001476	
Ixy = 0.00000437
Iyz = -0.00000408
Ixz = 0.00000118

m_INERTIA = np.array([[Ixx, Ixy, Ixz], [Ixy, Iyy, Iyz], [Ixz, Iyz, Izz]])	#actual inertia
#m_INERTIA = 0.001*np.array([[1.0,0.,0.],[0.,1.,0.],[0.,0.,1.]])	#identity inertia
m_INERTIA_inv = np.linalg.inv(m_INERTIA)	#inverse of inertia matrix

#Side panel areas
v_Ax = np.array([0.01,0.,0.])	#area vector perpendicular to x-axis in m^2
v_Ay = np.array([0.,0.01,0.])	#area vector perpendicular to y-axis in m^2
v_Az = np.array([0.,0.,0.01])	#area vector perpendicular to z-axis in m^2

#--------Simulation constants
CONTROL_STEP = 2.0	#control cycle time period in second
MODEL_STEP = 0.1	#step size in environmental data in seconds
#--------Magnetorquer parameters
INDUCTANCE = 68e-3	#Inductance of torquer in Henry
RESISTANCE = 107.0	#Resistance of torquer	in Ohm
PWM_FREQUENCY = 1e3 	#frequency of PWM signal 
PWM_AMPLITUDE = 3.3	#PWM amplitude in volt

TORQUER_Ax = 0.07**2	#Area of torquer monted on y-z plane
TORQUER_Ay = 0.07**2	#Area of torquer monted on x-z plane
TORQUER_Az = 0.07**2	#Area of torquer monted on x-y plane

#Disturbance model constants
SOLAR_PRESSURE = 4.56e-6	#in N/m^2
REFLECTIVITY = 0.2
r_COG_2_COM_b = np.array([-0.067e-2,-0.58e-2,-0.067e-2])
AERO_DRAG = 2.2
RHO = 0.218e-12