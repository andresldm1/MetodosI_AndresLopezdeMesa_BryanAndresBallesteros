# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:48:17 2023

@author: pc
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

class Mineral:
    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravity):
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity

    def silicato (Mineral):
        if "O" and "Si" in Mineral.composicion:
                
            return True
    
    
    def densidad (Mineral):
        densidad_agua = 997
        densidad_mineral = densidad_agua*float(Mineral.densidad)
        
        print(densidad_mineral + "kg/m^3")
    
    def color_mas_comun(Mineral):
       fig, ax = plt.subplots(figsize=(1, 1))
       ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=Mineral.color))
       ax.set_xlim(0, 1)
       ax.set_ylim(0, 1)
       ax.axis('off')
    
    def funcion_4(Mineral):
        if Mineral.rompimiento_por_fractura == True:
            print("La dureza del mineral es de" + Mineral.dureza + "," + 
                  "tiene una organizacion" + Mineral.sistema_cristalino + "y" + 
                  "tiene rompimiento por fractura.")
        if Mineral.rompimiento_por_fractura != True:
            print("La dureza del mineral es de" + Mineral.dureza + "," + 
                  "tiene una organizacion" + Mineral.sistema_cristalino + "y" + 
                  "tiene rompimiento por fractura.")
    
    
                  