class Evaluacion:
    def __init__(self, tipo:str, preguntas:list) -> None:
        self.tipo = tipo
        self.preguntas = preguntas
        self.calificacion = 0
    def get_tipo(self):
        return self.tipo
    def get_calificacion(self):
        return self.calificacion
    