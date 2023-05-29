import pygame
from pygame import K_q,K_DOWN
from Interactions import*
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
musique=sons()
clock = pygame.time.Clock()
def gerer_input(Player,carre,all_ennemies):
        for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                if event.key == K_DOWN:
                    Player.gerer_tir()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Player.rotation_gauche2()
            collision_joueur_carre(Player,carre)
        if keys[pygame.K_RIGHT]:
            Player.rotation_droite2()
            collision_joueur_carre(Player,carre)
        if keys[pygame.K_UP]:
            Player.mouvement()
            collisions_Player_Ennemy(Player,all_ennemies)
            collision_joueur_carre(Player,carre)
            pygame.time.delay(10)
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            Player.rotation_gauche2()
            pygame.time.delay(10)
            Player.mouvement()

        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            Player.rotation_droite2()
            collision_joueur_carre(Player,carre)
            pygame.time.delay(10)
            Player.mouvement()

        else:
            Player.glisse()


