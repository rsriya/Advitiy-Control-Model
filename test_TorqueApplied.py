import numpy as np
import unittest
import satellite
from TorqueApplied import ctrlTorqueToVoltage, currentToTorque

from ddt import ddt, data, unpack

@ddt
class TestTorqueApplied(unittest.TestCase):
    @file_data("test-data/test_TorqueApplied.json") 
# =============================================================================
#     order of data in json file --> Quaternion, v_magnetic_field_i, Control Torque from control law,
#     current vector with first element as time , voltage(output of ctrlTorqueToVoltage),Torque(output of currentToTorque)
# =============================================================================
    @unpack
    
    def test_ctrlTorqueToVoltage(self,value):        #converts control torque to voltage wiht help of earth's field
        v_magnetic_field_i= np.asarray(value[0])
        v_state=np.asarray(value[1])
        v_ctrlTorque=np.asarray(value[2])
        mySat = satellite.Satellite(v_state,1.0)
        
        mySat.setMag_i(v_magnetic_field_i)
        mySat.setControl_b(v_ctrlTorque)
        voltage = ctrlTorqueToVoltage(mySat)
        result= voltage
        self.assertTrue(np.allclose(result, np.asarray(value[4])))
        
    def test_currentToTorque(self,value):        #converts control torque to voltage wiht help of earth's field
        v_magnetic_field_i= np.asarray(value[1])
        v_state=np.asarray(value[0])
        v_current=np.asarray(value[3]) #first element should be time then next three are currents
        mySat = satellite.Satellite(v_state,1.0)
        
        mySat.setMag_i(v_magnetic_field_i)
        torque = currentToTorque(v_current, mySat)
        result= torque
        self.assertTrue(np.allclose(result,np.asarray(value[5])))
            
if __name__=='__main__':
    unittest.main(verbosity=2)
