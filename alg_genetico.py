# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:41:03 2021

@author: VladimirP11
"""

import random 

modelo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
largo = 10 #longitud de individuo
num_pob = 10 # numero depoblacion
pressure = 3 # individuos seleccionados para la reproduccion
mutation_chance= 0.2 # probabilidad de mutar

print('\n\tModelo: %s\n'%(modelo))

def crear_individuo(min,max):
    return [random.randint(min, max) for i in range(largo)]

def crerar_poblacion():
    return [crear_individuo(1, 9) for i in range(num_pob)]

def calcular_fitness(individuo):
    fitness = 0
    for i in range(len(individuo)):
        if individuo[i] == modelo[i]:
            fitness += 1
    return fitness

def seleccion_reproduccion(poblacion):
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
    for i in range(len(poblacion)-pressure):
        if random.random() <= mutation_chance:
            punto = random.randint(0, largo-1)
            new_value = random.randint(1, 9)
            while new_value == poblacion [i][punto]:
                new_value = random.randint(1, 9)
            poblacion[i][punto]= new_value
    
    return poblacion

poblacion = crerar_poblacion()
print("\n\t Poblacion inicial: \n%s"%(poblacion))

for i in range(500):
    poblacion = seleccion_reproduccion(poblacion)
    poblacion = mutacion(poblacion)
    print("\n\t Poblacion {i}: \n%s"%(poblacion))

print("\n\t Poblacion final: \n%s"%(poblacion))