import pygame
from main import *
from settings import *
import os

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
ventana_ancho = WIDTH
ventana_alto = HEIGHT
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pg.display.set_caption('Magic Fuckface in the Maze')

# Cargar la imagen de fondo del menú
fondo = pygame.image.load('resources/textures/cover.png')

# Cargar la música del menú
pygame.mixer.music.load('resources/sound/menu.mp3')
pygame.mixer.music.play(-1)  # Reproducir la música en bucle

# Bucle principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Dibujar el fondo del menú
    ventana.blit(fondo, (0, 0))

    # Actualizar la pantalla
    pygame.display.flip()
    # Cargar la imagen de start
    start_img = pygame.image.load('resources/textures/start.png')

    # Obtener las dimensiones de la imagen de start
    start_ancho = start_img.get_width()
    start_alto = start_img.get_height()

    # Definir la posición inicial de la imagen de start
    start_x = (ventana_ancho - start_ancho) // 2
    start_y = ventana_alto - start_alto - 20

    # Definir el estado de parpadeo de la imagen de start
    start_visible = True
    start_timer = pygame.time.get_ticks()

    # Bucle principal del juego
    while True:
        # Manejo de eventos

        for event in pygame.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_6):
                pg.quit()
                sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    # Ejecutar el código para iniciar el juego principal (main)
                    if __name__ == '__main__':
                        game = Game()
                        game.run()

        # Dibujar el fondo del menú
        ventana.blit(fondo, (0, 0))

        # Parpadeo de la imagen de start
        current_time = pygame.time.get_ticks()
        if current_time - start_timer >= 500:
            start_visible = not start_visible
            start_timer = current_time

        # Mostrar la imagen de start si está visible
        if start_visible:
            ventana.blit(start_img, (start_x, start_y))

        # Actualizar la pantalla
        pygame.display.flip()
