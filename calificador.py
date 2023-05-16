import pyautogui as robot
import os
import time
import json

import numpy as np
import pandas as pd

import subprocess
import re

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
ruta_base = ".\evaluaciones"

#------ CARGAR DATOS -------------
def cargar_datos():
    global alumnos
    archivos = os.listdir(ruta_base)
    list_alumnos = [nombre for nombre in archivos if os.path.isdir(os.path.join(ruta_base, nombre))]
    #nombre
    for alumno in list_alumnos:
        evaluaciones=[]
        list_evaluaciones=os.listdir(ruta_base+'/'+alumno)
        #evaluaciones que rindio
        if len(list_evaluaciones) > 0:
            for evaluacion in list_evaluaciones:
                list_ejercicios = os.listdir(ruta_base+'/'+alumno+'/'+evaluacion)
                nueva_evaluacion = None
                if len(list_ejercicios) > 0:
                    preguntas=[]
                    for pregunta in list_ejercicios:
                        #ejercicios por pregunta
                        if ".py" in pregunta or ".ipynb" in pregunta:
                            num_pregunta = ""
                            if ".py" in pregunta:
                                num_pregunta = f"p{list(pregunta)[-4]}"
                            else:
                                num_pregunta = f"p{list(pregunta)[-7]}"
                            nueva_pregunta = Pregunta(os.path.join(ruta_base, alumno, evaluacion), pregunta, num_pregunta)
                            preguntas.append(nueva_pregunta)
                            #print(json.dumps(nueva_pregunta.__dict__))#######################
                    nueva_evaluacion = Evaluacion(evaluacion,ruta_base+'/'+alumno,preguntas)
                    evaluaciones.append(nueva_evaluacion)
            alumnos.append(Alumno(alumno,ruta_base,evaluaciones))
#------- METODOS GENERALES --------
def obtener_archivo_pregunta(alumno: Alumno, evaluacion:str, pregunta:str):
    evaluaciones = alumno.get_evaluaciones()
    existe_pregunta = False
    nombre_archivo = ''
    for eva in evaluaciones:
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
def obtener_calificacion(ruta: str, archivo: str):

    """ruta = "./evaluaciones/Camac-Alexis-pc2-p1.py"
    comado = "python -m pylint " + ruta
    resultado = os.system(comado)"""
    
    #print("Resultado",resultado)
    ruta_archivo = os.path.join(ruta, archivo)
    print(ruta_archivo)
    resultado = subprocess.run(['pylint', ruta_archivo], capture_output=True, text=True)
    calificacion_linea = None
    calificacion = 0
    for linea in resultado.stdout.splitlines():
        if "Your code has been rated at" in linea:
            calificacion_linea = linea
            break

    if calificacion_linea:
        calificacion_match = re.search(r"(\d+(\.\d+)?)\/10", calificacion_linea)
        if calificacion_match:
            calificacion_str = calificacion_match.group(1)
            calificacion = float(calificacion_str)
            #print(f"Calificación de Pylint: {calificacion}")
        else:
            print("No se encontró una calificación válida en la salida de Pylint.")
    else:
        print("No se encontró una línea de calificación en la salida de Pylint.")

    return calificacion
def calificar_evaluacion():
    for alumno in alumnos:
        for eva in alumno.get_evaluaciones():
            calificacion_eva = 0
            for ejer in eva.get_preguntas():
                time.sleep(0.1)
                calificacion = obtener_calificacion(ejer.get_ruta_archivo(), ejer.get_archivo())
                ejer.set_calificacion(calificacion*10)
                calificacion_eva += calificacion
            calificacion_eva = calificacion_eva/len(eva.get_preguntas())
            eva.set_calificacion(calificacion_eva)

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
                plagio = Plagio()
                for alumno_b in alumnos_copia:
                    existe_b, archivo_alumno_b = obtener_archivo_pregunta(alumno_b, eval, f"P{(i+1)}")
                    if existe_b:
                        similitud = obtener_similitud(archivo_alumno_a, archivo_alumno_b)
                        if similitud > 0.7:
                            plagio.alumnos.append(alumno_b.get_nombre())
                            alumnos_copia.remove(alumno_b)
                if similitud > 0.7:
                    plagio.evaluacion = eval
                    plagio.pregunta = f"P{i}"
                    plagios.append(plagio)  
            if similitud > 0.7:
                plagio = Plagio()
                plagio.alumnos.append(alumno_a.get_nombre())
                plagio.evaluacion = eval
                plagio.pregunta = f"P{i}"
                plagios.append(plagio)

#----------- REPORTE ---------------------
def obtener_reporte():
    global alumnos
    reporte_alumnos = []
    for alumno in alumnos:
        reporte_nota_alumno = {
            "alumno":"",
            "PC1":{"p1":0,"p2":0,"p3":0,},
            "PC1":{"p1":0,"p2":0,"p3":0,},
            "PC2":{"p1":0,"p2":0,"p3":0,},
            "PC3":{"p1":0,"p2":0,"p3":0,},
            "PC4":{"p1":0,"p2":0,"p3":0,},
            "EP":{"p1":0,"p2":0,"p3":0,},
            "EF":{"p1":0,"p2":0,"p3":0,},
            "ES":{"p1":0,"p2":0,"p3":0,},
        }
        reporte_nota_alumno["alumno"] = alumno.get_nombre()
        for eva in alumno.get_evaluaciones():
            for ejer in eva.get_preguntas():
                reporte_nota_alumno[eva.get_tipo()][ejer.get_pregunta()] = ejer.get_calificacion()
        reporte_alumnos.append(reporte_nota_alumno)
    df = pd.json_normalize(reporte_alumnos)
    print(df)










def main():
    cargar_datos()
    """for alumno in alumnos:
        print(alumno.get_nombre())
        #print(json.dumps(alumno.__dict__))
        print(len(alumno.get_evaluaciones()))
        for eva in alumno.get_evaluaciones():
            print(eva.get_tipo())
            time.sleep(0.1)
            for ejer in eva.get_preguntas():
                print(ejer.get_archivo())"""
    calificar_evaluacion()
    obtener_reporte()
    procesar_plagio('PC1')


if __name__ == '__main__':
    main()
    