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
Missile1 = objets.weapon(fenetre)
Missile2 = objets.weapon(fenetre)
Missile3 = objets.weapon(fenetre)
Missile4 = objets.weapon(fenetre)
Missile5 = objets.weapon(fenetre)
Missile6 = objets.weapon(fenetre)
Missile7 = objets.weapon(fenetre)
Liste_missiles_dispo = []
tempref = pygame.time.get_ticks()
pygame.display.update()
fenetre.fill((0,0,0))

def remplir_liste_dispo():
    for k in range(0,8):
        Liste_missiles_dispo.append(1)


def global_update():
        pygame.time.delay(100)
        fenetre.fill((0,0,0))
        rect.dessin()
        rect.score()
        Player.dessin()
        if Missile.has_shoot:
            objets.tirer(Missile,Player,tempref)
            Missile.dessin()
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
                if event.key==pygame.K_UP:
                    Player.mouvement()
                if event.key==pygame.K_DOWN:
                    objets.transfert_vers_weapon(Missile,Player)
                    Missile.initialiser_tir()

    pygame.quit()

main()