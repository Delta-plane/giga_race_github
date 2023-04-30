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
        self.coeff = 0.25
        self.nb_ro_poss = 12
        self.List_rota = []
        self.current_list_id = 0
        self.limit_wall = 30
        self.rebound_strenght =38
    def generer_Liste_config_angle(self):
        for k in range(0,self.nb_ro_poss):
            self.List_rota.append((2*k*3.1415)/self.nb_ro_poss) #give the angle of self.A
        print(self.List_rota)

    def rotation2(self):
        self.A = (self.size*self.coeff*np.cos(self.List_rota[self.current_list_id])+self.x,self.size*self.coeff*np.sin(self.List_rota[self.current_list_id])+self.y)
        self.B = (self.size*self.coeff*np.cos(self.List_rota[self.current_list_id]+(2/3)*3.1415)+self.x,self.size*self.coeff*np.sin(self.List_rota[self.current_list_id]+(2/3)*3.1415)+self.y)
        self.C = (self.size*self.coeff*np.cos(self.List_rota[self.current_list_id]+(4/3)*3.1415)+self.x,self.size*self.coeff*np.sin(self.List_rota[self.current_list_id]+(4/3)*3.1415)+self.y)

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
    def rebond_mur_2(self):
        if self.x<self.limit_wall or self.x>screen_size_x - self.limit_wall or self.y<self.limit_wall or self.y>screen_size_y - self.limit_wall:
            self.x += np.cos(self.List_rota[self.current_list_id])*self.rebound_strenght*-1
            self.y += np.sin(self.List_rota[self.current_list_id])*self.rebound_strenght*-1
            self.rotation2()
    def rebond_mur(self):
        if self.x<self.limit_wall:
            self.x += self.rebound_strenght
        elif self.x>screen_size_x - self.limit_wall:
            self.x -= self.rebound_strenght
        elif self.y<self.limit_wall:
            self.y += self.rebound_strenght
        elif self.y>screen_size_y - self.limit_wall:
            self.y -= self.rebound_strenght

class weapon(object):
    def __init__(self,screen):
        self.screen = screen
        self.speed = 25
        self.x = 100
        self.y = 100
        self.hauteur = 5
        self.color = (255,255,255)
        self.tempref = 0
        self.has_shoot = False
    def dessin(self):
        pygame.draw.circle(self.screen,self.color,(int(self.x),int(self.y)),3)
    def initialiser_tir(self):
       self.tempref = pygame.time.get_ticks()
       self.has_shoot = True

class stock_missiles(object):
    def __init__(self,screen):
        self.nb_missiles = 4
        self.liste_missiles_valides = []
        self.screen = screen
        self.time_ms_before_shoot = 3000
        self.missile = [weapon(self.screen) for i in range(self.nb_missiles)]
        self.current_missile_shoot_id = 0
    def add_missiles(self):
        for n in range(0,self.nb_missiles):
            self.liste_missiles_valides.append(1)
    def update_missile_valide(self):
        for k in range(0,self.nb_missiles):
            if self.missile[k].tempref+self.time_ms_before_shoot<pygame.time.get_ticks() and not self.missile[k].has_shoot:
                self.liste_missiles_valides[k] = 1



def transfert_vers_vaisseau(Missile,Vaisseau):
    Missile.x = Vaisseau.A[0]
    Missile.y = Vaisseau.A[1]

def tirer(Missile,Vaisseau,tempref):
       if pygame.time.get_ticks()>Missile.tempref and Missile.has_shoot:
        Missile.x += np.cos(Vaisseau.List_rota[Vaisseau.current_list_id])*Missile.speed
        Missile.y += np.sin(Vaisseau.List_rota[Vaisseau.current_list_id])*Missile.speed
        if pygame.time.get_ticks()>Missile.tempref+1000:
            Missile.has_shoot = False





