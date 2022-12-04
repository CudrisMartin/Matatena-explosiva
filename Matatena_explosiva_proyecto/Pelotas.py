import pygame

#Parametros y funciones necesarios para la comunicación con el main
YI = 400

correr = False
sig_ronda = False
click = False
yi = YI

rebotes = 0

def iniciar_j():
  global correr, rebotes,click, sig_ronda
  rebotes = 0
  correr = True
  sig_ronda = False
  click = False
  yi = YI

def rev_correr():
  global correr
  return correr

def pasar_ronda(v):
  global sig_ronda
  sig_ronda = v

def rev_click():
  global click
  return click

def res_click():
  global click
  click = False

#Clase Pelota
class Pelota(pygame.sprite.Sprite):
  global yi
  sprites = [ #Sprites de la pelota
      pygame.image.load('Sprites\pelota\Pelota.png'),
      pygame.image.load('Sprites\pelota\Pelota explotada.png')
  ]
  
  tiempo = 0

  ANCHO = 300 #Alto y ancho de la ventana
  ALTO = 512

  image = pygame.transform.scale(sprites[0], (50, 50))

  #Aceleración y velocidad inicial de la pelota
  a = 12    #Aceleración proporcional velocidad de caida 
  vi = 80   #Velocidad proporcional velocidad de subida 

  def __init__(self) -> None:
    global yi
    super().__init__()
    self.image = pygame.image.load("Sprites\pelota\Pelota.png").convert()
    self.image = pygame.transform.scale(self.image,(40,40))
    self.image.set_colorkey("white")
    self.rect = self.image.get_rect()
    self.rect.x = 150 - (self.image.get_width()/2)
    self.rect.y = yi - (self.image.get_height()/2)

  def update(self):
    global correr, sig_ronda, click, rebotes, yi

    if rebotes == 0:
      self.image = pygame.image.load("Sprites\pelota\Pelota.png").convert()
      self.image = pygame.transform.scale(self.image,(40,40))
      self.image.set_colorkey("white")
    else:
      self.image = pygame.image.load("Sprites\pelota\Pelota explotada.png").convert()
      self.image = pygame.transform.scale(self.image,(40,40))
      self.image.set_colorkey("white")

    bottom = pygame.mouse.get_pressed()

    if bottom[0]:        
      if self.rect.collidepoint(*pygame.mouse.get_pos()):
        if sig_ronda == True: #Si se cliceka y se puede seguir a la siguiente ronda
          click = True
          yi = self.rect.y
          self.tiempo = 0
          rebotes = 0
          SFXrebote = pygame.mixer.Sound("Sonidos\Rebotar.ogg")
          pygame.mixer.Sound.play(SFXrebote)
    
    t = self.tiempo/1000 #Tiempo expresado en medidad más simples
    dy = 0               #inicialización variable de distancia
    
    if correr == True:
      self.tiempo += 10 #Velocidad del tiempo, si el juego corre muy lento aumentar este parametro

      t2 = pow(t,2)
      dy = -(self.vi* t)
      dy += (self.a*t2)*0.5
      dy = int(dy)
      if self.rect.y == YI and dy > 0: #Si la posición es igual a la inicial absoluta y la distancia es negativa
        SFXrebotar = pygame.mixer.Sound("Sonidos\Rebote.ogg")
        pygame.mixer.Sound.play(SFXrebotar)
        self.tiempo = 0                #Reiniciar tiempo reinicia rebote
                          #Es necesario cambiar la posición inicial relativa para evitar saltos
        rebotes += 1
        yi = YI 

    self.rect.y = yi + dy         #Cambio en la posición de la pelota
    
    if rebotes >= 2:
      correr = False
    
    
    
