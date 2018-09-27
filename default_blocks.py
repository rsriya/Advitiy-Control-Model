import qnv
import numpy as np
import frames as fs
#Default models of sensor : (ideal sensor) measured output = actual output (no noise or bias)

def sunsensor(sat,v_sv_i):
	v_sv_b = qnv.quatRotate(sat.getQ_BI(),v_sv_i)
	v_sv_o = qnv.quatRotate(sat.getQ_BO(),v_sv_i)
	return v_sv_b, v_sv_o;

def magmeter(sat,v_mag_i):
	v_mag_b = qnv.quatRotate(sat.getQ_BI(),v_mag_i)
	v_mag_o = qnv.quatRotate(sat.getQ_BO(),v_mag_i)
	return v_mag_b, v_mag_o;

def gps():
	m_sgp_output_i = np.genfromtxt('sgp_output.csv', delimiter=",")
	np.savetxt('gps_output.csv',m_sgp_output_i, delimiter=",")

def gyroscope(v_wBIB):
	return v_wBIB

def J2_propagator():
	m_sgp_output_i = np.genfromtxt('sgp_output.csv', delimiter=",")
	np.savetxt('J2_output.csv',m_sgp_output_i, delimiter=",")

#Default models of controller: (no controller)

def controller(sat):
	return(np.zeros(3))

#Default models of environment: (no disturbance)
def disturbance(sat):
	return(np.zeros(3))

#Default models of estimator: (by sanskriti on monday)
