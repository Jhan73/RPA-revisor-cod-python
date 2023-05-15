from evaluacion import Evaluacion

class Alumno :
    def __init__(self, nombre: str, ruta:str, evaluaciones:list[Evaluacion]) -> None:
        self.nombre = nombre
        self.ruta = ruta
        self.evaluaciones = evaluaciones
        self.promedio_practicas = 0
        self.promedio_final = 0

    def get_nombre(self):
        return self.nombre
    def get_ruta(self):
        return self.ruta
    def get_evaluaciones(self):
        return self.evaluaciones
    def get_promedio_practicas(self):
        return self.promedio_practicas
    def get_promedio_final(self):
        return self.promedio_final
    
    def set_promedio_practicas(self, promedio_practicas):
        self.promedio_practicas = promedio_practicas
    def set_promedio_final(self, promedio_final):
        self.promedio_final = promedio_final
    