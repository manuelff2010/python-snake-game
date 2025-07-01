import config 
import pygame
import game_objects as objects
class graficos():
    def __init__(self,tamaño_ventana,separador,pantalla,limites):
        self.tamaño_ventana= tamaño_ventana
        self.separador= separador
        self.pantalla= pantalla
        self.limits = limites
        self.configuracion = config.player_config()
    def matriz_builder(self):
        self.contorno = objects.cuadrados(
            (self.separador-1,self.separador-1),
            (self.tamaño_ventana[0]-(self.separador+1)*2,self.tamaño_ventana[1]-(self.separador+1)*2),
            self.configuracion.color_contorno,
            self.pantalla
            )
        self.cuadricula = []
        self.tamaño_celda = (
            int((self.tamaño_ventana[0]-(self.separador*2))/(self.limits+1)),
            int((self.tamaño_ventana[1]-(self.separador*2))/(self.limits+1))
            ) 
        self.y_posicion = self.separador
        self.x_posicion = self.separador
        color = 1
        for rango_y in range(self.limits+1):
            self.y_posicion += rango_y*self.tamaño_celda[1]
            for rango_x in range(self.limits+1):
                if color == 1:
                    color = 0
                else:
                    color = 1
                self.x_posicion += rango_x*self.tamaño_celda[0]
                self.cuadricula.append(objects.cuadrados(
                    (self.x_posicion,self.y_posicion),
                    self.tamaño_celda,
                    self.configuracion.color_tablero[color],
                    self.pantalla
                    ))
                self.x_posicion = self.separador
            self.y_posicion = self.separador
    def render_serpiente(self,cola):
        self.serpiente_render = []
        for i in cola:
            self.x_posicion += self.tamaño_celda[0] * i[0]
            self.y_posicion += self.tamaño_celda[1] * i[1]
            self.serpiente_render.append(objects.cuadrados(
                (self.x_posicion,self.y_posicion),
                self.tamaño_celda,
                self.configuracion.color_serpiente,
                self.pantalla
            ))
            self.x_posicion = self.separador
            self.y_posicion = self.separador
    def render_manzana(self,cordenada):
        self.x_posicion += self.tamaño_celda[0]*cordenada[0]
        self.y_posicion += self.tamaño_celda[1]*cordenada[1]
        self.manzana_render= objects.cuadrados(
            (self.x_posicion,self.y_posicion),
            self.tamaño_celda,
            self.configuracion.color_manzana,
            self.pantalla
        )
        self.x_posicion = self.separador
        self.y_posicion = self.separador
            