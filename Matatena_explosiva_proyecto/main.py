import pygame


###VARIABLES GLOBALES###
##RECURSOS##
fondo =  pygame.image.load('Sprites\Fondo.jpg')
pygame.display.set_caption("Matatena explosiva")
#Colores#
#Resolución#
w = 512
h = 300
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

Pantalla = pygame.display.set_mode((w,h))
Clock = pygame.time.Clock
