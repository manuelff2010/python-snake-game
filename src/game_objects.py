import pygame
class object():
    def __init__(self,posicion,tamaño,color,pantalla):
        self.posicion = posicion
        self.tamaño = tamaño
        self.color = color
        self.pantalla = pantalla
class cuadrados(object):
    def __init__(self,posicion,tamaño,color,pantalla):
        super().__init__(posicion,tamaño,color,pantalla)
    def renderizado(self):
        self.cubo_rect = pygame.Rect(
            self.posicion[0], self.posicion[1],
            self.tamaño[0], self.tamaño[1]
        )
        pygame.draw.rect(self.pantalla,self.color,self.cubo_rect)
class titulos(object):
    #titulos("prueba",32,(255,0,0),"arial",(10,10),screen)
    def __init__(self,texto,tamaño,color,font,posicion,pantalla):
        super().__init__(posicion,tamaño,color,pantalla)
        self.texto = texto
        self.font = font
    def renderizado(self):
        self.fuente = pygame.font.SysFont(self.font,self.tamaño)
        self.title = self.fuente.render(self.texto,True,self.color)
    def dibujo(self):
        self.pantalla.blit(self.title,self.posicion)
class botones(object):
    def __init__(self,posicion,tamaño,colores_boton,texto_y_color,font,pantalla):
        super().__init__(posicion,tamaño,colores_boton,pantalla)
        self.estado = 0
        self.texto = texto_y_color
        self.font = font
        self.caja_boton = pygame.Rect(self.posicion[0],self.posicion[1],self.tamaño[0],self.tamaño[1])
    def eventos(self,evento):
        if self.caja_boton.collidepoint(pygame.mouse.get_pos()):
            self.estado=1
            if evento.type == pygame.MOUSEBUTTONDOWN:
                self.estado=2
        else:
            self.estado=0
    def draw_button(self):
        self.fuente = pygame.font.SysFont(self.font[0],self.font[1])
        pygame.draw.rect(self.pantalla,self.color[self.estado],self.caja_boton)
        button_title = self.fuente.render(self.texto[0], True, self.texto[1][self.estado])
        box_title = button_title.get_rect(center = self.caja_boton.center)
        self.pantalla.blit(button_title,box_title)