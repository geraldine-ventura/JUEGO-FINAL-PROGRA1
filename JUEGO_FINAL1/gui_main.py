import pygame
import sys
from pygame.locals import *
from constantes import *
from gui_form_menu_game_l1 import FormGameLevel1  # Importa tu módulo

# Inicialización de Pygame y otras configuraciones
pygame.init()

# Configuración de la pantalla
flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
pygame.display.set_caption("Tu juego")

# Crear una instancia de la clase FormGameLevel1
game_level_1 = FormGameLevel1(w=ANCHO_VENTANA, h=ALTO_VENTANA)

# Bucle principal
while True:
    # Obtener eventos, teclas, etc.
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = pygame.time.Clock().tick(FPS)

    # Actualizar lógica del juego
    game_level_1.update(keys, delta_ms)

    game_level_1.draw(screen)

    # Renderizar/dibujar en la pantalla
    pygame.display.flip()
