%%SGP 4 model's test case given in (test case is run in 360 minutes(6hr) of interval)
%%http://www.celestrak.com/NORAD/documentation/spacetrk.pdf page 80
%1 88888U 80275.98708465 .00073094 13844-3 66816-4 0 8
%2 88888 72.8435 115.9689 0086731 52.6988 110.5714 16.05824518 105
%important terms
%for reference http://www.stltracker.com/resources/tle
% https://www.celestrak.com/NORAD/documentation/tle-fmt.asp
%also page 62  Chap orbital mechanics of book HandBook of Space Technology
%by Wilfried Ray et al
%1 88888U 80(epoach year)275.98708465(epoach day of year) .00073094(1st derivative of mean motion) 13844-3(second derivative of mean motion)
%66816-4(B-star drag) 0 8(checksum)
%2 88888 72.8435(inclination-degree) 115.9689(right ascension of ascending node) 0086731(eccentricity-decimal point assumed)
%52.6988(argument of perigee- deg) 110.5714(mean anamoly-deg)
%16.05824518(mean motion) 10(revolution number at epoach)5(checksum)%%


%%
%%TLE data of pratham
% 1 99999U 16005A   16((epoach year)) 270.24769735(epoach day of year)  .00000368(1st derivative of mean motion)  
%00000-0(second derivative of mean motion)  70534-4(B-star drag) 0  1235 (checksum)
%2 99999  98.2056(inclination-degree) 327.8012(right ascension of ascending node) 0027951(eccentricity-decimal point assumed) 
% 267.5222(argument of perigee- deg)   9.4278(mean anamoly-deg) 14.63691895(mean motion)    1(revolution number at epoach)3(checksum)


% output of the sgp model here is in position (m) and velocity (m/s)
% in the test data it is in position (km) and velocity (km/s)
%% TLE DATA of pratham dated 19 July 2017 from n2yo
% 1 41783U 16059A   17198.94132223 +.00000076(1st time deri mean motion) +00000-0 +24125-4 0  9997
% 2 41783 098.1648(incl) 259.9939(rsc) 0034865(ecc) 065.5965(arg prg) 294.8869(mean anaomaly) 14.62844671043094
%%
%%get latest tle data from https://www.space-track.org/#/tle 
%%
% commented data belongs to sgp test data
% non commented is of pratham
meanMo =   16.05824518; %14.62910114;  %;
orbEcc=   0.0086731; %0.0032873;% 0.0027951;%
orbInc= 72.8435;  % 98.1258;%
meanAno=  110.5714;  %26.7186;% 9.4278;%   %% change
argPer =  52.6988;  %333.2318;%267.5222; %    %% change
rghtAsc= 115.9689; %155.9141;%327.8012;%     %% change
SGPdragp1 =  .00073094;  %0.0000007;%  % from ---First time derivative of mean motion(rad/min^2)
SGPdragp2 =0.13844*10^(-3); %0;%     % Second time derivative of mean motion (rad/min^3
SGP4dragp = 0.66816*10^(-4); %0.24125*10^(-4);%
%Epyear EpJD and EpTime used for calculation of t0
% BUT   t0 is not used in sgp.m 
%sgp is meant to run when tle data equal to epoach
EpYear =  0; %1980
EpJD   = 0; %275.98..
EpTime  = 0 ;
revNo = 9;%10;

    n0 = 2*pi*meanMo/1440; % Mean motion (rad/min) 
    e0 = orbEcc; % Eccentricity (0.0<=e0>=1.0)   2)
    i0 = pi*orbInc/180; % Inclination (rad)      3)
    M0 = pi*meanAno/180; % Mean anomaly (rad)    4)
    w0 = pi*argPer/180; % Argument of perigee (rad)   5)
    Ohm0 = pi*rghtAsc/180; % Right ascension of the ascending node (rad) 6)
    dn0 = 2*2*pi*SGPdragp1/(1440^2); % First time derivative of mean motion(rad/min^2)
    ddn0 = 6*2*pi*SGPdragp2/(1440^3); % Second time derivative of mean motion (rad/min^3)
    Bstar = SGP4dragp; % SGP4 type drag coefficient
    % Mean year (400 year period) in days:
    meanYearDays = (400*365 + 4 * (100/4 - 1) + 1) / 400;
    % Time of epoch (since y2k)
    t0 = (EpYear*meanYearDays + EpJD + EpTime)*1440;
    modTLE = [t0 dn0 ddn0 Bstar i0 Ohm0 e0 w0 M0 n0 revNo];
    modTLE_launch1 =modTLE;
    save modTLE_launch1;
    %%
