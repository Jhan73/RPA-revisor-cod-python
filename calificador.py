import pyautogui as rpa
import os
import time
import numpy as np
import pandas as pd

#global archivos
#global rutas


archivos = []
rutas_archivos = []
alumnos = []
ruta_base = "./evaluaciones"

def obtener_datos_alumnos(ruta_base: str): #obtener todos los datos del alumno
                                            #nombre de los alumno
                                            #evaluaciones que rindio (PC1, PC2 ....)
    global alumnos
    archivos = os.listdir(ruta_base)
    alumnos = [nombre for nombre in archivos if os.path.isdir(os.path.join(ruta_base, nombre))]
    #for nombre in archivos:
       # if os.path.isdir(os.path.join(ruta_base, nombre)):
        #    alumnos.append(nombre)

def obtener_datos_evaluacion():#pregustas que realizo
                                #nombre del archivo por pregunta
                                
    pass
obtener_datos_alumnos(ruta_base)
print("Alumnos: ", alumnos)


 

def main():
    pass

if __name__ == '__main__':
    main()