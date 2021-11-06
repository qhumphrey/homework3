# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 15:41:27 2021

@author: qhumphre
"""

import numpy as np
import math
from scipy.integrate import trapz,quadrature,romb,romberg,dblquad
from scipy.interpolate import CubicSpline
np.set_printoptions(threshold=np.inf)

def Txy(x,y):
    z = 2*x*y + 2*x - x**2 -2*y**2 + 72
    return(z)
    
Tz = np.vectorize(Txy)    

x0 = 0
x1 = 8
y0 = 0
y1 = 6
delx = 0.1

X = np.arange(x0, (x1 + delx), delx)
Y = np.arange(y0, (y1 + delx), delx)
XX,YY = np.meshgrid(X,Y,sparse=True)

T = Txy(XX,YY)
Nx = XX.shape[1]
Ny = YY.shape[0]

# Trapezoidal Rule
ny = np.arange(0,Ny,1)
F=np.zeros(Ny)

for i in ny:
    Tzy = T[i,:]
    F[i]=trapz(Tzy,X)
    
Txy_trap=trapz(F,Y)
print("Average temperature on the plate using the Trapezoidal Rule is ", Txy_trap)

# Romberg Integration
Xx = np.arange(0,8.0078125, 0.0078125)
Yy = np.arange(0,6.0123,0.0123)

xz,yz=np.meshgrid(Xx,Yy,sparse=True)
zz=Txy(xz,yz)

for i in ny:
    Tzy = zz[i,:]
    F[i]=romb(Tzy,0.0078125)
    
FXY=CubicSpline(Yy,F)
Txy_romb=romberg(FXY,0,6)
print("The average temperature on the plate using the Romberg Method is ", Txy_romb)


# Built in python integrals
fdq = lambda y,x:(2*x*y+2*x-x**2-2*y**2+72)
FXY = dblquad(fdq,0,8,lambda x:0,lambda x:6)
print("The average temperature on the plater using the Romberg Method is ", FXY)