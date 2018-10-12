import numpy as np
from datetime import *
from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv
import math
import constants_1U as C1U

#line1 = ('1 41783U 16059A   18093.17383152  .00000069  00000-0  22905-4 0  9992') #Insert TLE Here
#line2 = ('2 41783  98.1258 155.9141 0032873 333.2318  26.7186 14.62910114 80995') 

## https://celestrak.com/NORAD/documentation/spacetrk.pdf    page 81
#line1 = ('1 88888U 16059A   80275.98708465 +.00073094 +13844-3 +66816-4 0  9998') #Insert TLE Here
#line2 = ('2 88888  72.8435 115.9689 0086731  52.6988 110.5714 16.05824518   105') 


line1 = ('1 25544U 98067A   08264.51782528 -.00002182 +00000-0 -11606-4 0 0001N')
line2 = ('2 25544 051.6416 247.4627 0006703 130.5360 325.0288 15.7212539156353N')
sat = twoline2rv(line1, line2, wgs72) #wgs72 is a particular model used by sgp4
pi = math.pi
print line1
SatNo = line1[2:7] 
#3    08-08    Classification (U=Unclassified)    U
ClassNo =line1[7]
#4	10-11	International Designator (Last two digits of launch year)	98
LaunchYear=float(line1[9:11])
#5	12-14	International Designator (Launch number of the year)	067
LaunchNumber=line1[11:14]
#6	15-17	International Designator (piece of the launch)	A
LaunchPiece=line1[14:17]
#7    19-20    Epoch Year (last two digits of year)    08
EpoachYr = float(line1[18:20])
#8    21-32    Epoch (day of the year and fractional portion of the day)    264.51782528 ##three number than decimal then 8 numbers
Epoach = float(line1[20:32])
#9    34-43    First Time Derivative of the Mean Motion divided by two [11]    -.00002182
DMeanMotion =float(line1[33:43])
if line1[33]=='-' :
    DMeanMotion =-1*DMeanMotion
#10 45-52    Second Time Derivative of Mean Motion divided by six (decimal point assumed)    00000-0
DDMeanMotion = float(line1[45:50])*10**(-5)
if line1[44]=='-' :
    DDMeanMotion =-1*DDMeanMotion
if line1[50]=='-' :
    DDMeanMotion =DDMeanMotion*10**(-float(line1[51]))
if line1[50]=='+' :
    DDMeanMotion =DDMeanMotion*10**(float(line1[51]))
##line1[45:52] = '00000-0'
#11    54-61    BSTAR drag term (decimal point assumed) [11]    -11606-4
#BStar =float(line1[53:61])
# self.assertTrue(line1[53]=='-') 
BStar = float(line1[54:59])
if line1[53]=='-' :
    BStar =-1*BStar
if line1[59]=='-' :
    BStar =BStar*10**(-float(line1[60]))
if line1[59]=='+' :
    BStar =BStar*10**(float(line1[60]))
#12    63-63    The number 0 (originally this should have been "Ephemeris type")    0
EphemerisT= line1[62] 
#13    65-68    Element set number. Incremented when a new TLE is generated for this object.[11]    292
ElementSetNo = line1[64:68]

##############################

print line2
#1    01-01    Line number    2
#2    03-07    Satellite number    25544
SanNo2 = line2[2:7] 
#3    09-16    Inclination (degrees)    51.6416
Incl_deg = float(line2[8:16])
#4    18-25    Right ascension of the ascending node (degrees)    247.4627
RAAN_deg = float(line2[17:25])
#5    27-33    Eccentricity (decimal point assumed)    0006703
Eccen = float(line2[26:33])/10**7
#6    35-42    Argument of perigee (degrees)    130.5360
ArgP =  float(line2[34:42] )
#7    44-51    Mean Anomaly (degrees)    325.0288
MeanAnamoly_deg = float(line2[43:51])
#8    53-63    Mean Motion (revolutions per day)    15.72125391
MeanMo= float(line2[52:63])
#9    64-68    Revolution number at epoch (revolutions)    56353
RevNo = float(line2[63:68])
#10    69-69    Checksum (modulo 10)    7

### Print
print('Satellite No. %s' % SatNo)
print('Class No. %s' %ClassNo)
print('International Designator (Last two digits of launch year) %s' %LaunchYear)
print('International Designator (Launch number of the year) %s' %LaunchNumber)
print('International Designator (piece of the launch) %s' %LaunchPiece)
print('Epoch Year (last two digits of year) %s' %EpoachYr)
print('Epoch (day of the year and fractional portion of the day) %s' %Epoach)
print('First Time Derivative of the Mean Motion divided by two %s' %DMeanMotion)
print('Second Time Derivative of Mean Motion divided by six (decimal point assumed) %s' %DDMeanMotion)
print('BSTAR drag term (decimal point assumed) %s' %BStar)
print('Ephemeris type %s' %EphemerisT)
print('Element set number (Incremented when a new TLE is generated for this object) %s' %ElementSetNo)

print('Satellite No. %s' % SanNo2)
print('Inclination (degrees) %s' % Incl_deg)
print('Right ascension of the ascending node (degrees) %s' % RAAN_deg)
print('Eccentricity (decimal point assumed) %s' % Eccen)
print('Argument of perigee (degrees) %s' % ArgP)
print('Mean Anomaly (degrees) %s' % MeanAnamoly_deg)
print('Mean Motion (revolutions per day) %s' % MeanMo)
print('Revolution number at epoch (revolutions)     %s' % RevNo)
