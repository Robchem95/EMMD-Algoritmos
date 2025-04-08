# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 10:28:08 2025

@author: rpach
"""

class Estudiante:
    def __init__(self, Nombre, Edad, grado):
        self.Nombre=Nombre
        self.Edad=Edad
        self.grado=grado
    
    def estudiar(self):
        print(f"el estudiante {self.Nombre} esta estudiando")

Estudiante1= Estudiante("Juan", "15", "primero")

Estudiante1.estudiar()
