import Constantes
import pygame
class boton:
    def __init__(self, ventana, imagen_ruta, pos=None):
        self.ventana = ventana
        self.ventana_rect = ventana.get_rect()
        escala = Constantes.ESCALA_B

        # Cargar imagen original
        self.imagen_original = pygame.image.load(imagen_ruta).convert_alpha()

        # Escalarla
        ancho = int(self.imagen_original.get_width() * escala)
        alto  = int(self.imagen_original.get_height() * escala)

        self.imagen = pygame.transform.scale(self.imagen_original, (ancho, alto))

        # Rectángulo
        self.rect = self.imagen.get_rect()

        if pos is None:
            self.rect.center = self.ventana_rect.center
        else:
            self.rect.topleft = pos

    def dibujar_boton(self):
        self.ventana.blit(self.imagen, self.rect)
