import pygame
from pygame.locals import*
pygame.init()
from constantes import*
from Ennemy import*
from Carre_centre import*
from Vaisseau import*
from Missiles import*
from Interactions import*
from Updates import*
from Input import*
from Limite_bordure import*
from Limite_carre_central import*

rect=Carre_central(fenetre)
Player = Space_ship(fenetre)

stock = stock_missiles(fenetre)
stock_ennemies = all_ennemies(fenetre)
stock_ennemies.ajout_ennemis()
pygame.display.update()
fenetre.fill((0,0,0))


def main():
    continuer = True
    while continuer:
        global_update(Player,stock_ennemies,rect)
        gerer_input(Player)

main()