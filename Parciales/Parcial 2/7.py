# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:15:31 2023

@author: pc
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


n = 500
x = np.linspace(-1 , 1 , n)
y = np.linspace(-1 , 1 , n)

def Punto7(x, y):
    if (x**2 + y**2) >= 1:
        return np.sqrt(x**2 + y**2)
    else:
        return 0

def Volumen ():
    for i in range(0 , n+1):
        for j in range(0, n+1):
            valor_promedio = (Punto7(x[i], y[j]) + Punto7(x[i] + 1, [j]) + Punto7(x[i], y[j + 1]) + Punto7(x[i] + 1, y[j + 1]))/4
            area_cuadrado = (x[i+1]-x[i]) * (y[j+1]-y[j])
    return valor_promedio * area_cuadrado
