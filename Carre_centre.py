import pygame
import numpy as np
from pygame.locals import*
pygame.init()
from constantes import*
police = pygame.font.SysFont("monospace" ,23)
def affiche_texte(texte, x, y, couleur,fenetre):
    text=police.render(texte,1,couleur)
    fenetre.blit(text,(x,y))



class Carre_central(object):
    def __init__(self,screen):
        self.sizex =0.3*screen_size_x
        self.sizey =0.25*screen_size_y
        self.x =0.5*screen_size_x-(0.5*self.sizex)
        self.y =0.5*screen_size_y-(0.5*self.sizey)
        self.score_val=0
        self.screen=screen
        self.color=(255,255,255)

    def dessin(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.sizex,self.sizey),5)

    def score(self):
        affiche_texte(("score"),(self.x+0.5*self.sizex),(self.y),(255,0,0),self.screen)
        affiche_texte(("10000"),(self.x+0.5*self.sizex),(self.y+23),(255,0,0),self.screen)
        affiche_texte(("high score"),(self.x+0.5*self.sizex-35),(self.y+46+40),(255,0,0),self.screen)
        affiche_texte(("0"),(self.x+0.5*self.sizex),(self.y+69+40),(255,0,0),self.screen)

