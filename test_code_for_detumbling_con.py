import satellite as sat
import numpy as np
import detumbling_con as detcon
 
iniState=np.zeros([7])
mag1=np.zeros([3])
mag2=np.array([1,1,1])
s = sat.Satellite(iniState,0)
s.setMag_b_m_p(mag1)
s.setMag_b_m_c(mag2)
magMoment = detcon.magMoment(s)
print magMoment