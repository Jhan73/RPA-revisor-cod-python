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
from plagio import Plagio


archivos = []
rutas_archivos = []
alumnos = []
plagios = []
ruta_base = "./evaluaciones"


"""def obtener_datos_alumnos(ruta_base: str): #obtener todos los datos del alumno
                                            #nombre de los alumno
                                            #evaluaciones que rindio (PC1, PC2 ....)
    global alumnos
    archivos = os.listdir(ruta_base)
    alumnos = [nombre for nombre in archivos if os.path.isdir(os.path.join(ruta_base, nombre))]
    for nombre in archivos:
        if os.path.isdir(os.path.join(ruta_base, nombre)):
            alumnos.append(nombre)

def obtener_datos_evaluacion(ruta_evaluacion:str):#pregustas que realizo
                                #nombre del archivo por pregunta
                                
    pass


def cargar_evaluaciones(preguntas:list[Pregunta]):
    pass



obtener_datos_alumnos(ruta_base)
print("Alumnos: ", alumnos)"""
#------ CARGAR DATOS -------------
def cargar_datos():
    archivos = os.listdir(ruta_base)
    list_alumnos = [nombre for nombre in archivos if os.path.isdir(os.path.join(ruta_base, nombre))]
    #nombre
    for alumno in list_alumnos:
        evaluaciones=[]
        evaluacion=os.listdir(ruta_base+'/'+alumno)
        #evaluaciones que rindio
        for examen in evaluacion:
            preguntas=[]
            ejercicios = os.path.join(ruta_base,alumno,examen)
            nueva_evaluacion = None
            for pregunta in ejercicios:
                #ejercicios por pregunta
                if ".py" in pregunta or ".ipynb" in pregunta:
                    nueva_pregunta = Pregunta(ruta_base+'/'+alumno+'/'+examen,str(pregunta))
                    preguntas.append(nueva_pregunta)
                    #print(json.dumps(nueva_pregunta.__dict__))#######################
                    if "pc1" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('PC1',ruta_base+'/'+alumno+'/'+examen,preguntas)
                    elif "pc2" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('PC2',ruta_base+'/'+alumno+'/'+examen,preguntas)
                    elif "pc3" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('PC3',ruta_base+'/'+alumno+'/'+examen,preguntas)
                    elif "pc4" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('PC4',ruta_base+'/'+alumno+'/'+examen,preguntas)
                    elif "ep" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('EP',ruta_base+'/'+alumno+'/'+examen,preguntas)
                    elif "ef" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('EF',ruta_base+'/'+alumno+'/'+examen,preguntas)
                    elif "es" in pregunta.lower():
                        nueva_evaluacion = Evaluacion('ES',ruta_base+'/'+alumno+'/'+examen,preguntas)
            evaluaciones.append(nueva_evaluacion)
        alumnos.append(Alumno(alumno,ruta_base,evaluaciones))
cargar_datos()


#------- METODOS GENERALES --------
def obtener_archivo_pregunta(alumno: Alumno, evaluacion:str, pregunta:str):
    evaluaciones = alumno.get_evaluaciones()
    existe_pregunta = False
    nombre_archivo = ''
    for eva in evaluaciones:
        print("tipo eva : ",eva.get_tipo())
        if eva.get_tipo() == evaluacion:
            path_pregunta = os.path.join(ruta_base,alumno.get_nombre(), evaluacion)
            archivos = os.listdir(path_pregunta)
            for pregun in eva.get_preguntas():
                
                if (pregunta + ".py").lower() in pregun.get_archivo().lower() or (pregunta + ".ipynb").lower() in pregun.get_archivo().lower():
                    for archivo in archivos:
                        ruta_archivo = os.path.join(path_pregunta, archivo)
                        if os.path.isfile(ruta_archivo):
                            if evaluacion.lower() in ruta_archivo:
                                nombre_archivo = os.path.basename(ruta_archivo)
                    existe_pregunta = True
    if existe_pregunta:
        path_pregunta = os.path.join(ruta_base, alumno.get_nombre, evaluacion, )
        return True, nombre_archivo
    else:
        return False, ""



# -------- CALIFICAR ------------- 
"""def calificar():
    for alumno in alumnos:
        if len(alumno.get_evaluaciones()) > 0:
            for evaluacion in alumno.get_evaluaciones():
                for pregunta in evaluacion.get_preguntas():
                    ruta = os.path.join(pregunta.get_ruta(), pregunta.get_archivo())
                    resultado = "python -m pylint " + ruta
                    pregunta.set_calificacion(os.system(resultado))


calificar()"""
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
    alumnos_copia = alumnos.copy()

    for i in range(3):
        for alumno_a  in alumnos_copia:
            similitud = 0
            existe_a, archivo_alumno_a = obtener_archivo_pregunta(alumno_a, eval, f"P{(i+1)}")
            if existe_a:
                alumnos_copia.remove(alumno_a)
                for alumno_b in alumnos_copia:
                    existe_b, archivo_alumno_b = obtener_archivo_pregunta(alumno_b, eval, f"P{(i+1)}")
                    if existe_b:
                        similitud = obtener_similitud(archivo_alumno_a, archivo_alumno_b)
                        if similitud > 0.7:
                            plagio = Plagio()
                            plagio.alumnos.append(alumno_b.get_nombre)
                            plagio.evaluacion = eval
                            plagio.pregunta = f"P{i}"
                            plagios.append(plagio)
                            alumnos_copia.remove(alumno_b)
            if similitud > 0.7:
                plagio = Plagio()
                plagio.alumnos.append(alumno_a.get_nombre)
                plagio.evaluacion = eval
                plagio.pregunta = f"P{i}"
                plagios.append(plagio)

procesar_plagio('PC1')
        








#-----------

def main():
    print("Main")

if __name__ == '__main__':
    main()
    