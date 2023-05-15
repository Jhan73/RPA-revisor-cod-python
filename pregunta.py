class Pregunta:
    def __init__(self, ruta_archivo: str, archivo:str) -> None:
        self.ruta_archivo = ruta_archivo
        self.archivo = archivo
        self.calificacion = 0

    def get_calificacion(self):
        return self.calificacion
    def get_ruta_archivo(self):
        return self.ruta_archivo
    def get_archivo(self):
        return self.archivo
    
    def set_calificacion(self, calificacion):
        self.calificacion = calificacion
    