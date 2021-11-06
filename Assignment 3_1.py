# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 11:59:44 2021

@author: qhumphre
"""

# Assignment 3
# 1. Solve the integral using the following numerical methods
# [0 1] sqrt(1+x**2)dx

# Trapezoidal Rule

import math
import numpy as np

x0 = 0
x1 = 1

# Define integrating function
def f(x):
    return math.sqrt(1 + x**2)

# Trapezoidal Method
def trapezoidal(x0,x1,n):
    # need to create a step size
    deltax = (x1 - x0)/n
    
    # Find the sum of the two points
    integration = f(x0) + f(x1)
    
    # need to calculate trapezoidal loop and extrapolation steps 
    # for i in range 1 to n
    for i in range(1,n):
        k = x0 + i*deltax
        integration += 2*f(k)
        
    # Finding final integration value
    integration = integration*(deltax/2)
    
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
fx = (1 + x**2)**0.5;
A = np.trapz(fx,x,deltax);
print("Integration results by using the built-in Trapezoidal function is: ", A)


# Simpson's Rule

def Simp13(x0, x1, n):
    # Step Size
    h1 = (x1 - x0)/n
    
    # Sum
    integration1 = f(x0) + f(x1)
    
    for i in range(1,n):
        k2 = x0 + i*h1
        
        if i%2 == 0: # if there is no remainder for i/2
            integration1 = integration1 + 2*f(k2)
        else:
            integration1 = integration1 + 4*f(k2)
            
        # Final integration value
        integration1 = integration1*(h1/3)
        
        return integration1
    
# Input Section
lowlim = x0
uplim = x1
sub_int = int(input('Enter n value: '))

# Call Simpson's 1/3 Rule
result1 = Simp13(lowlim, uplim, sub_int)
print("Integration result by Simpson's 1/3 rule: ", result1)

# Built-in Simpson's rule