import pygame
import os
import sys
import Constantes
import Boton
from pytmx.util_pygame import load_pygame
from Personaje import Personaje


pygame.init()


info_pantalla = pygame.display.Info()
ventana = pygame.display.set_mode((info_pantalla.current_w, info_pantalla.current_h))


Alto_Pantalla = info_pantalla.current_h
Ancho_Pantalla = info_pantalla.current_w

pygame.display.set_caption("Mi Juego")

#Movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#Conrolar Fps
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(Constantes.TIPO_L, Constantes.TAMAÑO_L)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
IMG_DIR = os.path.join(BASE_DIR, "Img")
SONIDOS_DIR = os.path.join(BASE_DIR, "Sonidos")



#funciones

def ruta_relativa(ruta):
    """Devuelve la ruta correcta tanto en .py como en .exe"""
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, ruta)


def verificar_colision_muro(rect):
    capas_colision = ["Capa de patrones 2", "Capa de patrones 3", "Capa de patrones 4","Capa de patrones 5"]
    
    for layer in tmx_data.visible_layers:
        if hasattr(layer, 'tiles') and layer.name in capas_colision:
            for x, y, tile in layer.tiles():
                if tile:
                    tile_rect = pygame.Rect(x * tmx_data.tilewidth,y * tmx_data.tileheight,tmx_data.tilewidth,tmx_data.tileheight)
                    if rect.colliderect(tile_rect):
                        return True
    return False

def dibujar_mapa_cam(jugador):
    cam_x = jugador.forma.x - Ancho_Pantalla // 2
    cam_y = jugador.forma.y - Alto_Pantalla // 2
   
    map_width = tmx_data.width * tmx_data.tilewidth
    map_height = tmx_data.height * tmx_data.tileheight
    
    cam_x = max(0, min(cam_x, map_width - Ancho_Pantalla))
    cam_y = max(0, min(cam_y, map_height - Alto_Pantalla))

    for layer in tmx_data.visible_layers:
        if hasattr(layer, 'tiles'):
            for x, y, tile in layer.tiles():
                if tile:
                    ventana.blit(tile,(x * tmx_data.tilewidth - cam_x, y * tmx_data.tileheight - cam_y ))
    return cam_x, cam_y



def posicion_X(pocision):
    x = (Ancho_Pantalla * pocision)
    return x

def posicion_Y(pocision):
    y = (Alto_Pantalla * pocision)
    return y

def barra_creatividad(puntos_creatividad):
    if puntos_creatividad <= 0:
        ventana.blit(barra_creatividad_0, (posicion_X(0.75), posicion_Y(0.01)))
    elif puntos_creatividad == 1:
        ventana.blit(barra_creatividad_1, (posicion_X(0.75), posicion_Y(0.01)))
    elif puntos_creatividad == 2:
        ventana.blit(barra_creatividad_2, (posicion_X(0.75), posicion_Y(0.01)))
    elif puntos_creatividad == 3:
        ventana.blit(barra_creatividad_3, (posicion_X(0.75), posicion_Y(0.01)))
    elif puntos_creatividad == 4:
        ventana.blit(barra_creatividad_4, (posicion_X(0.75), posicion_Y(0.01)))
    elif puntos_creatividad == 5:
        ventana.blit(barra_creatividad_5, (posicion_X(0.75), posicion_Y(0.01)))
    elif puntos_creatividad >= 6:
        ventana.blit(barra_creatividad_6, (posicion_X(0.75), posicion_Y(0.01)))

def barra_empatia(puntos_empatia):
    if puntos_empatia <= 0:
        ventana.blit(barra_empatia_0, (posicion_X(0.75), posicion_Y(0.13)))
    elif puntos_empatia == 1:
        ventana.blit(barra_empatia_1, (posicion_X(0.75), posicion_Y(0.13)))
    elif puntos_empatia == 2:
        ventana.blit(barra_empatia_2, (posicion_X(0.75), posicion_Y(0.13)))
    elif puntos_empatia == 3:
        ventana.blit(barra_empatia_3, (posicion_X(0.75), posicion_Y(0.13)))
    elif puntos_empatia == 4:
        ventana.blit(barra_empatia_4, (posicion_X(0.75), posicion_Y(0.13)))
    elif puntos_empatia == 5:
        ventana.blit(barra_empatia_5, (posicion_X(0.75), posicion_Y(0.13)))
    elif puntos_empatia >= 6:
        ventana.blit(barra_empatia_6, (posicion_X(0.75), posicion_Y(0.13)))
    
