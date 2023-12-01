# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:37:49 2023

@author: ENVY
"""
import numpy as np

P=np.array([[2,-1],[1,2],[1,1]])
y=np.array([2,1,4])
dot = np.dot(np.dot(np.linalg.inv(np.dot(P.T, P)),P.T), y)


print(dot)

prueba=np.linspace(0,5,100)

def valor1(prueba):
  return 2*prueba-2

def valor2(prueba):
  return (1-prueba)/2

def valor3(prueba):
  return 4-prueba


u1 = np.array([3, 1, 0, 1])
u2 = np.array([1, 2, 1, 1])
u3 = np.array([-1, 0, 2, -1])
b = np.array([-3, -3, 8, 9])

m = np.array(u1, u2, u3)

def minimos_cuadrados(matriz):
    col = np.column_stack((u1, u2, u3))
    t = np.transpose(col)
    AdotT = np.dot(t, col)
    
    inv = np.linalg.inv(AdotT)
    invdotT = np.dot(inv, t)
    peso = np.dot(invdotT,b)
    valor = np.dot(col,peso)
    for i in range(len(valor)):
        valor[i]=round(valor[i],14)
    
    return valor


