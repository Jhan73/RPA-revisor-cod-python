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

def obtener_datos_alumnos(ruta_base: str):
    global alumnos
    archivos = os.listdir(ruta_base)
    alumnos = [nombre for nombre in archivos if os.path.isdir(os.path.join(ruta_base, nombre))]
    #for nombre in archivos:
       # if os.path.isdir(os.path.join(ruta_base, nombre)):
        #    alumnos.append(nombre)
obtener_datos_alumnos(ruta_base)
print("Alumnos: ", alumnos)

def guardarNombresArchivo(ruta_carpeta):
    for item in os.listdir(ruta_carpeta):
        ruta_completa = os.path.join(ruta_carpeta, item)
        if os.path.isfile(ruta_completa):
            archivos.append(item)
            rutas_archivos.append(ruta_completa)




 

def main():
    pass

if __name__ == '__main__':
    main()