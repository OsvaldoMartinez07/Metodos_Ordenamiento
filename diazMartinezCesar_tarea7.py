#Subir a Github y separar en modulos para ordenarlo 
#Tener un modulo de ordenamiento otro de list


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
#PARTE 2

def metodo_de_lista():
    rep = True
    metodo_2 = False
    while True:
        try:
            if rep == True or metodo_2:
                print("Hola! Elije el método de ordenamiento para tu lista :)")
                print("""       --- MENÚ ---
                1. Bubble sort
                2. Selection sort
                3. Insertion sort
                4. Merge sort
                5. Quick sort
                6. Salir   
                """)
                print("Selecciona con un numero entero")
                metodo = int(input(">"))
                longitud = lista_parametros()
                time.sleep(1)
                limpiar()
                print(f"Metodo de ordenamiento: {metodo}")
                print(f"Longitud de lista: {longitud}")
                print("Espere . . . ")
                time.sleep(1)
                lista_ligada = llista() #creando lista vacia
                lista_ligada.construir_lista(longitud)
            time.sleep(1)
            limpiar()
            match metodo:
                case 1:
                    metodo = "Bubble sort"
                    lista_ligada.bubble_sort()
                    print("Asi termina la lista :)")
                    lista_ligada.mostrar()
                case 2:
                    metodo = "Selection sort"
                    lista_ligada.slection_sort(longitud)
                    print("Asi termina la lista :)")
                    lista_ligada.mostrar()
                case 3:
                    metodo = "Insertion sort"
                case 4:
                    metodo = "Merge sort"
                case 5:
                    metodo = "Quick sort"
                case 6:
                    break
                #Añadir salir despues
        except:
            print("Error_1: ingrese numeros enteros")
        print("Así termina la lista :)")
        rep = False
        lista_ligada.mostrar()
        print("¿Repetir animación? [y/n]")
        op = input("> ")
        if op == "y":
            lista_ligada = llista()
            lista_ligada.construir_lista(longitud)
            print("¿Elegir otro método? [y/n]")
            if input("> ") == "y":
                rep = True
        else:
            break   
        limpiar()
def main():
    run = metodo_de_lista()
    print("Programa finalizado")
    
if __name__ == '__main__':
    main()