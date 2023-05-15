import pyautogui as robot
import os
import time

import numpy as np
import pandas as pd

from pylint.lint import Run

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
alumnos = [Alumno]
plagios = []
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


def cargar_evaluaciones(preguntas:list[Pregunta]):
    pass



obtener_datos_alumnos(ruta_base)
print("Alumnos: ", alumnos)

# -------- CALIFICAR -------------


#-------- REVISAR PLAGIO ---------

def procesar(text):# Preprocesamiento del texto
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = [ps.stem(w.lower()) for w in tokens if not w in stop_words]
    return tokens

def comparar_codigo(code1, code2):# Comparación de códigos
    tokens1 = procesar(code1)
    tokens2 = procesar(code2)
    seq_matcher = SequenceMatcher(None, tokens1, tokens2)
    return seq_matcher.ratio()

def obtener_similitud(archivo1: str, archivo2: str):# Resultado de similitud
    #with open('./evaluaciones/Camac-Alexis-pc2-p1.py', 'r') as f1, open('./evaluaciones/Chanca-Jair-pc2-p1.py', 'r') as f2:
    with open(archivo1, 'r') as f1, open(archivo2, 'r') as f2:
        code1 = f1.read()
        code2 = f2.read()
    similitud = comparar_codigo(code1, code2)
    return similitud

def procesar_plagio(eval: str):
    global alumnos
    global plagios
    plagio_alumnos = []
    alumnos_copia = alumnos.copy()

    for alumno in alumnos_copia:
        evaluaciones_alumno = alumno.get_evaluaciones()
        for evaluacion in evaluaciones_alumno:
            if evaluacion == eval:

                pass

        archivo_pregunta
        for i in len(alumnos_copia):








#-----------
def calificar_evaluacion(preguntas: list[Pregunta]):
    
    for pregunta in preguntas:
        pass
    resultado = "python -m pylint " + 'ruta_evaluacion'
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