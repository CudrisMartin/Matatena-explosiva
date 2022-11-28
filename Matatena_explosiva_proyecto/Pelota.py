import pygame

sprites = [
    pygame.image.load('Sprites\Pelota\Pelota.png'),
    pygame.image.load('Sprites\Pelota\Pelota explotada.png')
]

ANCHO = 800
ALTO = 600
pelota = sprites[0].convert()

for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
                
         if event.button == pygame.BUTTON_LEFT:
          while gameover == False:
                                
           if pelota.bottom > ALTO:
            pelota.move_ip(0,5)
           elif pelota.bottom < ALTO:
            pelota.bottom = ALTO
                                
           if pelota == ALTO:
            pelota.bottom < (ALTO/2)
            pelota.move_ip(0,-4)
           elif pelota.bottom > (ALTO/2):
            pelota.bottom = (ALTO/2)
                        
          if gameover == True:
            pelota = sprites[1].convert()
            break
