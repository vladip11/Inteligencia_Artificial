# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:41:03 2021

@author: VladimirP11
"""

import random 

modelo = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1,1, 0, 1, 0, 1, 0,0, 1, 0, 1, 0, 1]
largo = 24 #longitud de individuo
num_pob = 20 # numero depoblacion
pressure = 3 # individuos seleccionados para la reproduccion
mutation_chance= 0.2 # probabilidad de mutar


def crear_individuo(min,max):
    return [random.randint(min, max) for i in range(largo)]

def crerar_poblacion():
    return [crear_individuo(0, 1) for i in range(num_pob)]

def calcular_fitness(individuo):
    fitness = 0
    for i in range(len(individuo)):
        if (individuo[i] == modelo[i]):
            fitness += 1
    return fitness

def seleccion_reproduccion(poblacion):
    fit = [abs(calcular_fitness(i)-24) for i in poblacion]
    print("fitnes de la poblacion: ")
    print(fit)
    puntuados = [ (calcular_fitness(i), i) for i in poblacion]
    puntuados = [i[1] for i in sorted(puntuados)]
    poblacion = puntuados
    selected = puntuados[(len(puntuados)-pressure):]
    
    for i in range(len(poblacion)-pressure):
        punto = random.randint(1, largo-1)
        padre = random.sample(selected, 2)
        
        poblacion[i][:punto] = padre[0][:punto]
        poblacion[i][punto:] = padre[1][punto:]
      
    return poblacion

def mutacion(poblacion):
    fit = [abs(calcular_fitness(i)-24) for i in poblacion]
    suma=0
    for i in fit:
        suma+=i
    if suma>0:
        for i in range(pressure):
            if random.random() <= mutation_chance:
                punto = random.randint(0, largo-1)
                new_value = random.randint(0,1)
                while new_value == poblacion [i][punto]:
                    new_value = random.randint(0,1)
                poblacion[i][punto]= new_value
    return poblacion
def imprimir_poblacion(poblacion,ad):
    print("\n\t Poblacion {}: \n".format(ad))
    for ind in poblacion:
        print("{}{}{}{}{}{}".format(ind[0],ind[1],ind[2],ind[3],ind[4],ind[5]))
        print("{}{}{}{}{}{}".format(ind[6],ind[7],ind[8],ind[9],ind[10],ind[11]))
        print("{}{}{}{}{}{}".format(ind[12],ind[13],ind[14],ind[15],ind[16],ind[17]))
        print("{}{}{}{}{}{}".format(ind[18],ind[19],ind[20],ind[21],ind[22],ind[23]))
        print("---------------------")

poblacion = crerar_poblacion()
imprimir_poblacion(poblacion,"inicial")

for i in range(150):
    poblacion = seleccion_reproduccion(poblacion)
    poblacion = mutacion(poblacion)
    #imprimir_poblacion(poblacion,"proceso")
imprimir_poblacion(poblacion,"final")


