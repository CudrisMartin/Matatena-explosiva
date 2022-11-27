import pygame, sys
import random, os
from fichas import Token


###VARIABLES GLOBALES###
##RECURSOS##
fondo =  pygame.image.load('.\Sprites\Fondo.jpg')
pygame.display.set_caption("Matatena explosiva")
#Colores#
#Resolución#
ANCHO = 800
ALTO = 600
#Variables importantes#
FPS = 30
#Variables auxiliares#
Clock = pygame.time.Clock()
#Estados#
gameover = False
play = False
dificultad = 1

def recargar_pantalla():
    global play, gameover, dificultad
    Pantalla.blit(fondo,(fondo.get_rect().width,0))

pygame.init()

Pantalla = pygame.display.set_mode((ANCHO,ALTO))
Clock = pygame.time.Clock

display = pygame.display.set_mode((ANCHO, ALTO))

count = 0

font = pygame.font.Font(None,30)



sprites= pygame.sprite.Group()

for i in range(20):
    ficha = Token()
    sprites.add(ficha)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
   
    for i in sprites:
        for j in sprites:
            if i.rect.colliderect(j) and j != i:
                sprites.remove(j)
                while True:
                    ficha = Token()
                    if not i.rect.colliderect(ficha):
                        sprites.add(ficha)
                        break

    bottom = pygame.mouse.get_pressed()
    if bottom[0]:
        for i in sprites:
            if i.rect.collidepoint(*pygame.mouse.get_pos()):
                sprites.remove(i)
                count += 1
                print("si")
                break

        

    sprites.update()
    display.fill('purple')
    sprites.draw(display)
    print(str(count))

    pygame.display.update()
