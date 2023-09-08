# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 22:25:23 2023

@author: pc
"""

archivo = 'expansion_termica.csv'

class ExpansionTermica:
    def __init__(archivo,self):
        self.temperatura = []
        self.volumen = []
        
        with open(self.archivo, 'r', encoding='latin-1') as archivo2:
            lines = archivo2.readlines()
                
            for index, line in enumerate(lines):
                if index == 0:
                    continue 
                
            puntos = line.strip().split(',')
            self.temperatura.append(float(puntos[0]))
            self.volumen.append(float(puntos[1]))
    
    def coeficiente (ExpansionTermica):
        
        i=0
           
        while i in range(0, len(self.temperatura)):

               v = self.volumen[i]
               h = self.temperatura[i] -self.temperatura[i-1]

        
        derivadaV = (self.volumen[i] - self.volumen[i-1])/(2*h)
        derivadaT = (self.temperatura[i] - self.temperatura[i-1]/(2*h))
        
        a = (derivadaV)/temperatura[i]*derivadaT
        
        
    
    


        
    
