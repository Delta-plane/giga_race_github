import pygame
from pygame import K_q,K_DOWN
def gerer_input(Player):
        for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                if event.key == K_DOWN:
                    Player.gerer_tir()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                Player.rotation_gauche2()
        if keys[pygame.K_RIGHT]:
            Player.rotation_droite2()
        if keys[pygame.K_UP]:
            Player.mouvement()
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            Player.rotation_gauche2()
            pygame.time.delay(10)
            Player.mouvement()
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            Player.rotation_droite2()
            pygame.time.delay(10)
            Player.mouvement()
        else:
            Player.glisse()


