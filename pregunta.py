class Pregunta:
    def __init__(self, ruta_archivo: str, archivo:str) -> None:
        self.ruta_archivo = ruta_archivo
        self.archivo = archivo
        self.calificacion = 0
        self.similitud = 0
        self.es_plagio = False
        self.pregunta = ""

    def get_calificacion(self):
        return self.calificacion
    def get_ruta_archivo(self):
        return self.ruta_archivo
    def get_archivo(self):
        return self.archivo
    def get_similtud(self):
        return self.similitud
    def get_es_plagio(self):
        return self.es_plagio
    
    def set_calificacion(self, calificacion):
        self.calificacion = calificacion
    