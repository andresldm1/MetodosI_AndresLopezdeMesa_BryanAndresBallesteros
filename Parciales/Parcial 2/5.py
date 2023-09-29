# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 18:52:24 2023

@author: pc
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

x = sym.symbols('x', real=True, positive=True)
n = 20

Laguerre = []  

for i in range(1, n + 1):
    Roots, Weights = np.polynomial.laguerre.laggauss(i)
    Laguerre.append(Roots)  

print(Laguerre)