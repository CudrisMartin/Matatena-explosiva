import pygame

correr = False
continuar = False

def iniciar_j():
  global correr
  correr = True

class Pelota(pygame.sprite.Sprite):
  sprites = [
      pygame.image.load('Sprites\Pelota\Pelota.png'),
      pygame.image.load('Sprites\Pelota\Pelota explotada.png')
  ]

  Reloj = pygame.time.Clock()

  tiempo = 0

  ANCHO = 300
  ALTO = 512
  yi = 400
  image = pygame.transform.scale(sprites[0], (50, 50))

  a = 12
  vi = 80

  def __init__(self) -> None:
    super().__init__()
    self.image = pygame.transform.scale(self.sprites[0], (50, 50)).convert()
    self.rect = self.image.get_rect()
    self.rect.x = 150
    self.rect.y = self.yi

  def update(self):
    global iniciado
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN : 
        if event.button == pygame.BUTTON_LEFT:                        
          self.tiempo = 0
    
    t = self.tiempo/1000
    dy = 0
    
    if correr == True:
      self.tiempo += 1

      t2 = pow(t,2)
      dy = -(self.vi* t)
      dy += (self.a*t2)*0.5
      dy = int(dy)
      if self.rect.y == self.yi and dy > 0:
        self.tiempo = 0
    
    self.rect.y = 400 + dy
    
    
    
