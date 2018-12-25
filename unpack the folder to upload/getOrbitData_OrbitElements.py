import numpy as np
from datetime import *
import constants_1U as C1U
import sgp

MeanMo = C1U.MeanMo 
Eccen = C1U.Eccen 
Incl_deg  = C1U.Incl_deg
MeanAnamoly_deg = C1U.MeanAnamoly_deg
ArgP =C1U.ArgP 
RAAN_deg = C1U.RAAN_deg
DMeanMotion = C1U.DMeanMotion
DDMeanMotion = C1U.DDMeanMotion
BStar = C1U.BStar

dT = np.linspace(0.0,100.0*60.0,(100*60*10 + 1)) ## dT is in seconds. total 100 minutes here. 10 is for 1/timestep
sgp_output = np.zeros([N,7])
sgp_output = np.zeros([ len(dT),7], dtype = 'float')
sgp_output[:,0],sgp_output[:,1:4],sgp_output[:,4:7] = sgp.sgp_fn(dT,MeanMo,Eccen,Incl_deg,MeanAnamoly_deg,ArgP,RAAN_deg,DMeanMotion,DDMeanMotion,BStar)
np.savetxt("sgp_output_1.csv", sgp_output, delimiter=",") #Saves sgp_output to csv file
