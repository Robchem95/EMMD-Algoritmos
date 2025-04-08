# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:47:05 2025

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
    total_clientes = 0
    clientes_potenciales = 0
    edades_potenciales=[]
    edades_totales=[]
    edades_prom_sup=[]
    
    edadStr = input("Ingrese la primera edad (o un número negativo para terminar): ")
    edadInt = int(edadStr)

    while edadInt >= 0:
        if edadInt>0:
           total_clientes += 1  # Contamos el cliente
        if 35 <= edadInt <= 45:
            clientes_potenciales += 1  # Contamos si es potencial
            edades_potenciales.append(edadInt)
            
        edades_totales.append(edadInt)
        claf_asignada=clasificador(edadInt)
        print(f"la edad del cliente es de {edadInt}, y su clasificación es\
              {claf_asignada}")
        
        edadStr = input("Siguiente edad (o un número negativo para terminar): ")
        edadInt = int(edadStr)
        
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
    print(edades_prom_sup)    
    
if __name__ == "__main__":
    main()
