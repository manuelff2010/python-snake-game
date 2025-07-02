import pygame
from logic import game_logic
import time
import game_objects as objects
import graphics
class game:
    def __init__(self):
        #inicializacion modulos
        pygame.init()
        self.logica = game_logic()
        #variables
        self.window_alto = 500
        self.window_ancho = 500
        self.separador = 30
        self.run = True
        self.tamaño_serpiente_inicio = self.logica.tamaño_serpiente
        self.pantalla = pygame.display.set_mode((self.window_ancho,self.window_alto))
        #llamadas a funciones
        self.graficos = graphics.graficos((self.window_ancho,self.window_alto),self.separador,self.pantalla,self.logica.limits)
        self.graficos_menu = graphics.graficos_menus(self.pantalla)
        self.graficos_menu.perdida_menu()
        self.graficos.matriz_builder()
        self.game_loop()
    def keys_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.logica.actualizar_direccion((-1, 0))
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.logica.actualizar_direccion((1, 0))
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.logica.actualizar_direccion((0, -1))
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.logica.actualizar_direccion((0, 1))
    def estados(self,i):
        if i.estado == 2:
            print(i.texto[0])
            if i.texto[0] == "jugar" or i.texto[0] == "volver a jugar":
                self.logica.new_game()
                self.logica.opcion = 1
            elif i.texto[0] == "salir":
                self.run = False
            elif i.texto[0] == "opciones":
                pass
            elif i.texto[0] == "ir al menu principal":
                self.logica.opcion = 0
    def game_loop(self):
        while self.run:
            time.sleep(0.1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if self.logica.opcion == 0:
                    for i in self.graficos_menu.menu_botones:
                        i.eventos(event)
                        self.estados(i)
                elif self.logica.opcion == 2:
                    for e in self.graficos_menu.menu_botones_perdida:
                        e.eventos(event)
                        self.estados(e)
            if self.logica.update() == 1:
                self.logica.opcion = 2
            self.keys_control()
            self.pantalla.fill(graphics.configuracion.color_fondo)
            self.builder()
            pygame.display.update()
    def builder(self):
        if self.logica.opcion == 1:
            self.graficos.contorno.renderizado()
            self.graficos.render_serpiente(self.logica.cola)
            self.graficos.render_manzana(self.logica.manzana, self.logica.tamaño_serpiente - self.tamaño_serpiente_inicio)
            self.graficos.puntaje.renderizado()
            self.graficos.puntaje.dibujo()
            for i in self.graficos.cuadricula:
                i.renderizado()
            for i in self.graficos.serpiente_render:
                i.renderizado()
            self.graficos.manzana_render.renderizado()
        elif self.logica.opcion == 0:
            self.graficos_menu.title(True)
            self.graficos_menu.menu_titulo.renderizado()
            self.graficos_menu.menu_titulo.dibujo()
            for i in self.graficos_menu.menu_botones:
                i.draw_button(100,10)
        elif self.logica.opcion == 2:
            self.graficos_menu.fondo.renderizado()
            self.graficos_menu.menu_titulo_perdida.renderizado()
            self.graficos_menu.menu_titulo_perdida.dibujo()
            for i in self.graficos_menu.menu_botones_perdida:
                i.draw_button(100,10)
game()