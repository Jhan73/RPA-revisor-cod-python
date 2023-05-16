import pyautogui as robot
import os
import time
import json

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
alumnos = []

plagios = []
ruta_base = "./evaluaciones"
    
#------ CARGAR DATOS -------------

def cargar_datos():
    archivos = os.listdir(ruta_base)
    list_alumnos = [nombre for nombre in archivos if os.path.isdir(os.path.join(ruta_base, nombre))]
    #nombre
    for nombre in list_alumnos:
        evaluaciones=[]
        evaluacion=os.listdir(ruta_base+'/'+nombre)
        path_evaluacion = os.path.join(ruta_base, nombre)
        #evaluaciones que rindio
        for examen in evaluacion:
            preguntas=[]
            ejercicios = os.listdir(ruta_base+'/'+nombre)
            nueva_evaluacion = None
            for pregunta in ejercicios:
                #ejercicios por pregunta
                if ".py" in pregunta or ".ipynb" in pregunta:
                    nueva_pregunta = Pregunta(ruta_base+'/'+nombre+'/'+examen,str(pregunta))
                    preguntas.append(nueva_pregunta)
                    #print(json.dumps(nueva_pregunta.__dict__))#######################
                    if "pc1" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('PC1',ruta_base+'/'+nombre+'/'+examen,preguntas)
                    elif "pc2" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('PC2',ruta_base+'/'+nombre+'/'+examen,preguntas)
                    elif "pc3" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('PC3',ruta_base+'/'+nombre+'/'+examen,preguntas)
                    elif "pc4" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('PC4',ruta_base+'/'+nombre+'/'+examen,preguntas)
                    elif "ep" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('EP',ruta_base+'/'+nombre+'/'+examen,preguntas)
                    elif "ef" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('EF',ruta_base+'/'+nombre+'/'+examen,preguntas)
                    elif "es" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('ES',ruta_base+'/'+nombre+'/'+examen,preguntas)
            evaluaciones.append(nueva_evaluacion)
        alumnos.append(Alumno(nombre,ruta_base,evaluaciones))
cargar_datos()
for alumno in alumnos:
    for eva in alumno.get_evaluaciones():
        for pre in eva.get_preguntas():
            print(pre.archivo)
