# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 20:08:30 2025

@author: rpach
"""
Lista_de_aprobados_directamente=[]    
Lista_de_aprobados_indirectamente=[]
Lista_de_no_aprobados=[]

class Estudiante:
    def __init__(self, Nombre, Nota_1, Nota_2, Nota_3):
        self.__Nombre=Nombre
        self.__Nota_1=Nota_1
        self.__Nota_2=Nota_2
        self.__Nota_3=Nota_3
    
    def get_nombre(self):
        return self.__Nombre

    def get_notas(self):
        return self.__Nota_1, self.__Nota_2, self.__Nota_3
    
    def aprobacion(self):
       
        if Nota_1>=6 and Nota_2>=6 and Nota_3>=6:
            print (f"{self.__Nombre} esta aprobado directamente")
            Lista_de_aprobados_directamente.append(self.__Nombre)
            
        elif Nota_1>=4 and Nota_2>=4 and Nota_3>=4:
            if (Nota_1+Nota_2+Nota_3)/3>=6:
                print(f"{self.__Nombre} esta aprobado indirectamente")
                Lista_de_aprobados_indirectamente.append(self.__Nombre)
            else:
                print (f"{self.__Nombre} No esta aprobado")
                Lista_de_no_aprobados.append(self.__Nombre)
        else:
            print (f"{self.__Nombre} No esta aprobado")
            Lista_de_no_aprobados.append(self.__Nombre)                    
              
while True:
    Nombre=input("ingrese el nombre del estudiante o fin para salir: ")
    if Nombre.lower()=="fin":
       break
    
    Nota_1=int(input("ingrese la nota 1: "))
    Nota_2=int(input("ingrese la nota 2: "))
    Nota_3=int(input("ingrese la nota 3: "))
    
    estudiante= Estudiante(Nombre, Nota_1, Nota_2, Nota_3)
    estudiante.aprobacion()

print(f"los aprobados directamente son: {Lista_de_aprobados_directamente}")
print(f"los aprobados indirectamente son: {Lista_de_aprobados_indirectamente}")
print(f"los no aprobados son: {Lista_de_no_aprobados}") 
    



