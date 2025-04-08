# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 11:05:33 2025

@author: rpach
"""

def clasificador(b):
    """clasifica a una persona de acuerdo a su edad como cliente potencial"""
    if b>45:
        return ("falso")
    if b<35:
        return ("falso")
    else:
        return ("verdadero")
    
def main():
 fp = open('datos.txt', 'r', encoding='utf8')
 diccedad={}
 for linea in fp:
  lineaLimpia = linea.strip()
  datosCliente = lineaLimpia.split(";")
  if(len(datosCliente) == 2):
   dni = int(datosCliente[0].strip())
   edad = int(datosCliente[1].strip())
   diccedad.update({dni:edad})  
 fp.close()
 
 
 
 dicNombres = {}
 fp = open('nombres.txt', 'r', encoding='utf8')
 for linea in fp:
  lineaLimpia = linea.strip()
  datosCliente = lineaLimpia.split(";")
  if(len(datosCliente) == 2):
   dni = int(datosCliente[0].strip())
   nombre = datosCliente[1].strip()
   dicNombres.update({dni: nombre})
 fp.close() 
 

  
 for dni in diccedad.keys():
     yedad=diccedad[dni]
     ynombre=dicNombres.get(dni, "desconocido")
     print(f"DNI: {dni}-Nombre:{ynombre}-Edad:{yedad}")

 edadInt=list(diccedad.values())
 
 total_clientes = 0
 clientes_potenciales = 0
 edades_potenciales=[]
 edades_totales=[]
 edades_prom_sup=[]
  
 for x in edadInt:
     if x>0:
        total_clientes += 1  # Contamos el cliente
        edades_totales.append(x)
     if 35 <= x <= 45:
         clientes_potenciales += 1  # Contamos si es potencial
         edades_potenciales.append(x)
         
 
 if total_clientes>0:    
    promedio_total=sum(edades_totales)/len(edades_totales)
 else:
    promedio_total=0

 for edad in edades_totales:
    if edad> promedio_total:
        edades_prom_sup.append(edad)
        
     
# Verificamos si hay clientes ingresados para evitar división por cero
 if total_clientes > 0:
    porcentaje = (clientes_potenciales / total_clientes) * 100
    print(f"\nTotal de clientes analizados: {total_clientes}")
    print(f"Clientes potenciales (35-45 años): {clientes_potenciales}")
    print(f"Porcentaje de clientes potenciales: {porcentaje:.2f}%")
 else:
    print("\nNo se ingresaron clientes válidos.")   

 print(f"la lista de edad de clientes potenciales es {edades_potenciales}")
 print(f"la lista de edad de todos los clientes  es {edades_totales}")
 print(f"el valor promedio de edad  es de {promedio_total:.2f}")
 cont_edad=len(edades_prom_sup)
 print(f"el número de edades que superan al promedio es de {cont_edad}")
 
 
 print("La lista de clientes potenciales es:")\
 
 for dni,edad in diccedad.items():
     if 35<=edad<=45:
         nombre=dicNombres.get(dni, "desconocido")
         print(f"{nombre}-{edad}")
 
 
    
if __name__ == '__main__':
 main()