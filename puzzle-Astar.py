import math
import os
import sys
import time
from queue import PriorityQueue


class Tablero:
    def __init__(self, estados):
        self.tamano = int(math.sqrt(len(estados)))
        self.estados = estados

    def ejecutar_accion(self, accion):
        nuevos_estados = self.estados[:]
        indice_vacio = nuevos_estados.index('0')
        if accion == 'L':
            if indice_vacio % self.tamano > 0:
                nuevos_estados[indice_vacio - 1], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[indice_vacio - 1]
        if accion == 'R':
            if indice_vacio % self.tamano < (self.tamano - 1):
                nuevos_estados[indice_vacio + 1], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[indice_vacio + 1]
        if accion == 'U':
            if indice_vacio - self.tamano >= 0:
                nuevos_estados[indice_vacio - self.tamano], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[
                    indice_vacio - self.tamano]
        if accion == 'D':
            if indice_vacio + self.tamano < self.tamano * self.tamano:
                nuevos_estados[indice_vacio + self.tamano], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[
                    indice_vacio + self.tamano]
        return Tablero(nuevos_estados)


class Nodo:
    def __init__(self, estado, padre, accion):
        self.estado = estado
        self.padre = padre
        self.accion = accion

    def __repr__(self):
        return str(self.estado.estados)

    def __eq__(self, otro):
        return self.estado.estados == otro.estado.estados

    def __hash__(self):
        return hash(self.estado)


def get_hijos(padre_Nodo):
    hijos = []
    accions = ['L', 'R', 'U', 'D']
    for accion in accions:
        hijo_estado = padre_Nodo.estado.ejecutar_accion(accion)
        hijo_Nodo = Nodo(hijo_estado, padre_Nodo, accion)
        hijos.append(hijo_Nodo)
    return hijos


def gcalc(Nodo):
    ''' calcula g(n): encuentra el costo del estado actual a partir del estado origen o inicial'''
    contador = 0
    while Nodo.padre is not None:
        Nodo = Nodo.padre
        contador += 1
    return contador


def hamming(estados):
    ''' heuristicaa Hamming: cuenta el numero de posiciones erroneas en diferentes estados'''
    distancia = 0
    objetivo_estados = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '0']
    for i in objetivo_estados:
        if objetivo_estados.index(i) - estados.index(i) != 0 and i != 0:
            distancia += 1
    return distancia


def manhattan_calculate(estados):
    '''heuristicaa Manhattan: cuenta el numero de cuadros a partir de una ubicacion en relacion a su posicion final'''
    contador = 0
    for i in range(0, 15):
        index = estados.index(str(i + 1))  # because range starts at 0
        contador += (abs((i / 4) - (index / 4)) + abs((i % 4) - (index % 4)))  # %4 is the column and /4 is the row
    return contador


def find_path(Nodo):
    '''Returns path back to input Nodo or source Nodo'''
    path = []
    while (Nodo.padre is not None):
        path.append(Nodo.accion)
        Nodo = Nodo.padre
    path.reverse()
    return path


def goal_test():
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '0']


def astar(estado_inicial, estado_objetivo, heuristica):
    '''A* Search Algorithm'''
    start_time = time.time()
    frontera = list()
    contador = 0
    visitado = dict()
    frontera.append(estado_inicial)
    visitado[estado_inicial.estado] = estado_inicial
    while frontera:
        minim = []
        holder = []
        for x in frontera:
            if heuristica == 0:
                minim.append(hamming(x.estado.estados) + gcalc(x))  # This is the F = h + g
            elif heuristica == 1:
                minim.append(manhattan_calculate(x.estado.estados) + gcalc(x))
            holder.append(x)
        m = min(minim)  # finds minimum F value
        estado_inicial = holder[minim.index(m)]

        if estado_inicial.estado.estados == estado_objetivo:  # solution found!
            end_time = time.time()
            print("\n\nSolucion:")
            print("Movimientos: " + str(' '.join(find_path(estado_inicial))))
            print("Numero de nodos expandidos: " + str(contador))
            print("Tiempo empleado: " + str(round((end_time - start_time), 3)))
            # print("Memory Used: " + str(sys.gettamanoof(visitado) + sys.gettamanoof(frontera)) + " kb")
            break

        frontera.pop(frontera.index(estado_inicial))
        for hijo in get_hijos(estado_inicial):
            contador += 1
            s = hijo.estado
            if s not in visitado or gcalc(hijo) < gcalc(visitado[s]):
                visitado[s] = hijo
                frontera.append(hijo)


def main():
    ei = ['1', '3', '4', '8', '5', '2', '0', '6', '9', '10', '7', '11', '13', '14', '15', '12']
    # ei = ['0', '15', '14', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1', '2', '3']

    heuristica = input("Enter heuristica either 'H' or 'M' (H is Hamming and M is Manhattan): ")
    if heuristica == 'H':
        heuristica = 0
    elif heuristica == 'M':
        heuristica = 1

    max_depth = 10
    root = Nodo(Tablero(ei), None, None)
    astar(root, goal_test(), heuristica)
    frontera = []
    frontera.append(root)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

