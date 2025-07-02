import random
class game_logic():
    def __init__(self):
        self.opcion = 0
        self.tamaño_serpiente = 4
        self.limits = 16
        self.direccion = (0,0)
        self.cola = [(0,0)]
        self.manzana = None
    def verificacion_cordenadas(self, a):
        if not a <= self.limits:
            return True
        elif not a >= 0:
            return False
        else:
            return None
    def actualizar_direccion(self,nueva_direccion):
        if not((self.direccion[0] != 0 and nueva_direccion[0] != 0) or (self.direccion[1] != 0 and nueva_direccion[1] != 0)):
            self.direccion = nueva_direccion
    def movimiento(self):
        if self.direccion != (0,0):
            self.nueva_cordenada = (self.cola[0][0] + self.direccion[0],self.cola[0][1] + self.direccion[1])
            verificacion_cordenada = (self.verificacion_cordenadas(self.nueva_cordenada[0]),self.verificacion_cordenadas(self.nueva_cordenada[1]))
            if not(verificacion_cordenada[0] == None and verificacion_cordenada[1] == None):
                if verificacion_cordenada[0] == None:
                    if verificacion_cordenada[1]:
                        self.nueva_cordenada = (self.nueva_cordenada[0],0)
                    else:
                        self.nueva_cordenada = (self.nueva_cordenada[0],self.limits)
                else:
                    if verificacion_cordenada[0]:
                        self.nueva_cordenada = (0,self.nueva_cordenada[1]) 
                    else:
                        self.nueva_cordenada = (self.limits,self.nueva_cordenada[1])
            self.cola.insert(0,self.nueva_cordenada)
        if len(self.cola) > self.tamaño_serpiente:
            self.cola.pop(-1)
    def validaciones(self):
        if self.manzana in self.cola:
            self.manzana = None
            self.tamaño_serpiente += 1
        if self.cola.count(self.cola[0]) > 1:
            return 1
    def generacion_manzana(self):
        if self.manzana == None:
            while True:
                nueva_manzana = (random.randrange(self.limits + 1), random.randrange(self.limits + 1))
                if self.cola.count(nueva_manzana) < 1:
                    break
            self.manzana = nueva_manzana
    def update(self):
        if self.opcion == 1:
            self.movimiento()
            if self.validaciones() == 1:
                return 1
            self.generacion_manzana()
            return 0
    def new_game(self):
        self.tamaño_serpiente = 4
        self.direccion = (0,0)
        self.cola = [(0,0)]
        self.manzana = None