def mouseLag():
    while pygame.mouse.get_pressed()[0]:
        pygame.event.pump()
        
def escalar_imagen(imagen, escala):
    ancho = int(imagen.get_width() * escala)
    alto = int(imagen.get_height() * escala)
    return pygame.transform.scale(imagen, (ancho, alto))

def Mensaje(texto, tiempo):
    fuente = pygame.font.Font(None, 40) 
    texto = fuente.render(texto, True, Constantes.COLOR_F)
    rect = pygame.Rect(0, posicion_Y(0.8), posicion_X(1), posicion_Y(0.8))
    pygame.draw.rect(ventana, Constantes.BLANCO_P, rect)

    ventana.blit(texto, (0, posicion_Y(0.8)))
    pygame.display.update()
    pygame.time.delay(tiempo)

tmx_data = load_pygame(ruta_relativa("Mapa/mapa.tmx"))

#Imagenes
barra_de_creatividad_6 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Creatividad", "C6.png")).convert_alpha()
barra_de_creatividad_5 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Creatividad", "C5.png")).convert_alpha()
barra_de_creatividad_4 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Creatividad", "C4.png")).convert_alpha()
barra_de_creatividad_3 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Creatividad", "C3.png")).convert_alpha()
barra_de_creatividad_2 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Creatividad", "C2.png")).convert_alpha()
barra_de_creatividad_1 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Creatividad", "C1.png")).convert_alpha()
barra_de_creatividad_0 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Creatividad", "C0.png")).convert_alpha()

barra_creatividad_6 = escalar_imagen(barra_de_creatividad_6, Constantes.ESCALA_BARRA_C)
barra_creatividad_5 = escalar_imagen(barra_de_creatividad_5, Constantes.ESCALA_BARRA_C)
barra_creatividad_4 = escalar_imagen(barra_de_creatividad_4, Constantes.ESCALA_BARRA_C)
barra_creatividad_3 = escalar_imagen(barra_de_creatividad_3, Constantes.ESCALA_BARRA_C)
barra_creatividad_2 = escalar_imagen(barra_de_creatividad_2, Constantes.ESCALA_BARRA_C)
barra_creatividad_1 = escalar_imagen(barra_de_creatividad_1, Constantes.ESCALA_BARRA_C)
barra_creatividad_0 = escalar_imagen(barra_de_creatividad_0, Constantes.ESCALA_BARRA_C)

barra_de_empatia_6 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Empatia", "E6.png")).convert_alpha()
barra_de_empatia_5 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Empatia", "E5.png")).convert_alpha()
barra_de_empatia_4 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Empatia", "E4.png")).convert_alpha()
barra_de_empatia_3 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Empatia", "E3.png")).convert_alpha()
barra_de_empatia_2 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Empatia", "E2.png")).convert_alpha()
barra_de_empatia_1 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Empatia", "E1.png")).convert_alpha()
barra_de_empatia_0 = pygame.image.load(os.path.join(IMG_DIR, "Barra de Empatia", "E0.png")).convert_alpha()

barra_empatia_6 = escalar_imagen(barra_de_empatia_6, Constantes.ESCALA_BARRA_E)
barra_empatia_5 = escalar_imagen(barra_de_empatia_5, Constantes.ESCALA_BARRA_E)
barra_empatia_4 = escalar_imagen(barra_de_empatia_4, Constantes.ESCALA_BARRA_E)
barra_empatia_3 = escalar_imagen(barra_de_empatia_3, Constantes.ESCALA_BARRA_E)
barra_empatia_2 = escalar_imagen(barra_de_empatia_2, Constantes.ESCALA_BARRA_E)
barra_empatia_1 = escalar_imagen(barra_de_empatia_1, Constantes.ESCALA_BARRA_E)
barra_empatia_0 = escalar_imagen(barra_de_empatia_0, Constantes.ESCALA_BARRA_E)

#Boton 


#Musica y Sonidos
pygame.mixer.music.load(os.path.join(SONIDOS_DIR, "musica_fondo.mp3"))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

#personajes
jugador_Animacion = []

