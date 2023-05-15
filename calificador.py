import pyautogui as robot
import os
import time
import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from difflib import SequenceMatcher

from pregunta import Pregunta
from evaluacion import Evaluacion
from alumno import Alumno


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
    """for nombre in archivos:
        if os.path.isdir(os.path.join(ruta_base, nombre)):
            alumnos.append(nombre)"""

def obtener_datos_evaluacion(ruta_evaluacion:str):#pregustas que realizo
                                #nombre del archivo por pregunta
                                
    pass
obtener_datos_alumnos(ruta_base)
print("Alumnos: ", alumnos)

def calificar_evaluacion(ruta_evaluacion):
    resultado = "python -m pylint " + ruta_evaluacion
    print("Resultado de evaluacion: ", resultado)
    return  os.system(resultado)

def verificar_plagio(evaluacion: Evaluacion, evaluaciones:list[dict:Evaluacion]):
    en = evaluaciones[0]['PC1']
    pass
 

def main():
    print("Main")
    valor = calificar_evaluacion('"./evaluaciones/BALLENA ESPINOZA, MARCELO ALONSO/PC2/Ballena-Marcelo-PC2-P1.py"')
    print("Valor del resultado: ",valor)

if __name__ == '__main__':
    main()