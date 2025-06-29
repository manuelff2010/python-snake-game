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
        self.fuente = pygame.font.SysFont(font,self.tamaño)
        self.title = self.fuente.render(self.texto,True,self.color)
    def dibujo(self):
        self.pantalla.blit(self.title,self.posicion)
class botones(object):
    #botones((100,100),(100,50),((200,200,200),(255,0,0)),("hola",(0,255,0)),"arial",16,)
    def __init__(self,posicion,tamaño,colores_boton,texto_y_color,font,tamaño_fuente):
        super().__init__(posicion,tamaño,colores_boton,pantalla)
        self.texto = texto_y_color
        self.tamaño_fuente = tamaño_fuente
        self.fuente = pygame.font.SysFont(font,self.tamaño_fuente)
        self.caja_boton = pygame.Rect(
            self.posicion[0],self.posicion[1],
            self.tamaño[0],self.tamaño[1]
        )
    def eventos(self,evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.caja_boton.collidepoint(evento.pos):
                print("pepito")
    def draw_button(self):
        if self.caja_boton.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.pantalla,self.color[1],self.caja_boton)
        else:
            pygame.draw.rect(self.pantalla,self.color[0],self.caja_boton)
        button_title = self.fuente.render(self.texto[0], True, self.texto[1])
        box_title = button_title.get_rect(center = self.caja_boton.center)
        pantalla.blit(button_title,box_title)