import numpy as np
import unittest
import satellite
import frames 
import default_blocks as defblock
from ddt import ddt, data, unpack, file_data

@ddt
class TestDefaultBlocks(unittest.TestCase):

	@file_data("test-data/test_defaultsunsensor.json")
	@unpack
	def test_sunsensor(self,value): 
		qBI = np.asarray(value[0])
		v_sv_i = np.asarray(value[1])

		v_pos_i = np.array([1e6,-2.03,-3.0])
		v_vel_i = np.array([2.0e3,2.8,-73.2])
		qBO = frames.qBI2qBO(qBI,v_pos_i,v_vel_i)
		state = np.hstack((qBO,np.zeros(3)))
		mySat = satellite.Satellite(state,12.0)
		mySat.setQ_BI(qBI)
		result = defblock.sunsensor(mySat,v_sv_i)
		v_expected = value[2],value[3];
		self.assertTrue(np.allclose(result,v_expected))
	
	@file_data("test-data/test_defaultsunsensor.json")
	@unpack
	def test_magmeter(self,value): 
		qBI = np.asarray(value[0])
		v_sv_i = np.asarray(value[1])

		v_pos_i = np.array([1e6,-2.03,-3.0])
		v_vel_i = np.array([2.0e3,2.8,-73.2])
		qBO = frames.qBI2qBO(qBI,v_pos_i,v_vel_i)
		state = np.hstack((qBO,np.zeros(3)))
		mySat = satellite.Satellite(state,12.0)
		mySat.setQ_BI(qBI)
		result = defblock.magmeter(mySat,v_sv_i)
		v_expected = value[2],value[3];
		self.assertTrue(np.allclose(result,v_expected))
	
	def test_gyroscope(self):
		v_w_BI_b = np.array((-3.9999, 4.8575, 0))
		self.assertTrue(np.allclose(defblock.gyroscope(v_w_BI_b),v_w_BI_b))

	sgp_output = np.genfromtxt('sgp_output.csv',delimiter=",")	
	defblock.J2_propagator()
	defblock.gps()
	gps_output= np.genfromtxt('gps_output.csv',delimiter=",")
	J2_output = np.genfromtxt('J2_output.csv',delimiter=",")
	T = sgp_output[:,0]
	l = np.linspace(0,len(T),12,int)	#Sample 7 data points from entire file
	
	@data(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9])
	def test_GPS(self,value):
		v_expected = self.sgp_output[int(value),1:4]
		v_result = self.gps_output[int(value),1:4]
		self.assertTrue(np.allclose(v_expected,v_result))
	
	@data(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9])
	def test_J2_propagator(self,value):
		v_expected = self.sgp_output[int(value),1:4]
		v_result = self.J2_output[int(value),1:4]
		self.assertTrue(np.allclose(v_expected,v_result))
		
	def test_controller(self):
		qBO = np.array([.0,0.,0.,1.])
		state = np.hstack((qBO,np.array([0.10050588,-0.05026119,-0.3014887])))
		mySat = satellite.Satellite(state,128.05)
		self.assertTrue(np.allclose(defblock.controller(mySat),np.zeros(3)))

	def test_disturbance(self):
		qBO = np.array([.0,0.,0.,1.])
		state = np.hstack((qBO,np.array([0.10050588,-0.05026119,-0.3014887])))
		mySat = satellite.Satellite(state,128.05)
		self.assertTrue(np.allclose(defblock.disturbance(mySat),np.zeros(3)))
	
if __name__=='__main__':
	unittest.main(verbosity=2)