from pregunta import Pregunta
class Evaluacion:
    def __init__(self, tipo:str, ruta:str, preguntas:list[Pregunta]) -> None:
        self.tipo = tipo
        self.ruta = ruta
        self.preguntas = preguntas
        self.calificacion = 0

    def get_tipo(self):
        return self.tipo
    def get_ruta(self):
        return self.ruta
    def get_preguntas(self):
        return self.preguntas
    def get_calificacion(self):
        return self.calificacion
    
    def set_calificacio(self, calificacion):
        self.calificacion = calificacion