for i in range(1, 3):
    imagen = pygame.image.load(os.path.join(IMG_DIR, "Jugador", f"frame_{i-1}.png"))
    imagen = escalar_imagen(imagen, Constantes.ESCALA_P)
    jugador_Animacion.append(imagen)

jugador = Personaje(jugador_Animacion, Constantes.ANCHO_P, Constantes.ALTO_P, 30, 475,flip_inicial=False)



Empatia_Animacion = []

for i in range(1, 4):
    imagen_Empatia = pygame.image.load(os.path.join(IMG_DIR, "Empatia", f"frame_{i-1}.png"))
    imagen_Empatia = escalar_imagen(imagen_Empatia, Constantes.ESCALA_E)
    Empatia_Animacion.append(imagen_Empatia)
    
Empatia = Personaje(Empatia_Animacion, Constantes.ANCHO_E, Constantes.ALTO_E, 1050, 115, flip_inicial=True)
    



Creatividad_Animacion = []

for i in range(1, 4):
    imagen_Creatividad = pygame.image.load(os.path.join(IMG_DIR, "Creatividad", f"frame_{i-1}.png"))
    imagen_Creatividad = escalar_imagen(imagen_Creatividad, Constantes.ESCALA_C)
    Creatividad_Animacion.append(imagen_Creatividad)

Creatividad = Personaje(Creatividad_Animacion, Constantes.ANCHO_C, Constantes.ALTO_C, 1700, 255 , flip_inicial=True)

jugador_imagen = pygame.image.load(os.path.join(IMG_DIR, "Jugador", "frame_0.png"))
jugador_imagen = escalar_imagen(jugador_imagen, Constantes.ESCALA_P)

Mezcla = []

for i in range(1, 3):
    imagen_Mezcla = pygame.image.load(os.path.join(IMG_DIR, "Mezcla", f"frame_{i-1}.png"))
    imagen_Mezcla = escalar_imagen(imagen_Mezcla, Constantes.ESCALA_M)
    Mezcla.append(imagen_Mezcla)


Mezcla = Personaje(Mezcla, Constantes.ANCHO_M, Constantes.ALTO_M, 1330, 830, flip_inicial=True)

    
#variables
I = True
Op1 = None
Op2 = None
Op3 = None
Op4 = None
Op5 = None
Op6 = None
mostrar_boton = False
puntosEmpatia = 0
puntosCreatividad = 0
respuesta1 = False
respuesta2 = False
respuesta3 = False
respuesta4 = False
respuesta5 = False
respuesta6 = False
R1 = False
R2 = False
R3 = False
R4 = False
R5 = False
R6 = False
 
#imagenes finales
finala_surf = pygame.image.load(os.path.join(IMG_DIR, "fondo", "FINALA.png")).convert()
finalb_surf = pygame.image.load(os.path.join(IMG_DIR, "fondo", "FINALB.png")).convert()
finalc_surf = pygame.image.load(os.path.join(IMG_DIR, "fondo", "FINALC.png")).convert()
finald_surf = pygame.image.load(os.path.join(IMG_DIR, "fondo", "FINALD.png")).convert()


finala_surf = pygame.transform.scale(finala_surf, (Ancho_Pantalla, Alto_Pantalla))
finalb_surf = pygame.transform.scale(finalb_surf, (Ancho_Pantalla, Alto_Pantalla))
finalc_surf = pygame.transform.scale(finalc_surf, (Ancho_Pantalla, Alto_Pantalla))
finald_surf = pygame.transform.scale(finald_surf, (Ancho_Pantalla, Alto_Pantalla))