%%
 dT = 0:0.1:100*60; % in seconds (100 min)
% dT = [0, 360, 720, 1080, 1440]
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % [X, V] = sgp(modTLE, dT/60); 
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % SGP_test_case_launch1 = [dT/60; X'; V'];
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % plot(dT, X)
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % save SGP_test_case_launch1.mat 


%% Summary and Conclusion
%Test case has be taken from SGP4 model from the referece 
%%http://www.celestrak.com/NORAD/documentation/spacetrk.pdf page 80
% gave into sgp.m and validated

%function [R,dR] = sgp(modTLE,dT)
%This code is a matlab implementation of the SGP Fortran code in the
% Startrack report #3.
%
% The matlab code was derived mainly by porting and editing the
% FORTRAN routines in NORAD’s Spacetrack report #3.
% According to a statement in that report, the document is free
% of copyrights and open to unlimited public distribution.
%
% This matlab code is distributed under the same conditions
%
%
% Created 15/10-2001 by
    % Klaus Krogsgaard & Torsten Lorentzen
% - - - - - - - - - - - - - - - - - - - - - - - - -
%
% SGP model for predicting orbit position.
%

% - - - - - - - - - - - - - - - - - - - - - - - - -
% Constants given by the modified NORAD TLE (all at epoch)
% - - - - - - - - - - - - - - - - - - - - - - - - -


t0 = modTLE(1);
dn0 = modTLE(2); % first time derivative of the mean motion
ddn0 = modTLE(3); % second time derivative of mean motion
Bstar = modTLE(4); % Drag parameter
i0 = modTLE(5); % inclination
Ohm0 = modTLE(6); % right ascension of the ascending node
e0 = modTLE(7); % eccentricity
w0 = modTLE(8); % argument of perigee
M0 = modTLE(9); % mean anormaly
n0 = modTLE(10); % mean motion
revNo = modTLE(11); % Number of revolutions before epoch
% - - - - - - - - - - - - - - - - - - - - - - - - -
% Other constants
% - - - - - - - - - - - - - - - - - - - - - - - - -
GM = 398603 * 10^9;
er = 6378.135; %% in km 
ke = 0.0743669161; %converted to er/min ^3/2
% aE = 6378160; % equatorial radius of the  Earth
aE = 1;% give result in Earth radii
min_per_day = 1440;
sec_per_day = 86400;
km_per_er = er;
J2 = 5.413080*10^-4 * 2; % second gravitational zonal harmonic of the Earth
J3 = -0.253881*10^-5; % third gravitational zonal harmonic of the Earth
J4 = -0.62098875*10^-6 * 8/3; % fourth gravitational zonal harmonic of the Earth
% - - - - - - - - - - - - - - - - - - - - - - - - -
% Local constants
% - - - - - - - - - - - - - - - - - - - - - - - - -
a1 = (ke/n0)^(2/3);
delta1 = 3/4 * J2 * (aE/a1)^2 * (3*((cos(i0))^2)-1)/((1-e0^2)^(3/2));
a0 = a1 * (1 - 1/3*delta1 - delta1^2 - 134/81*delta1^3);
p0 = a0 * (1 - e0^2);
q0 = a0 * (1-e0);
L0 = M0 + w0 + Ohm0;
dOhm = - (3/2) * J2 * (aE/p0)^2 * n0 * cos(i0);
dw = (3/4) * J2 * (aE/p0)^2 * n0 * (5*(cos(i0))^2-1);
% - - - - - - - - - - - - - - - - - - - - - - - - -
% Secular effects of drag and gravitation
% - - - - - - - - - - - - - - - - - - - - - - - - -
a = a0 * ( n0 ./ (n0 + 2*(dn0/2)*(dT) + 3*(ddn0/6)*dT.^2)).^(2/3); % vector
e = zeros(1,length(dT)); % vector
for i=1:length(a)
if ( a(i)>q0 )
e(i) = 1 - q0/a(i);
else
e(i) = 10^-6;
end;
end;
p = a .* (1-e.^2); % vector
OhmS0 = Ohm0 + dOhm * dT; % vector
wS0 = w0 + dw * (dT); % vector
Ls = mod(L0 + (n0 + dw + dOhm)*(dT) + dn0/2 * (dT).^2 + ddn0/6 * (dT).^3,2*pi); % vector
% - - - - - - - - - - - - - - - - - - - - - - - - -
% Long period periodic effects
% - - - - - - - - - - - - - - - - - - - - - - - - -
axNSL = e .* cos(wS0); % vector
ayNSL = e .* sin(wS0) - 1/2 * J3/J2 * aE./p * sin(i0); % vector
L = mod(Ls - 1/4 * J3/J2 * aE./p .* axNSL * sin(i0) * (3+5*cos(i0))/(1+cos(i0)),2*pi); % vector
% - - - - - - - - - - - - - - - - - - - - - - - - -
% Iteration for short period periodics below...
% - - - - - - - - - - - - - - - - - - - - - - - - -
tol = 10^-12;
U = mod(L - OhmS0,2*pi); % vector
Ew1 = U; % vector
Ew2 = Ew1; % vector
dEw = (U - ayNSL.*cos(Ew1) + axNSL.*sin(Ew1) - Ew1) ./ (-ayNSL.*sin(Ew1) - axNSL.*cos(Ew1) + 1); % vector

