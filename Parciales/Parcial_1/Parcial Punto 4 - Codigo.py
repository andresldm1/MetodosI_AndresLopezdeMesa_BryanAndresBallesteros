# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:26:34 2023

@author: pc
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

X = np.array([1.4, 3.5, 5.6])
Y = np.array([0.4007954931819738, 0.594128102489774, 0.29802795523938164])

def Lagrange(x,X,i):
    
    L = 1
    
    for j in range(X.shape[0]):
        if i != j:
            L *= (x - X[j])/(X[i]-X[j])
            
    return L
def Interpolate(x,X,Y):
    
    Poly = 0
    
    for i in range(X.shape[0]):
        Poly += Lagrange(x,X,i)*Y[i]
        
    return Poly


x = np.linspace(0.,6.,100)
y = Interpolate(x,X,Y)

y1 = np.interp(x,X,Y)

#se grafica
plt.plot(x,y,color='k')
plt.scatter(X,Y,color='r',marker='o')
plt.legend()

x = sym.Symbol('x',real=True)
y = Interpolate(x,X,Y)
y = sym.simplify(y)

print(y)



