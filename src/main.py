import pygame
from logic import game_logic
import time
import game_objects as objects
import graphics
class game:
    def __init__(self):
        #variables
        self.window_alto = 500
        self.window_ancho = 500
        self.separador = 30
        self.run = True
        #inicializacion modulos
        pygame.init()
        self.pantalla = pygame.display.set_mode((self.window_ancho,self.window_alto))
        self.logica = game_logic()
        self.graficos = graphics.graficos((self.window_ancho,self.window_alto),self.separador,self.pantalla,self.logica.limits)
        #llamadas a funciones
        self.graficos_menu = graphics.graficos_menus(self.pantalla)
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
    def game_loop(self):
        while self.run:
            time.sleep(0.1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                for i in self.graficos_menu.menu_botones:
                    i.eventos(event)
                    if i.estado == 2:
                        if i.texto[0] == "jugar":
                            self.logica.new_game()
                            self.logica.opcion = 1
                        elif i.texto[0] == "salir":
                            self.run = False
            self.pantalla.fill(graphics.configuracion.color_fondo)
            if self.logica.update() == 1:
                self.logica.opcion = 0
            self.keys_control()
            self.builder()
            pygame.display.update()
    def builder(self):
        if self.logica.opcion == 1:
            self.graficos.contorno.renderizado()
            self.graficos.render_serpiente(self.logica.cola)
            self.graficos.render_manzana(self.logica.manzana)
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
                i.draw_button()
        elif self.logica.opcion == 2:
            self.graficos_menu.perdida_menu()
            self.graficos_menu.fondo.renderizado()
            self.graficos_menu.menu_titulo.renderizado()
            self.graficos_menu.menu_titulo.dibujo()
game()