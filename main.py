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
from Niveau import*
from spawn import*


rect=Carre_central(fenetre)
Player = Space_ship(fenetre)

stock = stock_missiles(fenetre)
stock_ennemies = all_ennemies(fenetre)
stock_ennemies.ajout_ennemis()
pygame.display.update()
fenetre.fill((0,0,0))


def main():
    for s in range(2):
        continuer = True
        if not stock_ennemies.ennemies_2_kill > 0:
            print("owo")
            generer_niveau_2(stock_ennemies,Player,rect)
        while continuer:
            global_update(Player,stock_ennemies,rect)
            gerer_input(Player)
            if  not stock_ennemies.ennemies_2_kill > 0:
                continuer = False

main()