import pygame
import math

ANCHO = 300
ALTO = 512

frame = 0
playing  = False

def explotar():
    global playing, frame
    playing = True
    frame = 0

class Explosion(pygame.sprite.Sprite):

    tiempo = 0

    sprites = [ #Sprites de la pelota
      pygame.image.load('Sprites\pelota\EXLOSION1 PNG.png'),
      pygame.image.load('Sprites\pelota\EXLOSION2 PNG.png'),
      pygame.image.load('Sprites\pelota\EXLOSION3 PNG.png'),
      pygame.image.load('Sprites\pelota\EXLOSION4 PNG.png'),
      pygame.image.load('Sprites\pelota\EXLOSION5 PNG.png'),
      pygame.image.load('Sprites\pelota\EXLOSION5 PNG.png'),
    ]

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Sprites\pelota\EXLOSION5 PNG.png").convert()
        self.image = pygame.transform.scale(self.image, (120, 160))
        self.image.set_colorkey("white")
        self.rect = self.image.get_rect()
        self.rect.x = 150 -(self.image.get_width()/2)
        self.rect.y = 400 -(self.image.get_height()/2)
        

    def update(self):
        global frame, playing
        if playing == True:
            if frame < 4:
                frame = math.floor(self.tiempo/100)

                self.image = self.sprites[frame].convert()
                self.image = pygame.transform.scale(self.image, (140, 157))
                self.image.set_colorkey("white")
                self.rect = self.image.get_rect()
                self.rect.x = 150 -(self.image.get_width()/2)
                self.rect.y = 400 -(self.image.get_height()/2)

                if frame < 5:
                    self.tiempo += 1
                
            else:
                playing = False
                self.image = self.sprites[4]
                self.tiempo = 0
