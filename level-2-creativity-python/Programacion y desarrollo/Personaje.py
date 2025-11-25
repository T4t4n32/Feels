import pygame
import Constantes

class Personaje():
    def __init__(self,animacion,ancho,alto,x,y,flip_inicial=False):
        self.flip = flip_inicial
        self.animacion = animacion
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.imagen = self.animacion[self.frame_index]
        self.forma = pygame.Rect(0,0, ancho, alto)
        self.forma.center = (x,y)

    def actualizar_animacion(self,animacion_coldown):
        ANIMACION_COOLDOWN = animacion_coldown
        #actualizar animacion
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.update_time > ANIMACION_COOLDOWN:
            self.update_time = tiempo_actual
            self.frame_index += 1
            if self.frame_index >= len(self.animacion):
                self.frame_index = 0
        self.imagen = self.animacion[self.frame_index]
    
    def movimiento(self, delta_X, delta_y):
        if delta_X > 0:
            self.flip = False
        elif delta_X < 0:
            self.flip = True

        

    def dibujar(self, ventana,color):
        imagen_flip = pygame.transform.flip(self.imagen, self.flip, flip_y=False)
        ventana.blit(imagen_flip, self.forma)
        #pygame.draw.rect(ventana,color,self.forma, width=1)

    def  dibujar_con_camara(self, ventana,color,cam_x,cam_y):
        imagen_flip = pygame.transform.flip(self.imagen, self.flip, flip_y=False)
        ventana_x = self.forma.x - cam_x
        ventana_y = self.forma.y - cam_y
        ventana.blit(imagen_flip, (ventana_x, ventana_y))
        #pygame.draw.rect(ventana,color, (ventana_x, ventana_y, self.forma.width, self.forma.height), width=1)
    