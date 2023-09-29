# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:29:17 2023

@author: pc
"""
import numpy as np
import sympy as sym
import math as ma

x = sym.symbols('x', real=True, positive=True)
n = 20

Hermite = []  

for i in range(1, n + 1):
    Roots, Weights = np.polynomial.hermite.hermgauss(i)
    Hermite.append(Roots) 

def GetGaussHermiteRecursive(x, n):
    
    if n==0:
        poly = 1
    elif n==1:
        poly = 2*x
    else:
        poly = 2*x*GetGaussHermiteRecursive(x, n-1) - 2*(n-1)*GetGaussHermiteRecursive(x, n-2)
    
    return poly

def GetDiffHermite(n, x):
    Pn = GetGaussHermiteRecursive(x, n)

    return sym.diff(Pn, x, 1)  
     
def GetWeightsHermite (n):
    
    Roots = Hermite

    

    DHermite = []
    
    for i in range(n+1):
        DHermite.append(GetDiffHermite(i,x))
    
    Dpoly = sym.lambdify([x],DHermite[n-1],'numpy')
    Weights = ((2**(n-1))*np.math.factorial(n)*np.sqrt(np.pi))/((n**2)*(Dpoly(Roots))**2) 
    
    return Weights  



def funcion(roots, n, Hermite):
    return ((1/(np.sqrt(2*n)*ma.factorial(n)))) * (1/(np.pi(1/4)))*(roots)*(np.e((-roots*2/2)))*Hermite

def Integral(funcion, roots, n, Hermite):
    return (np.abs(funcion(roots, n, Hermite))*2)*(roots*2)

Roots, Weights = np.polynomial.hermite.hermgauss(n)

def respuesta (funcion, roots, n, Weights, Hermite):
    return sum(Integral(funcion, roots, n, Hermite)*Weights)