#variable para definir si ya se termino el juego o no
completado = False
#bucle principal
while I == True:
    reloj.tick(Constantes.FPS)
    ventana.fill(Constantes.COLOR_F)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                I = False
            # Manejo de teclado: actualizar banderas de movimiento
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    mover_izquierda = True
                if event.key == pygame.K_d:
                    mover_derecha = True
                if event.key == pygame.K_w:
                    mover_arriba = True
                if event.key == pygame.K_s:
                    mover_abajo = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mover_izquierda = False
                if event.key == pygame.K_d:
                    mover_derecha = False
                if event.key == pygame.K_w:
                    mover_arriba = False
                if event.key == pygame.K_s:
                    mover_abajo = False
    #si ya se respondieron todas las preguntas
    if R1 and R2 and R3 and R4 and R5 and R6:
        completado = True
    
    if completado:
        if puntosCreatividad > 0 and puntosEmpatia >0:
            if puntosCreatividad > puntosEmpatia:
                ventana.blit(finalb_surf, (0,0))
            elif puntosEmpatia > puntosCreatividad:
                ventana.blit(finala_surf, (0,0))
            else:
                ventana.blit(finalc_surf, (0,0))
        else: 
            ventana.blit(finald_surf, (0,0))

        pygame.display.update()
        continue
    if not completado:
        cam_x, cam_y = dibujar_mapa_cam(jugador)
 
        barra_creatividad(puntosCreatividad)
        barra_empatia(puntosEmpatia)

        #actualizar animaciones

        jugador.actualizar_animacion(Constantes.COLDOWN_ANIMACION_P)
        Empatia.actualizar_animacion(Constantes.COLDOWN_ANIMACION_E)
        Creatividad.actualizar_animacion(Constantes.COLDOWN_ANIMACION_C)
        Mezcla.actualizar_animacion(Constantes.COLDOWN_ANIMACION_M)
   
        #calculo de movimiento
        delta_x = 0
        delta_y = 0

        if mover_derecha == True:
            delta_x += Constantes.VELOCIDAD_P
        if mover_izquierda == True:
            delta_x -= Constantes.VELOCIDAD_P
        if mover_abajo == True:
            delta_y += Constantes.VELOCIDAD_P
        if mover_arriba == True:
            delta_y -= Constantes.VELOCIDAD_P

        if delta_x != 0 or delta_y != 0:
        
            nuevo_x = jugador.forma.copy()
            nuevo_x.x += delta_x
            
            nuevo_y = jugador.forma.copy()
            nuevo_y.y += delta_y
          
       
            if delta_x != 0 and not verificar_colision_muro(nuevo_x):
                jugador.forma.x += delta_x
      
            if delta_y != 0 and not verificar_colision_muro(nuevo_y):
                jugador.forma.y += delta_y    

        #mover jugador
        jugador.movimiento(delta_x, delta_y)
        jugador.dibujar_con_camara(ventana,Constantes.ROJO_P,cam_x,cam_y)
        Empatia.dibujar_con_camara(ventana,Constantes.VERDE_P,cam_x,cam_y)
        Creatividad.dibujar_con_camara(ventana,Constantes.AZUL_P,cam_x,cam_y)
        Mezcla.dibujar_con_camara(ventana,Constantes.AMARILLO_P,cam_x,cam_y)
        #empatia
        #primera pregunta
        if not respuesta1:   
            if jugador.forma.colliderect(Empatia.forma):

                if not mostrar_boton:
                    Mensaje("Hola! Bienvenid@ a la estación Empatía ~", 3000)
                    Mensaje("Esta estacion trata sobre entender sentimientos, ayudar a otros, ponerse en sus zapatos.", 4000)
                    Mensaje("Vamos con la primera pregunta",2000)
                    Mensaje("Si tu amigo está triste porque perdió su juguete, ¿qué haces?", 6000)

                    if Op1 is None:
                        Op1 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP1R1.png"), pos=(posicion_X(0.01), posicion_Y(0.8)))
                        Op2 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP2R1.png"), pos=(posicion_X(0.38), posicion_Y(0.8)))
                        Op3 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP3R1.png"), pos=(posicion_X(0.75), posicion_Y(0.8)))
    
                    mostrar_boton = True
                mouse_pos = pygame.mouse.get_pos()
                mouse_click = pygame.mouse.get_pressed()[0]
                if mostrar_boton:
                    if Op1 is not None and Op2 is not None and Op3 is not None:
                        Op1.dibujar_boton()
                        Op2.dibujar_boton()
                        Op3.dibujar_boton()
         
                if mouse_click:
                    if Op1.rect.collidepoint(mouse_pos):
                        pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"incorrecto.mp3")).play()
                        Mensaje("¡Incorrecto! -1 punto de empatía", 2000)
                        puntosEmpatia -= 1
                        mostrar_boton = False
                        print(puntosCreatividad)
                        print(puntosEmpatia) 
                        respuesta1 = True
                        R1 = True
                        Op1 = None 
                        mouseLag()
                    elif Op2.rect.collidepoint(mouse_pos):
                        pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                        puntosEmpatia += 1
                        Mensaje("¡Correcto! +1 puntos de empatía", 2000)
                        mostrar_boton = False
                        print(puntosCreatividad)
                        print(puntosEmpatia)
                        Op1 = None 
                        respuesta1 = True
                        R1 = True
                        mouseLag()
                    elif Op3.rect.collidepoint(mouse_pos):
                        pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                        puntosCreatividad += 1
                        Mensaje("¡Correcto! +1 punto de Creatividad", 2000)
                        mostrar_boton = False
                        print(puntosCreatividad)
                        print(puntosEmpatia) 
                        respuesta1 = True 
                        R1 = True
                        Op1 = None 
                        mouseLag()
        #segunda pregunta
        elif R1:
            if not respuesta2:  
                if jugador.forma.colliderect(Empatia.forma):
                    if not mostrar_boton:
                        Mensaje("¡Bien! ", 3000)
                        Mensaje("Ahora vamos por la segunda pregunta", 5000)
                        Mensaje("¿Qué haces cuando te sientes frustrado?", 6000)
 
                        if Op1 is None:
                            Op1 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP1R2.png"), pos=(posicion_X(0.01), posicion_Y(0.8)))
                            Op2 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP2R2.png"), pos=(posicion_X(0.38), posicion_Y(0.8)))
                            Op3 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP3R2.png"), pos=(posicion_X(0.75), posicion_Y(0.8)))
   
                        mostrar_boton = True
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_click = pygame.mouse.get_pressed()[0]
                    if mostrar_boton:
                        if Op1 is not None and Op2 is not None and Op3 is not None:
                            Op1.dibujar_boton()
                            Op2.dibujar_boton()
                            Op3.dibujar_boton()
         
                    if mouse_click:
                        if Op1.rect.collidepoint(mouse_pos):
                            pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"incorrecto.mp3")).play()
                            Mensaje("¡Incorrecto! -1 punto de empatía", 2000)
                            puntosEmpatia -= 1
                            mostrar_boton = False
                            print(puntosCreatividad)
                            print(puntosEmpatia) 
                            respuesta2 = True
                            Op1 = None 
                            R2 = True
                        elif Op2.rect.collidepoint(mouse_pos):
                            puntosEmpatia += 2
                            pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                            Mensaje("¡Correcto! +2 punto de empatía", 2000)
                            mostrar_boton = False
                            print(puntosCreatividad)
                            print(puntosEmpatia) 
                            respuesta2 = True
                            Op1 = None 
                            R2 = True
                        elif Op3.rect.collidepoint(mouse_pos):
                            pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                            puntosCreatividad += 1
                            Mensaje("¡Correcto! +1 punto de creatividad", 2000)
                            mostrar_boton = False
                            print(puntosCreatividad)
                            print(puntosEmpatia) 
                            respuesta2 = True 
                            Op1 = None 
                            R2 = True
      
        #Creatividad
        #primera pregunta
        if not respuesta3:   
            if jugador.forma.colliderect(Creatividad.forma):

                if not mostrar_boton:
                    Mensaje("Hola! Bienvenid@ a la estación de Creatividad ~", 3000)
                    Mensaje("Esta estación trata sobre la capacidad de generar ideas nuevas y originales para encontrar soluciones unicas", 5000)
                    Mensaje("Vamos con la primera pregunta",2000)
                    Mensaje("El camino está bloqueado por una piedra, ¿qué harías?", 6000)

                    if Op1 is None:
                        Op1 = Boton.boton(ventana,os.path.join(IMG_DIR, "Botones", "OP1R3.png"), pos=(posicion_X(0.01), posicion_Y(0.8)))
                        Op2 = Boton.boton(ventana,os.path.join(IMG_DIR, "Botones", "OP2R3.png"), pos=(posicion_X(0.38), posicion_Y(0.8)))
                        Op3 = Boton.boton(ventana,os.path.join(IMG_DIR, "Botones", "OP3R3.png"), pos=(posicion_X(0.75), posicion_Y(0.8)))
   
                    mostrar_boton = True
                mouse_pos = pygame.mouse.get_pos()
                mouse_click = pygame.mouse.get_pressed()[0]
                if mostrar_boton:
                     if Op1 is not None and Op2 is not None and Op3 is not None:
                        Op1.dibujar_boton()
                        Op2.dibujar_boton()
                        Op3.dibujar_boton()
         
                if mouse_click:
                    if Op1.rect.collidepoint(mouse_pos):
                        pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"incorrecto.mp3")).play()
                        Mensaje("¡Incorrecto! -1 punto de creatividad", 2000)
                        mostrar_boton = False
                        puntosCreatividad -= 1
                        print(puntosCreatividad)
                        print(puntosEmpatia) 
                        respuesta3 = True
                        R3 = True
                        Op1 = None 
                        mouseLag()
                    elif Op2.rect.collidepoint(mouse_pos):
                        pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                        Mensaje("¡Correcto! +1 punto de creatividad", 2000)
                        puntosCreatividad += 1
                        mostrar_boton = False
                        print(puntosCreatividad)
                        print(puntosEmpatia) 
                        respuesta3 = True
                        R3 = True
                        Op1 = None 
                        mouseLag()
                    elif Op3.rect.collidepoint(mouse_pos):
                        pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                        Mensaje("¡Correcto! +2 punto de creatividad", 2000)
                        puntosCreatividad += 2
                        mostrar_boton = False
                        print(puntosCreatividad)
                        print(puntosEmpatia) 
                        respuesta3 = True 
                        R3 = True
                        Op1 = None 
                        mouseLag()
        #segunda pregunta
        if R3:
            if not respuesta4:  
                if jugador.forma.colliderect(Creatividad.forma):
                    if not mostrar_boton:
                        Mensaje("¡Bien! ", 3000)
                        Mensaje("Ahora vamos por la segunda pregunta", 5000)
                        Mensaje("Te encuentras un lápiz tirado en el piso. ¿Qué haces?", 6000)
 
                        if Op1 is None:
                            Op1 = Boton.boton(ventana,os.path.join(IMG_DIR, "Botones", "OP1R4.png"), pos=(posicion_X(0.01), posicion_Y(0.8)))
                            Op2 = Boton.boton(ventana,os.path.join(IMG_DIR, "Botones", "OP2R4.png"), pos=(posicion_X(0.38), posicion_Y(0.8)))
                            Op3 = Boton.boton(ventana,os.path.join(IMG_DIR, "Botones", "OP3R4.png"), pos=(posicion_X(0.75), posicion_Y(0.8)))
                        mostrar_boton = True
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_click = pygame.mouse.get_pressed()[0]
                    if mostrar_boton:
                        if Op1 is not None and Op2 is not None and Op3 is not None:
                            Op1.dibujar_boton()
                            Op2.dibujar_boton()
                            Op3.dibujar_boton()
         
                    if mouse_click:
                        if Op1.rect.collidepoint(mouse_pos):
                            pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"incorrecto.mp3")).play()
                            Mensaje("¡Incorrecto! -1 punto de creatividad", 2000)
                            mostrar_boton = False
                            puntosCreatividad -= 1
                            print(puntosCreatividad)
                            print(puntosEmpatia) 
                            respuesta4 = True
                            Op1 = None
                            R4 = True 
                        elif Op2.rect.collidepoint(mouse_pos):
                            pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                            puntosEmpatia += 1
                            Mensaje("¡Correcto! +1 punto de Empatia", 2000)
                            mostrar_boton = False
                            print(puntosCreatividad)
                            print(puntosEmpatia) 
                            respuesta4 = True
                            Op1 = None
                            R4 = True  
                        elif Op3.rect.collidepoint(mouse_pos):
                            pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                            Mensaje("¡Correcto! +2 punto de creatividad", 2000)
                            puntosCreatividad += 2
                            mostrar_boton = False
                            print(puntosCreatividad)
                            print(puntosEmpatia) 
                            respuesta4 = True
                            Op1 = None 
                            R4 = True 
        #Mezcla     
        # primera pregunta                
        if not respuesta5:   
            if jugador.forma.colliderect(Mezcla.forma):
  
                if not mostrar_boton:
                    Mensaje("Hola! Bienvenid@ a mi estacion, yo soy el sabio Creapatía, una mezcla entre creatividad y empatia ~", 6000)
                    Mensaje("Yo soy el equilibrio entre la emoción que entiende y la mente que crea", 5000)
                    Mensaje("Vamos con la primera pregunta",2000)
                    Mensaje("Hay un puente roto en el camino y necesitan cruzar. ¿Qué harías?", 6000)

                    if Op1 is None:
                        Op1 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP1R5.png"), pos=(posicion_X(0.01), posicion_Y(0.8)))
                        Op2 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP2R5.png"), pos=(posicion_X(0.38), posicion_Y(0.8)))
                        Op3 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP3R5.png"), pos=(posicion_X(0.75), posicion_Y(0.8)))
   
                    mostrar_boton = True
                mouse_pos = pygame.mouse.get_pos()
                mouse_click = pygame.mouse.get_pressed()[0]
                if mostrar_boton:
                    if Op1 is not None and Op2 is not None and Op3 is not None:
                        Op1.dibujar_boton()
                        Op2.dibujar_boton()
                        Op3.dibujar_boton()
        
                if mouse_click:
                    if Op1.rect.collidepoint(mouse_pos):
                        pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"incorrecto.mp3")).play()
                        Mensaje("¡Incorrecto! -1 punto de empatía y -1 punto de creatividad", 2000)
                        mostrar_boton = False
                        puntosEmpatia -= 1
                        puntosCreatividad -= 1
                        print(puntosCreatividad)
                        print(puntosEmpatia) 
                        respuesta5 = True
                        R5 = True
                        Op1 = None 
                        mouseLag()
                    elif Op2.rect.collidepoint(mouse_pos):
                        pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                        Mensaje("¡Correcto! +1 punto de creatividad y +1 punto de empatía", 2000)
                        puntosEmpatia += 1
                        puntosCreatividad += 1
                        mostrar_boton = False
                        print(puntosCreatividad)
                        print(puntosEmpatia) 
                        respuesta5 = True
                        R5 = True
                        Op1 = None 
                        mouseLag()
                    elif Op3.rect.collidepoint(mouse_pos):
                        pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                        Mensaje("¡Correcto! +1 punto de creatividad", 2000)
                        puntosCreatividad += 1
                        mostrar_boton = False
                        print(puntosCreatividad)
                        print(puntosEmpatia) 
                        respuesta5 = True 
                        R5 = True
                        Op1 = None 
                        mouseLag()
        if R5:
            if not respuesta6:  
                if jugador.forma.colliderect(Mezcla.forma):
                    if not mostrar_boton:
                        Mensaje("¡Bien! ", 3000)
                        Mensaje("Ahora vamos por la segunda pregunta", 5000)
                        Mensaje("Cuando otro niño piensa diferente a ti…", 6000)

                        if Op1 is None:
                            Op1 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP1R6.png"), pos=(posicion_X(0.01), posicion_Y(0.8)))
                            Op2 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP2R6.png"), pos=(posicion_X(0.38), posicion_Y(0.8)))
                            Op3 = Boton.boton(ventana, os.path.join(IMG_DIR, "Botones", "OP2R6.png"), pos=(posicion_X(0.75), posicion_Y(0.8),))
                        mostrar_boton = True
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_click = pygame.mouse.get_pressed()[0]
                    if mostrar_boton:
                        if Op1 is not None and Op2 is not None and Op3 is not None:
                            Op1.dibujar_boton()
                            Op2.dibujar_boton()
                            Op3.dibujar_boton()
         
                    if mouse_click:
                        if Op1.rect.collidepoint(mouse_pos):
                            puntosEmpatia -= 1
                            puntosCreatividad -= 1
                            mostrar_boton = False
                            pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"incorrecto.mp3")).play()
                            Mensaje("¡Incorrecto! -1 punto de empatía y -1 punto de creatividad", 2000)
                            print(puntosCreatividad)
                            print(puntosEmpatia) 
                            respuesta6 = True
                            Op1 = None
                            R6 = True 
                        elif Op2.rect.collidepoint(mouse_pos):
                            puntosEmpatia += 1
                            mostrar_boton = False
                            pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                            Mensaje("¡Correcto! +1 punto de empatía", 2000)
                            print(puntosCreatividad)
                            print(puntosEmpatia) 
                            respuesta6 = True
                            Op1 = None 
                            R6 = True 
                        elif Op3.rect.collidepoint(mouse_pos):
                            puntosCreatividad += 1
                            mostrar_boton = False
                            pygame.mixer.Sound(os.path.join(SONIDOS_DIR,"correcto.mp3")).play()
                            Mensaje("¡Correcto! +1 punto de creatividad", 2000)
                            print(puntosCreatividad)
                            print(puntosEmpatia) 
                            respuesta6 = True
                            Op1 = None 
                            R6 = True                 
        pygame.display.update()
pygame.quit()