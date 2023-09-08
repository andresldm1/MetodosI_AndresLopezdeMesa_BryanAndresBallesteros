# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:58:00 2023

@author: pc
"""

import csv

minerales = []

with open('minerales.csv', newline='') as csvfile:
    reader = minerales.csv.DictReader(csvfile)
    
    next(reader, None)

    for row in reader:
        minerales.append(row)
    

def silicatos (minerales):
    numero = 0
    for i in range(len(minerales)):
        if "O" or "Si" in minerales[i][5]:
            numero += 1
    return numero
    
def promedio_densidad (minerales):
    
    suma = 0
    for i in range(len(minerales)):
        densidad = 997*minerales[i][7]
        suma += densidad
        
    promedio = suma/len(minerales)
    
    return promedio


        
        
