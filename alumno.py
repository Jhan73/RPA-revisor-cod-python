class Alumno :
    def __init__(self, nombre: str, pc1: dict, pc2:dict, pc3:dict, pc4:dict, ep:dict, ef:dict, es:dict) -> None:
        self.nombre = nombre
        self.pc1 = pc1
        self.pc2 = pc2
        self.pc3 = pc3
        self.pc4 = pc4
        self.ep = ep
        self.ef = ef
        self.es = es
    def get_nombre(self):
        return self.nombre
    