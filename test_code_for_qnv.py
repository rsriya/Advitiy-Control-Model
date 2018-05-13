import numpy as np
import qnv

q1=np.array([1,2,3,4])
q2=np.array([1,-2,-3,-4])
q3=np.array([1,-2,-3,4])
q4=np.array([1,2,3,-4])
q5=np.array([-1,-2,-3,4])
q6=np.array([-1,2,3,-4])
q7=np.array([0,2,-3,0])
q8=np.array([0,-2,3,0])
q9=np.array([0,0,0,0])

flag=1 # tessting for quatInv

G=qnv.quatInv(q1)
if (G == q2).all() == 0:
	flag=0

G=qnv.quatInv(q3)
if (G == q4).all() == 0:
	flag=0

G=qnv.quatInv(q5)
if (G == q6).all() == 0:
	flag=0

G=qnv.quatInv(q7)
if (G == q8).all() == 0:
	flag=0

G=qnv.quatInv(q9)
if (G == q9).all() == 0:
	flag=0

if flag == 1:
	print ("all cases passed for quatInv")
else:
	print ("error for quatInv")
 
flag=1 # testing for quatMultiplynorm
m1 = np.array([1,-1,-1,1])
m2 = np.array([-1,1,-1,-1])
m3 = np.array([0,1,1,-1])
m4 = np.array([0,1,-1,0])
m5 = np.array([0,0,-1,1])
m6 = np.array([0,4,0,0])
m7 = np.array([-1,-3,-1,-1])
m8 = np.array([-1,-1,-1,-1])
m9 = m6/np.linalg.norm(m6)
m10 = m7/np.linalg.norm(m7)
m11 = m8/np.linalg.norm(m8)

G=qnv.quatMultiplynorm(m1,m2)
if (G == m9).all() == 0:
	flag=0

G=qnv.quatMultiplynorm(m3,m2)
if (G == m10).all() == 0:
	flag=0

G=qnv.quatMultiplynorm(m4,m5)
if (G == m11).all() == 0:
	flag=0

if flag == 1:
	print ("all cases passed for quatMultiplynorm")
else:
	print ("error for quatMultiplynorm")

flag=1 # testing for quatMultiplynorm

G=qnv.quatMultiplyunnorm(m1,m2)
if (G == m6).all() == 0:
	flag=0

G=qnv.quatMultiplyunnorm(m3,m2)
if (G == m7).all() == 0:
	flag=0

G=qnv.quatMultiplyunnorm(m4,m5)
if (G == m8).all() == 0:
	flag=0

G=qnv.quatMultiplyunnorm(q9,q9)
if (G == q9).all() == 0:
	flag=0

if flag == 1:
	print ("all cases passed for quatMultiplyunnorm")
else:
	print ("error for quatMultiplyunnorm")
