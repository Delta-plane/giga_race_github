import pygame
from pygame.locals import*
pygame.init()
import objets
from constantes import*
fenetre = pygame.display.set_mode((screen_size_x,screen_size_y))
rect=objets.Carre_central(fenetre)
rect.dessin()
rect.score()
Player = objets.Triangle(fenetre)
Player.generer_Liste_config_angle()
Player.dessin()
Missile = objets.weapon(fenetre)
tempref = pygame.time.get_ticks()
pygame.display.update()
fenetre.fill((0,0,0))

def global_update():
        pygame.time.delay(100)
        fenetre.fill((0,0,0))
        rect.dessin()
        rect.score()
        Player.dessin()
        Missile.dessin()
        Missile.tirer(tempref)
        pygame.display.flip()




def main():
    continuer = True
    while continuer:
        global_update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    continuer = False
                if event.key == pygame.K_LEFT:
                    Player.rotation_gauche()
                if event.key == pygame.K_RIGHT:
                    Player.rotation_droite()
                if event.key == pygame.K_SPACE:
                    Missile.initialiser_tir()
                    Missile.tirer(tempref)
                if event.key==pygame.K_SPACE:
                    Player.mouvement()

    pygame.quit()

main()