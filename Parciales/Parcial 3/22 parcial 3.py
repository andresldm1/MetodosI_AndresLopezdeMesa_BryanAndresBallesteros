# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:36:08 2023

@author: ENVY
"""

import numpy as np

def Function(x):
    c = 729/10000
    return  c*np.sin(x)**2 + (np.sin(x))**6 - c

x = np.linspace(0,np.pi,50)
y = Function(x)

def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

def GetNewtonMethod(f,df,xn,itmax=100,precision=1e-8):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)

            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
    
    if it == itmax:
        return False
    else:
        return xn
    
root = GetNewtonMethod(Function,Derivative,1.)

def GetAllRoots(x, tolerancia=10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewtonMethod(Function,Derivative,i)
        
        if root != False:
            
            croot = np.round(root, tolerancia)
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots

Roots = GetAllRoots(x)
print(Roots)