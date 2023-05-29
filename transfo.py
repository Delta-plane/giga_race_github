import pygame
import numpy as np
from animation import*
from constantes import*
from sons import*
from Ennemy import*


def transformation(ennemies,tout_mechant):
    taille=len(ennemies)



    for i in range(0,taille):




        if ennemies[i].tran and ennemies[i].id=="Mine" and ennemies[i].Is_active:
            origin=ennemies[i].origin
            x=ennemies[i].x
            y=ennemies[i].y
            tout_mechant.new_basic_ennemy(i)
            ennemies[i].temp_transfo = pygame.time.get_ticks()
            ennemies[i].x=x
            ennemies[i].y=y
            ennemies[i].origin=origin
        elif ennemies[i].tran and ennemies[i].id=="Basic-Ennemy":
            origin=ennemies[i].origin
            x=ennemies[i].x
            y=ennemies[i].y
            tout_mechant.new_thunder(i)
            ennemies[i].temp_transfo = pygame.time.get_ticks()

            ennemies[i].x=x
            ennemies[i].y=y
            ennemies[i].origin=origin






def timer(ennemies):
    for mechant in ennemies:
        if mechant.id!="thunder_ennemy" and mechant.Is_active:
            mechant.temp_trans()

