# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 17:40:23 2025

@author: rpach
"""

class Persona:
    def __init__(self, _nom, _dni):
        self._nom = _nom
        self._dni = _dni  # Se mantiene como atributo numérico

    def getDNI(self):
        return self._dni  # No necesita paréntesis

    def getNombre(self):
        return self._nom

    # Métodos de comparación
    def __lt__(self, other):
        return self._dni < other._dni  # Compara con otra persona

    def __le__(self, other):
        return self._dni <= other._dni

    def __gt__(self, other):
        return self._dni > other._dni

    def __ge__(self, other):
        return self._dni >= other._dni

    def __eq__(self, other):
        return self._dni == other._dni

    def __ne__(self, other):
        return self._dni != other._dni

    def __str__(self):
        return f"Persona({self._dni} | {self._nom})"


# Bucle para ingresar datos
personas = []  # Lista para almacenar objetos Persona

while True:
    _nom = input("Ingrese el nombre del cliente o 'fin' para salir: ")
    if _nom.lower() == "fin":
        break
    
    _dni = int(input("Ingrese el número de DNI: "))
    
    # Crear objeto Persona
    persona = Persona(_nom, _dni)
    personas.append(persona)  # Guardamos la persona en la lista

# Mostrar todas las personas registradas
for p in personas:
    print(p) 

class promotor(Persona):
    def __init__(self,_nom,_dni,_clientes=None):
     super().__init__ (_nom,_dni)
     self._clientes=_clientes if _clientes is not None else []
     
    def addCliente (self, cliente):
        self._clientes.append (cliente)
    
    def getCntClientes (self):
        return len(self._clientes)
    
    def getClientes (self):
        return self._clientes
    
    def __str__(self):
        return f"Promotor({self._nom})"
    
class cliente(Persona):
    def __init__(self,_nom,_dni,_promotor,_tipoSeguro):
        super().__init__(_nom,_dni)
        self._promotor=_promotor
        self._tipoSeguro=[_tipoSeguro]
        
    def getPromotor (self):
        return (self._promotor)
    
    def addTipoSeguro (self,seguro):
        self._tipoSeguro.append(seguro)
        
    def getSeguros (self):
        return (self._tipoSeguro)
def main():     
 prom=promotor("Diego de la Vega", 24317128)
 cli01=cliente("Carlos Avellaneda",11765989,prom,"Seguro de vida")
 prom.addCliente(cli01)
 cli02=cliente("Analia Mendizabal",11765989,prom,"Seguro automotor NPE 321")
 cli02.addTipoSeguro("Seguro de Vida")
 prom.addCliente(cli02)
 cli03=cliente("Jaquin Mendez",11765989,prom,"Seguro automotor AB 321 ZF")
 prom.addCliente(cli03)

 print(f"{prom}")

 print("Listado de clientes:")

 for cli in prom.getClientes():
     print(f"{cli}")
     print("Productos contratados:")
     for s in cli.getSeguros():
      print(f"\t {s}")
        
if __name__ == "__main__":
    main()
