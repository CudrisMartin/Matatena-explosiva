import pygame, sys
from fichas import Token
from Pelotas import Pelota, iniciar_j, pasar_ronda, rev_click, res_click, rev_correr, num_rebotes
from Explosion import Explosion, explotar

###VARIABLES GLOBALES###
##RECURSOS##
fondo =  pygame.image.load('Sprites/fondos/fondo.jpg')
p_inicial = pygame.image.load('Sprites/fondos/Pantalla inicio.jpg')
pygame.display.set_caption("Matatena explosiva")
consolas = 'Matatena_explosiva_proyecto\PressStart2P-Regular.ttf'
#Colores#
Blanco = (255,255,255)
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
dificultad = 0

pygame.init()

display = pygame.display.set_mode((ANCHO, ALTO))

font = pygame.font.Font(None,30)

fichas= pygame.sprite.Group()

pelota = pygame.sprite.Group()
pelota.add(Pelota())

explosion = pygame.sprite.Group()
explosion.add(Explosion())

count = 0
ini = False
reb = 0

def crear_fichas():
    for i in range(dificultad):
        ficha = Token()
        fichas.add(ficha)

def MostrarTexto(pantalla, fuente, texto, color, dimensiones, x , y):
    letra= pygame.font.Font(fuente, dimensiones)
    superficie= letra.render(texto, False, color)
    rectangulo= superficie.get_rect()
    rectangulo.center=(x , y)
    pantalla.blit(superficie, rectangulo)
    
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
            iniciar_j()
            dificultad = 0
            count = 0
            ini = True
              
        for i in fichas:
            if i.rect.collidepoint(*pygame.mouse.get_pos()):
                fichas.remove(i)
                count += 1
                agarrar = pygame.mixer.Sound("Sonidos\Agarrar_ficha.ogg")
                pygame.mixer.Sound.play(agarrar)

    if count == dificultad:
        
        pasar_ronda(True) #comunica que se puede pasar a la siguiente ronda
        
        if rev_click():
            count = 0 
            dificultad += 1 
            fichas.empty()
            crear_fichas()
            pasar_ronda(False) #]Reinicia variable de pasar de ronda y click de la pelota
            res_click()        #]
            

    reb = num_rebotes()

    if reb == 1:
        #sfx = pygame.mixer.Sound("Sonidos\Explosion.ogg")
        #pygame.mixer.Sound.play(sfx)
        explotar()
        

    if not rev_correr() and ini == True:
        ini = False

    fichas.update()
    pelota.update()
    explosion.update()
    if ini == True:
        display.blit(fondo,(0,0))
        MostrarTexto(display,consolas,f"Objetivo: {dificultad}",Blanco,14,80,15)
        fichas.draw(display)
        pelota.draw(display)
        explosion.draw(display)
    else:
        display.blit(p_inicial,(0,0))
        MostrarTexto(display,consolas,f"Click para comenzar",Blanco,14,150,256)   

    pygame.display.update()

    