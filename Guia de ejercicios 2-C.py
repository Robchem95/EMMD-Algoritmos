# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 19:36:13 2025

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
    
    def ordenarClientes(self):
        """Ordena los clientes por DNI usando QuickSort manual"""
        self._clientes = self.quick_sort(self._clientes)

    def quick_sort(self, lista):
        """Implementación de QuickSort manual"""
        if len(lista) < 2:
            return lista  
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.getDNI() < pivote.getDNI()]
        iguales = [x for x in lista if x.getDNI() == pivote.getDNI()]
        mayores = [x for x in lista[1:] if x.getDNI() > pivote.getDNI()]
        return self.quick_sort(menores) + iguales + self.quick_sort(mayores)
    
    def buscarCliente (self, dni):
        """Busca un cliente por DNI usando búsqueda binaria."""
        izquierda, derecha = 0, len(self._clientes) - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            cliente_actual = self._clientes[medio]

            if cliente_actual.getDNI() == dni:
                return cliente_actual  # Cliente encontrado
            elif cliente_actual.getDNI() < dni:
                izquierda = medio + 1  # Buscar en la mitad derecha
            else:
                derecha = medio - 1  # Buscar en la mitad izquierda

        return None  # Cliente no encontrado
           
    def __str__(self):
        return f"Promotor({self._nom})"
    
class cliente(Persona):
    def __init__(self,_nom,_dni,_promotor,_tipoSeguro):
        super().__init__(_nom,_dni)
        self._promotor=_promotor
        self._tipoSeguro=[_tipoSeguro]
        
    def getPromotor (self):
        return (self._promotor.getNombre())
    
    def addTipoSeguro (self,seguro):
        self._tipoSeguro.append(seguro)
        
    def getSeguros (self):
        return (self._tipoSeguro)
    
    def __str__(self):
        return f"""cliente:{self._nom},DNI: {self._dni},
                   Promotor:{self._promotor},
                   Seguro:{self._tipoSeguro})"""

def main():
 prom=promotor("Diego de La Vega", 95581869)
 fp = open('clases.txt', 'r', encoding='utf8')
 for linea in fp:
  lineaLimpia = linea.strip()
  datosCliente = lineaLimpia.split(";")
  if(len(datosCliente) == 3):
   _dni = int(datosCliente[0].strip())
   _nom = str(datosCliente[1].strip())
   _tipoSeguro=str(datosCliente[2].strip())
   _Seguros=_tipoSeguro.split("|")
   nuevoCliente=cliente(_nom, _dni, prom, _Seguros)
   prom.addCliente(nuevoCliente)
 prom.ordenarClientes()
 print(prom)
 print("Listado de clientes ordenado por DNI: ")
 for cli in prom.getClientes():
    print (cli)
 print("\n🔍 Búsqueda de cliente por DNI 🔍")
 dni_buscar = int(input("Ingrese el DNI a buscar: "))
 cliente_encontrado = prom.buscarCliente(dni_buscar)

 if cliente_encontrado:
     print(f"✅ Cliente encontrado: {cliente_encontrado}")
 else:
     print("❌ Cliente no encontrado") 
 fp.close()
 


if __name__ == "__main__":
    main()