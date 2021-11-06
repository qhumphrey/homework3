# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 13:24:20 2021

@author: qhumphre
"""

import numpy as np
from scipy import integrate
from scipy import special

# F = 2*x**1.5
# x - meters, F - kN
x0 = 0
x1 = 10

def F(x):
     F = 2*x**1.5
     return F

# Built-in Gauss Quad Function  
z, w = integrate.quad(F, x0, x1)
print("Integration results by built in Gauss-Quad is: ", z)

# Gauss Quadrature
def gaussquad(F, x0, x1, n):
    [x,w] = special.orthogonal.roots_legendre(n + 1)
    G = 0.5*(x1-x0)*sum(w*F(0.5*(x1-x0)*x+0.5*(x0+x1)))
    return G

LL = x0
UL = x1
SI = int(input('Enter n value: '))
Gresult = gaussquad(F, LL, UL, SI)
print("Integration results by Gaussian Quadrature Method is: ", Gresult)


# Trapezoidal Rule
    
def trapezoidal(x0,x1,n):
    # need to create a step size
    h = (x1 - x0)/n
    
    # Find the sum of the two points
    integration = F(x0) + F(x1)
    
    # need to calculate trapezoidal loop and extrpolation steps 
    # for i in range 1 to n
    for i in range(1,n):
        k = x0 + i*h
        integration += 2*F(k)
        
    # Finding final integration value
    integration = integration*(h/2)
    
    return integration

# input secction
lower_limit = x0
upper_limit = x1
sub_interval = int(input('Enter n value: '))

# Call trapezoidal method
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal Method is: ", result)


# Built in Trapezoidal Function
N = 10;
deltax = (x1 - x0)/N;
x = np.linspace(x0,x1,N+1);
f = 2*x**1.5;
A = np.trapz(f,x,deltax);
print("Integration results by using the built-in Trapezoidal function is: ", A)