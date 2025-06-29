import pygame
from logic import game_logic
import time
import game_objects as objects
from graphics import graficos
class game:
    def __init__(self):
        #variables
        self.window_alto = 500
        self.window_ancho = 500
        self.separador = 30
        self.run = True
        self.celdas_color = ((100,200,100),(50,100,50))
        self.background_color = (50,100,50)
        #inicializacion modulos
        pygame.init()
        self.pantalla = pygame.display.set_mode((self.window_ancho,self.window_alto))
        self.logica = game_logic()
        self.graficos = graficos((self.window_ancho,self.window_alto),self.separador,self.pantalla,self.logica.limits)
        #llamadas a funciones
        self.graficos.matriz_builder(self.celdas_color)
        self.game_loop()
    def keys_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.logica.direccion = (-1, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.logica.direccion = (1, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.logica.direccion = (0, -1)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.logica.direccion = (0, 1)
    def game_loop(self):
        while self.run:
            time.sleep(0.1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.keys_control()
            self.logica.update()
            self.pantalla.fill(self.background_color)
            self.builder()
            pygame.display.update()
    def builder(self):
        self.graficos.contorno.renderizado()
        self.graficos.render_serpiente((255,0,0),self.logica.cola)
        for i in self.graficos.cuadricula:
            i.renderizado()
        for i in self.graficos.serpiente_render:
            i.renderizado()
game()