import random
import os
import time
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
#Class
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class llista:
    def __init__(self):
        self.cabeza = None #lista sin cosas :O
    def construir_lista( self, longitud):
        for _ in range(longitud):
            dato = random.randint(1, 99)
            nuevo = Nodo(dato)
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            #print(self.__str__) tal vez agregue
    def obtener_en_posicion(self, posicion):
        actual = self.cabeza
        contador = 0
        while actual:
            if contador == posicion:
                return actual.dato
            actual = actual.siguiente
            contador += 1
        return None
    def bubble_sort(self):
        if self.cabeza is None:
            return

        hubo_cambios = True
        print("")
        print("")
        while hubo_cambios:
            limpiar()
            self.mostrar()
            time.sleep(1.9)
            hubo_cambios = False
            actual = self.cabeza

            while actual and actual.siguiente:
                if actual.dato > actual.siguiente.dato:
                    # intercambio de datos
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                    hubo_cambios = True
                actual = actual.siguiente
    def slection_sort(self,longitud):
        movimientos = 0
        if self.cabeza is None:
            return
        actual = self.cabeza
        for _ in range(longitud):
            #print(f"Moviemientos: {movimientos}")
            limpiar()
            self.mostrar()
            time.sleep(1.9)
            min = actual
            buscador = actual.siguiente
            while buscador:#mientras no sea None
                if buscador.dato < min.dato:
                    min = buscador
                buscador = buscador.siguiente
            actual.dato, min.dato = min.dato, actual.dato
            actual = actual.siguiente
            #movimientos += 1
    def merge_sort(self):
        pass
            
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")
#FUNCIONES DE MAIN
def lista_parametros():
    print("Elije la longitud de tu lista :D")
    while True: 
        try:
            print("La longitud debe ser mayor a 0 y menor o igual a 30")
            longitud_lista = int(input(">"))
            if longitud_lista > 0 and longitud_lista <= 30:
                return longitud_lista
        except:
            print("La longitud de la lista debe ser un numero entero")