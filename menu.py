from clases import lista_parametros
from clases import limpiar
from clases import llista
import time
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