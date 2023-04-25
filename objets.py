import pygame
import numpy as np
from pygame.locals import*
pygame.init()
from constantes import*
police = pygame.font.SysFont("monospace" ,23)
def affiche_texte(texte, x, y, couleur,fenetre):
    text=police.render(texte,1,couleur)
    fenetre.blit(text,(x,y))
    pygame.display.flip()



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

class Triangle():
    def __init__(self,screen):
        self.screen = screen
        self.color = (255,255,0)
        self.size = 100
        self.middle_x = 100
        self.middle_y = 100
        self.A = (80,80)
        self.B = (120,80)
        self.C = (100,120)
        self.x = 100
        self.y = 100
        self.speed = 25
        self.nb_ro_poss = 12
        self.List_rota = []
        self.current_list_id = 0
    def generer_Liste_config_angle(self):
        for k in range(0,self.nb_ro_poss):
            self.List_rota.append((2*k*3.1415)/self.nb_ro_poss) #give the angle of self.A
        print(self.List_rota)

    def rotation2(self):
        self.A = (self.size*0.2*np.cos(self.List_rota[self.current_list_id])+self.x,self.size*0.2*np.sin(self.List_rota[self.current_list_id])+self.y)
        self.B = (self.size*0.2*np.cos(self.List_rota[self.current_list_id]+(2/3)*3.1415)+self.x,self.size*0.2*np.sin(self.List_rota[self.current_list_id]+(2/3)*3.1415)+self.y)
        self.C = (self.size*0.2*np.cos(self.List_rota[self.current_list_id]+(4/3)*3.1415)+self.x,self.size*0.2*np.sin(self.List_rota[self.current_list_id]+(4/3)*3.1415)+self.y)

    def rotation_gauche(self):
        if self.current_list_id ==0:
            self.current_list_id = self.nb_ro_poss-1
        else:
            self.current_list_id -=1
        self.rotation2()

    def rotation_droite(self):
        if self.current_list_id ==self.nb_ro_poss-1:
            self.current_list_id = 0
        else:
            self.current_list_id +=1
        self.rotation2()

    def dessin(self):
        pygame.draw.polygon(self.screen,self.color,(self.A,self.B,self.C))
    def mouvement(self):
        self.x += np.cos(self.List_rota[self.current_list_id])*self.speed
        self.y += np.sin(self.List_rota[self.current_list_id])*self.speed
        self.rotation2()

class weapon(object):
    def __init__(self,screen):
        self.screen = screen
        self.dx = 1
        self.dy = 1
        self.x = 100
        self.y = 100
        self.hauteur = 5
        self.color = (255,255,255)
        self.tempref = 0
        self.has_shoot = False
    def dessin(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),3)
    def initialiser_tir(self):
       self.tempref = pygame.time.get_ticks()
       self.has_shoot = True
    def tirer(self,tempref):
       if pygame.time.get_ticks()>self.tempref+5 and self.has_shoot:
        self.x += self.dx
        self.y += self.dy

#def transfert_vers_weapon(Missile,Vaisseau):
#    Missile.x = Vaisseau.B[0] + Missile.hauteur
 #   Missile.y = Vaisseau.B[0] + Missile.hauteur
  #  Missile.dx = Vaisseau.dx
   # Missile.dy = Vaisseau.dy






