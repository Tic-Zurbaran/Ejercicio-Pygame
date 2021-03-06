### Librerías ###

import pygame as pg
import sys

### Variables ###

# Colores 

black = (0,0,0)
white = (255,255,255)

# Pantalla

fps = 60
tamaño = (600,400)

### Setup ###

# Pygame

pg.init()

# Ventana 

pantalla = pg.display.set_mode(tamaño)
pg.display.set_caption('Space Invaders')
clock = pg.time.Clock()

# Imágenes

fondo = pg.image.load("fondo.png")
nave = pg.image.load("nave.png")

# Posiciones 

nave_pos_x = 300

nave_pos_y = 285


### Bucle de juego ###

while True:

	for event in pg.event.get():
		
		if event.type == pg.QUIT:
			sys.exit()

		if event.type == pg.KEYDOWN:

			if event.key == pg.K_a:
				nave_pos_x -= 10		

			if event.key == pg.K_d:
				nave_pos_x += 10

	### Figuras e imagenes ###

	pantalla.fill(white)

	pantalla.blit(fondo, (0,0))

	pantalla.blit(nave, (nave_pos_x, nave_pos_y))

	pg.display.update()


