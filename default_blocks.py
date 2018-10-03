import qnv
import numpy as np
import frames as fs
#Default models of sensor : (ideal sensor) measured output = actual output (no noise or bias)

def sunsensor(sat):
	v_sv_o = sat.getSun_o()
	v_q_BO = sat.getQ_BO()
	v_sv_b = qnv.quatRotate(v_q_BO,v_sv_o)
	
	return v_sv_b

def magmeter(sat):
	v_B_o = sat.getMag_o()
	v_q_BO = sat.getQ_BO()
	v_B_b = qnv.quatRotate(v_q_BO,v_B_o)
	return v_mag_b

def gps(sat):
	v_pos = sat.getPos() 
    v_vel = sat.getVel()
    time = sat.getTime()

	return np.hstack([v_pos_m,v_vel_m,time_m])

def gyroscope(v_wBIB):
	return v_wBIB

def J2_propagator(sat):
	v_pos = sat.getPos() 
    v_vel = sat.getVel()
    time = sat.getTime()
    
	return np.hstack([v_pos_m,v_vel_m,time_m])

#Default models of controller: (no controller)

def controller(sat):
	return(np.zeros(3))

#Default models of environment: (no disturbance)
def disturbance(sat):
	return(np.zeros(3))

#Default models of estimator: (returns qBO obtained by integrator)
def estimator(sat):
return(sat.getQ_BO())