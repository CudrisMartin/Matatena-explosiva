import pygame, sys
from fichas import Token
from Pelotas import Pelota
from Pelotas import iniciar_j

###VARIABLES GLOBALES###
##RECURSOS##
fondo =  pygame.image.load('Matatena_explosiva_proyecto\Sprites\Fondo.jpg')
pygame.display.set_caption("Matatena explosiva")
#Colores#
#Resolución#
ANCHO = 300
ALTO = 512
#Variables importantes#
FPS = 30
#Variables auxiliares#
Clock = pygame.time.Clock()
#Estados#
gameover = False
play = False
dificultad = 1

pygame.init()

display = pygame.display.set_mode((ANCHO, ALTO))

font = pygame.font.Font(None,30)

fichas= pygame.sprite.Group()

pelota = pygame.sprite.Group()
pelota.add(Pelota())

count = 0
ini = False

def crear_fichas():
    for i in range(dificultad):
        ficha = Token()
        fichas.add(ficha)

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
   
    for i in fichas:
        for j in fichas:
            if i.rect.colliderect(j) and j != i:
                fichas.remove(j)
                while True:
                    ficha = Token()
                    if not i.rect.colliderect(ficha):
                        fichas.add(ficha)
                        break

    bottom = pygame.mouse.get_pressed()
    if bottom[0]:
        if ini == False:
            ini == True
            crear_fichas()
            iniciar_j()
                
                
        else:
            for i in fichas:
                if i.rect.collidepoint(*pygame.mouse.get_pos()):
                    fichas.remove(i)
                    count += 1

    if count == dificultad:
        dificultad += 1
        crear_fichas()

    fichas.update()
    pelota.update()
    display.blit(fondo,(0,0))
    fichas.draw(display)
    pelota.draw(display)

    pygame.display.update()