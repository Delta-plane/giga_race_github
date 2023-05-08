import pygame
from pygame.locals import*
pygame.init()
from constantes import*
from Ennemy import*
from Carre_centre import*
from Vaisseau import*
from Missiles import*
from Interactions import*
from Limite_bordure import*
from Limite_carre_central import*
fenetre = pygame.display.set_mode((screen_size_x,screen_size_y))
rect=Carre_central(fenetre)
Player = Space_ship(fenetre)
Player.teleport()
Player.dessin()

stock = stock_missiles(fenetre)
stock_ennemies = all_ennemies(fenetre)
pygame.display.update()
fenetre.fill((0,0,0))

def global_update():
    fenetre.fill((0,0,0))
    Player.dessin()
    stock_ennemies.dessin_ennemis_valide()
    rect.dessin()
    Player.stock.dessin_missiles_valide()
    Player.rebond_carre(rect)
    verifier_les_collisions(stock_ennemies,Player)
    pygame.time.delay(30)
    pygame.display.update()


def main():
    continuer = True
    while continuer:
        global_update()
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



    pygame.quit()

main()