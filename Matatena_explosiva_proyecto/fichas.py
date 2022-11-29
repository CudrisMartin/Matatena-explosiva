import pygame as pg
import random

ANCHO = 300
ALTO = 512


class Token(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fichas_png = ["\Ficha Amarilla.png", "\Ficha Azul.png", "\Ficha Morada.png", "\Ficha Rosada.png", "\Ficha Verde.png"]
        self.image = pg.image.load("Sprites\Fichas"+random.choice(self.fichas_png)).convert()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.image.set_colorkey("white")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)

    def update(self):
	# Actualiza 
        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

        if self.rect.top < ALTO//2 + 50:
            self.rect.top = ALTO//2 + 50        