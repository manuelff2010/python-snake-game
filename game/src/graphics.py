import json
import logic 
import pygame
import game_objects as objects
configuracion = logic.player_config()
try:
    configuracion.color_contorno
except:
    configuracion = logic.player_config()
class graficos():
    def __init__(self,tamaño_ventana,separador,pantalla,limites):
        self.tamaño_ventana= tamaño_ventana
        self.separador= separador
        self.pantalla= pantalla
        self.limits = limites
    def matriz_builder(self):
        self.contorno = objects.cuadrados(
            (self.separador-1,self.separador-1),
            (self.tamaño_ventana[0]-(self.separador)*2,self.tamaño_ventana[1]-(self.separador)*2),
            configuracion.color_contorno,
            self.pantalla
            )
        self.cuadricula = []
        self.tamaño_celda = (
            int((self.tamaño_ventana[0]-(self.separador*2))/(self.limits+1)),
            int((self.tamaño_ventana[1]-(self.separador*2))/(self.limits+1))
            )
        self.inicio = (self.tamaño_ventana[0]- self.tamaño_celda[0] * (self.limits+1))/2
        self.y_posicion = self.inicio
        self.x_posicion = self.inicio
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
                    configuracion.color_tablero[color],
                    self.pantalla
                    ))
                self.x_posicion = self.inicio
            self.y_posicion = self.inicio
    def render_serpiente(self,cola):
        self.serpiente_render = []
        for i in cola:
            self.x_posicion += self.tamaño_celda[0] * i[0]
            self.y_posicion += self.tamaño_celda[1] * i[1]
            self.serpiente_render.append(objects.cuadrados(
                (self.x_posicion,self.y_posicion),
                self.tamaño_celda,
                configuracion.color_serpiente,
                self.pantalla
            ))
            self.x_posicion = self.inicio
            self.y_posicion = self.inicio
    def render_manzana(self,cordenada,numero):
        self.x_posicion += self.tamaño_celda[0]*cordenada[0]
        self.y_posicion += self.tamaño_celda[1]*cordenada[1]
        self.manzana_render= objects.cuadrados(
            (self.x_posicion,self.y_posicion),
            self.tamaño_celda,
            configuracion.color_manzana,
            self.pantalla
        )
        self.x_posicion = self.inicio
        self.y_posicion = self.inicio
        self.puntaje = objects.titulos(f"puntos: {numero}",15,(255,255,255),"arial",(10,10),self.pantalla)

class graficos_menus():
    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.color = 0
        botones = ["jugar","opciones","salir"]
        self.menu_botones = []
        boton_initial_position = 125
        for i in range(len(botones)):
            self.menu_botones.append(objects.botones(
                (125,boton_initial_position+i*75),
                (250,50),
                ((0,0,255),(0,255,0),(255,0,0)),
                (botones[i],(255,255,255)),
                ("arial",12),
                self.pantalla
            ))
    def title(self,rainbow):
        if rainbow:
            if self.color > len(configuracion.color_lista_titulo)-2:
                self.color = 0
            else:
                self.color += 1
            color = configuracion.color_lista_titulo[self.color]
        else:
            color = (255,255,255)
        self.menu_titulo = objects.titulos(
            "Snake game with python",
            40,color,
            "arial",
            (35,50),
            self.pantalla
        )
    def perdida_menu(self):
        botones = ["volver a jugar","ir al menu principal"]
        self.menu_botones_perdida = []
        boton_initial_position = 250
        for i in range(len(botones)):
            self.menu_botones_perdida.append(objects.botones(
                (125,boton_initial_position+i*75),
                (250,50),
                ((0,0,255),(0,255,0),(255,0,0)),
                (botones[i],(255,255,255)),
                ("arial",12),
                self.pantalla
            ))
        self.menu_titulo_perdida = objects.titulos(
            "Has perdido",
            35,
            (255,255,0),
            "arial",
            (150,150),
            self.pantalla
        )
        self.fondo = objects.cuadrados((100,100),(300,300),(50,200,50),self.pantalla)

basic_data = {
    "puestos": {

    },
    "colores": {
        "tablero": ((100,200,100),(50,100,50)),
        "serpiente": (255,0,0),
        "manzana": (0,0,255),
        "fondo": (50,100,50),
        "contorno": (0,0,0),
        "titulo_lista": [(255,0,0),(255,165,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130),(76,40,130)]
    },
    "juego": {
    }
}
class player_config():
    def __init__(self):
        self.configuracion = "serpiente/src/datos.json"
        try:
            with open(self.configuracion,"r") as data:
                self.datos = json.load(data)
                print(self.datos)
                self.creacion_variables()
        except:
            self.escritura(basic_data)
            player_config()
    def escritura(self,datos):
        with open(self.configuracion,"w") as data:
            json.dump(datos,data,indent=4)
    def creacion_variables(self):
        self.color_serpiente = self.datos["colores"]["serpiente"]
        self.color_manzana = self.datos["colores"]["manzana"]
        self.color_tablero = self.datos["colores"]["tablero"]
        self.color_fondo = self.datos["colores"]["fondo"]
        self.color_contorno = self.datos["colores"]["contorno"]
        self.color_lista_titulo = self.datos["colores"]["titulo_lista"]