for i=1:length(dEw)
if abs(dEw(i)) > 1
Ew2(i) = Ew1(i) + sign(dEw(i)); %vector
else
Ew2(i) = Ew1(i) + dEw(i);
end;
end;

for i=1:length(Ew1)
    count = 0;
while abs(dEw(i))>tol
    count = count+1
Ew1(i) = Ew2(i);
dEw(i) = (U(i) - ayNSL(i).*cos(Ew1(i)) + axNSL(i).*sin(Ew1(i)) - Ew1(i)) ./ ...
(-ayNSL(i).*sin(Ew1(i)) - axNSL(i).*cos(Ew1(i)) + 1);
if abs(dEw(i)) > 1
Ew2(i) = Ew1(i) + sign(dEw(i)); %vector
else
Ew2(i) = Ew1(i) + dEw(i);
end;
end;
end;
ecosE = axNSL.*cos(Ew2) + ayNSL.*sin(Ew2); % vector
esinE = axNSL.*sin(Ew2) - ayNSL.*cos(Ew2); % vector
SQeL = axNSL.^2 + ayNSL.^2; % vector
pL = a.*(1 - SQeL); % vector
r = a.*(1 - ecosE); % vector
dr = ke * sqrt(a)./r .* esinE; % vector
rdv = ke * sqrt(pL)./r; % vector
sinu = a./r .* (sin(Ew2) - ayNSL - axNSL.*esinE./(1+sqrt(1-SQeL))); % vector
cosu = a./r .* (cos(Ew2) - axNSL + ayNSL.*esinE./(1+sqrt(1-SQeL))); % vectro
u = mod(atan2( sinu,cosu ),2*pi); % vector
% - - - - - - - - - - - - - - - - - - - - - - - - -
% Short term perturbations
% - - - - - - - - - - - - - - - - - - - - - - - - -
rk = r + 1/4 * J2 * aE^2./pL * (sin(i0))^2 .* cos(2*u); % vector
uk = u - 1/8 * J2 * (aE./pL).^2 * (7 * (cos(i0))^2 - 1) .* sin(2*u); % vector
Ohmk = OhmS0 + 3/4 * J2 * (aE./pL).^2 * cos(i0) .* sin(2*u); % vector
ik = i0 + 3/4 * J2 * (aE./pL).^2 * sin(i0) * cos(i0) .* cos(2*u); % vector
% - - - - - - - - - - - - - - - - - - - - - - - - -
% Unit orientation vectors
% - - - - - - - - - - - - - - - - - - - - - - - - -
R = zeros(length(uk),3); % vector
dR = zeros(length(uk),3); % vector
for i=1:length(uk)
    M_vec = [ -sin(Ohmk(i))*cos(ik(i)) cos(Ohmk(i))*cos(ik(i)) sin(ik(i)) ]; % vector
N_vec = [ cos(Ohmk(i)) sin(Ohmk(i)) 0 ]; % vector
U_vec = M_vec * sin(uk(i)) + N_vec * cos(uk(i)); % vector
V_vec = M_vec * cos(uk(i)) - N_vec * sin(uk(i)); % vector
% - - - - - - - - - - - - - - - - - - - - - - - - -
% Position and velocity
% - - - - - - - - - - - - - - - - - - - - - - - - -
R(i,:) = rk(i) * U_vec; % vector
dR(i,:) = dr(i) * U_vec + rdv(i) * V_vec; % vector
end;
% - - - - - - - - - - - - - - - - - - - - - - - - -
% Transforming position to Cartesian coordinates in meters and velocity to meters/sec
% - - - - - - - - - - - - - - - - - - - - - - - - -
R = R * km_per_er /aE;
R = R * 1000;
dR = dR * km_per_er / aE * min_per_day / sec_per_day;
dR = dR * 1000;
SGP_test_case_launch1 = [dT/60; R'; dR'];
save SGP_test_case_launch1.mat 